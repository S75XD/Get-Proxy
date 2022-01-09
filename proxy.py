Done = """
██████╗░░█████╗░███╗░░██╗███████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝
██║░░██║██║░░██║██╔██╗██║█████╗░░
██║░░██║██║░░██║██║╚████║██╔══╝░░
██████╔╝╚█████╔╝██║░╚███║███████╗
╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝
"""
import os
try:
    import requests,colorama,socket
    from colorama import Fore
except:
    os.system("pip install colorama");os.system("pip install requests");os.system("pip install socket")

colorama.init(autoreset=True)
red=Fore.RED
yellow=Fore.YELLOW
blue=Fore.BLUE
green=Fore.GREEN
cyan=Fore.CYAN
white=Fore.WHITE

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clear()

print(f"""{blue}

    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
    ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ 
    ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  
    ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
{white}     By SaLeH | insta @8_uvw                                 
""")
user = socket.gethostname()
info = f'''
Hi {red}{user}{yellow} Thes app for get proxy..
    for http use nam (1)
        for socks4 use nam (2)
            for socks5 use nam (3)
'''
print(f'{yellow}{info}')
user = input("[/]Enter what you want [1/2/3]:")

#========================================== Code proxy .
if user =='1':
    url1 = "https://api.openproxylist.xyz/http.txt"
    r1 = requests.get(url1)
    results = r1.text
    with open (f"http.txt","w") as file:
        file.write(results)
        clear()
        print(Done)
        exit()

#========================================== Code proxy ..

if user =='2':
    url2 = "https://api.openproxylist.xyz/socks4.txt"
    r2 = requests.get(url2)
    results = r2.text
    with open (f"socks4.txt","w") as file:
        file.write(results)
        clear()
        print(Done)
        exit()

#========================================== Code proxy ...

if user =='3':
    url3 = "https://api.openproxylist.xyz/socks5.txt"
    r3 = requests.get(url3)
    results = r3.text
    with open (f"socks5.txt","w") as file:
        file.write(results)
        clear()
        print(Done)
        exit()
else:
    print("[-]nam not faond ):")
#========================================== :)



#Hi User (: Come To My account @8_uvw