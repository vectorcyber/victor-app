import os

from pyfiglet import Figlet

import requests

import re

f = Figlet()

print(f.renderText("VICTOR"))

print("1.Figlet Text")

print("2.Url Shorter")

print("3.S

s Bomber")

print("4.Calculator")

select=input("Select Operation ---> ")

if select=="1":

	text=input("Enter Text ---> ")	fig=Figlet()

	print(fig.renderText(text))

elif select=="2":

	link=input("Enter Site Link ---> ")

	url= "https://cleanuri.com/api/v1/shorten"

	job= {'url': link}

	urlshort= requests.post(url, data = job)

	print(urlshort.text)

elif select=="3":

	os.system("python3 smsbomber.py")

elif select=="4":

	os.system("python3 Calculator.py")

else:

	print("Error")import os

from pyfiglet import Figlet

import requests

import re

f = Figlet()

print(f.renderText("WikISaleh"))import os

from pyfiglet import Figlet

import requests

import re

f = Figlet()

print(f.renderText("WikISaleh"))

print("1.Figlet Text")

print("2.ddos-script")

print("3.sms Bomber")

print("4.Calculator")

select=input("Select Operation ---> ")

if select=="1":

	text=input("Enter Text ---> ")

	fig=Figlet()

	print(fig.renderText(text))

elif select=="2":

	link=input("Enter Site Link ---> ")

	url= "https://cleanuri.com/api/v1/shorten"

	job= {'url': link}

	urlshort= requests.post(url, data = job)

	print(urlshort.text)

elif select=="3":

	os.system("python3 smsbomber.py")

elif select=="4":

	os.system("python3 Calculator.py")

else:

	print("Error")

print("1.Figlet Text")

print("2.Url Shorter")

print("3.Sms Bomber")

print("4.Calculator")

select=input("Select Operation ---> ")

if select=="1":

	text=input("Enter Text ---> ")

	fig=Figlet()

	print(fig.renderText(text))

elif select=="2":

	link=input("Enter Site Link ---> ")

	url= "https://cleanuri.com/api/v1/shorten"

	job= {'url': link}

	urlshort= requests.post(url, data = job)

	print(urlshort.text)

elif select=="3":

	os.system("python3 smsbomber.py")

elif select=="4":

	os.system("python3 Calculator.py")

else:

	print("Error")
