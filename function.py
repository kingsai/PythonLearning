from datetime import datetime
# def currenttime(msg):
#     print(msg)
#     print(datetime.now())
#     print()

# currenttime('Hi')
# currenttime('Hey')

def initial(args, force_uppercase):
    if force_uppercase:
        return args[0:1].upper()
    else:
        return args[0:1]
    print('/N')

print(initial('jie', False))  
# print() 
print(initial('jie', True)) 
# print()  