from telethon import TelegramClient, events
import sqlite3
import webvuotlink
#api telegram
api_id = '20654149'
api_hash = '4422cfbd1810967f6a54c06cd0120fdc'
#database
conn = sqlite3.connect('duckyodb.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (uid TEXT, money INTEGER)')
conn.commit()
sqluserform = 'INSERT INTO users (uid, money) VALUES (?, ?)'
#link
finallink = {}
finalmoney = {}
f = open('links.txt').readlines()
for line in f:
    line = line.replace("\n","")
    line = line.split("|")
    finallink[line[1]] = line[0]
    money = int(line[2])
    finalmoney[line[1]] = money
#lay view cac link luc dau
webvuotlink.login_again('8link')
webvuotlink.login_again('yeumoney')
webvuotlink.login_again('1short')
webvuotlink.login_again('uptolink.cloud')
view = {}
for code in finallink:
    link = finallink[code]
    view[link] = int(webvuotlink.check_link(link))
#client
client = TelegramClient('session_name', api_id, api_hash)

#submit code
@client.on(events.NewMessage)
async def code_handle(event):
    if event.message.message.startswith('/nhapma '):
        code = event.message.message.replace('/nhapma ','')
        if code not in finallink:
            text = 'Bạn đã nhập sai code, vui lòng xem code code của mình'
            await event.respond(text)
            return
        chat = await event.get_chat()
        link = finallink[code]
        try:
            new_view = int(webvuotlink.check_link(link))
            if int(new_view) > int(view[link]):
                view[link] = view[link] + 1
                text = f'Bạn đã hoàn thành link {link}\n' + f'Phần thưởng: {finalmoney[code]}'
                cursor.execute(f'SELECT * FROM users WHERE uid={chat.id}')
                result = cursor.fetchone()
                money = result[1]
                uid = result[0]
                money = int(money) + int(finalmoney[code])
                cursor.execute(f'DELETE FROM users WHERE uid={uid}')
                conn.commit()
                user = (uid,money)
                cursor.execute(sqluserform,user)
                conn.commit()
                await event.respond(text)
            else:
                text = 'Bạn chưa hoàn thành nhiệm vụ hoặc hệ thống không tính view của bạn hoặc bạn đã làm nhiệm vụ này rồi'
                await event.respond(text)
        except:
            try:
                if '8link' in link:
                    webvuotlink.login_again('8link')
                elif 'yeumoney' in link:
                    webvuotlink.login_again('yeumoney')
                elif '1short' in link:
                    webvuotlink.login_again('1short')
                elif 'uptolink.cloud' in link:
                    webvuotlink.login_again('uptolink.cloud')
                new_view = int(webvuotlink.check_link(link))
                if int(new_view) > int(view[link]):
                    view[link] = view[link] + 1
                    text = f'Bạn đã hoàn thành link {link}\n' + f'Phần thưởng: {finalmoney[code]}'
                    cursor.execute(f'SELECT * FROM users WHERE uid={chat.id}')
                    result = cursor.fetchone()
                    money = result[1]
                    uid = result[0]
                    money = int(money) + int(finalmoney[code])
                    cursor.execute(f'DELETE FROM users WHERE uid={uid}')
                    conn.commit()
                    user = (uid,money)
                    cursor.execute(sqluserform,user)
                    conn.commit()
                    await event.respond(text)
                else:
                    text = 'Bạn chưa hoàn thành nhiệm vụ hoặc hệ thống không tính view của bạn hoặc bạn đã làm nhiệm vụ này rồi'
                    await event.respond(text)
            except:
                text = 'Liên kết '+link+' bị lỗi,vui lòng thử nhiệm vụ khác'
                await event.respond(text)
#quest
async def nhiemvu():
    text = "làm nhiệm vụ trùng sẽ không tính nên bạn hay làm theo thứ tự từ trên xuống dưới để tránh làm bị trùng.\n\n Sau khi vượt thì hãy copy mã bạn nhận được và nhắn cho bot với cú pháp: /nhapma (mã bạn nhận đươc)\n\n"
    cnt = 1
    for code in finallink:
        link = finallink[code]
        money = finalmoney[code]
        nhiemvu = f"link {cnt}: " + link + f' ,phần thưởng: {money}'
        text = text + nhiemvu+'\n\n'
        cnt+=1
    return text

#start
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    chat = await event.get_chat()
    text = '''
Các câu lệnh của bot:
"/task" : làm nhiệm vụ kiếm tiền
"/account" : kiểm tra tài khoản
"/withdraw" : gửi yêu cầu rút tiền đến admin

Mọi khó khăn,thắc mắc xin vui lòng liên hệ qua admin: @kiemtienonline43
'''
    cursor.execute(f"SELECT uid from users WHERE uid = {chat.id}")
    result = cursor.fetchall()
    if result == []:
        user = (str(chat.id),0)
        cursor.execute(sqluserform,user)
        conn.commit()
    await event.respond(text)

#lay nhiem vu
@client.on(events.NewMessage(pattern='/task'))
async def get_task(event):
    await event.respond(await nhiemvu())

#account
@client.on(events.NewMessage(pattern='/account'))
async def get_account(event):
    chat = await event.get_chat()
    uid = chat.id
    cursor.execute(f'SELECT * FROM users WHERE uid={uid}')
    result = cursor.fetchone()
    answer = f"""
uid👤: {uid}
money💰: {result[1]}đồng
"""
    await event.respond(answer)

#withdraw money
@client.on(events.NewMessage(pattern='/withdraw'))
async def withdraw(event):
    chat = await event.get_chat()
    uid = chat.id
    cursor.execute(f'SELECT * FROM users WHERE uid={uid}')
    result = cursor.fetchone()
    money = result[1]
    if money < 10000:
        text = 'Bạn cần phải có tối thiêu 10000 đồng trong tài khoản để thực hiện yêu cầu rút tiền'
        await event.respond(text)
        return
    text = f'Đã đặt lệnh rút cho số tiền {money} đồng  thành công, admin sẽ sớm liên hệ với bạn hoặc bạn có thể nhắn tin đến admin qua: @kiemtienonline43'
    cursor.execute(f'DELETE FROM users WHERE uid={uid}')
    conn.commit()
    money = 0
    user = (uid,money)
    cursor.execute(sqluserform,user)
    conn.commit()
    await event.respond(text)
    
    
#addmoney
@client.on(events.NewMessage(pattern='/addmoney '))
async def add_money(event):
    chat = await event.get_chat()
    uid = chat.id
    if uid != 6100239828:
        text = 'Câu lệnh này bạn không có quyền sử dụng'
        await event.respond(text)
        return
    message = event.message.text
    message = message.replace("/addmoney ","")
    message = message.split(" ")
    uid = message[0]
    cursor.execute(f'SELECT * FROM users WHERE uid={uid}')
    result = cursor.fetchone()
    money = result[1]
    for char in message[1]:
        if (char < '0' or char > '9'):
            text = 'Số tiền nhập vào phải là số'
            await event.respond(text)
            return
    text = f'Đã cộng {message[1]} đồng cho uid: {uid}'
    money = int(int(money) + int(message[1]))
    cursor.execute(f'DELETE FROM users WHERE uid={uid}')
    conn.commit()
    user = (uid,money)
    cursor.execute(sqluserform,user)
    conn.commit()
    await event.respond(text)

#deductmoney
@client.on(events.NewMessage(pattern='/deductmoney '))
async def deduct_money(event):
    chat = await event.get_chat()
    uid = chat.id
    if uid != 6100239828:
        text = 'Câu lệnh này bạn không có quyền sử dụng'
        await event.respond(text)
        return
    message = event.message.text
    message = message.replace("/deductmoney ","")
    message = message.split(" ")
    uid = message[0]
    cursor.execute(f'SELECT * FROM users WHERE uid={uid}')
    result = cursor.fetchone()
    money = result[1]
    for char in message[1]:
        if (char < '0' or char > '9'):
            text = 'Số tiền nhập vào phải là số'
            await event.respond(text)
            return
    text = f'Đã trừ {message[1]} đồng cho uid: {uid}'
    money = int(int(money) - int(message[1]))
    cursor.execute(f'DELETE FROM users WHERE uid={uid}')
    conn.commit()
    user = (uid,money)
    cursor.execute(sqluserform,user)
    conn.commit()
    await event.respond(text)


#getview
@client.on(events.NewMessage(pattern='/getview'))
async def get_view(event):
    chat = await event.get_chat()
    uid = chat.id
    if uid != 6100239828:
        text = 'Câu lệnh này bạn không có quyền sử dụng'
        await event.respond(text)
        return
    text = 'view hien tai:\n'
    for code in finallink:
        link = finallink[code]
        _view = view[finallink[code]]
        text = text + f'link: {link} ,view: {_view}.\n'
    await event.respond(text)
with client:
    client.run_until_disconnected()