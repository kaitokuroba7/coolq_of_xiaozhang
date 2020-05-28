import re
from typing import Optional
from aiocache import cached
from nonebot import MessageSegment
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.command.argfilter import extractors, validators
import random
import requests


@cached(ttl=12 * 60 * 60)
async def search_song_id(keyword: str) -> Optional[int]:
    QQ_MUSIC_SEARCH_URL_FORMAT = 'https://music.jeeas.cn/v1/search?s={''}&format=&from=music'
    keyword = keyword.strip()
    if not keyword:
        return None
    resp = requests.get(QQ_MUSIC_SEARCH_URL_FORMAT.format(keyword))
    payload = resp.json()
    if not isinstance(payload, dict) or \
            not payload.get('result'):
        return None

    try:
        if payload['result']['songs'][0]['ar'][0]['id'] == 1046043:
            # await session.send(MessageSegment.at(844814749) + ' 开心，饺子搜到了最爱的女友的歌！')
            i = random.randint(0, 19)
            return payload['result']['songs'][i]['id']

        for i in range(30):
            if payload['result']['songs'][i]['ar'][0]['id'] == 1046043:
                # await session.send(MessageSegment.at(844814749) + MessageSegment.face(21)
                                  # + ' 开心，饺子搜到了最爱的女友的歌！')
                return payload['result']['songs'][i]['id']
            elif payload['result']['songs'][i]['ar'][0]['id'] == 1180155:
                # await session.send(MessageSegment.at(844814749) + MessageSegment.face(13)
                                  # + ' 饺子知道了，'
                                  # '是捕梦网的歌，中国第四大运营商')
                return payload['result']['songs'][i]['id']

        if i == 29:
            return payload['result']['songs'][0]['id']

    except (TypeError, KeyError, IndexError):
        return None