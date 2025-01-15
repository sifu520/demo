import base64


def base64_encrypt(text):
    """
    对输入的文本进行Base64加密（编码）
    """
    text_bytes = text.encode('utf-8')  # 将文本转换为字节类型，因为Base64操作针对字节
    encrypted_bytes = base64.b64encode(text_bytes)
    return encrypted_bytes.decode('utf-8')  # 再转换回字符串返回


def base64_decrypt(encrypted_text):
    """
    对输入的Base64加密文本进行解密（解码）
    """
    encrypted_bytes = encrypted_text.encode('utf-8')
    try:
        decrypted_bytes = base64.b64decode(encrypted_bytes)
        return decrypted_bytes.decode('utf-8')
    except base64.binascii.Error:  # type: ignore
        print("输入的内容不是合法的Base64编码格式，请检查输入！")
        return None


print('''
       文本加密解密程序
1.加密
2.解密

''')

x1 = input("请输入对应序号:")
if x1 == "1":
    jiami = input("请输入要加密的内容:")
    encrypted_result = base64_encrypt(jiami)
    print("加密后的结果:", encrypted_result)
elif x1 == "2":
    jiemi = input("请输入要解密的内容:")
    decrypted_result = base64_decrypt(jiemi)
    print("解密后的结果:", decrypted_result)
else:
    print("输入序号不正确")

print("程序已结束！")
