#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  17:56
# 文件名 ： get_current_task.py
# 开发工具： PyCharm
"""
获取当前的任务列表
"""


async def get_current_task(n_name):
    if n_name == '小张':
        with open('xiaozhang_task.txt') as f_obj:
            content = f_obj.read()
            content = content.split()

    elif n_name == '小王':
        with open('xiaowang_task.txt') as f_obj:
            content = f_obj.read()
            content = content.split()

    return content