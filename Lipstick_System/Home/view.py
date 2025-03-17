from Lipstick_System import app
from Lipstick_System.mongo import lipsticks,users,memberLike,historys
import bson
from flask import Flask, render_template, request, redirect, session, jsonify
import re

@app.route('/')
def index():
    return render_template('Home/HomePage.html')  # 或者重定向到 /home

@app.route('/home')
def home():
    lipstick_1028=lipsticks.find({"brand":"1028"})
    lipstick_heme=lipsticks.find({"brand":"heme"})
    lipstick_solone=lipsticks.find({"brand":"solone"})
    lipstick_immeme=lipsticks.find({"brand":"I'M MEME"})
    lipstick_maybelline=lipsticks.find({"brand":"maybelline"})
    ##
    lipstick_loreal=lipsticks.find({"brand":"L'Oréal"})
    lipstick_BOBBIBROWN=lipsticks.find({"brand":"BOBBI BROWN"})
    ##

    return render_template('Home/HomePage.html',lipstick_1028=lipstick_1028,lipstick_heme=lipstick_heme,lipstick_solone=lipstick_solone
                           ,lipstick_immeme=lipstick_immeme,lipstick_maybelline=lipstick_maybelline,lipstick_loreal=lipstick_loreal,lipstick_BOBBIBROWN=lipstick_BOBBIBROWN
                           )

@app.route('/add_history', methods=["POST"])
def add_history():
    link_inf= request.form.get('link_url')
    print(link_inf)
    lip_like=lipsticks.find_one({"pic":link_inf})    
    print(lip_like)
    response_data = {'message': 'unsuccess'}

    if(session.get('user_name') != False and session.get('user_name') != None):
        response_data = {'message': 'success'}
        m=users.find_one({"user_name":session.get('user_name')})
        input={}
        input["_id"] = bson.ObjectId(str(m["_id"])[-12:]+str(lip_like["_id"])[-12:])
        input["user_id"] = m["_id"]
        input["lip_id"] = lip_like["_id"]
        try:
            historys.insert_one(input)
        except:
            pass
    return jsonify(response_data)

@app.route('/member_add_like', methods=["POST"])
def add_to_like():
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

    

@app.route('/pic_search')
def Picture_search():
    return render_template('Search/Pic_Search.html')

@app.route('/color_search')
def Color_search():
    return render_template('Search/Color_Search.html')

@app.route('/text_search')
def Text_search():
    brands_result = lipsticks.distinct('brand')
    re=""
    lips={};
    result=[];
    i=0;
    for x in brands_result:
        lips[i]=lipsticks.find({ "brand": x },{"_id":0, "name": 1, "color": 1, "color_code": 1 })
        lipstick=[];
        for y in lips[i]:
            lipstick.append(y["name"]+"->"+y["color"]+"->"+y["color_code"]);
        result.append(lipstick);
        re=re+","+x
        i+=1;
    return render_template('Search/Text_Search.html',brand=re,lips=result)

# if __name__ == "__main__":
#     app.run(debug=True)
