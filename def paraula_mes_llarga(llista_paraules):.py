def paraula_mes_llarga(llista_paraules):
    """Retorna la paraula amb més caràcters de la llista."""
    if not llista_paraules:  # Comprovar si la llista està buida
        return None  # Retorna None si la llista és buida
    
    # Assumeix que la primera paraula és la més llarga
    mes_llarga = llista_paraules[0]
    
    for paraula in llista_paraules:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula  # Actualitza la més llarga
    
    return mes_llarga

# Proves de la funció
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))  # Retorna "Paraula"
print(paraula_mes_llarga(["gat", "cavall", "gos"]))             # Retorna "cavall"
print(paraula_mes_llarga(["a", "b", "c"]))                      # Retorna "a"
print(paraula_mes_llarga([]))                                   # Retorna None