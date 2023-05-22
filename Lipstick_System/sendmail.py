from Lipstick_System import mail
from flask_mail import Message
from threading import Thread
from flask import render_template, current_app

def send_mail(sender, recipients, subject, template, mailtype='html', **kwargs):
    """
    sender:的部份可以考慮透過設置default
    recipients:記得要list格式
    subject:是郵件主旨
    template:
        mailtype=body:郵件內容文字
        mailtype=txt、html:樣板名稱
    mailtype:
        html:html樣板(預設)
        txt:txt樣板
        body:文字方式
    **kwargs:參數
    """
    app = current_app._get_current_object()
    msg = Message(subject,
                  sender=sender,
                  recipients=recipients)
    if mailtype == 'html':
        msg.html = render_template(template + '.html', **kwargs)
        print(msg.html)
    elif mailtype == 'txt':
        msg.body = render_template(template + '.txt', **kwargs)
    elif mailtype == 'body':
        msg.body = template
    mail.send(msg)
    #  使用多線程
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()

# def send_async_email(app, msg):
#     with app.app_context():
        