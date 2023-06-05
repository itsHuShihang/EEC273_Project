import os
import random

event_1 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
event_2 = ['a', 'c', 'd', 'b', 's']
event_3 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
event_4 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']

# generate a file called "activities_generated.dat" if it does not exit
file_name = "activites_generated.dat"
if os.path.exists(file_name):
    os.makedirs(file_name)


def randomEventWriteInFile(file, event: list, error: int, repeat: int, ignore: int) -> None:
    """
    :param file: 文件流 - 你要操作的读入文件流
    :param event: 事件流 - 你要基于哪个事件数组进行随机遍历
    :param error: 错误率 - 百分比整数, 出错的概率直接替换原来的事件至26个字母中其中一个可能与之前的重复
    :param repeat: 重复率 - 百分比整数, 重复率会在原来的元素再追加一个
    :param ignore: 忽略率 - 百分比整数, 忽略率会直接跳过当前元素直接进行下一个元素
    :return: void
    """
    for item in event:
        # Simulate error with a 10% probability
        if random.random() < error / 100:
            # Replace the item with a random letter
            item = random.choice('abcdefghijklmnopqrstuvwxyz')

        # Write the item to the file
        file.write(item)

        # Simulate repetition with a 5% probability
        if random.random() < repeat / 100:
            file.write(item)

        # Simulate ignoring with a 5% probability
        if random.random() < ignore / 100:
            continue
    file.write("\n")


# write data to the file
with open("activities_generated.dat", 'a') as ag:  # OPTION: or change 'a' to 'w'
    randomEventWriteInFile(ag, event_1, 10, 5, 5)
    randomEventWriteInFile(ag, event_2, 10, 5, 5)

# read data from the file to the test -> 这部分就是你example下方的我没做任何修改按照你的需求也不需要修改
