def slice_simple():
    texto = "Awesome"
    print(texto[:3].lower())
    if len(texto)%2==0:
        print(texto[int(len(texto)/2)-1:int(len(texto)/2)+2].lower())
    else:
        print(texto[round(len(texto)/2)-2:round(len(texto)/2)+1].lower())   

    print(texto[:4].lower()+texto[-3:].lower())
        
