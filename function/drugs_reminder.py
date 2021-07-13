import asyncio
import datetime

from graia.application.message.chain import MessageChain
from graia.application.message.elements.internal import Plain
from graia.application.friend import Friend



async def drugs_reminder(app):
    friend_qq=1621631707
    time=datetime.datetime.now()
    hour=time.hour
    s=''
    if hour==10:
        s='起床了嘛？没有早八的时候睡会儿懒觉也是应该的！但要记得吃饭喔www'
    elif hour==13:
        s='最近要打疫苗不吃药但要好好吃饭啊！'
    elif hour==17:
        s='大郎，该吃饭啦.jpg'

    
    if s=="":
        return
    
    message_send=MessageChain.create([Plain(s)])

    await app.sendFriendMessage(friend_qq,message_send)

# test clock for minutes
# async def clock(app):
#     while True:
#         cur_time=datetime.datetime.now()
#         delta=datetime.timedelta(minutes=1)
#         next_time=datetime.datetime.combine(cur_time.date(),datetime.time(cur_time.hour,cur_time.minute,0))+delta
#         sleep_seconds=next_time-cur_time
#         print(sleep_seconds)
#         await asyncio.sleep(sleep_seconds.total_seconds())
#         print("时间矫正完成。当前时间：", datetime.datetime.now())
#         await drugs_reminder(app)

# test clock for hours
async def clock(app):
    while(True):
        cur_time=datetime.datetime.now()
        delta=datetime.timedelta(hours=1)
        next_time=datetime.datetime.combine(cur_time.date(),datetime.time(cur_time.hour,0,0))+delta
        sleep_seconds=next_time-cur_time
        await asyncio.sleep(sleep_seconds.total_seconds())
        print("时间矫正完成。当前时间：", datetime.datetime.now())
        while True:
            t=datetime.datetime.now()
            if t.minute!=0:
                break
            asyncio.create_task(drugs_reminder(app))
            if t.second!=0:
                break
            await asyncio.sleep(3600)