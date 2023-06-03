event_1= ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
event_2= ['a', 'c', 'd', 'b', 's']
event_3= ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
event_4= ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']

with open("activities_generated.dat",'a') as ag:
    for i in event_1:
        ag.write(i)
    ag.write("\n")
    for i in event_2:
        ag.write(i)
    ag.write("\n")
with open("activities_generated.dat",'+r') as ag:
    test=ag.readlines()

print(test)

evve=[[] for i in range(30)] 
# TODO: 30 is not enough here, how to ensure the number is enough

i=0
for str in test:
    for item in str:
        if item !='\n':
            evve[i].append(item)
        if item == '\n':
            i=i+1
            i=i%30  # TODO: need a better solution if out of range
print(evve)