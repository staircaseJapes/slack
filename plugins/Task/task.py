from errbot import BotPlugin, botcmd

class Task(BotPlugin):
    """Integration between Slack and Todoist"""

    @botcmd(split_args_with=None)
    def task(self, msg, args):
        """Print channel and sender"""
        channel = msg.to
        yield str(channel)
        yield msg.frm