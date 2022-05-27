

dec = {'H': '072'}


text = '072454072'

data = list(text)

def get_key(val):
    for key, value in dec.items():
         if val == value:
             return key
             
    return "Invalid value"


add = ""
for i in data:
    add += i
    if len(add) > 2:
        x = get_key(add)
        add = ""
        print(x)

        


    

def action(opt, frmt, data):
    if opt == 1 and frmt == 1:
        




