def SuperASCII(userdict, SuperAsciiDict):
    for i in userinput:
        if userdict[i] == SuperAsciiDict.index(i)+1:
            continue
        else:
            print("it is not valid")
            exit()

if __name__ == "__main__":
    userinput = input("Enter the String: ")
    SuperAsciiDict = []
    num = ord('a')
    for i in range(26):
        SuperAsciiDict.append(chr(num))
        num += 1
    userdict = {}
    for i in userinput:
        if i in userdict.keys():
            userdict[i] += 1
        else:
            userdict[i] = 1
    SuperASCII(userdict,SuperAsciiDict)
    print("It is Valid")