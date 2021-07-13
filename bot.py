import asyncio

from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session, message
from graia.application.message.chain import MessageChain
from graia.application.message.elements.internal import App, Plain,Image
from graia.application.friend import Friend
from graia.application.event.lifecycle import ApplicationLaunched



from function.drugs_reminder import drugs_reminder,clock


loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8098", # 填入 httpapi 服务运行的地址
        authKey="ShotrayBot", # 填入 authKey
        account=2972537442, # 你的机器人的 qq 号
        websocket=True # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)

@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend):
    await app.sendFriendMessage(  friend, MessageChain.create([
        Plain("好好吃饭啦，夸夸！")
    ]))

# @bcc.receiver("FriendMessage")
# async def friend_message_listener(app:GraiaMiraiApplication,friend:Friend):
#     message=MessageChain.create([
#         Image.fromLocalFile("C:/Users/69529/Desktop/temp/123.jpg")
#     ])
#     await app.sendFriendMessage(friend,message)

@bcc.receiver(ApplicationLaunched)
async def drug(app:GraiaMiraiApplication):
    asyncio.create_task(clock(app))


app.launch_blocking()