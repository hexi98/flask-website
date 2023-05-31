from flask import Flask, render_template,request
from markupsafe import escape
import test as poem_gen
import json
name = 'He xi'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
app = Flask(__name__)

# @app.route('/user/<name>')
# def user_page(name):
#     return f'User: {escape(name)}'
locationNames = ["钟山","青溪","石头城","三山","新亭","凤凰台","乌衣巷","白鹭洲","玄武湖","冶城","雨花台","方山","朱雀桥","秦淮河","东山","摄山","牛首山","中华门","桃叶渡","长干里","覆舟山","莫愁湖","景阳楼","瓦官寺","光宅寺","新街口","新林浦","清凉寺","燕子矶","劳劳亭","随园","八功德水","中山门","内桥","北门桥","杏花村","谢公墩","半山园","挹江门","麾扇渡","中山路","大行宫","状元境","饮马巷","大王府巷","泥马巷","金銮巷","落星岗","白门"]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html',locationNames = locationNames)

@app.route('/test/<LocationName>',methods=['POST'])
def test(LocationName):
    result = {"poem":poem_gen.userTest(LocationName)}
    data = request.get_json()
    return result



@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码
