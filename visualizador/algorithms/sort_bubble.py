# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():

 if i>=n-1:
    global items,n,i,j
    if i>=n-1:
        return{"done": True}
    swap=False
    if items[j]>items[j+1]:
        j,j+1=j+1,j
        swap= True
    if j>= n-i-1:
        j=0
        i+=1
    return {"j":j, "i":i, "swap":swap, "done":False}

    return {"done": True}