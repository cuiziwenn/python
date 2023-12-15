import config

def get_news_data(news_num,per_news_count):
    """ 根据页码获取要展示的数据列表
    :param news_num: 页码
    :param per_news_count: 每页数据条数
    :return: 数据列表
    """
    start_index = (news_num - 1) * per_news_count
    end_index = news_num * per_news_count

    data_list = []
    read_row_count = 0
    with open(config.VIDEO_FILE_PATH,mode='r',encoding='utf-8') as file_object:
        for line in file_object:
            if start_index <= read_row_count < end_index:
                data_list.append(line.strip())
            if read_row_count >= end_index:
                break
            read_row_count += 1
    return data_list

def show_tables(news_num,per_news_count,data_list):
    index = (news_num - 1) * per_news_count + 1
    for num, line in enumerate(data_list, index):
        row_list = line.split(',')
        print(num,row_list)

def execute():
    """分页看新闻"""
    print("分页看新闻，每页显示10条")
    # 每页显示10条，一共有999条
    per_news_count, total_count = 10, 999

    # 计算页码最大值
    max_news_num, remainder = divmod(total_count,per_news_count)
    if remainder:
        max_news_num += 1

    while True:
        num = input("请输入页码(范围{}-{})(Q/q退出):")
        if num.upper() == "Q":
            break
        if not num.isdecimal():
            print("页码输入有误,请重新输入")
            continue
        num = int(num)
        if num < 1 or num > max_news_num:
            num = 1
        page_string = "第{}页".format(num)
        print(page_string)

        data_list = get_news_data(num,per_news_count)
        show_tables(num,per_news_count,data_list)