class Cypher:

    def encode_Cesar_cypher(string, cipher=7):

        coded_list = []
        string = string.replace(" ", "")
        string = string.lower()
        for letter in string:
            num = ord(letter)
            num = num + cipher
            if num > 122:
                inverse = num - 122
                new_num = 96 + inverse
                char = chr(new_num)
                coded_list.append(char)
            else:
                char = chr(num)
                coded_list.append(char)

        string = "".join(coded_list)
        return string


    def decode_Cesar_cypher(string, cipher=7):
        decoded_list = []
        for letter in string:
            num = ord(letter)
            num = num - cipher
            if num < 97:
                inverse = 97 - num
                new_num = 123 - inverse
                char = chr(new_num)
                decoded_list.append(char)
            else:
                char = chr(num)
                decoded_list.append(char)
        string = "".join(decoded_list)
        return string

code = Cypher.encode_Cesar_cypher("hello zanthor I hope you are having a great day")
print(code)
decode = Cypher.decode_Cesar_cypher(code)
print(decode)
