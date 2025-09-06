import requests,os
try: 
    import pyfiglet
except:
    os.system("pip install pyfiglet")
    import pyfiglet

red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
white = "\033[1m\033[37m"

def logo(name):
    banner = pyfiglet.figlet_format(name, font="slant")
    print(f"\033[1m\033[31m{banner}\033[0m") 

logo("AnkuCode")

def getip():
    search=input(f'{yellow} 1-Get your ip info:\n 2- Search an Ip\n----> Enter 1/2: {cyan}')
    if search.lower()=='2':
        ip=input(f"{green}Enter IP: {yellow}")
        url=f'https://ipinfo.io/{ip}'
    elif search.lower()=='1':
        url=f'https://ipinfo.io/json'
    rq=requests.get(url)
    
    response="❗️ Lets fetch  IP Info:\n"
    if rq.status_code==200:
        okreq=rq.json()
        response+=f"IP: {okreq.get('ip')}\n"
        response+=f"Around City: {okreq.get('city')}\n"
        response+=f"Region: {okreq.get('region')}\n"
        response+=f"country: {okreq.get('country')}\n"
        response+=f"LOC: {okreq.get('loc')}\n"
        response+=f"ORG: {okreq.get('org')}\n"
        response+=f"POSTAL : {okreq.get('postal')}\n"
        response+=f"TimeZone : {okreq.get('timezone')}\n"
        response+=f"Developer : @AnkuCode\n"
    return response

#send to tg 
def send_Tg(BOT_TOKEN,ID,message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': ID, 'text': message, 'parse_mode': 'Markdown'}
    requests.post(url,data=payload)
    print(f"{green}Done sent to telegram...\n\n")

def result():
    result=getip()
    print(f"\n\n\n{yellow}1-Show ip info:\n2- Send info to telegram:\n")
    choose=input(f"{red}choose 1/2--->")
    if choose.lower()=='2':
        BOT_TOKEN=input(f"{cyan}Enter Bot token:{yellow} ")

        Id=int(input(f"{yellow}Enter chat ID: {cyan}"))
        try:
            send_Tg(BOT_TOKEN,Id,result)
        except Exception as a:
            print(a)

    else:
        print(f"\n{green}{result}{white}")

result()
