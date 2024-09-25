#Group names: Jiayi Chen, Aderson Pham
#Assignment : No.1
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
        result.append("Number")
    
    #Check if input is reserved word
    if input in reserved:
        result.append("Reserved")
    
    #Check if input is identifier
    elif input[0] == '_' or input[0].isalpha():
        flag = True
        for char in input:
            if not char.isdigit() and not char.isalpha():
                flag = False
        if (flag):
            result.append("Identifier")
    print(input + ": ")
    for str in result:
        if str == "Number":
            print("Number: Yes")
        else:
            print("Number: No")
        if str == "Identifier":
            print("Identifier: Yes")
        else:
            print("Identifier: No")
        if str == "Reserved":
            print("Reserved: Yes")
        else:
            print("Reserved: No")
    print(result)
    return result
            
def main():
    operation("Token")
    operation("K-mart")
    operation("23andMe")
    operation("456")

main()
