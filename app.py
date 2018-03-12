from flask import Flask
from wallet import wallet

app = Flask(__name__)

app.register_blueprint(wallet, url_prefix='/wallet')

app.run()