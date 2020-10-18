import requests as req
import os
import sys
from colorama import init, AnsiToWin32, Fore, Back

print(Fore.RED ,"************************")
print(Fore.GREEN ,"follow me:mr_mobin_dan")
print(Fore.CYAN ,"***********************")
mobindan =input("=>")

e=req.get('https://tools.keycdn.com/geo.json?host='+mobindan).json()

print(Fore.GREEN ,e)
