import unittest

import mock
import irc.client

import pyborg_irc2
import pyborg

class TestReplys(unittest.TestCase):
    # @mock.patch('socket.socket.connect')
    # # @mock.patch('socket.socket')
    # def test_connect(self, patched_wrap, ):
    #     # This test is doesn't test anything and starts a loop
    #     mod = pyborg_irc2.ModIRC(pyborg.pyborg.pyborg)
    #     mod.start()
    #     print patched_wrap.call_args
    #     mod.disconnect()
    
    @mock.patch('pyborg_irc2.ModIRC.strip_nicks', side_effect=lambda x, _: x)
    @mock.patch('pyborg_irc2.ModIRC.learn')
    @mock.patch('irc.connection')
    def test_respond(self, c, learn, stripnicks):
        mod = pyborg_irc2.ModIRC(pyborg.pyborg.pyborg)
        our_event = irc.client.Event(type=None, source=None, target=u"#ranarchism", arguments=[u"Hello Pyborg"])
        mod.on_pubmsg(c, our_event)
        learn.assert_called_with(our_event.arguments[0].encode('utf-8'))
    
    @mock.patch('pyborg_irc2.ModIRC.strip_nicks', side_effect=lambda x, _: x)
    @mock.patch('pyborg_irc2.ModIRC.reply')
    @mock.patch('pyborg_irc2.ModIRC.learn')
    @mock.patch('irc.connection')
    def test_nick_reply(self, c, learn, reply, stripnicks):
        mod = pyborg_irc2.ModIRC(pyborg.pyborg.pyborg)
        # nick = mod.connection.get_nickname()
        nick = 'steve'
        # c.get_nickname.return_value = "steve"
        mod.connection.real_nickname = nick
        our_event = irc.client.Event(type=None, source=None, target=None, arguments=[u'%s: yolo swagins' % nick])
        mod.on_pubmsg(c, our_event)
        learn.assert_called_with(our_event.arguments[0].split(":")[1].encode('utf-8'))
        reply.assert_called_with(u" yolo swagins")
