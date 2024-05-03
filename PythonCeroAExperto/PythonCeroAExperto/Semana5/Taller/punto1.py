def ObtenerMayor(n1, n2,n3):
    texto = "es el numero mayor."
    if n2 <= n1 >= n3:
        return (f"{n1} {texto}")
    elif n1 <= n2 >= n3:
        return (f"{n2} {texto}")
    else:
        return (f"{n3} {texto}")
        
print(ObtenerMayor(14, 8, 10))