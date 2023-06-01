from flask import Flask, render_template,request
from markupsafe import escape
from flaskWebsite.static.python.main import *
from flaskWebsite.static.python.model import *
from flaskWebsite.static.python.config import *
import torch as t
from flaskWebsite.static.python.generate import *


def userTest(LocationName):
    print("正在初始化......")
    datas = np.load("flaskWebsite/static/python/tang.npz",allow_pickle=True)
    data = datas['data']
    ix2word = datas['ix2word'].item()
    word2ix = datas['word2ix'].item()
    model = PoetryModel(len(ix2word), Config.embedding_dim, Config.hidden_dim)
    model.load_state_dict(t.load(Config.model_path, 'cpu'))
    if Config.use_gpu:
        model.to(t.device('cuda'))
    print("初始化完成！\n")
    # print("请输入您想要的诗歌首句，可以是五言或七言")
    start_words = str(LocationName)
    gen_poetry = ''.join(generate(model, start_words, ix2word, word2ix))
    print("生成的诗句如下：%s\n" % (gen_poetry))
    
    return gen_poetry

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

locationNames = ["钟山","青溪","石头城","三山","新亭","凤凰台","乌衣巷","白鹭洲","玄武湖","冶城","雨花台","方山","朱雀桥","秦淮河","东山","摄山","牛首山","中华门","桃叶渡","长干里","覆舟山","莫愁湖","景阳楼","瓦官寺","光宅寺","新街口","新林浦","清凉寺","燕子矶","劳劳亭","随园","八功德水","中山门","内桥","北门桥","杏花村","谢公墩","半山园","挹江门","麾扇渡","中山路","大行宫","状元境","饮马巷","大王府巷","泥马巷","金銮巷","落星岗","白门"]

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html',locationNames = locationNames)

@app.route('/test/<LocationName>',methods=['POST'])
def test(LocationName):
    result = {"poem":userTest(LocationName)}
    data = request.get_json()
    return result



@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('errors/404.html'), 404  # 返回模板和状态码

if __name__ == '__main__':
    app.run(
      host='0.0.0.0',
      port= 5000,
      debug=True
    )