import random  # 获取随机数
import string

# print(string.ascii_lowercase)   # 获取26个小写字母
# print(string.ascii_uppercase)   # 获取26个大写字母
# print(string.digits)   # 获取0-9数字
# print(string.punctuation)  # 获取特殊符号：!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 生成一个随机字符
all_char = string.ascii_lowercase + string.ascii_uppercase + string.digits
random_char = random.choice(all_char)
#
#
a = ""
for i in range(4):
    random_char = random.choice(all_char)
    a += random_char
print("获取的机数：",a)
# print(string.punctuation)
