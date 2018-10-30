import random
a = random.sample(range(100), 10)
def b (mylist):
     c  = len(mylist) - 1 #c = последняя цыфра
     for z in range(0, c):
          for x in range(0, c):
               if mylist[x] > mylist[x+1]:
                    mylist[x], mylist[x+1] = mylist[x+1], mylist[x]


     return mylist
d = b(a)
print(d)