import re

# a = re.match("inet", "inet 地址:192.168.12.55 广播:192.168.12.255")
# print(a.group())   # 从头开始匹配

a = re.match("\w+", "inet 地址:192.168.12.55 广播:192.168.12.255")
print(a.group())   # 从头开始匹配


a = re.search('(\d{2})(\d{2})(\d{2})(\d{4})', "ID:371425199203159809, name:tom")
print(a.groups())


a = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})",
           "ID:371425199203159809, name:tom")
print(a.group())
print(a.groups())
print(a.groupdict())
print(a.groupdict("city"))

           
a = re.search("(\d{1,3}\.){3}\d{1,3}",
              "inet 地址:192.168.12.55 广播:192.168.12.255")
print(a.group())

a = re.findall("\d+", "1ffds23ddf234fds324343")         # 取数字
print(a)

a = re.findall("\D+", "1ffds23ddf234fds324343") # 或者[a-zA-Z]+   取字母
print(a)

a = re.split("\d+", "ab3dff8787dfdfs87fd4")
print(a)

a = re.sub("\d+", "\t".expandtabs(4), "fsf34df3df4d54vf4f5fd45df", count=2)
print(a)


# a = re.split("\\\\", r"c:\users\data\python35")
a = re.split("\\\\", r"c:\\users\data\python35")
print(a)

a = re.search('a', r"ABC", flags=re.I)
print(a.group())
