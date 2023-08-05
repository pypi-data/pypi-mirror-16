import sys
import asyncio
import argparse

import irc3
import zmq
from zmq import ZMQError
from irc3.plugins.autojoins import AutoJoins

from vexbot.adapters.messaging import ZmqMessaging


@irc3.plugin
class AutoJoinMessage(AutoJoins):
    requires = ['irc3.plugins.core', ]

    def __init__(self, bot):
        super().__init__(bot)

    def connection_lost(self):
        self.bot.messaging.send_status('DISCONNECTED')
        super(AutoJoinMessage, self).connection_lost()

    def join(self, channel=None):
        super(AutoJoinMessage, self).join(channel)
        self.bot.messaging.send_status('CONNECTED')

    @irc3.event(irc3.rfc.KICK)
    def on_kick(self, mask, channel, target, **kwargs):
        self.bot.messaging.send_status('DISCONNECTED')
        super().on_kick(mask, channel, target, **kwargs)

    @irc3.event("^:\S+ 47[1234567] \S+ (?P<channel>\S+).*")
    def on_err_join(self, channel, **kwargs):
        self.bot.messaging.send_status('DISCONNECTED')
        super().on_err_join(channel, **kwargs)


@irc3.plugin
class EchoToMessage(object):
    requires = ['irc3.plugins.core',
                'irc3.plugins.command']

    def __init__(self, bot):
        self.bot = bot

    @irc3.event(irc3.rfc.PRIVMSG)
    def message(self, mask, event, target, data):
        nick = mask.split('!')[0]
        message = data
        self.bot.messaging.send_message(author=nick, message=str(message))


def create_irc_bot(nick,
                   password,
                   host=None,
                   port=6667,
                   realname=None,
                   channel=None):

    config = dict(ssl=False,
                  includes=['irc3.plugins.core',
                            'irc3.plugins.command',
                            'irc3.plugins.human',
                            __name__])

    if realname is None:
        realname = nick
    if channel is None:
        channel = nick

    config['nick'] = nick
    config['password'] = password
    config['host'] = host
    config['port'] = port
    config['username'] = realname
    config['autojoins'] = channel
    config['level'] = 30

    bot = irc3.IrcBot.from_config(config)

    return bot


async def _check_subscription(bot):
    while True:
        await asyncio.sleep(1)
        msg = None
        try:
            msg = bot.messaging.sub_socket.recv_multipart(zmq.NOBLOCK)
        except zmq.error.Again:
            pass
        if msg:
            print(msg)


def main(nick,
         password,
         host,
         channel,
         publish_address,
         subscribe_address,
         service_name):

    irc_client = create_irc_bot(nick,
                                password,
                                host,
                                channel=channel)

    try:
        messaging = ZmqMessaging(service_name,
                                 publish_address,
                                 subscribe_address,
                                 socket_filter='irc')

        messaging.start_messaging()
    except ZMQError:
        return
    # Duck type messaging onto irc_client, FTW
    irc_client.messaging = messaging

    irc_client.create_connection()
    irc_client.add_signal_handlers()
    event_loop = asyncio.get_event_loop()
    asyncio.ensure_future(_check_subscription(irc_client))
    try:
        event_loop.run_forever()
    except KeyboardInterrupt:
        pass
    event_loop.close()
    sys.exit()


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nick')
    parser.add_argument('--password')
    parser.add_argument('--host')
    parser.add_argument('--channel')
    parser.add_argument('--publish_address')
    parser.add_argument('--subscribe_address')
    parser.add_argument('--service_name')

    return parser.parse_args()


if __name__ == '__main__':

    kwargs = vars(_get_args())
    main(**kwargs)
