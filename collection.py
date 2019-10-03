Jie = {}
Jie['first'] = 'Jie'
Jie['last'] = 'Sun'

Yan = {'first': 'Yanhong', 'last': 'Tan'}

people = [Jie, Yan]
people.append({'first': 'Bill', 'last': 'Gates'})

presenter = people[0:2]
# print(Jie)
# print(people)
# print(presenter)
# print(len(presenter))

# for name in people:
#     print(name)

index = 0
while index < len(people):
    print(index)
    print(people[index])    
    index += 1