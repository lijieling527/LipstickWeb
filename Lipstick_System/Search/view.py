from Lipstick_System import app
import re
from flask import Flask, render_template, request, redirect, session, jsonify
from Lipstick_System.mongo import lipsticks,users,memberLike
from math import dist
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
        
@app.route('/priceSort/<method>', methods=["POST"])
def priceSort(method):
    like_list= eval(request.form.get('result'))
    print(like_list)
    is_true = method.lower() == 'true'
    like_list = sorted(like_list, key=lambda x: convert_to_integer(x['price']), reverse=is_true)
    rendered_template = render_template('Search/RecommendPage.html',result=like_list)
    return jsonify(html=rendered_template)

@app.route('/member_add_like_com', methods=["POST"])
def add_to_like_com():
    like_inf= request.form.get('image_url')
    lip_like=lipsticks.find_one({"pic":like_inf})      
    response_data = {'message': 'unsuccess'}

    if(session.get('user_name') != False and session.get('user_name') != None):
        response_data = {'message': 'success'}
        m=users.find_one({"user_name":session.get('user_name')})
        input={}
        input["_id"] = bson.ObjectId(str(m["_id"])[-12:]+str(lip_like["_id"])[-12:])
        input["user_id"] = m["_id"]
        input["lip_id"] = lip_like["_id"]

        try:
            memberLike.insert_one(input)
        except:
            pass
    return jsonify(response_data)

@app.route('/passform', methods=["POST"])
def passColor():
    input=request.form["confirmColor"]
    r=int(input[1:3], 16)
    g=int(input[3:5], 16)
    b=int(input[5:7], 16)
    input=f'rgb({r},{g},{b})'
    main=(r,g,b)
    res=[]
    for y in lipsticks.find({},{"_id":0}):
        if "rgb"in y['color_code']:
            import ast
            other=ast.literal_eval(y['color_code'][4:-2])
            # other=other[:-2]
            
            if(dist(main,other)<100):
                res.append(y)
    
    return render_template('Search/RecommendPage.html',color=input,result=res)   
 
@app.route('/passtext', methods=["POST"])
def passText():
    input=request.form["confirmColor"]
    input=re.sub("[\'[\"]", "", input)
    input=input.strip(']').split("->")
    lip_result = lipsticks.find({"name":input[0],"color":input[1]},{"_id":0})
    lip=[y for y in lip_result]
    main=eval(lip[0]['color_code'][4:-1])
    
    res=[]
    for y in lipsticks.find({},{"_id":0}):
        if "rgb"in y['color_code']:
            import ast
            other=ast.literal_eval(y['color_code'][4:-2])
            # other=other[:-2]
            
            if(dist(main,other)<100):
                res.append(y)
    
    return render_template('Search/RecommendPage.html',color=lip,result=res)