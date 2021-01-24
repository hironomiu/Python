from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


@respond_to('メンション')
def mention_func(message):
    message.reply('メンション')
