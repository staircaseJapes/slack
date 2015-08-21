from errbot import BotPlugin, botcmd
import time
import json
from slackclient import SlackClient
from pytodoist import todoist

def plain_name(code):
    dump = json.loads(sc.api_call("users.info", user=code))
    return dump['user']['name']


class Task(BotPlugin):
    """Integration between Slack and Todoist"""

    @botcmd(split_args_with=None)
    def task(self, msg, args):
        """Print channel and sender"""
        frm = str(msg.frm)
        msg = [str(x) for x in args]
        target = str([x for x in msg if x[0] =="@"])
        yield target

        """
        channel = frm.split('/')[0]
        sender = frm.split('/')[1]
        target = str([x for x in msg if x[0] =="@"])
        task = " ".join([x for x in msg if x[0] != "@"])
        for i in msg:
            yield i
        yield target
        yield task
        """