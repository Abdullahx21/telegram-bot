import asyncio
import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 33100412
api_hash = 'f396bd3f73d628658fdcdf94395ceb20'
group_target = '@Ta3fi_group'
WAIT_SECONDS = 30

session_string = os.environ.get('SESSION_STRING')

async def delete_after_delay(event, delay):
    await asyncio.sleep(delay)
    try:
        await event.delete()
        print(f"[-] تم حذف الرسالة {event.id}")
    except Exception as e:
        print(f"[!] فشل: {e}")

async def main():
    client = TelegramClient(StringSession(session_string), api_id, api_hash)
    await client.start()
    print("[+] تم الاتصال!")
    
    group_entity = await client.get_entity(group_target)
    me = await client.get_me()
    print(f"[+] مراقبة: {group_entity.title}")

    @client.on(events.NewMessage(chats=group_entity))
    async def handler(event):
        if event.sender_id == me.id:
            asyncio.create_task(delete_after_delay(event, WAIT_SECONDS))

    await client.run_until_disconnected()

asyncio.run(main())