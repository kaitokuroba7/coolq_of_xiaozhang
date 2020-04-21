#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  16:30
# 文件名 ： get_name.py
# 开发工具： PyCharm
"""
输入id号，返回昵称
"""
from nonebot import on_command, CommandSession


def get_nickname(session: CommandSession):
    usr_id = session.event.user_id
    if usr_id == 1027380683:
        n_name = '小张'
    elif usr_id == 844814749:
        n_name = '小王'
    return n_name
