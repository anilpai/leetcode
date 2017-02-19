import re
string = '12abc20yz68'
print(sum(map(int, re.findall(r'\d+', string))))
