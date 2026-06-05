def function(y):
    if len(y) == 1:
        return "z"
    else:
        return "z" + function(y[1:])

# Análisis solicitado en el Problema #10:
# ¿Qué hace el código?
# Retorna un string compuesto únicamente de letras 'z', 
# con el mismo largo que el string original 'y'.

x = function("aaa")
print(f"Resultado de function('aaa'): {x}") # Imprime "zzz"
