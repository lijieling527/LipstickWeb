from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from gevent import pywsgi
from config import Config
from pymongo.mongo_client import MongoClient

mail = Mail()
app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
mail.init_app(app)

client = MongoClient(Config.URI)
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