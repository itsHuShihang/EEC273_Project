event = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
with open("activities_generated.dat",'a') as ag:
    for i in event:
        ag.write(i)
    ag.write("\n")
with open("activities_generated.dat",'+r') as ag:
    test=ag.readlines()
print(test)