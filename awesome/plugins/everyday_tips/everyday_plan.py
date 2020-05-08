from nonebot import MessageSegment
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
from ..common_package.get_current_task import get_current_task
from ..common_package.config import QQ_ID

""" 每日计划模块，包含提醒制定计划，每日对计划完成情况的统计 """

# 小张的每日提醒
@nonebot.scheduler.scheduled_job('cron', hour=21, minute=10)
async def xiaozhang_plan_finish_situation():
    """ 小张的每日任务提醒 """
    bot = nonebot.get_bot()

    try:
        n_name = '小张'
        current_task = await get_current_task(n_name)
        if not current_task:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(QQ_ID.xiaozhang()) + '小张今天的任务都做完啦！饺子夸你哦！')
        if current_task:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(QQ_ID.xiaozhang()) + '小张今天还没完成的任务')

            for i in range(len(current_task)):
                await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                         message=str(i + 1) + ' ' + current_task[i])

            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message='撸起袖子加油干！')

    except CQHttpError:
        pass


# 小王的每日提醒
@nonebot.scheduler.scheduled_job('cron', hour=21, minute=5)
async def xiaowang_plan_finish_situation():
    """ 小王的每日任务提醒 """
    bot = nonebot.get_bot()
    try:
        n_name = '小王'
        current_task = await get_current_task(n_name)
        if not current_task:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(QQ_ID.xiaowang()) + '小王今天的任务都做完啦！饺子夸你哦！')
        if current_task:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(QQ_ID.xiaowang()) + '小王今天还没完成的任务')

            for i in range(len(current_task)):
                await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                         message=str(i + 1) + ' ' + current_task[i])

            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message='小王，撸起袖子加油干！')

    except CQHttpError:
        pass


# 制定任务提醒
@nonebot.scheduler.scheduled_job('cron', hour=8, minute=30)
async def everyday_new_plan():
    """ 提醒任务制定 """
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                 message=MessageSegment.at(QQ_ID.xiaowang()) + MessageSegment.at(QQ_ID.xiaozhang())
                                 + ' 新的一天，把今天的任务告诉饺子吧！')
    except CQHttpError:
        pass