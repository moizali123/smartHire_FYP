import random

def get_random(lst):
    a = random.choice(lst)
    lst.remove(a)
    return a,lst

def for_ques1():
    integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                     14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    samp = get_random(integer_list)
    return samp

def for_ques2(lst):
    samp2 = get_random(lst)
    return samp2


