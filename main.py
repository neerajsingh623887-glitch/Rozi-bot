from pyrogram import Client, filters

API_ID = 22064323
API_HASH = "ee841533493e0ae16e090c88809ddb56"
BOT_TOKEN = "8010124270:AAGcXUeXYdxs9GRxeVbeUwDYaUGE9B5AL54"

app = Client("rozi_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hey! I'm Rozi Movie Bot. Search movies in @movielockerhau group!")

app.run()
