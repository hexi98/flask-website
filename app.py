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

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html',name = name,movies = movies)

@app.route('/test',methods=['POST'])
def test():
    result = {"poem":poem_gen.userTest()}
    print(result)
    # data = request.get_json()
    return result



@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码