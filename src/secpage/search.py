"""实现功能：搜索专区"""

import re
import config


def search_by_id(value):
    """根基ID精确搜索"""
    data_list = []
    with open(config.VIDEO_FILE_PATH, mode='r', encoding='utf-8') as file_object:
        for line in file_object:
            line = line.strip()
            if value == line.split(',')[0]:
                data_list.append(line)
    return data_list


def search_value_text(value):
    """根据关键字模糊搜索"""
    data_list = []
    with open(config.VIDEO_FILE_PATH, mode='r', encoding='utf-8') as file_object:
        for line in file_object:
            line = line.strip()
            if value in line.split(',')[1]:
                data_list.append(line)
    return data_list


def show_tables(data_list):
    """输出内容"""
    print(data_list)
    for num, line in enumerate(data_list, 1):
        row_list = line.split(',')
        print(num, row_list[1])


def execute():
    print("搜索专区")

    while True:
        text = input("请输入要搜索的内容，支持[id搜索和key搜索](Q/q退出):")
        if text.upper() == 'Q':
            break
        match_object = re.match("(id|key)=(\w+)", text.strip())
        if not match_object:
            print("输入有误，请重新输入")

        name,value = match_object.groups()

        mapping = {
            "id": search_by_id,
            "key": search_value_text,
        }
        data_list = mapping[name](value)
        show_tables(data_list)

