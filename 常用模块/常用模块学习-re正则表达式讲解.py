#!/usr/bin/env python
#_*_coding:utf-8_*_
import re

"""
f = open("兼职白领学生空姐模特护士联系方式.txt",'r',encoding="gbk")

phones = []

for line in f:
    name,city,height,weight,phone = line.split()
    if phone.startswith('1') and len(phone) == 11:
        phones.append(phone)

print(phones)

"""
# f = open(file='user_test.txt',mode='r',encoding='utf8')
#
# phones= []
#
# for line in f:
#     name,city,height,weight,phone = line.split()
#     if phone.startswith('1') and len(phone) == 11:
#         phones.append(phone)
#
# print(phones)

'''
re模块
    正则表达式就是字符串的匹配规则，在多数编程语言里都有相应的支持，python里对应的模块是re

常用的表达式规则
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾， 若指定flags MULTILINE ,re.search('foo.$','foo1\nfoo2\n',re.MULTILINE).group() 会匹配到foo1
'*'     匹配*号前的字符0次或多次， re.search('a*','aaaabac')  结果'aaaa'
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次 ,re.search('b?','alex').group() 匹配b 0次
'{m}'   匹配前一个字符m次 ,re.search('b{3}','alexbbbs').group()  匹配到'bbb'
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配， re.search("(abc){2}a(123|45)", "abcabca456c").group() 结果为'abcabca45'


'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的，相当于re.match('abc',"alexabc") 或^
'\Z'    匹配字符结尾，同$ 
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'

'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","3714811993


re的匹配语法有以下几种
    re.match 从头开始匹配
    re.search 匹配包含
    re.findall 把所有匹配到的字符放到以列表中的元素返回
    re.split 以匹配到的字符当做列表分隔符
    re.sub 匹配字符并替换
    re.fullmatch 全部匹配
    
'''
# f = open(file='user_test.txt',mode='r',encoding='utf8')
# data = f.read()
#
# print(re.findall("[0-9]{11}",data))

# s ='abc1d3e'
# re.match('[0-9]',s)
# re.match('[0-9]',a)
# print(re.match('[0-9]',s))

'''
re.match  从头匹配
re.search 全局匹配
span   字符串找到具体位置
s ='abc1d3e'
import re
re.match('[0-9]',s)
re.match('[0-9]','1bdfd')
Out[5]: <_sre.SRE_Match object; span=(0, 1), match='1'>
re.search('[0-9]',s)
Out[6]: <_sre.SRE_Match object; span=(3, 4), match='1'>
re.search('[0-9]',s).group()
Out[7]: '1'
match_res = re.search('[0-9]',s)
if  match_res:
    print(match_res.group())
    
1
re.findall('[0-9]',s)
Out[10]: ['1', '3']


re.search('^ab','abd')
Out[13]: <_sre.SRE_Match object; span=(0, 2), match='ab'>  
re.search('b$','ab')
Out[14]: <_sre.SRE_Match object; span=(1, 2), match='b'>   以b结尾
re.match('bob$','bob')
Out[17]: <_sre.SRE_Match object; span=(0, 3), match='bob'>   绝对匹配 很少用
re.search('a*','aaaabac')
Out[18]: <_sre.SRE_Match object; span=(0, 4), match='aaaa'>     匹配*号前的字符0次或多次
re.search('a*','aaaalex').group()
Out[20]: 'aaaa'
re.search('ab*','aaaaalex')
Out[21]: <_sre.SRE_Match object; span=(0, 1), match='a'>
re.search('ab*','abbaaaalex')
Out[22]: <_sre.SRE_Match object; span=(0, 3), match='abb'>
re.search('ab*','abbbbaaaalex')
Out[23]: <_sre.SRE_Match object; span=(0, 5), match='abbbb'>
re.search('a?','aaabbb')
Out[28]: <_sre.SRE_Match object; span=(0, 1), match='a'>   匹配前一个字符1次或0次 
re.search('a{2}','addaad')
Out[32]: <_sre.SRE_Match object; span=(3, 5), match='aa'>  匹配前一个字符m次 
re.search('.{2}','addaad')
Out[33]: <_sre.SRE_Match object; span=(0, 2), match='ad'>

re.search('[0-9]{2}','addaaad23')
Out[37]: <_sre.SRE_Match object; span=(7, 9), match='23'>  匹配前一个字符n到m次
re.search('[a-z]{1,2}','2lex')
Out[43]: <_sre.SRE_Match object; span=(1, 3), match='le'>

re.search('[a|A]lex','Alex')
Out[50]: <_sre.SRE_Match object; span=(0, 4), match='Alex'> 匹配|左或|右的字符

re.search('([a-z]+)([0-9]+)','alex123').groups()   分组匹配
Out[57]: ('alex', '123')

re.search('\Aalex','alex')
Out[58]: <_sre.SRE_Match object; span=(0, 4), match='alex'>  只从字符开头匹配，或^

re.search('\d+','alex2')
Out[59]: <_sre.SRE_Match object; span=(4, 5), match='2'>
re.search('\d','alex2')
Out[60]: <_sre.SRE_Match object; span=(4, 5), match='2'>    匹配数字0-9  只要匹配到一个  就结束匹配

re.search('\D+','al^%$exa23456234f222')
Out[61]: <_sre.SRE_Match object; span=(0, 8), match='al^%$exa'>   匹配非数字 


re.search('\w+','alexa23456234f222')
Out[64]: <_sre.SRE_Match object; span=(0, 17), match='alexa23456234f222'>
re.search('\w+','al^%$exa23456234f222')
Out[65]: <_sre.SRE_Match object; span=(0, 2), match='al'>      匹配非[A-Za-z0-9]

re.search('\W+','al^%$exa23456234f222')
Out[67]: <_sre.SRE_Match object; span=(2, 5), match='^%$'>   取出特殊字符

In[71]: re.search('\s+','alex\njack\tdd\rmack')
Out[71]: <_sre.SRE_Match object; span=(4, 5), match='\n'>
In[72]: re.findall('\s+','alex\njack\tdd\rmack')
Out[72]: ['\n', '\t', '\r']       匹配空白字符
 
'''
'''
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾， 若指定flags MULTILINE ,re.search('foo.$','foo1\nfoo2\n',re.MULTILINE).group() 会匹配到foo1
'*'     匹配*号前的字符0次或多次， re.search('a*','aaaabac')  结果'aaaa'
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次 ,re.search('b?','alex').group() 匹配b 0次
'{m}'   匹配前一个字符m次 ,re.search('b{3}','alexbbbs').group()  匹配到'bbb'
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配， re.search("(abc){2}a(123|45)", "abcabca456c").group() 结果为'abcabca45'


'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的，相当于re.match('abc',"alexabc") 或^
'\Z'    匹配字符结尾，同$ 
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'

'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").
groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}
'''

s = '371481199306143242'
# print(re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s).groups())

res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())
