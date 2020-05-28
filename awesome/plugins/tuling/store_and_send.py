from ..common_package.date_tag import get_time_tag
from ..common_package.date_tag import write_time_tag
from ..common_package.date_tag import write_get_up_time
import nonebot
import datetime

async def store_and_send_message(name: str, message: str):
    """ 消息转达以及早起时间记录 """
    bot = nonebot.get_bot()
    if name == '小王':
        if '~' in message.strip():
            await bot.send_private_msg(user_id=1027380683, message='小王的消息：'+message)
        time = datetime.datetime.now()
        if time.hour >6 and time.hour < 22 :
            filepath_time_tag = "python_files/coolq_of_xiaozhang/database/date.txt"
            filepath_get_up_time = "python_files/coolq_of_xiaozhang/database/get_up_time.txt"
            time_in_txt = get_time_tag(filepath_time_tag)
            if time_in_txt != str(time.date()):
                write_time_tag(filepath_time_tag) 
                write_get_up_time(filepath_get_up_time)
                await bot.send_private_msg(user_id=844814749, message='小王，饺子收到你的起床时间啦~')
    if name == '小张':
        if '~' in message.strip():
            await bot.send_private_msg(user_id=844814749, message='小张的消息：'+message)
        
        time = datetime.datetime.now()
        if time.hour >6 and time.hour < 15:
            filepath_time_tag = "python_files/coolq_of_xiaozhang/database/date_of_xiaozhang.txt"
            filepath_get_up_time = "python_files/coolq_of_xiaozhang/database/get_up_time_of_xiaozhang.txt"
            time_in_txt = get_time_tag(filepath_time_tag)
            if time_in_txt != str(time.date()):
                write_time_tag(filepath_time_tag) 
                write_get_up_time(filepath_get_up_time)
                await bot.send_private_msg(user_id=1027380683, message='小张，今日起床时间已经查收')
    if name == 'other':
        pass