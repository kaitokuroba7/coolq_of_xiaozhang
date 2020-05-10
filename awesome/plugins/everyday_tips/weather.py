from nonebot import MessageSegment
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
from ..weather.data_source import get_weather_of_city
from ..common_package.config import QQ_ID

# 小王的天气提醒任务
@nonebot.scheduler.scheduled_job('cron', hour=7, minute=45)
async def weather_of_wang():
    """ 小王的天气提醒 """
    bot = nonebot.get_bot()
    weather_rep = await get_weather_of_city('江北')
    try:
        #await bot.send_group_msg(group_id=QQ_ID.our_group(),
                             #    message=MessageSegment.at(QQ_ID.xiaowang()) + ' 早上好，饺子来预报天气啦！')
        #await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                # message='小王，' + weather_rep + '小王，饺子爱你噢！')

        await bot.send_private_msg(user_id=QQ_ID.xiaowang(),
                                 message=' 早上好，饺子来预报天气啦！')
        await bot.send_private_msg(user_id=QQ_ID.xiaowang(),
                                 message='小王，' + weather_rep + '小王，饺子爱你噢！')
    except CQHttpError:
        pass


# 小张的天气提醒任务
@nonebot.scheduler.scheduled_job('cron', hour=7, minute=6)
async def weather_of_zhang():
    """ 小张的天气提醒 """
    bot = nonebot.get_bot()
    weather_rep = await get_weather_of_city('宁波')
    try:
        await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                 message=MessageSegment.at(QQ_ID.xiaozhang()) + ' 早上好，饺子来预报天气啦！')
        await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                 message='小张，' + weather_rep)
    except CQHttpError:
        pass


# 小孙的天气提醒任务
@nonebot.scheduler.scheduled_job('cron', hour=7, minute=7)
async def weather_of_sun():
    """ 小孙的天气提醒 """
    bot = nonebot.get_bot()
    weather_rep = await get_weather_of_city('杭州')
    try:
        await bot.send_private_msg(user_id=QQ_ID.xiaosun(),
                                 message=' 早上好，饺子来预报天气啦！')
        await bot.send_private_msg(user_id=QQ_ID.xiaosun(),
                                 message='小孙，' + weather_rep )
    except CQHttpError:
        pass
