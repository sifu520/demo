'''
for循环语法格式:

for i in 容器数据类型对象:
    循环语句
'''

# # (1) 遍历字符串
# s = "abcdefg"
# for i in s:
#     print("hello yuan")
#     print(i)
#
# # (2) 遍历列表
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in l:
#     print("hello yuan")
#     print(i)

# (3) range循环
for i in range(1, 101):  # 循环1-100次
    print(i)

# (4) range进阶用法  range(start,end,step=1)
for i in range(1, 101, 2):  # 循环1-100次,每次加2
    print(i)

for i in range(100, 1, -1):  #100到1显示，步长为-1
    print(i)
