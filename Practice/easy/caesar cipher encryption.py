def caesarCipherEncryptor(string, key):
    z = ord("z")
    new_string = ""
    if (key / 26) > 1:
        mod = key // 26
        mod1 = 26 * mod
        key = abs(key - mod1)
    for letter in string:
        num = ord(letter)
        num1 = num + key
        if num1 > z:
            temp = num1 - z
            new_string += chr(ord("a") - 1 + temp)
        else:
            new_string += chr(num1)
    return new_string




string = "xyz"
key = 54

x = caesarCipherEncryptor(string, key)
print(x)