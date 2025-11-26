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
<<<<<<< HEAD
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



    
=======
    if i>n-1:
         return {"done": True}
    swap=False
    if fase=="buscar":
        j_actual=j
    if i<n and items[j] < items[min_idx]:
        min_idx = j

    j += 1

    if j >= n:
            fase = "swap"
    return {"a": min_idx,"b": j_actual,"swap": False,"done": False}

    elif fase == "swap":
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            result = {"a": i,"b": min_idx,"swap": True,"done": False}
        else:
            result = {"a": i,"b": min_idx,"swap": False,"done": False}

        i += 1
        if i >= n - 1:
            return {"done": True}

        j = i + 1
        min_idx = i
        fase = "buscar"

        return result
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.

return {"done": True}
>>>>>>> 6ee94ccecd9700f0909b52476e3574664bd7bdd2
