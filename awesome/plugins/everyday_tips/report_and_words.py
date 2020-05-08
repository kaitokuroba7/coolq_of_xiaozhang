from nonebot import MessageSegment
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
from ..common_package.get_love_word import get_love_word
from ..common_package.morning_report import plot_morning_get_up
from ..common_package.get_love_word import remove_get_up_time
from ..common_package.config import QQ_ID
from .import library
import datetime
""" 发给小王的信息，里面包含了起床时间报告，傍晚的悄悄话以及晚上睡觉的提醒 """

# 在每天的晚上19：45发布起床报告
@nonebot.scheduler.scheduled_job('cron', hour=19, minute=45)
async def get_up_time_report():
    """ 最近七天的起床报告 """
    bot = nonebot.get_bot()
    now = datetime.datetime.now()
    
    try:
        plot_morning_get_up()
        await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                message=MessageSegment.image('%s.png' %str(now.date())))
        await bot.send_private_msg(user_id=QQ_ID.xiaowang(),message='小王~你的起床时间统计来啦，饺子做的哦~')                       
        await bot.send_private_msg(user_id=QQ_ID.xiaowang(),message=MessageSegment.image('%s.png' %str(now.date())) )
    except CQHttpError:
        pass


# 在每日的16：10 添加饺子的情话
@nonebot.scheduler.scheduled_job('cron', hour=16, minute=10)
async def love_word_at_dusk():
    """ 傍晚的情话 """
    bot = nonebot.get_bot()
    word = get_love_word()
    try: 
        await bot.send_group_msg(group_id=QQ_ID.our_group(), message=MessageSegment.at(QQ_ID.xiaowang()))                                     
        await bot.send_group_msg(group_id=QQ_ID.our_group(), message='小王~'+word.rstrip()) 
        await bot.send_private_msg(user_id=QQ_ID.xiaowang(), message='小王~'+word.rstrip())                     
        # await bot.send_private_msg(user_id=QQ_ID.xiaowang(), message='饺子P的照片~')
        # await bot.send_private_msg(user_id=1027380683, message=MessageSegment.image('2020-05-03.png'))
    except CQHttpError:
        pass


# 不睡觉提醒
@nonebot.scheduler.scheduled_job('cron', hour=0, minute=29)
async def sleep_tip():
    """ 0：30的提醒 """
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                 message=MessageSegment.at(QQ_ID.xiaowang()) + ' 好啦，快睡觉吧小王！你不睡饺子睡不着~')
        await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                 message=MessageSegment.at(QQ_ID.xiaozhang()) + '晚安小张~')

    except CQHttpError:
        pass
