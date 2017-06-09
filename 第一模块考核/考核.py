
n = 1
sum = 0
while n<=100:
    if n % 2 == 1:  # 奇数
        sum += n
    else:
        sum += -n
    n += 1

print(sum)


name = ['alex', 'eric', 'rain']
name_str ='_'.join(name)
# name_str = '%s_%s_%s'%(name[0], name[1], name[2])
print(name_str)

# name_str = ''
# for index,val in enumerate(name):
#     name_str =

# pirnt
