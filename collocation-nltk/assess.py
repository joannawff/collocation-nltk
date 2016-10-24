# -*- coding;utf-8 -*-
__author__ = 'joann'

common_dir='./same.txt'
source_dir='./CollocationWord.txt'
result_dir='./collocation.txt'
source_set = set()
result_set = set()

def read_collocation(file):
    fr = open(file,'r')
    collocation_set = set()
    while 1:
        line = fr.readline()
        if not line:
            break
        line = line.strip().rstrip('_').strip()
        collocation_set.add(line)
    return collocation_set

def output(common_set):
    fw = open(common_dir, 'w')
    for item in common_set:
        fw.write("%s\n" % item)
    fw.close()

def stat():
    source_len = len(source_set)
    result_len = len(result_set)
    common = [colloc for colloc in result_set if colloc in source_set]
    output(common)
    common_len = len(common)
    print source_len, result_len, common_len
    precise = round(common_len * 1.0 / result_len,4)
    recall = round(common_len * 1.0 / source_len,4)
    f1 = round(2 * precise * recall / (precise + recall),4)
    print "precise:%s\trecall:%s\tf1:%s" % (precise, recall, f1)


source_set = read_collocation(source_dir)
result_set = read_collocation(result_dir)
stat()