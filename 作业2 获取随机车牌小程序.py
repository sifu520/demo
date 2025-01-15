import random
import string

count = 0
while count <= 3:
    car_nums = []  # 存储供用户选择的号
    for i in range(20):
        n1 = "".join(random.sample(string.digits, 5))
        car_nums.append(n1)
        print(f"{i + 1}苏G·{n1}")
    choice = input("输入你喜欢的车牌号码：").strip()  # 输入数据并清除前后的空格
    if choice in car_nums:  # 代表选择是合法的
        print(f"恭喜你选择了新车牌号：{choice}")
        exit("Good Luck.")
    else:
        print("不合法的选择...")
    count += 1
