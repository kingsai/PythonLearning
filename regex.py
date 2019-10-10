import re

# phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())
# print(mo)

# phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is (415)-555-4242.')
# print('Phone number found: ' + mo.group(1))
# print('Phone number found: ' + mo.group(2))
# print('Phone number found: ' + mo.group(0))
# print('Phone number found: ' + mo.group())
# print( mo.groups())
# # mo.groups()
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))

# greedyHaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
# print(mo1.group())

# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHaHa')
# print(mo2.group())

# vowelRegex = re.compile(r'[aeiouAEIOU]')
# consonantRegex = re.compile(r'[^aeiouAEIOU]')

# mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# mo2 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(mo)
# print(mo2)

# atRegex = re.compile(r'.at')
# mo = atRegex.findall('The cat in the hat sat on the flat mat')
# print(mo)

# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: AI Last Name: Sweigart')
# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)
