import requests
import random

def random_text(length):
    text = ''
    length = int(length)
    for _ in range(length):
        if random.randint(0,1) % 2 ==0:
            text = text + chr(random.randint(ord('a'),ord('z')))
        else:
            text = text + chr(random.randint(ord('0'),ord('9')))
    return text
def add_note(title,code):
    url = 'https://anotepad.com/note/create'
    payload = {
        "notetype":"PlainText",
        "noteaccess":"2",
        "notepassword":"",
        "notequickedit":"false",
        "notequickeditpassword":"",
        "notetitle":title,
        "notecontent":code
    }
    username = 'vuotlinktele@gmail.com'
    password = 'pipipop0'
    response = requests.post(url, data=payload, auth=(username, password))
    json = response.json()
    return str(json['notenumber'])

links = {}
def web8link():
    number = int(input('Nhập số link của web 8link cần tạo:'))
    if number == 0:
        return
    money = int(input('Nhập số tiền của web 8link (đồng):'))
    print("Đang tạo link...")
    for i in range(number):
        code = '8link'+random_text(10)
        link = "https://anotepad.com/notes/"+add_note(f'code của bạn là:',code)
        api_url = 'https://partner.8link.io/api/public/gen-shorten-link?apikey=d95ec4fefd881ad82870ba6d39ac8040e4a45cb2a55a7d8ecbcd03e22a794a05&url='+link+'&target_domain=https://8link.io'
        response = requests.get(url=api_url)
        json = response.json()
        link = json["shortened_url"]
        links[link] = (code,money)
    print("Tạo hoàn tất")

def webyeumoney():
    number = int(input('Nhập số link của web yeumoney cần tạo:'))
    if number == 0:
        return
    money = int(input('Nhập số tiền của web yeumoney (đồng):'))
    print("Đang tạo link...")
    for i in range(number):
        code = 'yeumoney'+random_text(10)
        link = "https://anotepad.com/notes/"+add_note('code của bạn là:',code)
        api_url = 'https://yeumoney.com/QL_api.php?token=8255f9ee51a12d6e6043505950dea96e3506fca3d3b72767a008284500e4a3c1&format=json&url='+link
        response = requests.get(url=api_url)
        json = response.json()
        link = json["shortenedUrl"]
        links[link] = (code,money)
    print("Tạo hoàn tất")


def webuptolink_cloud():
    number = int(input('Nhập số link của web uptolink.cloud cần tạo:'))
    if number == 0:
        return
    money = int(input('Nhập số tiền của web uptolink.cloud (đồng):'))
    print("Đang tạo link...")
    for i in range(number):
        code = 'uptolink.cloud'+random_text(10)
        link = "https://anotepad.com/notes/"+add_note('code của bạn là:',code)
        api_url = 'https://uptolink.cloud/api?api=dafecca377546a66cb9d0876c47372ec4caf0ec0&url='+link
        response = requests.get(url=api_url)
        json = response.json()
        link = json["shortenedUrl"]
        links[link] = (code,money)
    print("Tạo hoàn tất")

def webuptolink_io():
    number = int(input('Nhập số link của web uptolink.io cần tạo:'))
    if number == 0:
        return
    money = int(input('Nhập số tiền của web uptolink.io (đồng):'))
    print("Đang tạo link...")
    for i in range(number):
        code = 'uptolink.io'+random_text(10)
        link = "https://anotepad.com/notes/"+add_note('code của bạn là:',code)
        api_url = 'https://uptolink.io.vn/api?api=2ccd1b6158fdbc3ef2ad2c0d00786dae6cce34de&url='+link
        response = requests.get(url=api_url)
        json = response.json()
        link = json["shortenedUrl"]
        links[link] = (code,money)
    print("Tạo hoàn tất")

web8link()
webyeumoney()
webuptolink_cloud()
webuptolink_io()
def log_link():
    with open('links.txt','w',encoding='utf-8') as f:
        for link in links:
            text = link+'|'+str(links[link][0])+'|'+str(links[link][1])+'\n'
            f.write(text)

log_link()