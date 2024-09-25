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
        result.append("Number")
    else:
        result.append("Not Number")
    
    #Check if input is reserved word
    if input in reserved:
        result.append("Reserved")
    else:
        result.append("Not Reserved")
    
    #Check if input is identifier
    if input[0] == '_' or input[0].isalpha():
        flag = True
        for char in input:
            if not char.isdigit() and not char.isalpha():
                flag = False
        if (flag):
            result.append("Identifier")
        else:
            result.append("Not Identifier")
    print(input + ": ")
    if "Number" in result:
        print("Number: Yes")
    else:
        print("Number: No")
    if "Identifier" in result:
        print("Identifier: Yes")
    else:
        print("Identifier: No")
    if "Reserved" in result:
        print("Reserved: Yes")
    else:
        print("Reserved: No")
    print()
            
def main():
    operation("K-Mart")
    operation("23andMe")
    operation("456")

main()
