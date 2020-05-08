#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  12:46
# 文件名 ： check_tip.py
# 开发工具： PyCharm
from nonebot import MessageSegment
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
import datetime
from ..common_package.get_current_task import get_current_task
from .import library
from .import everyday_plan
from .import weather
from .import report_and_words

"""
这个模块里有每日的打卡提醒、天气提醒、制定计划提醒、睡觉的提醒、图书馆的提醒
这里的时间都是任意的
"""

# 图书馆签到签退
library.sign_in_9_20()
library.sign_out_15_50()
library.sign_in_17_10()
library.sign_out_19_40()


# 每日任务提醒
everyday_plan.everyday_new_plan()  # 制定新计划
everyday_plan.xiaowang_plan_finish_situation()
everyday_plan.xiaozhang_plan_finish_situation()

# 每日的天气提醒
weather.weather_of_wang() # 小王的天气提醒
weather.weather_of_zhang() # 小张的天气提醒

# 起床报告与傍晚情话
report_and_words.love_word_at_dusk() # 傍晚情话
report_and_words.get_up_time_report() # 起床报告



# 测试临时任务
@nonebot.scheduler.scheduled_job('cron', hour=21, minute=35)
async def _():
    """ 临时任务 """
    bot = nonebot.get_bot()
    now = datetime.datetime.now()
    if str(now.date()) == '2020-05-06':
        try:
            # plot_morning_get_up()
            # filepath_get_up_time = "python_files/coolq_of_xiaozhang/database/get_up_time_of_xiaozhang.txt"
            #await bot.send_group_msg(group_id=1064439850,
                                    #message=MessageSegment.image('%s.png' %str(now.date())))
            await bot.send_private_msg(user_id=844814749,message='小王~快看~饺子给你做的图~')                       
            await bot.send_private_msg(user_id=844814749,message=MessageSegment.image('wanan.jpg'))
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



