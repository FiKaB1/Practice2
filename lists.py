thislist=[1,2,3,4,5,6]
print(thislist)
print(type(thislist))
list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(thislist[3])
print(thislist[-2])
print(thislist[2:4])
print(thislist[:5])
print(thislist[2:])
print(thislist[-5:-3])
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list")


liss=["Ali","Kapan","Amangul"]
liss[2]="Murat"
print(liss)
liss[0:2]=["Aruna","Zhanibek"]
print(liss)

liss[1:3]=["Fatima"]
print(liss)
liss[0:2]=["ali","kapan","karim"]

print(liss)


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
thislist.append("Lemon")
print(thislist)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


sandar=[1,2,3,4,4,5,6]
sandar.remove(4)
print(sandar)
sandar.pop(0)
print(sandar)
sandar.pop()
print(sandar)
del sandar[0]
print(sandar)


sandar.clear()
print(sandar)
del sandar

sandar=[1,2,3,4,5,6]
for x in sandar:
  print(x)

for i in range(len(sandar)) :
  print(sandar[i],end=" ")
i=0
while i<len(sandar) :
  print(sandar[i])
  i+=1

[print(x)  for x in sandar ]


fruits=["apple","banana","lemon","kilk"]
xn=[]
for x in fruits:
  if "a" in x:
    xn.append(x)

print(xn)

fruits=["apple","banana","lemon","kilk"]
xn=[x for x in fruits if "a" in x]
print(xn)

newlist = [x.upper() for x in fruits]



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


soz="Ali"
soz=soz[::-1]
print(soz)


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)



list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)