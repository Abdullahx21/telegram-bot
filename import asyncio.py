import asyncio
from telethon import TelegramClient, events

# --- [ ضع بياناتك الصحيحة هنا ] ---
api_id = 33100412               # من my.telegram.org
api_hash = 'f396bd3f73d628658fdcdf94395ceb20'     # من my.telegram.org
group_target = '@Ta3fi_group'    # مثال: 'https://t.me/xxx'
WAIT_SECONDS = 30

async def delete_after_delay(event, delay):
    await asyncio.sleep(delay)
    try:
        await event.delete()
        print(f"[-] تم حذف الرسالة {event.id} بنجاح.")
    except Exception as e:
        print(f"[!] فشل حذف الرسالة {event.id}: {e}")

async def main():
    client = TelegramClient('session', api_id, api_hash)
    
    await client.start()
    print("[+] تم الاتصال بنجاح!")
    
    try:
        group_entity = await client.get_entity(group_target)
        me = await client.get_me()
        
        print(f"[+] المراقبة نشطة على: {group_entity.title}")
        
        @client.on(events.NewMessage(chats=group_entity))
        async def handler(event):
            if event.sender_id == me.id:
                print(f"[+] رسالة جديدة {event.id}.. عداد {WAIT_SECONDS} ثانية..")
                asyncio.create_task(delete_after_delay(event, WAIT_SECONDS))
        
        await client.run_until_disconnected()
    except Exception as e:
        print(f"[X] خطأ: {e}")

if __name__ == '__main__':
    asyncio.run(main())