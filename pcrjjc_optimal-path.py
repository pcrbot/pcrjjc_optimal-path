import numpy as np
from hoshino import Service, priv
from hoshino.typing import CQEvent, MessageSegment as ms

sv = Service('_jjcjijian_', manage_priv=priv.SUPERUSER, visible=False)

@sv.on_prefix('偷屁股计算')
async def arena_miner(bot, ev: CQEvent):
    try:
       n = int(ev.message.extract_plain_text())
    except:
       return
    if 1<=n<=15001:

      lst=[str(n)+"→"]
      for _ in range(40):
       if 70<n<=15001:
         n = 0.85 * n
         n = int(n // 1)
         lst.append(str(n)+"→")


       elif 10 < n <= 70:
         n = int(n - 10)
         lst.append(str(n)+'→')
       elif 0 < n <= 10:
         lst.append(1)
         break
    else:
        bug=f"数据出错，请输入15001以内的正整数"
        await bot.send(ev,bug)
    msg=''.join('%s' %id for id in lst)
    print(msg)
    await bot.send(ev,msg)


