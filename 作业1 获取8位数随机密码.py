# 自动生成一组8位字符的密码
import random
import string
# string.ascii_letters   获取小写和大写字母
# string.ascii_lowercase 获取小写字母
# string.ascii_uppercase 获取大写字母
# string.digits 获取0-9数字
# string.punctuation 获取特殊符号：!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 将大小写字母、数字和特殊符号 拼接到all_char变量中
all_char = string.ascii_letters + string.digits   # + string.punctuation
passwd = ""
for i in range(8):
    # 将随机获取的字符串赋值给random_char
    random_char = random.choice(all_char)
    # 将passwd值+random_char值，赋值给passwd
    passwd += random_char
# 打印输出结果
print("随机生成的密码为：", passwd)
