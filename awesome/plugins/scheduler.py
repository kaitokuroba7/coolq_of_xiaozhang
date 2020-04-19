from datetime import datetime

import nonebot
from nonebot import MessageSegment
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))

    if now.weekday() == 3 and now.hour == 20:
        try:
            await bot.send_group_msg(group_id=1064439850,
                                     message='小王，小王！《青春有你2》开始啦，快去看吧！')
        except CQHttpError:
            pass

    if now.weekday() == 5 and now.hour == 20:
        try:
            await bot.send_group_msg(group_id=1064439850,
                                     message='小王，小王！《青春有你2》开始啦，快去看吧！')
        except CQHttpError:
            pass

    if now.hour == 23:
        try:
            await bot.send_group_msg(group_id=1064439850,
                                     message='要上床啦，晚安，小王！晚安，小张！')
        except CQHttpError:
            pass

    if now.hour == 0:
        try:
            await bot.send_group_msg(group_id=1064439850,
                                     message=MessageSegment.at(844814749) + '睡觉啦，睡觉啦，小王明天还要考研，实习，改论文！')
        except CQHttpError:
            pass

    if now.hour == 24:
        try:
            await bot.send_group_msg(group_id=1064439850,
                                     message=MessageSegment.at(844814749) + '睡觉啦，睡觉啦，小王明天还要考研，实习，改论文！')
        except CQHttpError:
            pass

    if now.hour == 17:
        try:
            await bot.send_group_msg(group_id=1064439850,
                                     message=MessageSegment.at(844814749) + MessageSegment.at(1027380683) +
                                     '傍晚好，小王，小张，你们吃晚饭了嘛！')
        except CQHttpError:
            pass

    if now.hour == 9:
        try:
            await bot.send_group_msg(group_id=1064439850,
                                     message='早安啊，小王！早安啊，小张！你们有没有互道早安呢！')
        except CQHttpError:
            pass

    if now.hour > 7:
        try:
            await bot.send_group_msg(group_id=1064439850,
                                     message=f'饺子来报时啦！现在是北京时间{now.hour}点整啦！')
            await bot.send_group_msg(group_id=1064439850,
                                     message='饺子懂事又可爱，饺子一直陪着你们哦~')
        except CQHttpError:
            pass
