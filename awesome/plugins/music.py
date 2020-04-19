#  _*_ coding:utf-8 _*_
# 程序员：10273
# 开发日期 ：  12:20
# 文件名 ： music.py
# 开发工具： PyCharm
import logging
import asyncio
import re
import time
from typing import Optional

from aiocache import cached
from nonebot import MessageSegment
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.command.argfilter import extractors, validators
import random
import requests

__plugin_name__ = '点歌'

QQ_MUSIC_SEARCH_URL_FORMAT = 'http://music.eleuu.com/search?keywords={''}&format'


@cached(ttl=12 * 60 * 60)
async def search_song_id(keyword: str, session: CommandSession) -> Optional[int]:
    keyword = keyword.strip()
    if not keyword:
        return None
    resp = requests.get(QQ_MUSIC_SEARCH_URL_FORMAT.format(keyword))
    payload = resp.json()
    if not isinstance(payload, dict) or \
            not payload.get('result'):
        return None

    try:
        if payload['result']['songs'][0]['artists'][0]['id'] == 1046043:
            await session.send(MessageSegment.at(844814749)+' 开心，饺子搜到了最爱的女友的歌！')
            i = random.randint(0, 29)
            return payload['result']['songs'][i]['id']

        for i in range(30):
            if payload['result']['songs'][i]['artists'][0]['id'] == 1046043:
                await session.send(MessageSegment.at(844814749)+' 开心，饺子搜到了最爱的女友的歌！')
                return payload['result']['songs'][i]['id']

        if i == 29:
            return payload['result']['songs'][0]['id']

    except (TypeError, KeyError, IndexError):
        return None


@on_command('music', aliases=['点歌', '音乐'], only_to_me=False)
async def music(session: CommandSession):
    id = session.event.user_id
    if id == 1027380683:
        n_name = '小张'
    elif id == 844814749:
        n_name = '小王'
    keyword = session.get('keyword', prompt=n_name+',你想听什么歌呢？',
                          arg_filters=[
                              extractors.extract_text,
                              str.strip,
                              validators.not_empty('歌名不能为空哦，请重新发送')
                          ])
    song_id = await search_song_id(keyword, session)
    if song_id is None:
        await session.send('没有找到这首歌呢')
    await session.send(MessageSegment.music('163', song_id))


@music.args_parser
async def _(session: CommandSession):
    stripped_text = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_text:
            session.state['keyword'] = stripped_text
        return


CALLING_KEYWORDS = {'来一首', '点一首', '整一首', '播放', '点歌', '放一首'}


@on_natural_language(keywords=CALLING_KEYWORDS)
async def _(session: NLPSession):
    sp = re.split('|'.join(CALLING_KEYWORDS), session.msg_text, maxsplit=1)
    if sp:
        return IntentCommand(90.0, 'music',
                             args={'keyword': sp[-1].strip(' 吧呗'),
                                   'from_nlp': True})
