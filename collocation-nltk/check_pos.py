# -*- coding:utf-8 -*-
__author__ = 'joann'

import nltk

input_dir='./CollocationWord.txt'
output_dir='./pos.txt'
def output(pos):    #输出词性文件
    fw = open(output_dir,'a')
    fw.write('%s\n'%(pos))
    fw.close()

def read_base():
    fr = open(input_dir,'r')
    while 1:
        line = fr.readline()
        if not line:
            break
        line = line.strip().rstrip('_').strip() #避免类似“in_hand_”的情况
        tokens = line.split('_')
        print tokens
        item_pos = '_'.join([pos for (word, pos) in nltk.pos_tag(tokens)])
        output(item_pos)

read_base()