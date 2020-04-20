#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  18:20
# 文件名 ： add_new_job.py
# 开发工具： PyCharm
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg
import datetime
from apscheduler.triggers.date import DateTrigger # 一次性触发器
from nonebot import on_command, scheduler
from .get_name import get_nickname
from nonebot import MessageSegment


@on_command('tip')
async def _(session: CommandSession):
    usr_id = session.event.user_id
    n_name = get_nickname(session)
    text = session.get('city', prompt=n_name + '需要饺子提醒什么呢？ '
                                               '格式为:提示事项 时间'
                                               '(时间格式为04201200)代表4月20日12:00')
    # session.pause('什么时候提醒你呀？')
    # news_time = session.get('city', prompt=n_name + '格式是0420 02:22')
    text_list = text.split()
    news_time = text_list[1] + ' 2020'
    # newsTime = '0404 15:50'
    GMT_FORMAT = '%m%d%H%M %Y'

    try:
        newsTime = datetime.datetime.strptime(news_time, GMT_FORMAT)
        try:
            print(text_list[2])
        except IndexError:
            text_list.append('无')
        if text_list[2] == '无':
            pass
        elif text_list[2] == '小王':
            usr_id = 844814749
            n_name = '小王'
        elif text_list[2] == '小张':
            usr_id = 1027380683
            n_name = '小张'

        await session.send(MessageSegment.face(21)
                           + '开心！计划任务成功！饺子将在北京时间'
                             '“%s”提醒你哦~' % newsTime)
        trigger = DateTrigger(
            run_date=newsTime
        )

        # 添加任务
        scheduler.add_job(
            func=session.send,  # 要添加任务的函数，不要带参数
            trigger=trigger,  # 触发器
            args=(MessageSegment.at(usr_id) + n_name + "，饺子提醒你去“" + text_list[0] + '”啦',),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
            # kwargs=None,
            misfire_grace_time=60,  # 允许的误差时间，建议不要省略
            jobstore='default',  # 任务储存库，在下一小节中说明
        )
    except ValueError:
        await session.send("日期匹配错误，重新唤醒一下饺子吧！")




# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'提醒'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'tip')