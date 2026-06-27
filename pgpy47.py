def lenword(STRING):
    t=()
    l=STRING.split()
    for i in l:
        t+=(len(i),)
    return t
print("come let us have some fun")
print(lenword("come let us have some fun"))        
