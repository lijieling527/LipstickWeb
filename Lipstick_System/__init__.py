from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from gevent import pywsgi
from config import Config
from pymongo.mongo_client import MongoClient
import os
mail = Mail()
app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
# server = pywsgi.WSGIServer(('127.0.0.2', 5000), app)
port = int(os.environ.get("PORT", 5000))
server = pywsgi.WSGIServer(('0.0.0.0', port), app)
mail.init_app(app)

client = MongoClient(Config.URI, tls=True, tlsAllowInvalidCertificates=True)

db = client.LIPSTICK_SYSTEM

from Lipstick_System.Login_Register import view
from Lipstick_System.Home import view
from Lipstick_System.Collection import view
from Lipstick_System.History import view
from Lipstick_System.Search import view

# homepage css優化
# email token新增
# 環境變數
# search