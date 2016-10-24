# -*- coding:utf-8 -*-
__author__ = 'joann'

import nltk
import sys
from nltk.collocations import *
from nltk.corpus import stopwords,webtext
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures, spearman_correlation, ranks_from_scores
import codecs
import re

pos_dir='./pos.txt'
output_dir = './collocation.txt'
#stopwords = [',','.','...','-','--','\'','\"',';','<','>','?','!',':','_']
#pos_set = set(['NN_NN','JJ_NN','VB_NN','NN_NN_NN','JJ_NN_NN','NN_JJ_NN','JJ_JJ_NN','NN_IN_NN','IN_DT_NN'])
pos_set = set()
collocation_set = set()
people_pos_set = set(['PRP','NNP'])
be_pos_set = set(['VBD','VBP','VBZ'])
prone_pos_set = set(['PRP$'])

def read_pos():
    fr = open(pos_dir,'r')
    while 1:
        line = fr.readline()
        if not line:
            break
        line = line.strip()
        pos_set.add(line)

def output():
    #fw = codecs.open(''.join([output_dir, file, '.txt']), 'w')
    fw = codecs.open(output_dir, 'a')
    for item in collocation_set:
        fw.write("%s\n" % item)
    fw.close()

def get_collocation(item):
    item_pos = '_'.join([pos for (word,pos) in nltk.pos_tag(item)])
    if item_pos not in pos_set: #只抽取满足词性组合的搭配词
        return
    item_word_list = []
    for (word,pos) in nltk.pos_tag(item): #获取搭配短语的词性
        if pos in prone_pos_set:
            item_word_list.append('one\'s')
        if pos in people_pos_set:
            item_word_list.append('sb')
        elif pos in be_pos_set:
            item_word_list.append('be')
        else:
            item_word_list.append(word.lower())
    #output('_'.join(item_word_list))
    collocation_set.add('_'.join(item_word_list))

def demo(scorer_bam = None, compare_scorer_bam = None, scorer_tam=None, compare_scorer_tam=None):
    if scorer_bam is None:
        scorer_bam = BigramAssocMeasures.likelihood_ratio
    if compare_scorer_bam is None:
        compare_scorer_bam = BigramAssocMeasures.raw_freq

    if scorer_tam is None:
        scorer_tam = TrigramAssocMeasures.likelihood_ratio
    if compare_scorer_tam is None:
        compare_scorer_tam = BigramAssocMeasures.raw_freq

    regex = '^[A-Za-z]+$'   #正则表达式匹配英文单词
    str_regex = re.compile(regex)
    for file in webtext.fileids():  # 根据文件逐个处理
        words_list = []
        for word in webtext.words(file):
            if not str_regex.match(word):   #如果不是纯英文单词，则跳过
                continue
            words_list.append(word)

        # 获取二元搭配，窗口大小为3,4,5
        for window_size in range(3,4):
            bcf = BigramCollocationFinder.from_words(words_list,window_size)
            bcf.apply_freq_filter(window_size)

            for item in bcf.nbest(scorer_bam, 1000):
                get_collocation(item)   #获取搭配次词
        # 获取三元搭配
        for window_size in range(3, 4):
            tcf = TrigramCollocationFinder.from_words(words_list, window_size)
            tcf.apply_freq_filter(window_size)
            # tcf.apply_word_filter(word_filter)
            #corr = spearman_correlation(ranks_from_scores(tcf.score_ngrams(scorer)),
              #                          ranks_from_scores(tcf.score_ngrams(compare_scorer)))
            for item in tcf.nbest(scorer_tam, 1000):
                get_collocation(item)

if __name__ == '__main__':
    import sys
    from nltk.metrics import BigramAssocMeasures
    try:
        scorer_bam = eval('BigramAssocMeasures.' + sys.argv[1])
    except IndexError:
        scorer_bam = None
    try:
        compare_scorer_bam = eval('BigramAssocMeasures.' + sys.argv[2])
    except IndexError:
        compare_scorer_bam = None
    try:
        scorer_tam = eval('TrigramAssocMeasures.' + sys.argv[3])
    except IndexError:
        scorer_tam = None
    try:
        compare_scorer_tam = eval('TrigramAssocMeasures.' + sys.argv[4])
    except IndexError:
        compare_scorer_tam = None

    read_pos()
    demo(scorer_bam, compare_scorer_bam, scorer_tam, compare_scorer_tam)
    output()