"""
该函数用以获得情话，并将其在本文中删除
同时用于随机获取要发送的早安信息！
"""
from random import randint

def get_love_word() -> str:
    """ 获取情话 """
    filepath = "python_files/coolq_of_xiaozhang/database/lover's prattle.txt"
    with open(filepath) as obj_file:
        lines = obj_file.readlines()
        love_word = lines[0]
        lines.pop(0)
        content = ''.join(lines)
    with open(filepath, 'w') as obj_file:
        obj_file.write(content)
    return love_word

def get_nick_name() -> str:
    """ 获取提醒昵称 """
    filepath_nickname = "python_files/coolq_of_xiaozhang/database/nick_name.txt"
    with open(filepath_nickname) as obj_file:
        lines = obj_file.readlines()  # 形成一个列表
        count_name = randint(0, len(lines)-1)
        nick_name = lines[count_name]
    return nick_name


def get_morning_word() -> str:
    """ 从早安语录中抽出一条，获得早安提醒 """
    filepath_words = "python_files/coolq_of_xiaozhang/database/morning_words.txt"
    with open(filepath_words) as obj_file:
        lines = obj_file.readlines()  # 形成一个列表
        count_word = randint(0, len(lines)-1)
        morning_word = lines[count_word]   
    return morning_word   