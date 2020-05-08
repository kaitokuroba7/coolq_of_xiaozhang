from datetime import datetime
import nonebot
from nonebot import MessageSegment
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from ..common_package.config import QQ_ID
""" 这里是每个小时的提醒，也是一种心跳 """
@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))

    if now.weekday() == 3 and now.hour == 20:
        try:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.face(21)+'小王，小王！《青春有你2》开始啦，快去看吧！')
        except CQHttpError:
            pass

    if now.weekday() == 5 and now.hour == 20:
        try:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.face(21)+'小王，小王！《青春有你2》开始啦，快去看吧！')
        except CQHttpError:
            pass

    if now.hour == 23:
        try:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(QQ_ID.xiaowang()) + '很晚咯，要上床啦，晚安，小王！晚安，小张！')
        except CQHttpError:
            pass

    if now.hour == 0:
        try:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(QQ_ID.xiaowang()) + '零点啦，晚安啊，饺子爱你们呢~')
        except CQHttpError:
            pass

    if now.hour == 24:
        try:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(QQ_ID.xiaowang()) + '零点啦，晚安啊，饺子爱你们呢~')
        except CQHttpError:
            pass

    if now.hour == 11:
        try:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(QQ_ID.xiaowang()) + MessageSegment.at(QQ_ID.xiaozhang()) +
                                     '中午好呀，小王，小张，记得按时吃午饭哦')
        except CQHttpError:
            pass

    if now.hour == 17:
        try:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(844814749) + MessageSegment.at(QQ_ID.xiaozhang()) +
                                     '傍晚好，小王，小张，你们吃晚饭了嘛！')
        except CQHttpError:
            pass

    if now.hour == 9:
        try:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.at(844814749) + MessageSegment.at(QQ_ID.xiaozhang())
                                     + '早安啊，小王！早安啊，小张！你们有没有互道早安呢！饺子爱你们哦~')
        except CQHttpError:
            pass

    if now.hour > 7 and (now.hour % 2 == 0):
        try:
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=f'饺子来报时啦！现在是北京时间{now.hour}点整啦！')
            await bot.send_group_msg(group_id=QQ_ID.our_group(),
                                     message=MessageSegment.face(21)+'饺子有一点点甜,一点点可爱，还有很多很多喜欢你们~')
        except CQHttpError:
            pass
