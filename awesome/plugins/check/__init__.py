#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  22:37
# 文件名 ： check.py
# 开发工具： PyCharm
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from ..common_package.get_current_task import get_current_task
from nonebot import MessageSegment
from ..common_package.get_name import get_nickname
from ..plan import get_task


@on_command('打卡')
async def check(session: CommandSession):
    n_name = get_nickname(session)
    current_task = await get_current_task(n_name)
    arg = session.get('', prompt=n_name + '，你要打卡哪个任务呢')

    if not current_task:
        await session.send(MessageSegment.at(id) + n_name + '，你今天的任务都完成啦！饺子夸你哦！么么哒！')
    else:
        await session.send(MessageSegment.at(id) + n_name + '当前的计划列表是：')
        for i in range(len(current_task)):
            await session.send(str(i + 1) + ' ' + current_task[i].strip())

        await get_check_command(session, n_name, arg)


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'打卡'})
async def _():
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, '打卡')


async def check_task(arg, n_name):
    """ 打卡函数,若任务存在则删除,返回对应信息，不存在返回信息 """
    tasks = await get_current_task(n_name) # 获取任务
    if arg in tasks:
        tasks.remove(arg)
        await get_task(tasks, n_name)  # 把删除后的任务写入文件
        content = n_name + '打卡“' + arg + '” 成功'
    else:
        content = n_name + '，不要骗饺子哦，你根本没有这个计划！'

    return content
        
async def result_of_check(session: CommandSession, n_name):
    tasks = await get_current_task(n_name)
    if type(tasks) == list:
        if tasks:
            await session.send(n_name + '你当前的任务为:')
            for i in range(len(tasks)):
                await session.send(str(i + 1) + ' ' + tasks[i])
        else:
            await session.send(n_name + '，你今天的任务都完成啦！饺子夸你哦！么么哒！')
    else:
        await session.send(tasks)


async def get_check_command(session, n_name, arg):
    """ 获取任务并打卡 """
    # arg = session.get('', prompt=n_name + '，你要打卡哪个任务呢')
    content = await check_task(arg, n_name)
    await session.send(content)  # 向用户发送信息
    await result_of_check(session, n_name)
