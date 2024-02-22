# [1, 1, 2, 3, 5...]

def fibonnati(n: int):
    sequencia = [0, 1]

    # print(sequencia[-2])
    while len(sequencia) < n:
        proximo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_numero)
    
    return sequencia
    

        
print(fibonnati(10))