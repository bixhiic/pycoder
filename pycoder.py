import requests
from bs4 import BeautifulSoup
import time, os


MENU = ['''
+-------------------------+
|   Wellcome to Pycoder   |
+-------------------------+ 

Select Method:

[1] To Crypt
[2] To Decrypt

[5] Exit

''',
'''
+-------------------------+
|   Wellcome to Pycoder   |
+-------------------------+ 

Select a format to use: 

[1] Decimal
[2] Octal
[3] Hexadecimal
[4] Binary

[5] Exit

''']


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
                value = '00100000'
            result.append(str(value))
                                        
    return chain.join(result) 



def decrypt(data, format):
    '''Crypt data to selected format'''
    pass



def convert(opt, frmt, data):
    '''Convert data from ~option~ to ~format~:
        [#] Option -> (crypt / decrypt)
        [#] Format -> (decimal, octal, hexadecimal, binary)    
    '''

    # crypt
    if opt == '1':
        code = crypt(data=data, format=frmt)
        return code
    else:
        code = decrypt(data=data, format=frmt)
        return code    
    



while True:   
  
    print(MENU[0])
    opt = str(input(">> "))
    os.system('clear')
    if opt == '5':
        print('[%] Exiting...')
        time.sleep(1)
        break
    elif opt == '1' or opt == '2':
        os.system('clear')
        print(MENU[1])
        frmt = str(input('>> '))
        os.system('clear')
        data = input('[*] Write or copy text here >> ')
        result = convert(opt=opt, frmt=frmt, data=data)
        os.system('clear')
        print(f'\n\n[^] Code: {result} \n\n')
        input('Press any key to restart...')
        os.system('clear')

    else:
        os.system('clear')
        print('\n [%] ERROR! \n\n Select a valid option')




    # elif opt == '1':
    #     data = input('[*] Write or copy text here >> ')
    #     text = crypt(data=data, format=opt)
    #     print(text)
    # elif opt == '2':
    #     data = input('[*] Write or copy text here >> ')
    #     text = crypt(data=data, format=opt)
    #     print(text)

    # elif opt == '3':
    #     data = input('[*] Write or copy text here >> ')
    #     text = crypt(data=data, format=opt)
    #     print(text)

    # elif opt == '4':
    #     data = input('[*] Write or copy text here >> ')
    #     text = crypt(data=data, format=opt)
    #     print(text)
    # else:
    #     print('Select a correct option!')                



