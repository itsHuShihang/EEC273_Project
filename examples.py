import os

event_1 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
event_2 = ['a', 'c', 'd', 'b', 's']
event_3 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
event_4 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']

# generate a file calle "activities_generated.dat" if it does not exit
file_name = "activities_generated.dat"
if not os.path.exists(file_name):
    os.makedirs(file_name)

# write data to the file
with open("activities_generated.dat", 'a') as ag:  # OPTION: or change 'a' to 'w'
    for i in event_1:
        ag.write(i)
    ag.write("\n")
    for i in event_2:
        ag.write(i)
    ag.write("\n")


# read data from the file to the test
# TODO: change a name for "test"
with open("activities_generated.dat", '+r') as ag:
    test = ag.readlines()

print(test)

N_loop = 10
acts_per_loop = 21
N_line = N_loop*acts_per_loop
print("N_line is ", N_line)

evve = [[] for i in range(N_line)]
# TODO: 30 is not enough here, how to ensure the number is enough

index = 0
for str in test:
    for item in str:
        if item != '\n':
            evve[index].append(item)
        if item == '\n':
            index = index+1
            index = index % N_line  # TODO: need a better solution if out of range
print(evve)
for i in range(len(evve)):
    if len(evve[i]):
        print(i, evve[i])
