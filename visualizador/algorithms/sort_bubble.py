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
    global items, n, i, j

    # Si ya terminamos todas las pasadas
    if n <= 1 or i >= n - 1:
        return {"done": True}

    # Comparar los elementos en j y j+1
    a = j
    b = j + 1
    swap = False

    if items[a] > items[b]:
        # Hacemos el intercambio
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzar punteros
    j += 1
    if j >= n - i - 1:
        # Terminó una pasada completa, reiniciamos j y avanzamos i
        j = 0
        i += 1

    # Si ya terminamos todas las pasadas
    if i >= n - 1:
        return {"done": True}

    return {"a": a, "b": b, "swap": swap, "done": False}