#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  12:46
# 文件名 ： check_tip.py
# 开发工具： PyCharm
from nonebot import MessageSegment
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
from ..weather.data_source import get_weather_of_city
from ..common_package.get_current_task import get_current_task
from ..common_package.get_love_word import get_love_word
from ..common_package.morning_report import plot_morning_get_up
import datetime
"""
这个模块里有每日的打卡提醒、天气提醒、制定计划提醒、睡觉的提醒
"""


@nonebot.scheduler.scheduled_job('cron', hour=17, minute=30)
async def _():
    """ 饺子的每日情话 """
    word = get_love_word()
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=1064439850, message=MessageSegment.at(844814749))
        await bot.send_group_msg(group_id=1064439850, message='小王~'+word.rstrip())                      
        # await bot.send_private_msg(user_id=844814749, message='小王~'+word.strip())
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour=22, minute=29)
async def _():
    """ 早期报告 """
    bot = nonebot.get_bot()
    now = datetime.datetime.now()
    try:
        plot_morning_get_up()
        await bot.send_group_msg(group_id=1064439850,
                                    message=MessageSegment.image('%s.png' %str(now.date())))
    except CQHttpError:
        pass




@nonebot.scheduler.scheduled_job('cron', hour=21, minute=10)
async def _():
    """ 小张的每日任务提醒 """
    bot = nonebot.get_bot()

    try:
        n_name = '小张'
        current_task = await get_current_task(n_name)
        if not current_task:
            await bot.send_group_msg(group_id=1064439850,
                                     message=MessageSegment.at(1027380683) + '小张今天的任务都做完啦！饺子夸你哦！')
        if current_task:
            await bot.send_group_msg(group_id=1064439850,
                                     message=MessageSegment.at(1027380683) + '小张今天还没完成的任务')

            for i in range(len(current_task)):
                await bot.send_group_msg(group_id=1064439850,
                                         message=str(i + 1) + ' ' + current_task[i])

            await bot.send_group_msg(group_id=1064439850,
                                     message='撸起袖子加油干！')

    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour=21, minute=5)
async def _():
    """ 小王的每日任务提醒 """
    bot = nonebot.get_bot()
    try:
        n_name = '小王'
        current_task = await get_current_task(n_name)
        if not current_task:
            await bot.send_group_msg(group_id=1064439850,
                                     message=MessageSegment.at(844814749) + '小王今天的任务都做完啦！饺子夸你哦！')
        if current_task:
            await bot.send_group_msg(group_id=1064439850,
                                     message=MessageSegment.at(844814749) + '小王今天还没完成的任务')

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
                                 message=MessageSegment.at(844814749) + MessageSegment.at(1027380683)
                                 + ' 新的一天，把今天的任务告诉饺子吧！')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour=7, minute=5)
async def _():
    """ 小王的天气提醒 """
    bot = nonebot.get_bot()
    weather_rep = await get_weather_of_city('奉化')
    try:
        await bot.send_group_msg(group_id=1064439850,
                                 message=MessageSegment.at(844814749) + ' 早上好，饺子来预报天气啦！')
        await bot.send_group_msg(group_id=1064439850,
                                 message='小王，' + weather_rep + '小王，饺子爱你噢！')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour=7, minute=6)
async def _():
    """ 小张的天气提醒 """
    bot = nonebot.get_bot()
    weather_rep = await get_weather_of_city('舟山')
    try:
        await bot.send_group_msg(group_id=1064439850,
                                 message=MessageSegment.at(1027380683) + ' 早上好，饺子来预报天气啦！')
        await bot.send_group_msg(group_id=1064439850,
                                 message='小张，' + weather_rep)
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour=0, minute=29)
async def _():
    """ 0：30的提醒 """
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=1064439850,
                                 message=MessageSegment.at(844814749) + ' 好啦，快睡觉吧小王！你不睡饺子睡不着~')
        await bot.send_group_msg(group_id=1064439850,
                                 message=MessageSegment.at(1027380683) + '晚安小张~')

    except CQHttpError:
        pass



