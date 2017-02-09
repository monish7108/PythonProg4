def encryption(userinput,mylist):
    output = ""
    for i in userinput:
        if i in mylist:
            output+=mylist[mylist.index(i)-3]
        else:output+=i
    print(output)


if __name__=="__main__":
    userinput = input("Enter the input: ")
    mylist = []
    for i in range(26):
        mylist.append(chr(ord('A') + i))
    encryption(userinput,mylist)