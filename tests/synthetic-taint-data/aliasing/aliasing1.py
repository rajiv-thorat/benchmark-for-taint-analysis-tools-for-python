from class_a import ClassA
from class_b import ClassB
import random
import sys
from helper import run_cmd

if __name__=='__main__':
    a = ClassB()
    p = ClassB()

    b = ClassA()
    q = ClassA()

    if random.randint(1, 10) < 5:
        x = a
        y = b
    else:
        x = p
        y = q

    x.a_instance = y
    q.random_data = sys.argv[1]
    run_cmd(a.a_instance.random_data)