###app to post slack comments onto the threads


import time
import json
from slackclient import SlackClient
from pytodoist import todoist

# Initialise slack tokens
token = "xoxp-3434164274-3434164280-9087563412-a33082"      # found at https://api.slack.com/#auth)
sc = SlackClient(token)

# Initialise todoist tokens
user = todoist.login('johno@rocketer.co.uk', '42164216')


# Takes in a channel name and message before posting there
def post(thread, message):
    sc.api_call("chat.postMessage", channel=thread, text=message, username="Daily Tasks")


# Start pulling the toodoist channel
def gentasks(channel):
    project = user.get_project(channel[1:])
    tasks = project.get_tasks()
    for task in tasks:
        if task.indent == 1:
            post(channel, task.content)


gentasks("#aviva-car")