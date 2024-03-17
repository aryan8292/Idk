import time
from telegram import Bot

# Initialize your Telegram Bot token
bot_token = '6757602766:AAGoyMR6dpnOk2R_BQWaybi9qae6xisi3yo'
bot = Bot(token=bot_token)

#• Define the group chat ID where you want to send messages
group_chat_id = '-1001836402007'

#• List of messages to send
messages = ["Message 1", "Message 2", "Message 3", "Message 4"]

#• Send messages every 30 seconds
for message in messages:
    bot.send_message(chat_id=group_chat_id, text=message)
    time.sleep(30)
