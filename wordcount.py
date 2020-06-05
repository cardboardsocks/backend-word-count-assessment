#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Ben McKenzie, demo, and jaspal"
# originally thought something was wrong with my code, so i went through the demo, but it turns out i used args ainstead of argv...

import sys




def create_word_dict(filename):
    word_dict = {}
    with open(filename) as f:
        for line in f.readlines():
            for word in line.lower().split():
                if word in word_dict:
                    word_dict[word] +=1
                else:
                    word_dict[word] = 1
    return word_dict

    # word_count = {}
    # f = open(filename, 'r')
    # for line in f:
    #     words = line.split()
    #     for word in words:
    #         word = word.lower()
    #         if word in word_count:
    #             word_count[word] += 1
    #         else:
    #             word_count[word] = 1
    # f.close()
    # return word_count
    


    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """

def print_words(filename):
    new_dict = create_word_dict(filename)
    dict_items = new_dict.items()
    sorted_items = sorted(dict_items)
    for word in sorted_items:
        print(str(word[0]) + ' : ' + str(word[1]))


    # word_count = create_word_dict(filename)
    # words = sorted(word_count.keys())
    # for word in words:
    #     print(word, word_count[word])
    # new_dict = create_word_dict(filename)

    # for word in sorted(new_dict.keys()):
    #     print(word, new_dict[word])
    
def get_count(x):
    return x[1]

def print_top(filename):
    """Prints the top count listing for the given file."""
    # new_dict = make_word_dict(filename)
    # dict_items = new_dict.items()
    # sorted_items = sorted(dict_items, key=lambda x: x[1], reverse = True)
    # for word in sorted_items[:20]:
    #     print(str(word[0]) + ' : ' + str(word[1]))

    word_count = create_word_dict(filename)
    items = sorted(word_count.items(), key=get_count, reverse=True)
    for item in items[:20]:
        print(item[0], item[1])

# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
