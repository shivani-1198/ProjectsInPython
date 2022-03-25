def CheckEmail(email):

    k,d,j = 0,0,0
    
    if len(email) >= 6: #1
        if email[0].isalpha(): #2
            if ("@" in email) and (email.count("@") == 1): #3
                if (email[-3] == ".") ^ (email[-4] == "."): #4
                    for i in email:
                        if i == i.isspace(): #5
                            k = 1
                        elif i.isalpha():
                            if i == i.upper(): #5
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1
    
                    if k == 1 or j == 1 or d == 1:
                        print("Wrong Email because of fifth error")
                    else:
                        print("Right Email!")
                else:
                    print("Wrong Email because of fourth error")
            else:
                print("Wrong Email because of third error")
        else:
            print("Wrong Email because of second error")
    else:
        print("Wrong Email because of first error")


email = raw_input("Enter your Email : ")
CheckEmail(email)