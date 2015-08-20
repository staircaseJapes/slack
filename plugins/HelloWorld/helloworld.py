from errbot import BotPlugin, botcmd

class HelloWorld(BotPlugin):
    """Example 'Hello, world!' plugin for Err"""

    @botcmd(split_args_with=None)
    def hello(self, msg, args):
        """Say hello to the world"""
        channel = msg.to
        yield str(channel)
        yield msg.frm