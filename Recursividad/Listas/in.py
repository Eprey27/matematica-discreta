def dato(a, L):
    Lista = L.copy()  # Crear una copia de la lista para evitar modificar la original
    
    if not Lista:
        return "Dato no encontrado"
    
    Vl = Lista[-1]
    
    if str(a) == str(Vl):
        return "Dato encontrado"
    
    Lista.pop()  # Eliminar el último elemento de la lista
    
    return dato(a, Lista)

# Ejemplo de uso
data_list = [10, 20, 30, 40, 50]
result = dato(30, data_list)
print(result)  # Debería imprimir "Dato encontrado"
