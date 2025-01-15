x = input("要转换进制的十进制数：")
s = "二进制：{n:b}   八进制：{n:o}   十进制：{n:d}  十六进制：{n:x}"
print(s.format(n=int(x)))

x = input("要转换科学计数法的十进制数字：")
s = "{n:e}"
print(s.format(n=int(x)))

x = input("要转为百分数的十进制数字：")
s = "{n:%}"
print(s.format(n = float(x)))