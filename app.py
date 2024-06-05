import asyncio
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
import random

account_list = [

    ('user_id', 'username', 'phone', 'appid', 'app_hash', 'telethon_hash'),

]

join_what = [
    '/start refID', #ex. /start 1234567890
]

async def main():
    for i, account in enumerate(account_list):
        print(f"{i} [{account[1]}] - Starting...")
        j = 10
        
        start_message = random.choice(join_what)
        
        
        async with TelegramClient(StringSession(account[5]), account[3], account[4]) as client:
            # Track if the captcha has been solved
            captcha_solved = False

            @client.on(events.NewMessage(chats='WTFollow_bot'))
            async def handler(event):
                nonlocal captcha_solved
                
                if 'Choose your language' in event.raw_text:
                    for row in event.message.reply_markup.rows:
                        for button in row.buttons:
                            if button.text == '🇷🇺':
                                await client(GetBotCallbackAnswerRequest(
                                    peer=event.message.peer_id,
                                    msg_id=event.message.id,
                                    data=button.data
                                ))
                                print("Clicked on 🇷🇺")
                                return
                elif 'Решите каптчу' in event.raw_text:
                    print(event.raw_text)
                    await asyncio.sleep(2)
                    
                    # Find the appropriate button based on the text in the captcha
                    for row in event.message.reply_markup.rows:
                        for button in row.buttons:
                            if button.text == '🌧' and 'дождевое облако' in event.raw_text:
                                await client(GetBotCallbackAnswerRequest(
                                    peer=event.message.peer_id,
                                    msg_id=event.message.id,
                                    data=button.data
                                ))
                                print("Clicked on дождевое облако")
                                captcha_solved = True
                                return
                            elif button.text == '🌨' and 'облако и снег' in event.raw_text:
                                await client(GetBotCallbackAnswerRequest(
                                    peer=event.message.peer_id,
                                    msg_id=event.message.id,
                                    data=button.data
                                ))
                                print("Clicked on облако и снег")
                                captcha_solved = True
                                return
                            elif button.text == '🌩' and ('грозовое облако' in event.raw_text or "облако с грозой" in event.raw_text):
                                await client(GetBotCallbackAnswerRequest(
                                    peer=event.message.peer_id,
                                    msg_id=event.message.id,
                                    data=button.data
                                ))
                                print("Clicked on грозовое облако")
                                captcha_solved = True
                                return
                            elif button.text == '🌥' and 'солнце за облаком' in event.raw_text:
                                await client(GetBotCallbackAnswerRequest(
                                    peer=event.message.peer_id,
                                    msg_id=event.message.id,
                                    data=button.data
                                ))
                                print("Clicked on солнце за облаком")
                                captcha_solved = True
                                return
                            elif button.text == '🌦' and 'солнце и дождь' in event.raw_text:
                                await client(GetBotCallbackAnswerRequest(
                                    peer=event.message.peer_id,
                                    msg_id=event.message.id,
                                    data=button.data
                                ))
                                print("Clicked on солнце и дождь")
                                captcha_solved = True
                                return
                            elif button.text == '☁️' and 'чистое облако' in event.raw_text:
                                await client(GetBotCallbackAnswerRequest(
                                    peer=event.message.peer_id,
                                    msg_id=event.message.id,
                                    data=button.data
                                ))
                                print("Clicked on чистое облако")
                                captcha_solved = True
                                return

            # Send the initial command to start the bot interaction
            await client.send_message('WTFollow_bot', start_message)

            # Wait for the captcha to be solved
            while not captcha_solved:
                await asyncio.sleep(3)
                j-=1
                print(f"[{account[1]}]  Waiting for captcha to be solved...")
                
                if j <= 0:
                    break
        
        
        await asyncio.sleep(random.randint(5, 60))

if __name__ == '__main__':
    print("""
          

  _    _ _     _     _             _____          _      
 | |  | (_)   | |   | |           / ____|        | |     
 | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___ 
 |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \\
 | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
 |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|
                                                         
                   by Aero25x                                           
          
          """)
    asyncio.run(main())
