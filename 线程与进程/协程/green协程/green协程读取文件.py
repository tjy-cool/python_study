
from greenlet import greenlet
import queue


def open_file():

    with open('aa.txt', 'r', encoding='utf-8') as f:
        for line in f:
            q.put(line)
            


def write_file():
    with open('bb.txt', 'w', encoding='utf-8') as f:
        f.write(q.get())
        


if __name__ == '__main__':
    q = queue.Queue()
    gr1 = greenlet(open_file)
    gr2 = greenlet(write_file)
    gr1.switch()
