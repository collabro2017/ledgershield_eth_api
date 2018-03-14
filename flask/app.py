from flask import Flask
from wallet import wallet

app = Flask(__name__)

app.register_blueprint(wallet, url_prefix='/wallet')

if __name__ == "__main__":
	app.run()
