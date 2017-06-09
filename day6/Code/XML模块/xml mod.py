#!/usr/bin/env python
# Funtion:      
# Filename:

import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print(child.tag, child.attrib)
    for i in child.iter('year'):
    # for i in child:

        print('\t', i.tag, i.attrib, i.text)

# 只遍历year节点
for node in root.iter('year'):
    print(node.tag, node.text)

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('update','True')
tree.write('xmltest.xml')

# 删除
for country in root.findall('country'):
    if int(country.find('rank').text) > 50:
        root.remove(country)
tree.write('test2.xml')

