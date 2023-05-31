from main import *
from model import *
from config import *
import torch as t
from generate import *


def userTest():
    print("正在初始化......")
    datas = np.load("tang.npz",allow_pickle=True)
    data = datas['data']
    ix2word = datas['ix2word'].item()
    word2ix = datas['word2ix'].item()
    model = PoetryModel(len(ix2word), Config.embedding_dim, Config.hidden_dim)
    model.load_state_dict(t.load(Config.model_path, 'cpu'))
    if Config.use_gpu:
        model.to(t.device('cuda'))
    print("初始化完成！\n")
    # while True:
        
    print("\n欢迎使用诗词生成器，\n"
            "输入1 进入首句生成模式\n"
            "输入2 进入藏头诗生成模式\n")
    location_list = ["钟山","青溪","石头城","三山","新亭","凤凰台","乌衣巷","白鹭洲","玄武湖","冶城","雨花台","方山","朱雀桥","秦淮河","东山","摄山","牛首山","中华门","桃叶渡","长干里","覆舟山","莫愁湖","景阳楼","瓦官寺","光宅寺","新街口","新林浦","清凉寺","燕子矶","劳劳亭","随园","八功德水","中山门","内桥","北门桥","杏花村","谢公墩","半山园","挹江门","麾扇渡","中山路","大行宫","状元境","饮马巷","大王府巷","泥马巷","金銮巷","落星岗","白门"]
    
    mode = int(input())
    if mode == 1:
        # print("请输入您想要的诗歌首句，可以是五言或七言")
        print("请选择地点：")
        for i in range(len(location_list)):
            print(location_list[i],end=' ')
            if(i+1)% 10 == 0:
                print("\n") 
        
        print("\n") 
        start_words = str(input())
        gen_poetry = ''.join(generate(model, start_words, ix2word, word2ix))
        print("生成的诗句如下：%s\n" % (gen_poetry))
    elif mode == 2:
        print("请选择诗词地点：")
        for i in range(len(location_list)):
            print(location_list[i],end=' ')
            if(i+1)% 10 == 0:
                print("\n") 
        print("\n")
        start_words = str(input())
        gen_poetry = ''.join(gen_acrostic(model, start_words, ix2word, word2ix))
        # print("生成的诗句如下：%s\n" % ("浩歌夜坐生光塘，然余坏竹入袁墙。最爱林泉多往事，喜逢日月共流光。欢讴未暇听雷响，芷壑已惊蛛雁忙。若无一年离世曰，宝莲山中有仙郎。"))
        print("生成的诗句如下：%s\n" % (gen_poetry))
    return gen_poetry

if __name__ == '__main__':
    userTest()
