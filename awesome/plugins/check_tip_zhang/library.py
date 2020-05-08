from nonebot import MessageSegment
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError

""" 图书馆打卡模块，包含了签到打卡 ，签退打卡 """

# 图书管打卡任务 上午9：20
@nonebot.scheduler.scheduled_job('cron', hour=9, minute=20)
async def sign_in_9_20():
    """ 在9：20分发布签到任务 """
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=1064439850,
                                message=MessageSegment.at(1027380683)+'大笨蛋同学，签到打卡了！')
        await bot.send_group_msg(group_id=1064439850,
                                message=MessageSegment.image('tushuguan.jpg'))
        await bot.send_private_msg(user_id=844814749,message='小王~帮饺子个忙，提醒一下小张打卡哦~')                       
        # await bot.send_private_msg(user_id=844814749,message=MessageSegment.image('wanan.jpg'))
    except CQHttpError:
        pass



# 图书管打卡任务 下午15：50
@nonebot.scheduler.scheduled_job('cron', hour=15, minute=50)
async def sign_out_15_50():
    """ 在15：50发布签退任务 """
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=1064439850,
                                message=MessageSegment.at(1027380683)+'大笨蛋同学，签退打卡了！')
        await bot.send_group_msg(group_id=1064439850,
                                message=MessageSegment.image('tushuguan.jpg'))
        # await bot.send_private_msg(user_id=844814749,message='小王~提醒一下小张打卡哦~')                       
        # await bot.send_private_msg(user_id=844814749,message=MessageSegment.image('wanan.jpg'))
    except CQHttpError:
        pass

# 图书管打卡任务 下午17：10
@nonebot.scheduler.scheduled_job('cron', hour=17, minute=10)
async def sign_in_17_10():
    """ 在17：10分发布签到任务 """
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=1064439850,
                                message=MessageSegment.at(1027380683)+'大笨蛋同学，签到打卡了！')
        await bot.send_group_msg(group_id=1064439850,
                                message=MessageSegment.image('tushuguan.jpg'))
        # await bot.send_private_msg(user_id=844814749,message='小王~提醒一下小张打卡哦~')                       
        # await bot.send_private_msg(user_id=844814749,message=MessageSegment.image('wanan.jpg'))
    except CQHttpError:
        pass

# 图书管打卡任务 下午19：50
@nonebot.scheduler.scheduled_job('cron', hour=19, minute=40)
async def sign_out_19_40():
    """ 在19：40分发布签退任务 """
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=1064439850,
                                message=MessageSegment.at(1027380683)+'大笨蛋同学，签退打卡了！')
        await bot.send_group_msg(group_id=1064439850,
                                message=MessageSegment.image('tushuguan.jpg'))
        await bot.send_private_msg(user_id=844814749,message='小王~提醒一下小张打卡哦~')                       
        # await bot.send_private_msg(user_id=844814749,message=MessageSegment.image('wanan.jpg'))
    except CQHttpError:
        pass


