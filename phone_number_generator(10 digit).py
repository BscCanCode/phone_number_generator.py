#Generating a 10 digit mobile phone number,which is random

import random
import string

prefix=str(random.choice([9,8,7,6])) #converting to string because python gives error if tried to do int+str
suffix=''.join(random.choices(string.digits,k=9)) #this is str, str+str is possible but str+int not possible thats why converted prefix to str
phone_num=prefix+suffix
print("The 10-digit phone number generated is:",phone_num)
print("----------------X-------------------------")
print("The phone number is generated successfully!")
