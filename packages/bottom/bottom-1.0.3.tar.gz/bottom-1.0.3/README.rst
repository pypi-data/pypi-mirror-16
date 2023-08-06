.. image:: https://readthedocs.org/projects/bottom/badge?style=flat-square
    :target: http://bottomdocs.readthedocs.org/
.. image:: https://img.shields.io/travis/numberoverzero/bottom/master.svg?style=flat-square
    :target: https://travis-ci.org/numberoverzero/bottom
.. image:: https://img.shields.io/coveralls/numberoverzero/bottom/master.svg?style=flat-square
    :target: https://coveralls.io/github/numberoverzero/bottom
.. image:: https://img.shields.io/pypi/v/bottom.svg?style=flat-square
    :target: https://pypi.python.org/pypi/bottom
.. image:: https://img.shields.io/github/issues-raw/numberoverzero/bottom.svg?style=flat-square
    :target: https://github.com/numberoverzero/bottom/issues
.. image:: https://img.shields.io/pypi/l/bottom.svg?style=flat-square
    :target: https://github.com/numberoverzero/bottom/blob/master/LICENSE

asyncio-based rfc2812-compliant IRC Client (3.5+)

bottom isn't a kitchen-sink library.  Instead, it provides a consistent API
with a small surface area, tuned for performance and ease of extension.
Similar to the routing style of bottle.py, hooking into events is one line.

Installation
============
::

    pip install bottom

Getting Started
===============

Create an instance::

    import bottom

    host = 'chat.freenode.net'
    port = 6697
    ssl = True

    NICK = "bottom-bot"
    CHANNEL = "#bottom-dev"

    bot = bottom.Client(host=host, port=port, ssl=ssl)


Send nick/user/join when connection is established::

    @bot.on('CLIENT_CONNECT')
    def connect(**kwargs):
        bot.send('NICK', nick=NICK)
        bot.send('USER', user=NICK,
                 realname='https://github.com/numberoverzero/bottom')
        bot.send('JOIN', channel=CHANNEL)


Respond to ping::

    @bot.on('PING')
    def keepalive(message, **kwargs):
        bot.send('PONG', message=message)


Echo messages (channel and direct messages)::

    @bot.on('PRIVMSG')
    def message(nick, target, message, **kwargs):
        """ Echo all messages """

        # Don't echo ourselves
        if nick == NICK:
            return
        # Respond directly to direct messages
        if target == NICK:
            bot.send("PRIVMSG", target=nick, message=message)
        # Channel message
        else:
            bot.send("PRIVMSG", target=target, message=message)


Finally, connect and run the bot forever::

    bot.loop.create_task(bot.connect())
    bot.loop.run_forever()

API
===

The full API consists of 1 class, with 6 methods::

    async Client.connect()

    async Client.disconnect()

    Client.send(command, **kwargs)

    @Client.on(event)

    async Client.wait(event)

    Client.trigger(event, **kwargs)


Versioning  and RFC2812
=======================

* Bottom follows semver for its **public** API.

  * Currently, ``Client`` is the only public member of bottom.
  * IRC replies/codes which are not yet implemented may be added at any time,
    and will correspond to a patch - the function contract of ``@on`` method
    does not change.
  * You should not rely on the internal api staying the same between minor
    versions.
  * Over time, private apis may be raised to become public.  The reverse will
    never occur.


Contributing
============

Contributions welcome!  When reporting issues, please provide enough detail to
reproduce the bug - sample code is ideal.  When submitting a PR, please make
sure ``tox`` passes (including flake8).

Development
-----------

bottom uses ``tox``, ``pytest`` and ``flake8``.  To get everything set up::

    # RECOMMENDED: create a virtualenv with:
    #     pyenv virtualenv 3.5.0 bottom
    git clone https://github.com/numberoverzero/bottom.git
    pip install tox
    tox


TODO
----

* Better ``Client`` docstrings
* Add missing replies/errors to ``unpack.py:unpack_command``

  * Add reply/error parameters to ``unpack.py:parameters``
  * Document events, client.send


Contributors
------------
* `fahhem <https://github.com/fahhem>`_
* `thebigmunch <https://github.com/thebigmunch>`_
* `tilal6991 <https://github.com/tilal6991>`_
* `AMorporkian <https://github.com/AMorporkian>`_
* `nedbat <https://github.com/nedbat>`_
* `Coinkite Inc <https://github.com/coinkite>`_

API
===


Client.on(event)(func)
----------------------

This decorator is the main way you'll interact with a ``Client``.  For a given
event name, it registers the decorated function to be invoked when that event
occurs.  Your decorated functions should always accept \*\*kwargs, in case
unexpected kwargs are included when the event is triggered.

The usual IRC commands sent from a server are triggered automatically, or can
be manually invoked with ``trigger`` below.  Additionally, you may register
handlers for any string, making it easy to extend bottom with your own signals.


Not all available arguments need to be used.  For instance, both of the
following are valid::

    @bot.on('PRIVMSG')
    def event(nick, message, target, **kwargs):
        """ Doesn't use user, host.  argument order is different """
        # message sent to bot - echo message
        if target == bot.nick:
            bot.send('PRIVMSG', target, message=message)
        # Some channel we're watching
        elif target == bot.monitored_channel:
            logger.info("{} -> {}: {}".format(nick, target, message))


    @bot.on('PRIVMSG')
    def func(message, target, **kwargs):
        """ Just waiting for the signal """
        if message == codeword && target == secret_channel:
            execute_heist()

Handlers do not need to be async functions - non async will be wrapped prior to
the bot running.  For example, both of these are valid::

    @bot.on('PRIVMSG')
    def handle(message, **kwargs):
        print(message)

    @bot.on('PRIVMSG')
    async def handle(message, **kwargs):
        await async_logger.log(message)

Finally, you can create your own events to trigger and handle.  For example,
let's catch SIGINT and gracefully shut down the event loop::

    import signal

    def handle_sigint(signum, frame):
        print("SIGINT handler")
        bot.trigger("my.sigint.event")
    signal.signal(signal.SIGINT, handle_sigint)


    @bot.on("my.sigint.event")
    async def handle(**kwargs):
        print("SIGINT trigger")
        await bot.disconnect()

        # Signal a stop before disconnecting so that any reconnect
        # coros aren't run by the last run_forever sweep.
        bot.loop.stop()


    bot.loop.create_task(bot.connect())
    bot.loop.run_forever()  # Ctrl + C here


Client.trigger(event, \*\*kwargs)
---------------------------------

Manually inject a command or reply as if it came from the server.  This is
useful for invoking other handlers. Note that because trigger doesn't block,
registered callbacks for the event won't run until the event loop yields to
them.

Events don't need to be valid irc commands; any string is available.

::

    # Manually trigger `PRIVMSG` handlers:
    bot.trigger('privmsg', nick="always_says_no", message="yes")

::

    # Rename !commands to !help
    @bot.on('privmsg')
    def parse(nick, target, message, **kwargs):
        if message == '!commands':
            bot.send('privmsg', target=nick,
                     message="!commands was renamed to !help in 1.2")
            # Don't make them retype it, trigger the correct command
            bot.trigger('privmsg', nick=nick,
                        target=target, message="!help")


Because the ``@on`` decorator returns the original function, you can register
a handler for multiple events.  It's especially important to use ``**kwargs``
correctly here, to handle different keywords for each event.

::

    # Simple recursive-style countdown
    @bot.on('privmsg')
    @bot.on('countdown')
    async def handle(target, message, remaining=None, **kwargs):
        # Entry point, verify command and parse from message
        if remaining is None:
            if not message.startswith("!countdown"):
                return
            # !countdown 10
            remaining = int(message.split(" ")[-1])

        if remaining == 0:
            message = "Countdown complete!"
        else:
            message = "{}...".format(remaining)
        # Assume for now that target is always a channel
        bot.send("privmsg", target=target, message=message)

        if remaining:
            # After a second trigger another countdown event
            await asyncio.sleep(1, loop=bot.loop)
            bot.trigger('countdown',
                        target=target,
                        message=message,
                        remaining=remaining - 1)


Client.wait(event)
------------------

** This is a coroutine. **

Wait for an event to trigger::

    @bot.on("client_disconnect")
    async def reconnect(**kwargs):
        # Trigger an event that may cascade to a client_connect.
        # Don't continue until a client_connect occurs, which may be never.

        bot.trigger("some.plugin.connection.lost")

        await client.wait("client_connect")

        # If we get here, one of the plugins handled connection lost by
        # reconnecting, and we're back.  Send some messages, etc.
        client.send("privmsg", target=bot.CHANNEL, message="Happy Birthday!")


Client.connect()
----------------

** This is a coroutine. **

Connect to the client's host, port.

Attempt to reconnect using the client's host, port::

    @bot.on('client_disconnect')
    async def reconnect(**kwargs):
        # Wait a few seconds
        await asyncio.sleep(3, loop=bot.loop)
        await bot.connect()
        # Now that we're connected, let everyone know
        bot.send('privmsg', target=bot.channel, message="I'm back.")


You can schedule a connect without blocking by using the client's event loop::


    @bot.on('client_disconnect')
    def reconnect(**kwargs):
        # Wait a few seconds

        # Note that we're not in a coroutine, so we don't have access
        # to await and asyncio.sleep
        time.sleep(3)

        # After this line we won't necessarily be connected.
        # We've simply scheduled the connect to happen in the future
        bot.loop.create_task(bot.connect())

        print("Reconnect scheduled.")

Client.disconnect()
-------------------

** This is a coroutine. **

Immediately disconnect from the server.

Disconnect from the server if connected::

    @bot.on('privmsg')
    async def suicide_pill(nick, message, **kwargs):
        if nick == "spy_handler" and message == "last stop":
            await bot.disconnect()


Like ``Client.connect``, we can use the bot's event loop to schedule a
disconnect::

    bot.loop.create_task(bot.disconnect())


Client.send(command, \*\*kwargs)
--------------------------------

Send a command to the server.

.. _supported_commands:

Supported Commands
==================

::

    client.send('PASS', password='hunter2')

::

    client.send('NICK', nick='WiZ')

::

    # mode is optional, default is 0
    client.send('USER', user='WiZ-user', realname='Ronnie')
    client.send('USER', user='WiZ-user', mode='8', realname='Ronnie')

::

    client.send('OPER', user='WiZ', password='hunter2')

::

    # Renamed from MODE
    client.send('USERMODE', nick='WiZ')
    client.send('USERMODE', nick='WiZ', modes='+io')

::

    client.send('SERVICE', nick='CHANSERV', distribution='*.en',
                type='0', info='manages channels')

::

    client.send('QUIT')
    client.send('QUIT', message='Gone to Lunch')

::

    client.send('SQUIT', server='tolsun.oulu.fi')
    client.send('SQUIT', server='tolsun.oulu.fi', message='Bad Link')

::

    # If channel has n > 1 values, key MUST have 1 or n values
    client.send('JOIN', channel='0')  # send PART to all joined channels
    client.send('JOIN', channel='#foo-chan')
    client.send('JOIN', channel='#foo-chan', key='foo-key')
    client.send('JOIN', channel=['#foo-chan', '#other'], key='key-for-both')
    client.send('JOIN', channel=['#foo-chan', '#other'], key=['foo-key', 'other-key'])

::

    client.send('PART', channel='#foo-chan')
    client.send('PART', channel=['#foo-chan', '#other'])
    client.send('PART', channel='#foo-chan', message='I lost')

::

    # Renamed from MODE
    client.send('CHANNELMODE', channel='#foo-chan', modes='+b')
    client.send('CHANNELMODE', channel='#foo-chan', modes='+l', params='10')

::

    client.send('TOPIC', channel='#foo-chan')
    client.send('TOPIC', channel='#foo-chan', message='')  # Clear channel message
    client.send('TOPIC', channel='#foo-chan', message='Yes, this is dog')

::

    # target requires channel
    client.send('NAMES')
    client.send('NAMES', channel='#foo-chan')
    client.send('NAMES', channel=['#foo-chan', '#other'])
    client.send('NAMES', channel=['#foo-chan', '#other'], target='remote.*.edu')

::

    # target requires channel
    client.send('LIST')
    client.send('LIST', channel='#foo-chan')
    client.send('LIST', channel=['#foo-chan', '#other'])
    client.send('LIST', channel=['#foo-chan', '#other'], target='remote.*.edu')

::

    client.send('INVITE', nick='WiZ-friend', channel='#bar-chan')

::

    # nick and channel must have the same number of elements
    client.send('KICK', channel='#foo-chan', nick='WiZ')
    client.send('KICK', channel='#foo-chan', nick='WiZ', message='Spamming')
    client.send('KICK', channel='#foo-chan', nick=['WiZ', 'WiZ-friend'])
    client.send('KICK', channel=['#foo', '#bar'], nick=['WiZ', 'WiZ-friend'])

::

    client.send('PRIVMSG', target='WiZ-friend', message='Hello, friend!')

::

    client.send('NOTICE', target='#foo-chan', message='Maintenance in 5 mins')

::

    client.send('MOTD')
    client.send('MOTD', target='remote.*.edu')

::

    client.send('LUSERS')
    client.send('LUSERS', mask='*.edu')
    client.send('LUSERS', mask='*.edu', target='remote.*.edu')

::

    client.send('VERSION')

::

    # target requires query
    client.send('STATS')
    client.send('STATS', query='m')
    client.send('STATS', query='m', target='remote.*.edu')

::

    # remote requires mask
    client.send('LINKS')
    client.send('LINKS', mask='*.bu.edu')
    client.send('LINKS', remote='*.edu', mask='*.bu.edu')

::

    client.send('TIME')
    client.send('TIME', target='remote.*.edu')

::

    client.send('CONNECT', target='tolsun.oulu.fi', port=6667)
    client.send('CONNECT', target='tolsun.oulu.fi', port=6667, remote='*.edu')

::

    client.send('TRACE')
    client.send('TRACE', target='remote.*.edu')

::

    client.send('ADMIN')
    client.send('ADMIN', target='remote.*.edu')

::

    client.send('INFO')
    client.send('INFO', target='remote.*.edu')

::

    # type requires mask
    client.send('SERVLIST', mask='*SERV')
    client.send('SERVLIST', mask='*SERV', type=3)

::

    client.send('SQUERY', target='irchelp', message='HELP privmsg')

::

    client.send('WHO')
    client.send('WHO', mask='*.fi')
    client.send('WHO', mask='*.fi', o=True)

::

    client.send('WHOIS', mask='*.fi')
    client.send('WHOIS', mask=['*.fi', '*.edu'], target='remote.*.edu')

::

    # target requires count
    client.send('WHOWAS', nick='WiZ')
    client.send('WHOWAS', nick='WiZ', count=10)
    client.send('WHOWAS', nick=['WiZ', 'WiZ-friend'], count=10)
    client.send('WHOWAS', nick='WiZ', count=10, target='remote.*.edu')

::

    client.send('KILL', nick='WiZ', message='Spamming Joins')

::

    # server2 requires server1
    client.send('PING', message='Test..')
    client.send('PING', server2='tolsun.oulu.fi')
    client.send('PING', server1='WiZ', server2='tolsun.oulu.fi')

::

    # server2 requires server1
    client.send('PONG', message='Test..')
    client.send('PONG', server2='tolsun.oulu.fi')
    client.send('PONG', server1='WiZ', server2='tolsun.oulu.fi')

::

    client.send('AWAY')
    client.send('AWAY', message='Gone to Lunch')

::

    client.send('REHASH')

::

    client.send('DIE')

::

    client.send('RESTART')

::

    # target requires channel
    client.send('SUMMON', nick='WiZ')
    client.send('SUMMON', nick='WiZ', target='remote.*.edu')
    client.send('SUMMON', nick='WiZ', target='remote.*.edu', channel='#foo-chan')

::

    client.send('USERS')
    client.send('USERS', target='remote.*.edu')

::

    client.send('WALLOPS', message='Maintenance in 5 minutes')

::

    client.send('USERHOST', nick='WiZ')
    client.send('USERHOST', nick=['WiZ', 'WiZ-friend'])

::

    client.send('ISON', nick='WiZ')
    client.send('ISON', nick=['WiZ', 'WiZ-friend'])

.. _supported_events:

Supported Events
================

These commands are received from the server, or dispatched using
``Client.trigger(...)``.

::

    # Local only events
    client.trigger('CLIENT_CONNECT')
    client.trigger('CLIENT_DISCONNECT')

* PING
* JOIN
* PART
* PRIVMSG
* NOTICE
* RPL_WELCOME (001)
* RPL_YOURHOST (002)
* RPL_CREATED (003)
* RPL_MYINFO (004)
* RPL_BOUNCE (005)
* RPL_MOTDSTART (375)
* RPL_MOTD (372)
* RPL_ENDOFMOTD (376)
* RPL_LUSERCLIENT (251)
* RPL_LUSERME (255)
* RPL_LUSEROP (252)
* RPL_LUSERUNKNOWN (253)
* RPL_LUSERCHANNELS (254)
