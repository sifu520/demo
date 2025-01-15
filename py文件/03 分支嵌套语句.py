pid = input("请输入你到身份证号：")
# 身份证号位数是否是18位
if len(pid) == 18:
    print("打印个人基本信息")
    # （1）打印性别，身份证号倒数第二位如果是偶数，代表是女生，否则男生
    num = int(pid[16])  # 把字符串数字"5"转换位整型数字5
    if num % 2 == 0:
        print("你是女生")
    else:
        print("你是男生")
    # （2）打印籍贯
    jiGuanCode = pid[:6]
    print("jiGuanCode", jiGuanCode)  # 320704
    if jiGuanCode == "320704":
        print("籍贯：连云港市")
    elif jiGuanCode == "110000":
        print("籍贯：北京市")
    elif jiGuanCode == "120000":
        print("籍贯：天津市")
    elif jiGuanCode == "310000":
        print("籍贯：上海市")
    else:
        print("不是直辖市")
else:
    print("你输入的身份证号有误，程序结束！")
