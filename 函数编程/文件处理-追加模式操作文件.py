# s =  open(file='1.txt',mode='a',encoding='gbk')
# s.write('\n开发者  ls  sldow')
# s.close()

# l = open(file='1.txt',mode='r', encoding='gbk')
# print(l.read())
# l.close()
# 文件操作时，以'1'或'ab'模式打开  怎只能追加，即：在原来内容尾部追加内容
#  ab 写入时需要直接传入以某种编码01000101 即：字节类型
#  a和 encoding 写入时需要传入 unicode 字符串，内部会根据 encoding 指定的编码将 unicod 字符串转换为该编码


