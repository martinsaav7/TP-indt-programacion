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

    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    return {"done": True}
