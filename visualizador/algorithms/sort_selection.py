n = 0
i = 0
j = 0
min_idx = 0
fase = ""
items = []

def init(vals):
   
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"
def step():
    global items, n, i, j, min_idx, fase
    if i >= n - 1:
        return {"done": True}

    if fase == "buscar":
      
        j_actual = j if j < n else n - 1

        if j < n:
            if items[j] < items[min_idx]:
                min_idx = j
            j += 1
            return {"a": min_idx,"b": j_actual,"swap": False,"done": False }
        fase = "swap"
        return { "a": min_idx,"b": j_actual,"swap": False, "done": False }
    if fase == "swap":
        hizo_swap = False
        i_actual = i           
        min_actual = min_idx   
        if min_idx != i:
         
            items[i], items[min_idx] = items[min_idx], items[i]
            hizo_swap = True
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"
        return {"a": i_actual,"b": min_actual, "swap": hizo_swap, "done": False}



    
