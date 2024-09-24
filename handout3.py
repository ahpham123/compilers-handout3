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
    print ("waat")
    #List of reserved words
    reserved = ["while", "for", "switch", "do"]
    
    #Check if input is digit
    if (input.isdigit()):
        return "Number"
    
    #Check if input is reserved word
    if input in reserved:
        return "Reserved"
    
    #Check if input is identifier
    elif input[0] == '_' or input[0].isalpha():
        for char in input:
            if not char.isdigit() or not char.isalpha():
                return False
        return "Identifier"
    print ("wat")
            
        
    

def main():
    print(operation("Token"))
    print("?")

main()
