lista = [5,10,2,3,1]

#AKO JE DUZINA LISTE VECA OD 1
    # uzmes mid,R je od mida dalje, L je od 0 do mida
    #rekurzija sa R i sa L
    # dok je i manji od duzine L i dok je j manji od duzine R provjeri koji je manji i taj stavi prvo u listu
    #ono sto je ostalo dodaj u listu


def merge_sort(lista):
    if len(lista)>1:
        mid = len(lista)//2

        L = lista[:mid]
        R = lista[mid:]

        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        while i<len(L) and j < len(R):
            if L[i]<R[j]:
                lista[k] = L[i]
                i+=1
            else:
                lista[k] = R[j]
                j+=1
            k+=1


        while i<len(L):
            lista[k] = L[i]
            i+=1
            k+=1

        while j<len(R):
            lista[k] = R[j]
            j+=1
            k+=1



merge_sort(lista)
print(lista)
