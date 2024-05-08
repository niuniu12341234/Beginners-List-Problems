print ("===Biggest, Smallest and Average===")
numsList = [56,121,49,33,4,67,34,40]
average = (sum(numsList)/len(numsList))
print ("The biggest number in the list is",max(numsList))
print ("The smallest number in the list is",min(numsList))
print ("The average of all the numbers is",average)
print ("===Same Start and End===")
stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
for elem in stringsList:
    if (len(elem) >=2 and (elem.endswith(elem[0].upper()) or elem.endswith(elem[0].lower()))):
        print(elem)
print ("===I Like Pesto===")
foods = []
for i in range(8):
    ipt = input("What's your favourite food?\n>> ")
    iptInFoods = False
    for f in foods:
        if ipt == f[0]:
            f.append(ipt)
            iptInFoods = True
            break
    if not iptInFoods:
        foods.append([ipt])
times = 0
mostElements = []
unmostElements = []
for f in foods:
    if len(f) >= times:
        mostElements.append(f[0])
        times = len(f)
    else:
        unmostElements.append(f[0])

for e in mostElements:
    print(e, 'is loved by', times, "people!")
    for _ in range(times):
        print('I love', e)

print('Other foods are:')
for u in unmostElements:
    print(u)
