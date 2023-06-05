import os
import random

event_1 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
event_2 = ['a', 'c', 'd', 'b', 's']
event_3 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
event_4 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']




def randomEventWriteInFile(file, event: list, error: int, repeat: int, ignore: int) -> None:
    """
    :param file: 文件流 - 你要操作的读入文件流
    :param event: 事件流 - 你要基于哪个事件数组进行随机遍历
    :param error: 错误率 - 百分比整数, 出错的概率直接替换原来的事件至26个字母中其中一个可能与之前的重复
    :param repeat: 重复率 - 百分比整数, 重复率会在原来的元素再追加一个
    :param ignore: 忽略率 - 百分比整数, 忽略率会直接跳过当前元素直接进行下一个元素
    :return: void
    """

    if_write=1
    for item in event:
        # Simulate ignoring with a 5% probability
        if random.random() < ignore / 100:
            if_write=0
            continue

        # Simulate error with a 10% probability
        elif random.random() < error / 100:
            # Replace the item with a random letter
            item = random.choice('abcdefghijklmnopqrstuvwxyz')

        # Simulate repetition with a 5% probability
        elif random.random() < repeat / 100:
            file.write(item)

        # Write the item to the file
        if_write=1
        file.write(item)


    if if_write:
        file.write("\n")



if __name__ == '__main__':

    # generate a file called "activities_generated.dat" if it does not exit
    file_name = "activites_generated.dat"
    if os.path.exists(file_name):
        os.makedirs(file_name)

    # write data to the file
    with open("activities_generated.dat", 'a') as ag:  # OPTION: or change 'a' to 'w'
        randomEventWriteInFile(ag, event_1, 10, 5, 5)
        randomEventWriteInFile(ag, event_2, 10, 5, 5)

    # read data from the file to the event_seq -> 这部分就是你example下方的我没做任何修改按照你的需求也不需要修改
    with open("activities_generated.dat", '+r') as ag:
        event_seq = ag.readlines()

    print(event_seq)

    N_loop = 10
    acts_per_loop = 21
    N_line = N_loop*acts_per_loop
    print("N_line is ", N_line)

    evve = [[] for i in range(N_line)]
    # TODO: 30 is not enough here, how to ensure the number is enough

    index = 0
    for str in event_seq:
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
