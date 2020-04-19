#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  22:37
# 文件名 ： check.py
# 开发工具： PyCharm
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .my_task import show_task
from nonebot import MessageSegment

@on_command('check')
async def check(session: CommandSession):
    id = session.event.user_id
    if id == 1027380683:
        n_name = '小张'
    elif id == 844814749:
        n_name = '小王'
    current_task = await show_task(n_name)

    if not current_task:
        await session.send(MessageSegment.at(id) + n_name + '，你今天的任务都完成啦！饺子夸你哦！么么哒！')
    else:
        await session.send(MessageSegment.at(id) + n_name + '当前的计划列表是：')
        for i in range(len(current_task)):
            await session.send(str(i + 1) + ' ' + current_task[i])

        await get_check_command(session, n_name)


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'打卡'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'check')


async def check_task(arg, n_name):
    """" 打卡函数 """
    if n_name == '小张':
        filename = 'xiaozhang_task.txt'
    elif n_name == '小王':
        filename = 'xiaowang_task.txt'
    with open(filename) as f_obj:
        content = f_obj.read()
        content = content.split()
        if arg in content:
            content.remove(arg)
            with open(filename, 'w') as f_obj:
                f_obj.write(' '.join(content))
        else:
            content = n_name + '，不要骗饺子哦，你根本没有这个计划！'
    return content


async def result_of_check(session: CommandSession, tasks, arg, n_name):
    if type(tasks) == list:
        if tasks:
            await session.send(n_name + '打卡“' + arg + '”成功，你还没有完成的计划是')
            for i in range(len(tasks)):
                await session.send(str(i + 1) + ' ' + tasks[i])
        else:
            await session.send(n_name + '，你今天的任务都完成啦！饺子夸你哦！么么哒！')
    else:
        await session.send(tasks)


async def get_check_command(session, n_name):
    """ 获取任务并打卡 """
    arg = session.get('', prompt=n_name + '，你要打卡哪个任务呢')
    tasks = await check_task(arg, n_name)
    await result_of_check(session, tasks, arg, n_name)

