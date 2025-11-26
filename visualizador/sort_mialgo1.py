# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i=0
j=0
gap=0

def init(vals):
    global items, n,gap,i,j
    items = list(vals)
    n = len(items)
    # TODO: inicializar punteros/estado
    gap= n//2
    i= gap
    j =i
def step():
    global items, n,gap,i,j
    
    if gap == 0:
        return {"done": True}
    a=j
    b=j-gap
    swap=False
    if items[a]<items[b]:
        items[a],items[b]=items[b],items[a]
        swap=True
        j =j - gap
    else:
        i +=1
        if i<n:
            j=1
        else:
            gap=gap//2
            i=gap
            j=i
    if gap==0:
        return {"done":True}
    
    return{"a":a,"b":b,"swap":swap,"done":False}
    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1return {"done": True}
