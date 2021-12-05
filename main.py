from random import randint

def ifelseSample(score):
    if score == 100:
        print('好棒 滿分')
    elif score >= 90:
        print('好棒 A級')
    elif score >= 80:
        print('還不錯 B級')
    elif score >= 70:
        print('還行 C級')
    elif score >= 60:
        print('普通請繼續加油 C級')
    else:
        print('痾... D級')

def normalWhileLoopSample():
    while (number := randint(0, 9)) != 5:
        print(number)
    print('找到5啦!')

def forInSample():
    names = ['a', 'b', 'c']

    for name in names:
        print(name.upper())

    for i in range(len(names)):
        print(f'names[{i}]= {names[i]}')

    for i,n in enumerate('victor'):
        print(f'index: {i} {n}')

def zipSample():
    print(list(zip([1,2,3], ['a','b','c'])))

def passSample():
    num = 10
    while num != 0:
        print(num)
        num = num - 1
    else:
        pass

def comprehensionSample():
    args = [1,2,3,4,5]
    result = [int(arg) * int(arg) for arg in args]
    print(result)

def normalMethod(a, b):
    return a * b

def defaultMethodParameter(a, b, c = 1):
    return a * b * c

def prepend1(elem, lt = []):
    lt.insert(0, elem)
    return lt

if __name__ == '__main__':

    name = 'Victor'
    if name == 'Victor':
        print('Hi Victor')
    else:
        print('Hi Guest')

    print('if else if 範例')
    ifelseSample(int(input('請輸入分數: ')))

    print('while loop 範例')
    normalWhileLoopSample()

    print('for in 範例')
    forInSample()

    print('zip 範例, 將兩個list 向拉鍊一樣一一配對')
    zipSample()

    print('pass 代表什麼都不做, 只是為了用來維持語法完整性')
    passSample()

    print('comprehension 語法: [運算式 for a in b] , 每次運算的結果會被收集成一個list')
    comprehensionSample()

    print(f'一般method使用, {normalMethod(2, 10)=}')
    print(f'可讓一般方法參數有預設值, {defaultMethodParameter(2, 10)=}')
    print(f'python不支援重載 可以使用參數預設值的方式模擬, {defaultMethodParameter(2, 10, 10)=}')
    print(f'python 會依照定義建立相關資源, 這是有可能踩到的陷阱 {prepend1(10)=}, {prepend1(0, [20, 30])=},'
          f' 因為執行到def method時就建立了[], 而這個list會一直存在,所以若使用預設參數此參數就會一直是同一個, 不注意就會造成意料之外的結果 {prepend1(100)=}')
