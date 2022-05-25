import requests
from bs4 import BeautifulSoup
import pandas as pd


response = requests.get("https://www.ascii-code.com/")

soup = BeautifulSoup(response.text, features="lxml")

char_list = [] 
decimal_list =[] 
octal_list = [] 
hexa_list = [] 
bin_list = [] 

table_list = soup.find_all('table')[1]
trs = table_list.find_all('tr')[1:]
row = [tr.find_all('td') for tr in trs]
    
for tag in row:
    decimal_list.append(str(tag[1].text.strip()))
    octal_list.append(str(tag[2].text.strip()))
    hexa_list.append(str(tag[3].text.strip()))
    bin_list.append(str(tag[4].text.strip()))
    char_list.append(str(tag[5].text.strip()))

  
for i in range(0,68):
        decimal_list[i] = '0' + decimal_list[i]



print(f'Valores en decimal')
print(decimal_list)
print(f'Valores en octal')
print(octal_list)
print(f'Valores en hexadecimal')
print(hexa_list)
print(f'Valores en binario')
print(bin_list)
print(f'Valores en caracteres')
print(char_list)