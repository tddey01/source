#!/usr/bin/env python
#_*_coding:utf-8_*_
"""


"""

# 自己创建xml文档

import xml.etree.ElementTree as ET


new_xml = ET.Element("namelist")  #root  根
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
sex.text = '33'
name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(new_xml) #生成文档对象
et.write("test.xml", encoding="utf-8",xml_declaration=True)

ET.dump(new_xml) #打印生成的格式