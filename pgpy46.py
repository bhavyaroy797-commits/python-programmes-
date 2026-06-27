def countnow(PLACES):
    for i in PLACES:
        if len(PLACES[i])>5:
            print(PLACES[i].upper())
PLACES={1:'delhi',2:'mumbai',3:'goa',4:'new york'}
countnow(PLACES)
