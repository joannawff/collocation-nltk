# collocation-nltk
This is an example of extracting phrase collocations using NLTK. 

1.配置
环境：python2.7.11
安装工具：nltk
运行工具：pycharm

2.运行步骤
step1：check_pos.py，获取验证集的短语词性组合；
    输入：ColllocationWord.txt，输出：pos.txt
step2：main.py，主要过程，抽取短语集合；（主要过程，生成的文件也就是搭配结果文件）
    输入：文件名
    输出：collocation.txt
step3：assess.py，评估过程，对照验证集，计算精确率、召回率、F1值
    输入：collocaiton.txt，ColllocationWord.txt
    输出：same.txt，以及精确率、召回率、F1值

3.其他
本过程的路径都是相对路径，因此整个工程放置在任何目录都可以。
若要检验其他语料，请将文本放入./data/路径下。
