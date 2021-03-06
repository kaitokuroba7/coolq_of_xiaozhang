#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  14:02
# 文件名 ： my_task.py
# 开发工具： PyCharm
from nonebot import MessageSegment
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from ..common_package.get_name import get_nickname
from ..common_package.get_current_task import get_current_task
# 任务列表的读取

@on_command('My_task')
async def _(session: CommandSession):
    n_name = get_nickname(session)  # 得到昵称
    tasks = await get_current_task(n_name)
    if not tasks:
        await session.send(MessageSegment.at(id) + n_name + '，你今天的任务都完成啦！饺子夸你哦！么么哒！')
    elif tasks:
        await session.send(MessageSegment.at(id) + n_name + '你的当前任务是')
        for i in range(len(tasks)):
            await session.send(str(i + 1) + ' ' + tasks[i])


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'列表'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'My_task')




