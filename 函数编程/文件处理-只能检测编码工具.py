#!/usr/bin/env  python3
# coding utf-8

"""
# >>> import chardet
# >>> f = open('1.txt',mode='rb')
# >>> date= f.read()
# >>> print(date)
# b'\xd0\xd5\xc3\xfb\t    \xb5\xd8\xc7\xf8\t\xc9\xed\xb8\xdf\t\xcc\xe5\xd6\xd8\t\xb5\xe7\xbb\xb0\n\xbf\xf6\xd3\xbd\xc3\xdb \t\xb1\xb1\xbe\xa9\t171\t48\t13651054608\n\xcd\xf5\xd0\xc4\xd1\xd5 \t\xc9\xcf\xba\xa3\t169\t46\t13813234424\n\xc2\xed\xcf\xcb\xd3\xf0 \t\xc9\xee\xdb\xda\t173\t50\t13744234523\n\xc7\xc7\xd2\xe0\xb7\xc6 \t\xb9\xe3\xd6\xdd\t172\t52\t15823423525\n\xc2\xde\xc3\xce\xd6\xf1 \t\xb1\xb1\xbe\xa9\t175\t49\t18623423421\n\xc1\xf5\xc5\xb5\xba\xad \t\xb1\xb1\xbe\xa9\t170\t48\t18623423765\n\xd4\xc0\xc4\xdd\xc4\xdd \t\xc9\xee\xdb\xda\t177\t54\t18835324553\n\xba\xd8\xcd\xf1\xdd\xe6 \t\xc9\xee\xdb\xda\t174\t52\t18933434452\n\xd2\xb6\xe8\xf7\xdd\xe6\t\xc9\xcf\xba\xa3\t171\t49\t18042432324\n\xb6\xc5\xe6\xa9\xe6\xa9 \xb1\xb1\xbe\xa9  167 49 13324523342'
# >>> chardet.detect(date)
# {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
# >>> date.decode('gb2312')   字符解码
# '姓名\t    地区\t身高\t体重\t电话\n况咏蜜 \t北京\t171\t48\t13651054608\n王心颜 \t上海\t169\t46\t13813234424\n马纤羽 \t深圳\t173\t50\t13744234523\n乔亦菲 \t广州\t172\t52\t1518623423421\n刘诺涵 \t北京\t170\t48\t18623423765\n岳妮妮 \t深圳\t177\t54\t18835324553\n贺婉萱 \t深圳\t174\t52\t18933434452\n叶梓萱\t上海\t171\t49\t18042432324\n杜姗姗 北京  167 49 13324523342'
# >>>
"""

import  chardet

f = open(file='1.txt',mode='rb')
data = f.read()
f.close()

result = chardet.detect(open('1.txt',mode='rb').read())
print(result)