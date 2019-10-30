#!/usr/bin/env python
#_*_coding:utf-8_*_

"""
re的匹配语法有以下几种
re.match 从头开始匹配
re.search 匹配包含
re.findall 把所有匹配到的字符放到以列表中的元素返回
re.split 以匹配到的字符当做列表分隔符
re.sub 匹配字符并替换
re.fullmatch 全部匹配

"""
import re
# s = '371481199306143242'

# res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
# s = 'alex22jac23in31jinxin50'
# print(s.split('[0-9]'))
# print(re.split('\d',s))

# print(re.findall('\d+',s))



# s = 'alex22jac23in31j|inxi-lobn50'
# print(re.split('\d+|#|-',s))

# s = 'alex22jac23i\n31j|inxi-lobn50'
# print(re.split('\|',s))

# s = 'alex22jac23i\sn31j|inxi-lobn50'
# print(re.split('\\\\',s))

# s1 = 'alex22jac23i\\sn31j|inxi-lobn50'
# re.sub('\d+','_',s1)
# 'alex_jac_i\\sn_j|inxi-lobn_'

# s1 = 'alex22jac23i\\sn31j|inxi-lobn50'
# re.sub('\d+','_',s1,count=2)
# Out[15]: 'alex_jac_i\\sn31j|inxi-lobn50'

"""
re.fullmatch('\w+@\w+\.com|cn|edu',"alex@oldboydeu.com")
Out[19]: <_sre.SRE_Match object; span=(0, 18), match='alex@oldboydeu.com'>
re.fullmatch('\w+@\w+\.(com|cn|edu)',"alex@oldboydeu.com")
Out[20]: <_sre.SRE_Match object; span=(0, 18), match='alex@oldboydeu.com'>
re.fullmatch('\w+@\w+\.(com|cn|edu)',"alex@oldboydeu.cn")
Out[21]: <_sre.SRE_Match object; span=(0, 17), match='alex@oldboydeu.cn'>
re.fullmatch('\w+@\w+\.(com|cn|edu)',"alex@oldboydeu.org")
"""

'''
re.compile('\w+@\w+\.(com|cn|edu)')
Out[23]: re.compile(r'\w+@\w+\.(com|cn|edu)', re.UNICODE)
pattern=re.compile('\w+@\w+\.(com|cn|edu)')
pattern
Out[25]: re.compile(r'\w+@\w+\.(com|cn|edu)', re.UNICODE)
pattern.fullmatch('alex@oldbedum.com')    
Out[27]: <_sre.SRE_Match object; span=(0, 17), match='alex@oldbedum.com'>
'''
"""
标识符
Flags标志符
re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
M(MULTILINE): 多行模式，改变'^'和'$'的行为
S(DOTALL): 改变'.'的行为,make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.
X(re.VERBOSE) 可以给你的表达式写注释，使其更可读，下面这2个意思一样

re.match(pattern, string, flags=0)

从起始位置开始根据模型去字符串中匹配指定内容，匹配单个
pattern 正则表达式
string 要匹配的字符串
flags 标志位，用于控制正则表达式的匹配方式
"""
'''
a = re.compile(r"""\d + # the integral part
                \. # the decimal point
                \d * # some fractional digits""", 
                re.X)

b = re.compile(r"\d+\.\d*")
'''
s =  ' - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
re.search(r'\([^()]+\)',s).group()#可拿到最里层的括号中的值

'(-40/5)'