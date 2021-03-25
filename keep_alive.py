from flask import Flask
from threading import thread

app = Flask('24/7Tech4Help')


@app.route('/')
def home():
	return "✔ Bot is online"


def run():
	app.run(host='1.1.1.1', port=2021)

def keep_alive():
	t = thread(target=run)
	t.start()
 