import requests
import time
import csv
import json
import sys

# 基础的进度条
# for i in range(1, 101):
#     print('\r', end='')
#     print('进度:{}% '.format(i), "▓" * (i // 2), end='')
#     sys.stdout.flush()
#     time.sleep(0.05)


# 带有时间的进度条
#
# t = 60
# print('**********带有时间的进度条****************')
# start = time.perf_counter()
# for i in range(t + 1):
#     finsh = '▓' * i
#     need_do = '-' * (t - i)
#     progress = (i / t) * 100
#     dur = time.perf_counter() - start
#     print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(progress, finsh, need_do, dur), end='')
#     time.sleep(0.05)


# 使用tqdm库的进度条

# from tqdm import tqdm
# for i in tqdm(range(1,60)):
#       '''代码'''
#     time.sleep(0.05)


# 使用alive_progress库的进度条
# from alive_progress import alive_bar
#
# with alive_bar(len(range(100))) as bar:
#     for item in range(100):
#         # 显示进度
#         bar()
#         '''代码'''
#         time.sleep(0.05)



# 使用pysimpleGUI库的进度条

# import PySimpleGUI as sg
# count=range(100)
# for i,item in enumerate(count):
#     sg.one_line_progress_meter('实时进度条',i+1,len(count),'-key-')
#     '''代码'''
#     time.sleep(0.05)


# 使用progressbar库的进度条

import progressbar
p=progressbar.ProgressBar()

for i in p(range(100)):
    '''代码'''
    time.sleep(0.05)