from Lipstick_System import app
from Lipstick_System.mongo import lipsticks,users,memberLike
from flask import Flask, render_template, request, redirect, session, flash,jsonify
import bson
import re

def convert_to_integer(string):
    if "NT$" in string:
        string = string.replace("NT$", "")
    string = string.strip()  # 去除可能存在的额外空格
    try:
        integer_value = int(string)
        return integer_value
    except ValueError:
        print("字符串无法转换为整数。")
        
@app.route('/collectionPagePriceSort/<method>', methods=["POST"])
def collectionPagepriceSort(method):
    like_list= eval(request.form.get('result'))
    is_true = method.lower() == 'true'
    like_list = sorted(like_list, key=lambda x: convert_to_integer(x['price']), reverse=is_true)
    rendered_template = render_template('Collection/LikePage.html',like_like=like_list)
    return jsonify(html=rendered_template)


@app.route('/member_delete_like', methods=["POST"])
def delete_to_like():
    #print("ok")
    like_inf= request.form.get('image_url')
    lip_like=lipsticks.find_one({"pic":like_inf})    

    if(session.get('user_name') != False and session.get('user_name') != None):
        m=users.find_one({"user_name":session.get('user_name')})
        print(m)
        d=memberLike.find_one({"lip_id":lip_like["_id"],"user_id": m["_id"]})
        try:
            memberLike.delete_one(d)
            for x in memberLike.find():
                print(x)
        except:
            pass
    return redirect('/collection') 


@app.route('/collection')
def like():
    m = users.find_one({"user_name":session.get('user_name')})
    uid = memberLike.find({"user_id":m["_id"]})

    like_list = []
    for x in uid:
        lip_list = lipsticks.find_one({"_id":x["lip_id"]})
        data = lip_list.pop('_id')
        like_list.append(lip_list)
       
    return render_template('Collection/LikePage.html',like_like=like_list)