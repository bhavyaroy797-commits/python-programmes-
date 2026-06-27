def rev(n) :
    if len(n)==0 :
        return n
    return rev(n[1:])+n[0]
m= 1749 
m_str = str(m)
rev_m = rev(m_str)
print("Reversed Number is: " + rev_m)


