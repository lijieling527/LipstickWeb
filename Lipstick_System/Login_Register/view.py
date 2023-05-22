from Lipstick_System import app
from Lipstick_System.mongo import users
from flask import Flask, render_template, request, redirect, session, flash
from Lipstick_System.sendmail import send_mail
from Lipstick_System.Login_Register.model import UserRegister, FormRegister, FormLogin, ResetPwd

@app.route('/check_login', methods=["POST"])
def check_login():
    input = {'email': request.form["email"],
             'password': request.form["password"]}

    form = FormLogin(input)

    if(form.email_validation() == False):
        return redirect('/register')   
    
    if(form.password_validation() == False):
        flash('輸入密碼有誤', 'pwd')
        return redirect('/login') 
    
    session['user_name'] = form.getUserName()
    session['email'] = form.getEmail()
    return redirect('/home')

@app.route('/check_if_login')
def check_if_login():
    if(session.get('user_name') != False and session.get('user_name') != None):
        return redirect('/member')
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('Login_Register/Login.html')

@app.route('/check_register', methods=["POST"])
def signup():
    input = {'user_name': request.form["user_name"],
             'email': request.form["email"],
             'password': request.form["password"],
             'check_password': request.form["check_password"]}
    form = FormRegister(input)

    if form.password_validation() == False:
        flash('與輸入密碼不一致', 'pwd')
        return redirect('/register')
    
    if form.email_validation() == False:
        flash('此信箱已經被註冊', 'email')
        return redirect('/register')
    
    new_user = UserRegister(input)
    session['user_name'] = input['user_name']
    session['email'] = input['email']
    return redirect('/home')
        

@app.route('/register')
def register():
    return render_template('Login_Register/Register.html')

@app.route('/forget_pwd')
def forget_pwd():
    return render_template('Login_Register/Forget_password.html')

@app.route('/check_if_can_reset_pwd', methods=["POST"])
def check_if_can_reset_pwd():
    email = request.form["email"]
    email_result = users.find_one({
        "email": email
    })
    if(email_result == None):
        flash('請確認信箱是否正確')
        return redirect('/forget_pwd')
    session['email'] = email_result['email']
    session['user_name'] = email_result['user_name']
    return redirect('/forget_password')

@app.route('/forget_password', methods=['GET', 'POST'])
def forget_password():
    send_mail(sender='melodylin22563@gmail.com',
              recipients=[session['email']],
              subject='Reset Your Password',
              template='ResetEmail',
              user_name=session['user_name'],
              mailtype='html')
    flash('Please Check Your Email. Then Click link to Reset Password')
    #  寄出之後將使用者導回login，並且送出flash message
    return redirect('/login')
    
@app.route('/logout')
def logout():
    session['user_name'] = False
    session['email'] = False
    return redirect('/home')

@app.route('/member')
def member():
    return render_template('Login_Register/MemberPage.html', user_name = session['user_name'])

@app.route('/user_confirm')
def user_confirm():
    return redirect('/reset_password')

@app.route('/reset_password')
def reset_password():
    return render_template('Login_Register/Reset_password.html')

@app.route('/check_reset_pwd', methods=['POST'])
def check_reset_pwd():
    input = {'email': session['email'],
             'password': request.form["password"],
             'check_password': request.form["password2"]}
    form = ResetPwd(input)
    if(form.password_validation() == False):
        flash('與輸入密碼不一致')
        return redirect('/reset_password')
    form.reset_password()
    return redirect('/login')