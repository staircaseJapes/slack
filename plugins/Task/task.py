from errbot import BotPlugin, botcmd

class Task(BotPlugin):
    """Integration between Slack and Todoist"""

    @botcmd(split_args_with=None)
    def task(self, msg, args):
        """Print channel and sender"""
        frm = str(msg.frm)
        msg = [str(x) for x in args]
        channel = frm.split('/')[0]
        sender = frm.split('/')[1]
        target = str([x for x in msg if x[0] =="@"])
        task = " ".join([x for x in msg if x[0] != "@"])
        for i in msg:
            yield i
        yield target
        yield task