import os
import shutil
import random

entries_covid = os.listdir('2/train/covid')
test_covid = random.sample(entries_covid,50)


for i in test_covid:
    original = 'D:\\machine_learning_ex\\chest\\2\\train\\covid\\' + str(i)
    target = 'D:\\machine_learning_ex\\chest\\2\\test\\covid\\' + str(i)
    shutil.move(original, target)


entries_normal= os.listdir('2/train/normal')
test_normal = random.sample(entries_normal,50)


for i in test_normal:
    original = 'D:\\machine_learning_ex\\chest\\2\\train\\normal\\' + str(i)
    target = 'D:\\machine_learning_ex\\chest\\2\\test\\normal\\' + str(i)
    shutil.move(original, target)

