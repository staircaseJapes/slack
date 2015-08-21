from errbot import BotPlugin, botcmd

class Task(BotPlugin):
    """Integration between Slack and Todoist"""

    @botcmd(split_args_with=None)
    def task(self, msg, args):
        """Print channel and sender"""
        frm = str(msg.frm)
        msg = args
        channel = frm.split('/')[0]
        sender = frm.split('/')[1]
        yield frm 
        yield msg