#!/usr/bin/python

import sys
import getopt
import string
import random

def checkArgs(lines, max_size, output_file):
    if not (lines and max_size and output_file):
        return False
    if type(lines) != int:
        return False
    if type(max_size) != int:
        return False
    if type(output_file) != str:
        return False
    return True

def randomWord(size):
    word = ""
    for i in range(0, size):
        word += random.choice(string.ascii_letters + string.digits)
    return word

def randomDigits(size):
    digits = ""
    for i in range(0, size):
        digits += random.choice(string.digits)
    return digits

def main(argv):
    usage = "{0} -l <nb_lines> -s <max_size> -o <output_file> [-i]".format(sys.argv[0])
    lines = None
    max_size = None
    output_file = None
    generate_integers = False

    try:
        opts, args = getopt.getopt(argv, "hli:s:o:")
        for opt, arg in opts:
            if opt in ('-h'):
                print usage
                sys.exit()
            elif opt in ('-l'):
                 lines = int(arg)
            elif opt in ('-s'):
                max_size = int(arg)
            elif opt in ('-o'):
                output_file = arg
            elif opt in('-i'):
                generate_integers = True
            print "Generating integers"
        if not checkArgs(lines, max_size, output_file):
            raise getopt.GetoptError("Args error")

    except getopt.GetoptError:
        print usage
        sys.exit(2)

    with open(output_file, 'w') as my_file:
        for line in range(0, lines):
            if not generate_integers:
                word = randomWord(max_size)
            else:
                word = randomDigits(size)
            print "{0} {1}".format(line, word)
            my_file.write(word + '\n')

if __name__ == '__main__':
    main(sys.argv[1:])
