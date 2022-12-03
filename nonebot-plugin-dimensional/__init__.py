import random
from .config import *
from nonebot.adapters.onebot.v11.helpers import (
    Cooldown,
    CooldownIsolateLevel,
)
from nonebot import on_keyword, on_regex
from nonebot.params import RegexGroup
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment

#去掉注释即可使用
#ikun = on_keyword({'ikun','只因','鸡哥','鸡你太美','蔡徐坤','小黑子'}, priority=99, block=False, state={
#        'pm_name':        'ikun图',
#        'pm_description': '小黑子是吧~',
#        'pm_usage':       '只因~',
#        'pm_priority':    1
#    })

ecy_img = on_regex(r'^来点(二次元|二刺螈|银发|兽耳|星空|竖屏|横屏)图?$', priority=13, block=True)

#@ikun.handle()
#async def _(event:MessageEvent):
#     if random.random()<= 0.5:
#        await ikun.finish(MessageSegment.image('https://www.duxianmen.com/api/ikun/'))
#     else:
#        return

cooldown = Cooldown(
    cooldown=cooldown_time, prompt="二次元图片冷却ing", isolate_level=CooldownIsolateLevel.USER
)
@ecy_img.handle([cooldown])
async def ecy_img_handler(event: MessageEvent, regexGroup=RegexGroup()):
    urls = [
        'https://www.dmoe.cc/random.php',
        'https://acg.toubiec.cn/random.php',
        'https://api.ixiaowai.cn/api/api.php',
        'https://dev.iw233.cn/api.php?sort=iw233'
    ]
    img_type = regexGroup[0]
    if img_type in ['二次元', '二刺螈']:
        url = random.choice(urls)
    elif img_type == '银发':
        url = 'https://dev.iw233.cn/api.php?sort=yin'
    elif img_type == '兽耳':
        url = 'https://dev.iw233.cn/api.php?sort=cat'
    elif img_type == '星空':
        url = 'https://dev.iw233.cn/api.php?sort=xing'
    elif img_type == '竖屏':
        url = 'https://dev.iw233.cn/api.php?sort=mp'
    elif img_type == '横屏':
        url = 'https://dev.iw233.cn/api.php?sort=pc'
    else:
        url = ''
    #api
    await ecy_img.send('正在努力找图ing..请稍候...')
    await ecy_img.send(MessageSegment.image(file=url))