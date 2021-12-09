import random
from random import randint
import builtins


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

    for i, n in enumerate('victor'):
        print(f'index: {i} {n}')


def zipSample():
    print(list(zip([1, 2, 3], ['a', 'b', 'c'])))


def passSample():
    num = 10
    while num != 0:
        print(num)
        num = num - 1
    else:
        pass


def comprehensionSample():
    args = [1, 2, 3, 4, 5]
    result = [int(arg) * int(arg) for arg in args]
    print(result)


def normalMethod(a, b):
    return a * b


def defaultMethodParameter(a, b, c=1):
    return a * b * c


def prepend1(elem, lt=[]):
    lt.insert(0, elem)
    return lt


def methodParameterSample1(name, age):
    return {'name': name, 'age': age}


def sum(*numbers):
    print(f'{type(numbers)=}')
    result = 0;
    for number in numbers:
        result += number

    return result


def ajax(url, **userSettings):
    settings = {
        'method': userSettings.get('method'),
        'content': userSettings.get('content'),
        'body': userSettings.get('body')
    }
    print(f'{url=}, {settings=}')


def positionalOnlySample1(a: int, /, b: str):
    return a + int(b)


def positionalOnlySample2(a: int, *, b: str):
    return a + int(b)


def strListUpper(list, mapper):
    result = []
    for ele in list:
        result.append(mapper(ele))

    return result


xx = 10


def outer():
    yy = 20
    xx = 100

    def inner():
        zz = 30
        print(f'{xx=}')
        print(f'{yy=}')
        print(f'{zz=}')

    inner()
    print(f'{xx=}')
    print(f'{yy=}')


def testLocals():
    ggyy = 100
    print(locals())


def testGlobal():
    global aa
    aa = 1000


def add(a: int, b: int) -> int:
    return a + b


def sum2(*numbers: int) -> int:
    result: int = 0;
    for num in numbers:
        result += num
    return result


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
    print(f'method方法參數擺放不一定要按照順序, 可以利用參數名稱指定: {methodParameterSample1(name = "victor", age= 35)=}')
    print(f'使用*做引數拆解, 不過看起來這種用法需要照順序: {methodParameterSample1(*("victor", 35))=}')
    print(f'**可讓dict針對對應key做引數拆解: {methodParameterSample1(**{"name": "victor", "age": 35})=}')
    print(f'方法參數上加上* 代表不定長度引數,會被收集為一個tuple: {sum(1,2,3,4,5)=}')
    print('----------')
    print('當參數過多時可用**定義參數')
    print(f'使用**來定義參數,讓指定關鍵字讓指定關鍵字參數收集為dict: {ajax("http://127.0.0.1", method="post",content="json", body="123123")=}')
    print(f'{ajax("http://127.0.0.1", **{"method":"post","content":"json","body":"123123"})=}')
    print('----------')
    print(f'參數加上/代表前面的參數順序需一至且不可使用關鍵字參數的方式: {positionalOnlySample1(1, "2")=}, {positionalOnlySample1(1, b="2")=}')
    # 下列會報錯
    # positionalOnlySample1(a=1, b='2')
    # positionalOnlySample1(b='2', 1)
    print(f'參數加上*代表後面的參數需要使用關鍵字參數的方式: {positionalOnlySample2(1, b= "2")=}')
    # 下列會報錯
    # positionalOnlySample2(b="2", 1)
    # positionalOnlySample2(1, "2")

    print()
    print(f'在python內函式也是一個物件, {type(sum)=}')
    print(f'也可以這樣用: {strListUpper(["a", "b", "c"], mapper=str.upper)=}')

    print(f'也可以用lambda, 格式--> lambda 變數: 表達式, {strListUpper(["a", "b", "c"], lambda ele: str.upper(ele))=}')
    print('若lambda不需要參數就直接冒號就可以了, 如下')
    lambdaTest = lambda: randint(1, 10)
    print(f'{lambdaTest()=}')
    print('若lambda多參數的狀況加逗號就可以, 如下')
    lambdaTest = lambda n1, n2: n1 if n1 > n2 else n2
    print(f'{lambdaTest(1, 20)=}')

    print()
    print('python變數不用事先宣告, 在指定值的時候就可成為變數, 並建立自己的作用範圍, 在存取變數時會先從自己的範圍內尋找, 若找不到才往外尋找')
    print('全域變數實際上是以模組檔案為界')
    outer()
    print(f'{xx=}')
    print(f'dir函式可用來查詢指定物件尚可使用的名稱與函式: {dir(builtins)=}')
    print(f'python上有個locals函式,可用來查詢區域變數的名稱與數值: ')
    testLocals()
    print('可以使用global關鍵字將變數宣告為全域, 如下')
    testGlobal()
    print(f'{aa=}')
    print(f'python3還新增了nonlocal關鍵字, 指名變數非區域變數讓直譯器依照區域函式、外包函式、全域、內建的順序來尋找變數')

    print()
    print('------ Type Hint ------')
    # 提示method型態
    add(1, 2)
    # 提示變數型態
    names: list = ['victor', 'bob']
    # 進一步提示元素型態
    data: list[str] = ['aa', 'bb']
    user: tuple[str, int] = ('g', 1)
    passwd: dict[str, str] = {'victor': 'abc123456', 'bob': 'xxx123'}

    # 不定長度引數的type hint表示法
    sum2(1, 2, 3)
    print('------ Type Hint ------')
