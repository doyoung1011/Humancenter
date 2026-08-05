
import fn.fn as fn

a= fn.add(1,2)
print(a)
 
# b=fn.sub(1,2)
# print(b)
    
from  fn.fn import sub

b=sub(3,2)
print(b)

import random
print(random.random())

from random import random
print(random())

from  fn.fn import Hero
h=Hero()
h.attack()

from fn.fn import Superman
s=Superman()
s.attack()

import urllib.request 
response=urllib.request.urlopen('http://google.com')
print(response.read().decode('utf-8'))