"""代码框架实现用户交互"""

from src.secpage import download, search, news


def run():
    func_dict = {
        '1': {'title': "新闻专区", 'func': news.execute},
        '2': {'title': "搜索专区", 'func': search.execute},
        '3': {'title': "下载专区", 'func': download.execute}
    }
    tips = ";".join(["{}.{}".format(k, v['title']) for k, v in func_dict.items()])

    while True:
        print(tips)
        chine = input("请选择进入专区:")
        if chine.upper() == "Q":
            break
        data_dict = func_dict.get(chine)
        if not data_dict:
            print("请重新输入您要选择的专区:")
            continue

        data_dict['func']()
