import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90)) 
lowercaseLetter1=chr(random.randint(97,122)) 
num=random.randint(1,1000)


password = uppercaseLetter1 + lowercaseLetter1 + str (num)
password = shuffle(password)


print(password)
