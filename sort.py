#!/usr/bin/python

import sys
import getopt
from timeit import default_timer as timer

def checkArgs(input_file, sorting_method, output_file):
    if not (input_file and sorting_method and output_file):
        return False
    return True

def builtin(words):
    words.sort()
    return words

#50k = 263s
def bubble(words):
    for j in range(len(words), 0, -1):
        for i in range(0, j - 1, 1):
            if words[i] > words[i + 1]:
                tmp = words[i]
                words[i] = words[i + 1]
                words[i + 1] = tmp
    return words

#50k => 476s
def bubble2(words):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(words) - 1, 1):
            if words[i] > words[i+1]:
                swap = True
                tmp = words[i]
                words[i] = words[i + 1]
                words[i + 1] = tmp
    return words

# 50k => 112s
def insertion(words):
    ordered_list = []
    for word in words:
        i  = 0
        while i < len(ordered_list) and word > ordered_list[i]:
            i += 1

        ordered_list.insert(i, word)
    return ordered_list

def select_min_index(words, i):
    min_val = None
    min_index = None
    while i < len(words):
        if min_val > words[i] or min_val is None:
            min_val = words[i]
            min_index = i
        i += 1
    return min_index

# 50k => 260s
def selection(words):
    for index, value in enumerate(words):
        min_index = select_min_index(words, index)
        tmp  = words[index]
        words[index] = words[min_index]
        words[min_index] = tmp
    return words

def main(argv):
    usage = "{0} -i <input_file> -s <sorting_method> -o <output_file>".format(sys.argv[0])
    input_file = None
    sorting_method = None
    output_file = None
    words = []
    sorting_methods = {'bubble': bubble, 'bubble2' : bubble2, 'builtin' : builtin, 'insertion' : insertion, 'selection' : selection}

    try:
        opts, args = getopt.getopt(argv, "hi:s:o:")
        for opt, arg in opts:
            if opt in ('-h'):
                print usage
                sys.exit()
            elif opt in ('-i'):
                input_file = arg
            elif opt in ('-s'):
                sorting_method = arg
            elif opt in ('-o'):
                 output_file = arg
        if not checkArgs(input_file, sorting_method, output_file):
            raise getopt.GetoptError("Arguments error")

    except getopt.GetoptError:
        print usage
        sys.exit(2)

    with open(input_file, 'r') as ifile:
        words = ifile.read().splitlines()

    start = timer()
    sorted_words = sorting_methods[sorting_method](words)
    end = timer()
    print "Elapsed time {0}: ".format(end - start)

    with open(output_file, "w") as ofile:
        for i in sorted_words:
            ofile.write(i + "\n")

if __name__ == "__main__":
    main(sys.argv[1:])
