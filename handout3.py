#Group names: Jiayi Chen, Aderson Pham
#Assignment : Handout #3
#--------------------------------------------------------
# Write a program to read one token at a
# time from the given text file and determine whether the token is
# i. A number
# ii. An identifier (must start with underscore or a letter, followed by
# more letters, more digits, or more underscores
# iii. A reserved word. List of reserved words: string reserved[5]={“while”, “for”, “switch”, “do”,
# “return” };
# -------------------------------------
# Sample output for #1
# Token number identifier reserved word
# K-mart no no no
# 23andMe no no no
# 456 yes no no
# ...........

def operation(input):
    #Empty list to append classifications
    result = []

    #List of reserved words
    reserved = ["while", "for", "switch", "do"]

    #Check if input is digit
    if (input.isdigit()):
        result.append("Yes")
    else:
        result.append("No")
    
    #Check if input is reserved word
    if input in reserved:
        result.append("Yes")
    else:
        result.append("No")
    
    #Check if input is identifier
    if input[0] == '_' or input[0].isalpha():
        flag = True
        for char in input:
            if not char.isdigit() and not char.isalpha():
                flag = False
        if (flag):
            result.append("Yes")
            res = f"{input:<10}" + f"{result[0]:>15}" + f"{result[1]:>15}" + f"{result[2]:>15}"
            print(res)
        else:
            result.append("No")
            res = f"{input:<10}" + f"{result[0]:>15}" + f"{result[1]:>15}" + f"{result[2]:>15}"
            print(res)
            
def main():
    #2 lines below are cited from https://www.geeksforgeeks.org/read-a-text-file-into-a-string-variable-and-strip-newlines-in-python/?ref=oin_asr10
    data = open("words.txt", 'r').read()
    data = data.split("\n")
    print(data)
    print("Token               Number        Identifier    Reserved Word")
    for str in data:
        operation(str)
main()
