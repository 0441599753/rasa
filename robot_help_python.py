# start
import time
from datetime import datetime
import random
t1 = datetime.now()
def wait(n):
    time.sleep(n)
def limitation1(x,y,t1,t2):
    if x == y:
        return t1
    else:
        return t2
def limitation2(x,y,t1,t2):
    if x > y:
        return t1
    else:
        return t2
def limitation3(x,y,t1,t2):
    if x < y:
        return t1
    else:
        return t2
def limitation4(x,y,t1,t2):
    if x >= y:
        return t1
    else:
        return t2
def limitation5(x,y,t1,t2):
    if x <= y:
        return t1
    else:
        return t2
def calculator(n1,n2,d):
    if d == '+':
        j = n1 + n2
        return j
    elif d == '-':
        m = n1 - n2
        return m
    elif d == '*':
        z = n1 * n2
        return z
    elif d == '/':
        t = n1 / n2
        return t
    elif d == 'power':
        p = n1 ** n2
        return p
    else:
        return "Error"
def len_of_list(lst):
    sh = 0
    l = []
    for _ in lst:
        sh +=1
        l.append(sh)
    return len(l)
def list1(lst,n,y):
    lst[n] = y
def list2(lst1,lst2):
    sh2 = -1
    if len(lst1) == 0:
        print("Len of your list is zero.")
    else:
        for _ in range(len(lst1)):
            sh2 +=1
            r = lst1[sh2]
            lst2.append(r)
def loop_print_for_list(lst):
    sh3 = -1
    for _ in range(len(lst)):
        sh3+=1
        r1 = lst[sh3]
        print(r1)
def loop_limitation_equal_for_list(lst,t1,t2,t3):
    sh4 = -1
    for _ in range(len(lst)):
        sh4+=1
        if lst[sh4] == t1:
            print(t2)
        else:
            print(t3)
def replace_element_of_list(lst,t1,t2):
    li = []
    sh5 = -1
    for _ in range(len(lst)):
        sh5+=1
        if lst[sh5] == t1:
            lst[sh5] = t2
        else:
            li.append('False')
    return li
def hour_python():
    hour1 = t1.hour
    return hour1
def minute_python():
    minute1 = t1.minute
    return minute1
def dat():
    date = t1.date()
    return date
def make_random_number_for_list(lst,n,p,q):
    if len(lst) > 0:
        print("Your list is zero.")
    else:
        while len(lst) < n:
            r = random.randint(p,q)
            lst.append(r)
def div(n1,n2):
    l = []
    f1 = n1 // n2
    l.append(f1)
    f2 = n1 % n2
    l.append(f2)
    return l
# The end
