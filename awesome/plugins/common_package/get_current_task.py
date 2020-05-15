#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  17:56
# 文件名 ： get_current_task.py
# 开发工具： PyCharm
"""
获取当前的任务列表
返回值为列表，不带反斜杠
"""

async def get_current_task(n_name):
    new_contents = []
    if n_name == '小张':
        filepath = 'python_files/coolq_of_xiaozhang/database/task_of_xiaozhang.txt'
        with open(filepath) as f_obj:
            contents = f_obj.readlines()
            for content in contents:
                new_contents.append(content.strip())

    elif n_name == '小王':
        filepath = 'python_files/coolq_of_xiaozhang/database/task_of_xiaowang.txt'
        with open(filepath) as f_obj:
            contents = f_obj.readlines()
            for content in contents:
                new_contents.append(content.strip())

    return new_contents