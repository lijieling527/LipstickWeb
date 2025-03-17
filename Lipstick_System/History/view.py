from Lipstick_System import app
from Lipstick_System.mongo import lipsticks,users,memberLike,historys
from flask import Flask, render_template, request, redirect, session, jsonify
import bson

def convert_to_integer(string):
    if "NT$" in string:
        string = string.replace("NT$", "")
    string = string.strip()  # 去除可能存在的额外空格
    try:
        integer_value = int(string)
        return integer_value
    except ValueError:
        print("字符串无法转换为整数。")

@app.route('/member_delete_history', methods=["POST"])
def member_delete_history():
    print("ok")
    his_inf= request.form.get('image_url')
    lip_his=lipsticks.find_one({"pic":his_inf})    

    if(session.get('user_name') != False and session.get('user_name') != None):
        #response_data = {'message': 'success'}
        m=users.find_one({"user_name":session.get('user_name')})
        #print(m)
        d=historys.find_one({"lip_id":lip_his["_id"],"user_id": m["_id"]})
        print(d)
        try:
            historys.delete_one(d)
        except:
            pass
    return redirect('/history')

@app.route('/history')
def history():
    m = users.find_one({"user_name":session.get('user_name')})
    uid = historys.find({"user_id":m["_id"]})
    his_list = []
    for x in uid:
        lip_list = lipsticks.find_one({"_id":x["lip_id"]})
        data = lip_list.pop('_id')
        his_list.append(lip_list)
        
    print(his_list)
    return render_template('History/HistoryPage.html',member_history=his_list)

@app.route('/historyPagepriceSort/<method>', methods=["POST"])
def historyPagepriceSort(method):
    like_list= eval(request.form.get('result'))
    is_true = method.lower() == 'true'
    like_list = sorted(like_list, key=lambda x: convert_to_integer(x['price']), reverse=is_true)
    rendered_template = render_template('History/HistoryPage.html',member_history=like_list)
    return jsonify(html=rendered_template)