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
from ..common_package.get_love_word import get_love_word
from nonebot import MessageSegment
import random
import nonebot


@nonebot.scheduler.scheduled_job('cron', hour=0, minute=1)
async def _():
    """ 在随机时间增加饺子的悄悄话 """
    delta = datetime.timedelta(hours=random.randint(12,15), minutes= random.randint(1, 58))
    # delta = datetime.timedelta(minutes=1)
    trigger = DateTrigger(
        run_date=datetime.datetime.now() + delta 
    )
    bot = nonebot.get_bot()
    try:
        await bot.send_private_msg(user_id=1027380683, message='饺子的情话任务在%s发送' %str(trigger))

    except CQHttpError:
        pass
    """ 获取情话 """
    word = get_love_word()
    bot = nonebot.get_bot()
    # 添加任务
    scheduler.add_job(
        func=bot.send_private_msg,  # 要添加任务的函数，不要带参数
        trigger=trigger,  # 触发器
        # args=(1027380683, '小王5',),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
        kwargs={'user_id':844814749, 'message':'小王~'+word.strip()+' ~来自饺子的悄悄话~'},
        misfire_grace_time=60,  # 允许的误差时间，建议不要省略
        jobstore='default',  # 任务储存库，在下一小节中说明
    )


@nonebot.scheduler.scheduled_job('cron', hour=18, minute=45)
async def _():
    """ 在随机时间增加情话 """
    delta = datetime.timedelta(hours=random.randint(1,5), minutes= random.randint(1, 15))
    # delta = datetime.timedelta(minutes=1)
    trigger = DateTrigger(
        run_date=datetime.datetime.now() + delta 
    )
    bot = nonebot.get_bot()
    try:
        await bot.send_private_msg(user_id=1027380683, message='来自小张的情话任务在%s发送' %str(trigger))

    except CQHttpError:
        pass
    """ 获取情话 """
    word = get_love_word()
    bot = nonebot.get_bot()
    # 添加任务
    scheduler.add_job(
        func=bot.send_private_msg,  # 要添加任务的函数，不要带参数
        trigger=trigger,  # 触发器
        # args=(1027380683, '小王5',),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
        kwargs={'user_id':844814749, 'message':'来自小张的情话：小王~'+word.strip()+' ~~饺子抄送~~'},
        misfire_grace_time=60,  # 允许的误差时间，建议不要省略
        jobstore='default',  # 任务储存库，在下一小节中说明
    )



@nonebot.scheduler.scheduled_job('cron', hour=8, minute=1)
async def _():
    """ 早安功能 """
    delta = datetime.timedelta(minutes= random.randint(1, 58))
    # delta = datetime.timedelta(minutes=1)
    trigger = DateTrigger(
        run_date=datetime.datetime.now() + delta 
    )
    bot = nonebot.get_bot()
    try:
        await bot.send_private_msg(user_id=1027380683, message='早安任务在%s发送' %str(trigger))

    except CQHttpError:
        pass
    bot = nonebot.get_bot()
    # 添加任务
    scheduler.add_job(
        func=bot.send_private_msg,  # 要添加任务的函数，不要带参数
        trigger=trigger,  # 触发器
        # args=(1027380683, '小王5',),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
        kwargs={'user_id':844814749, 'message':'早安啊，小王~ 今天饺子和小张也喜欢你~'},
        misfire_grace_time=60,  # 允许的误差时间，建议不要省略
        jobstore='default',  # 任务储存库，在下一小节中说明
    )

