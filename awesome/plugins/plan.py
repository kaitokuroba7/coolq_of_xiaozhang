import nonebot
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.default_config import *
import config


@on_command('task', aliases=['使用帮助', '帮助', '使用方法'])
async def _(session: CommandSession):
    id = session.event.user_id
    if id == 1027380683:
        n_name = '小张'
    elif id == 844814749:
        n_name = '小王'
    arg = session.get('city', prompt=n_name + '，你今天的计划是什么呢？')
    await session.send(n_name + '今天的计划是')
    tasks = await get_task(arg, n_name)
    for i in range(len(tasks)):
        await session.send(str(i+1)+' '+tasks[i])


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'制定'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'task')


async def get_task(arg, n_name):
    tasks = arg.split()
    if n_name == '小张':
        with open('xiaozhang_task.txt', 'w') as f_obj:
            f_obj.write(arg)
    elif n_name == '小王':
        with open('xiaowang_task.txt', 'w') as f_obj:
            f_obj.write(arg)
    return tasks

# 添加


