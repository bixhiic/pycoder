import requests
from bs4 import BeautifulSoup
import time



response = requests.get("https://www.ascii-code.com/")

soup = BeautifulSoup(response.text, features="lxml")

char_list = [] 
decimal_list =[] 
octal_list = [] 
hexa_list = [] 
bin_list = [] 

char_dict = {} 
decimal_dict ={} 
octal_dict = {} 
hexa_dict = {} 
bin_dict = {} 

table_list = soup.find_all('table')[1]
trs = table_list.find_all('tr')[1:]
row = [tr.find_all('td') for tr in trs]
    
# LISTING TABLE DATA    
for tag in row:
    decimal_list.append(str(tag[1].text.strip()))
    octal_list.append(str(tag[2].text.strip()))
    hexa_list.append(str(tag[3].text.strip()))
    bin_list.append(str(tag[4].text.strip()))
    char_list.append(str(tag[5].text.strip()))


for i in range(0,68):
        decimal_list[i] = '0' + decimal_list[i]


# MAKING DICTS
def add(dic, key, value):
    dic[key] = value

for j in range(96):
    add(decimal_dict, char_list[j] , decimal_list[j])
    add(octal_dict, char_list[j] ,   octal_list[j])
    add(hexa_dict, char_list[j] , hexa_list[j])
    add(bin_dict, char_list[j] , bin_list[j])



def crypt(data, format):
    '''Crypt data to selected format'''
    
    chain = ''
    result = []
    
    if format == '1':
        for i in data:
            value = decimal_dict.get(i)
            if value == None:
                value = '032'
            result.append(str(value))

    elif format == '2':
        for i in data:
            value = octal_dict.get(i)
            if value == None:
                value = '032'
            result.append(str(value))

    elif format == '3':
        for i in data:
            value = hexa_dict.get(i)
            if value == None:
                value = '032'
            result.append(str(value))
    
    elif format == '4':
        for i in data:
            value = bin_dict.get(i)
            if value == None:
                value = '032'
            result.append(str(value))
                                        
    return chain.join(result) 



def decrypt():
    '''Crypt data to selected format'''
    pass



menu = '''
+-------------------------+
|   Wellcome to Pycoder   |
+-------------------------+ 

This script helps to crypt some text in diferent formats, please choose one:

[1] Decimal
[2] Octal
[3] Hexadecimal
[4] Binary

[5] Exit
'''
print(menu)

while True:
    print('\nOption?')
    opt = str(input(">> "))
    if opt == '5':
        print('[%] Exiting...')
        time.sleep(1)
        break

    elif opt == '1':
        data = input('[*] Write or copy text here >> ')
        text = crypt(data=data, format=opt)
        print(text)
    elif opt == '2':
        data = input('[*] Write or copy text here >> ')
        text = crypt(data=data, format=opt)
        print(text)

    elif opt == '3':
        data = input('[*] Write or copy text here >> ')
        text = crypt(data=data, format=opt)
        print(text)

    elif opt == '4':
        data = input('[*] Write or copy text here >> ')
        text = crypt(data=data, format=opt)
        print(text)
    else:
        print('Select a correct option!')                

     