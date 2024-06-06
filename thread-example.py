import threading
import time

def DoingHomework(_Homeork, _delay, _name):

    print(f"{_name}에게 {_Homeork}만큼의 숙제가 주어졌습니다\n")

    for _ in range(_Homeork):
        print(f"{_name}이(가) {_+1}의 숙제를 완료하였습니다.\n")
        time.sleep(_delay)

    print(f"{_name}이 숙제를 끝마쳤습니다\n")

thread_1 = threading.Thread(target= DoingHomework, args = (5, 0.4, ' 1학년'))
thread_1.start()

DoingHomework(6,0.1, '3학년')
