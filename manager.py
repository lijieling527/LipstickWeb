import os
from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from gevent import pywsgi

app = Flask(__name__)
# app.config.from_object(Config)

# 初始化 Flask 扩展
mail = Mail(app)
bcrypt = Bcrypt(app)

if __name__ == "__main__":
    # 让 Render 监听正确的端口
    port = int(os.environ.get("PORT", 10000))
    server = pywsgi.WSGIServer(("0.0.0.0", port), app)
    server.serve_forever()