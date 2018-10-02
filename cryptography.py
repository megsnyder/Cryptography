"""
cryptography.py
Author: Meg
Credit: None

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
n=0
m=0
o=0
sum1 = []
encrypt = []
string = ' '
associations.find('c')
associations[8]
inpu1t= input("Enter e to encrypt, d to decrypt, or q to quit: ")
if inpu1t == 'e':
    mess = input("Message: ")
    key = input("Key: ")
    list1=list(mess)
    list2=list(key)
    if len(list2)<len(list1):
        diff =len(list1)-len(list2)
        for n in range(0,diff):
            list2.append(list2[n])
            n+=1
    tuples=list(zip(list1,list2))
    for i in list1:
        add1=associations.find(list1[m])+associations.find(list2[m])
        if add1>len(associations):
            add2=add1-len(associations)
        else:
            add2=add1
        sum1.append(add2)
        m+=1

    for i in range(0,len(sum1)):
        index=associations[sum1[o]]
        encrypt.append(index)
        o+=1
    for i in encrypt:
        string+=i
    print(string)
elif inpu1t == 'd':
    mess = input("Message: ")
    key = input("Key: ")
    list1=list(mess)
    list2=list(key)
    if len(list2)<len(list1):
        diff =len(list1)-len(list2)
        for n in range(0,diff):
            list2.append(list2[n])
            n+=1
    tuples=list(zip(list1,list2))
    for i in list1:
        add1=associations.find(list1[m])-associations.find(list2[m])
        if add1>len(associations):
            add2=add1-len(associations)
        else:
            add2=add1
        sum1.append(add2)
        m+=1

    for i in range(0,len(sum1)):
        index=associations[sum1[o]]
        encrypt.append(index)
        o+=1
    for i in encrypt:
        string+=i
    print(string)
elif inpu1t == 'q':
    print("Goodbye!")
else:
    print("Did not understand command, try again.")