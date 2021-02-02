'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

#get users input setnece
sentence = input("enter sentence")
#get user symbol
symbol = input("enter symbol")
#get letter to replace
letter = input("enter letter to replace")
#replace all occurences of first letter with symbol

anwser = sentence.replace(letter, symbol)
print(anwser)