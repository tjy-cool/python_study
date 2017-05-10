#!/usr/bin/env python
# Funtion:      
# Filename:

import shutil

# with open("random_test.py", 'r', encoding='utf-8') as f1, \
#         open("random_test_new.py","w", encoding="utf-8") as f2:
#     shutil.copyfileobj(f1,f2)

# # 将源文件拷贝为目标文件，不用打开文件
# shutil.copy(r"E:\vscode_pragram\mine\Python3\Python_learning\day2\Code\dict_test.py", "test")
#
# # 只拷贝文件，不拷贝属性
# shutil.copyfile(r"E:\vscode_pragram\mine\Python3\Python_learning\day2\Code\dict_test.py", "test")
#
# # 只拷贝属性，不拷贝文件内容
# shutil.copymode(r"E:\vscode_pragram\mine\Python3\Python_learning\day2\Code\dict_test.py", "test")
#
# 拷贝目录
# shutil.copytree(r"E:\vscode_pragram\mine\Python3\Python_learning\day2\Code","day2_new")

# 删除目录
# shutil.rmtree(r'E:\vscode_pragram\mine\Python3\Python_learning\day6\Code1')

# 打包
shutil.make_archive(r'code', 'zip',
                    base_dir=r'E:\vscode_pragram\mine\Python3\Python_learning\day2\Code')


# 压缩模块
import zipfile
import gzip

zipfile.ZipFile(r"E:\vscode_pragram\mine\Python3\Python_learning\day2\Code")
