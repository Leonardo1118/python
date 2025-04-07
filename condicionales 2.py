"""
 La palabra clave **`elif`** en Python se utiliza como una abreviación de **"else if"** y forma parte de las estructuras condicionales. Su función principal es permitir verificar **condiciones adicionales** cuando una condición anterior en un bloque `if` no se cumple.
### **Papel principal de `elif`:**
1. **Probar múltiples condiciones**:
    - Un `if` maneja la primera condición.
    - Si esta no se cumple, los bloques `elif` permiten evaluar otras condiciones en un orden específico.

2. **Evitar múltiples bloques `if` independientes**:
    - Se ejecuta **sólo el primer bloque de código cuya condición sea verdadera**, incluso si hay más condiciones después que también se cumplan.

### **Cómo funciona junto con `if` y `else`:**
- Comienza evaluando el `if`
- Si la condición del `if` es falsa**, evalúa el primer **`elif`
- Si el primer `elif` también es falso**, pasa al siguiente `elif` (si existe), y así sucesivamente.
- Finalmente, si **ninguna de las condiciones anteriores se cumple**, ejecuta el bloque **`else`** (si está presente).


"""

print("verificacion de etapa de vida ")

edad = int(input("ingrese su edad: "))

if 60 <= edad <= 100:
    print("adulto mayor de edad")
elif 18 <=edad <60:
    print("adulto")
elif 1<= edad <= 18 :
    print("menor de edad")
else : print("edad invalida")