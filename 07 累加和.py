# (1) 计算1+2+3+......+100的累加和

# sum = 0
# for i in range(1, 101):
#     sum += i
#     print(i)
# print(sum)

# (2) 计算1-100所有偶数和
sum1 = 0
sum2 = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum1 += i
    else:
        sum2 += i
print("1-100偶数的和为：", sum1)
print("1-100基数的和为：", sum2)
