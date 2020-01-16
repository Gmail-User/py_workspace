# number = 0
# while number < 10:          # number 값이 10 이상이면, 반복을 빠져나감
#     number = number + 1     # 1씩 number 변수값 증가
#     # 수행시킬 코드
#     print('number:', number)

def funcInTemp2():
    print('temp::funcInTemp invoked.')
    pass

# func3 = lambda : None
func3 = lambda : print('temp::func2 invoked.')

for number in range(1, 11):     # 1 ~ 10까지(11은 포함안됨) 숫자생성
    print('number:', number)

print(__name__)

if (__name__ == '__main__'):
    import sys
    # del sys       # To unimport 'sys'

    from pprint import pprint as pp
    
    print(type(sys))
    print(sys)

    pp(sys.path)
    pp(sys.argv)
    pass

print('-'*30)

import os
print(os.getcwd()) # <--------------------- ******

from temp import temp as tt
print(dir())

print('-'*30)