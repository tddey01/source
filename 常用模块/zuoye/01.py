def calculator(expression='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + '
                          '7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'):
    '''
    计算器
    总逻辑：
        1.先找出内层括号，然后计算其内的终值，用终值替换原表达式
        2.然后重复以上过程
    无括号部分计算逻辑:
        1.先截断为数字和运算符的列表，数字可包含负号；
        2.运算列表中的值并替换，先乘除后加减；
    :param expression: 字符串表达式
    :return:表达式计算值
    '''
    print(eval(expression))
import re
operatorDict = {
    '+': lambda a, b: float(a) + float(b),
    '-': lambda a, b: float(a) - float(b),
    '*': lambda a, b: float(a) * float(b),
    '/': lambda a, b: float(a) / float(b),
}

def calWithOutBrackets(expression='-1+2*3/4-5*-3'):
    # 截断为数字和运算符的列表
    for i in operatorDict:
        expression = expression.replace(i, 's' + i + 's')
        l = expression.split('s')
        # l2将填充为一个数字和运算的列表，数字可以带负号
        l2 = []
        i = 0
        while i < len(l):
            if l[i] == '':
                l2.append(l[i + 1] + l[i + 2])  # 带负号的数字
                i += 2
            else:
                l2.append(l[i])  # 不带负号的数字和运算符
            i += 1
        # 运算乘除
        i = 1
        while i < len(l2):
            if l2[i] in ['*', '/']:
                l2[i - 1:i + 2] = [operatorDict[l2[i]](l2[i - 1], l2[i + 1])]
            else:
                i += 2
        # 运算加减
        while len(l2) > 1:
            l2[0:3] = [operatorDict[l2[1]](l2[0], l2[2])]
        return str(l2[0])

    expression = expression.replace(' ', '')
    check = re.search('\([^\(\)]+\)', expression)
    while check:
        checkValue = check.group()
        # print(checkValue)
        expression = expression.replace(checkValue, calWithOutBrackets(checkValue[1:-1]))
        check = re.search('\([^\(\)]*\)', expression)
    else:
        return calWithOutBrackets(expression)