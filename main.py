import os, sys, requests, threading, time, random, string, json, httpx
from fake_useragent import UserAgent


YELLOW  = '\033[33m'
CYAN    = '\033[36m'
BLUE    = '\033[34m'
GREEN   = '\033[32m'
MAGENTA = '\033[35m'
RED     = '\033[31m'
RESET   = '\033[39m'



os.system("cls && title Advanced Persistent Threat 29 Kahoot Raper!")




def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())




class Kahoot(object):

    def interface():
        global code_id
        global username
        logo = """\033[36m
        logo
        """
        print(logo)
        code_id = input("<\033[36m/\033[39m> Game PIN: ")
        print("<\033[36m/\033[39m> \033[36m[\033[39m1\033[36m] \033[39mRandom Usernames \033[36m| [\033[39m2\033[36m] \033[39mCustom Usernames")
        choice = input("<\033[36m/\033[39m>: ")
        if choice == "1":
            username = input("")
        elif choice == "2":
            len = random.randint(0,9)
            return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(len)) 

        else:
            print("<\033[31mx\033[39m> Wrong Input")
    
    
            
    def join_session():
        with httpx.Client(proxies=proxies) as client:
            x = client.get(f"https://kahoot.it/reserve/session/{code_id}/?{session_id}") 
            if x.status_code == 200:
                print((f"[</> Session] Joined: {username}"))
            else:
                print(("[x] failed"))

        ...




    def Attack():
        ...
        #random answers

    def modules():

        global proxies, session_id
        agent = UserAgent().chrome
        session_id = random.randint(000000000000,265833902815)
        proxylist = open("data/proxies.txt", "r").read().splitlines()
        proxy = random.choice(proxylist)
        proxies = {
            "http://": f"http://{proxy}",
        }

        headers = {
            "authority": 'kahoot.it',
            "method": 'GET',
            "path": f"/reserve/session/{code_id}/?{session_id}",
            "scheme": "https",
            "accept": 'application/json, text/plain, */*',
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "referer": "https://kahoot.it/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": str(agent),

        }
    def main():
        Kahoot.interface()
        Kahoot.modules()
        Kahoot.join_session()

threading.Thread(target=Kahoot.main).start()
