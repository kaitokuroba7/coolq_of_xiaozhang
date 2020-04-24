#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  18:20
# 文件名 ： add_new_job.py
# 开发工具： PyCharm
import datetime
from apscheduler.triggers.date import DateTrigger # 一次性触发器
from nonebot import on_command, scheduler
from aiocqhttp.exceptions import Error as CQHttpError
from ..common_package.get_name import get_nickname
from nonebot import MessageSegment
import random
import nonebot


@nonebot.scheduler.scheduled_job('cron', hour=0, minute=1)
async def _():

    delta = datetime.timedelta(hours=random.randint(9,23), minutes= random.randint(1, 58))
    # delta = datetime.timedelta(minutes=1)
    trigger = DateTrigger(
        run_date=datetime.datetime.now() + delta 
    )
    bot = nonebot.get_bot()
    try:
        await bot.send_private_msg(user_id=1027380683, message='任务在%s发送' %str(trigger))

    except CQHttpError:
        pass
    """ 获取情话 """
    filepath = "python_files/coolq_of_xiaozhang/lover's prattle.txt"
    with open(filepath) as obj_file:
        lines = obj_file.readlines()
        word = lines[0]
        lines.pop(0)
        content = ''.join(lines)
    bot = nonebot.get_bot()
    # 添加任务
    scheduler.add_job(
        func=bot.send_private_msg,  # 要添加任务的函数，不要带参数
        trigger=trigger,  # 触发器
        # args=(1027380683, '小王5',),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
        kwargs={'user_id':844814749, 'message':'小王~'+word.strip()},
        misfire_grace_time=60,  # 允许的误差时间，建议不要省略
        jobstore='default',  # 任务储存库，在下一小节中说明
    )
    with open(filepath, 'w') as obj_file:
        obj_file.write(content)





