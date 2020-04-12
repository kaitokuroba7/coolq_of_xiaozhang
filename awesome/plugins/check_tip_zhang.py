#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  12:46
# 文件名 ： check_tip.py
# 开发工具： PyCharm
from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour=21, minute=10)
async def _():
    """ 小张的提醒 """
    bot = nonebot.get_bot()
    # now = datetime.now(pytz.timezone('Asia/Shanghai'))

    try:
        n_name = '小张'
        current_task = await get_current_task(n_name)
        if not current_task:
            await bot.send_group_msg(group_id=1064439850,
                                     message='小张今天的任务都做完啦！饺子夸你哦！')
        if current_task:
            await bot.send_group_msg(group_id=1064439850,
                                     message='小张今天还没完成的任务')

            for i in range(len(current_task)):
                await bot.send_group_msg(group_id=1064439850,
                                         message=str(i + 1) + ' ' + current_task[i])

            await bot.send_group_msg(group_id=1064439850,
                                     message='撸起袖子加油干！')

    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour=21, minute=5)
async def _():
    """ 小王的提醒 """
    bot = nonebot.get_bot()
    # now = datetime.now(pytz.timezone('Asia/Shanghai'))

    try:
        n_name = '小王'
        current_task = await get_current_task(n_name)
        if not current_task:
            await bot.send_group_msg(group_id=1064439850,
                                     message='小王今天的任务都做完啦！饺子夸你哦！')
        if current_task:
            await bot.send_group_msg(group_id=1064439850,
                                     message='小王今天还没完成的任务')

            for i in range(len(current_task)):
                await bot.send_group_msg(group_id=1064439850,
                                         message=str(i + 1) + ' ' + current_task[i])

            await bot.send_group_msg(group_id=1064439850,
                                     message='小王，撸起袖子加油干！')

    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour=8, minute=30)
async def _():
    """ 提醒任务制定 """
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=1064439850,
                                 message='新的一天，把今天的任务告诉饺子吧！')
    except CQHttpError:
        pass


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
