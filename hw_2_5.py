import random
from string import ascii_letters
a = sorted(random.sample(range(10), 10)reverse=True),
b = ascii_letters
for i in range(len(a)):
    print(a[i])
    print(b[a[i]-1:random.randint(len(a),len(b)):])