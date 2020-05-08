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
from ..common_package.get_love_word import remove_get_up_time
from .import library
from .import everyday_plan
import datetime
"""
这个模块里有每日的打卡提醒、天气提醒、制定计划提醒、睡觉的提醒
这里的时间都是任意的
"""

# 图书馆签到签退
library.sign_in_9_20()
library.sign_out_15_50()
library.sign_in_17_10()
library.sign_out_19_40()


# 每日任务提醒
everyday_plan.everyday_new_plan()
everyday_plan.xiaowang_plan_finish_situation()
everyday_plan.xiaozhang_plan_finish_situation()

# 在每日的16：10 添加饺子的情话
@nonebot.scheduler.scheduled_job('cron', hour=16, minute=10)
async def _():
    """ 傍晚的情话 """
    bot = nonebot.get_bot()
    word = get_love_word()
    try: 
        await bot.send_group_msg(group_id=1064439850, message=MessageSegment.at(844814749))                                     
        await bot.send_group_msg(group_id=1064439850, message='小王~'+word.rstrip()) 
        await bot.send_private_msg(user_id=844814749, message='小王~'+word.rstrip())                     
        # await bot.send_private_msg(user_id=844814749, message='饺子P的照片~')
        # await bot.send_private_msg(user_id=1027380683, message=MessageSegment.image('2020-05-03.png'))
    except CQHttpError:
        pass


# 测试临时任务
@nonebot.scheduler.scheduled_job('cron', hour=21, minute=35)
async def _():
    """ 临时任务 """
    bot = nonebot.get_bot()
    now = datetime.datetime.now()
    if str(now.date()) == '2020-05-06':
        try:
            # plot_morning_get_up()
            filepath_get_up_time = "python_files/coolq_of_xiaozhang/database/get_up_time_of_xiaozhang.txt"
            remove_get_up_time(filepath_get_up_time)
            #await bot.send_group_msg(group_id=1064439850,
                                    #message=MessageSegment.image('%s.png' %str(now.date())))
            await bot.send_private_msg(user_id=844814749,message='小王~快看~饺子给你做的图~')                       
            await bot.send_private_msg(user_id=844814749,message=MessageSegment.image('wanan.jpg'))
        except CQHttpError:
            pass


# 在每天的晚上19：45发布起床报告
@nonebot.scheduler.scheduled_job('cron', hour=19, minute=45)
async def _():
    """ 早起报告 """
    bot = nonebot.get_bot()
    now = datetime.datetime.now()
    try:
        plot_morning_get_up()
        await bot.send_group_msg(group_id=1064439850,
                                message=MessageSegment.image('%s.png' %str(now.date())))
        await bot.send_private_msg(user_id=844814749,message='小王~你的起床时间统计来啦，饺子做的哦~')                       
        await bot.send_private_msg(user_id=844814749,message=MessageSegment.image('%s.png' %str(now.date())) )
    except CQHttpError:
        pass






# 小王的天气提醒任务
@nonebot.scheduler.scheduled_job('cron', hour=7, minute=45)
async def _():
    """ 小王的天气提醒 """
    bot = nonebot.get_bot()
    weather_rep = await get_weather_of_city('江北')
    try:
        #await bot.send_group_msg(group_id=1064439850,
                             #    message=MessageSegment.at(844814749) + ' 早上好，饺子来预报天气啦！')
        #await bot.send_group_msg(group_id=1064439850,
                                # message='小王，' + weather_rep + '小王，饺子爱你噢！')

        await bot.send_private_msg(user_id=844814749,
                                 message=' 早上好，饺子来预报天气啦！')
        await bot.send_private_msg(user_id=844814749,
                                 message='小王，' + weather_rep + '小王，饺子爱你噢！')
    except CQHttpError:
        pass


# 小王的天气提醒任务
@nonebot.scheduler.scheduled_job('cron', hour=7, minute=6)
async def _():
    """ 小张的天气提醒 """
    bot = nonebot.get_bot()
    weather_rep = await get_weather_of_city('宁波')
    try:
        await bot.send_group_msg(group_id=1064439850,
                                 message=MessageSegment.at(1027380683) + ' 早上好，饺子来预报天气啦！')
        await bot.send_group_msg(group_id=1064439850,
                                 message='小张，' + weather_rep)
    except CQHttpError:
        pass


# 不睡觉提醒
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



