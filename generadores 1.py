"""
### **¿Qué es un generador en Python?**
Un **generador** es una función que usa la palabra clave `yield` para devolver elementos uno a uno según se necesiten, en lugar de devolver toda la secuencia al mismo tiempo como lo haría una lista.
### **¿Por qué son útiles los generadores?**
- **Eficiencia de memoria**: No almacenan todos los elementos en memoria. Generan cada elemento bajo demanda.
- **Cálculo lento**: Útiles cuando calcular un elemento es costoso y no necesitas todos los datos al mismo tiempo.
- **Iteración infinita**: Se pueden usar para producir secuencias infinitas sin problemas de memoria.

### **¿Cómo funciona `yield` en un generador?**
A diferencia de una función con `return`, que termina su ejecución y devuelve un valor, cuando una función usa `yield`:
1. Suspende la ejecución de la función y devuelve el valor actual al llamador.
2. Conserva (pausa) su estado interno, lo cual significa que puede reanudar desde donde se había quedado.

### **¿Qué hace `next()` en un generador?**
La función `next()` se utiliza para obtener el siguiente valor de un generador. Cuando llamas a `next()`:
1. El generador ejecuta el código desde donde se quedó (estado de suspensión).
2. Se detiene nuevamente en la siguiente instrucción `yield`, devolviendo el valor especificado después de `yield`.
3. Si ya no hay más valores que generar, se lanza la excepción `StopIteration`.




"""
print("funion tradicional con return")
def generador_pares(limite):
    num= 1
    lista=[]
    while num <limite:
        lista.append(num*2)
        num += 1
    return lista

print(generador_pares(10))



print("funion con yield")
def generador_pares(limite):
    num= 1

    while num <limite:
        yield num*2

        num = num + 1

resultadoPares= generador_pares(10)

# for i in resultadoPares:
#     print(i)                                      #recorremos el objeto iterable e impriimos sus valores


#con next podemos entrar en un estado de suspencia entre llamda y llamada
print("primer valor")
print(next(resultadoPares))

print("segundo valor")

print(next(resultadoPares))

print("tercer valor")

print(next(resultadoPares))


"""
Por cada llamada a `next()`, el generador **reanuda la ejecución desde la última pausa** (es decir, desde el último `yield`). Esto crea el "estado de suspensión" .

### **Un detalle importante sobre `StopIteration`**
Si llamas demasiadas veces a `next()` y el generador ya no tiene más valores que ofrecer (porque ha completado su función), Python lanza automáticamente la excepción `StopIteration`. Esto es completamente esperado cuando iteras manualmente.
 

"""
