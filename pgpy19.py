def display(str):
    m=""
    for i in range(0,len(str)):
        if (str[i].isupper()):
            m+=str[i].lower()
        elif (str[i].islower()):
            m+=str[i].upper()
        else:
            if i%2==0:
               m+=str[i-1]
            else:
                m+="#"
    print(m)
display("Fun@World2.0")

