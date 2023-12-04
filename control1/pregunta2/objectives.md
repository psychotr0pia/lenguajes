| Objective | Status |
|-----------|--------|
| **1. Modificar la gramática para incluir orientación** | DONE |
|   1.1 Puntero con atributo orientacion | DONE |
|   1.2 Modificar gramática, agregar ROTAR | DONE |
|   1.3 Modificar parser, agregar ROTAR NUMBER | DONE |
|   1.4 Implementar lógica en main | DONE |
| **2. Permitir que el Puntero avance en la dirección de su orientación** | TODO |
|   2.1 Modificar parser, agregar MOVER NUMBER | DONE |
|   2.2 Implementar logica en main    
| **3. Habilitar desplazamiento sin especificar punto de destino** | DONE |
| **4. Permitir que el Puntero avance en sentido contrario con valor negativo** | DONE |
| **5. Posibilitar rotación del Puntero hacia un punto específico** | DONE |
| **6. Construir Árbol de Sintaxis Abstracta (AST)** | DONE |
| **7. Mostrar AST al final de cada programa** | DONE, falta que sea "bonito" |

---

#### Example Usage:
- rotar(90) //el puntero rota 90 grados. DONE
- mover(20) //el puntero se mueve 20 puntos en la orientación actual. DONE
- mover(150, 200) //cambia orientación en dirección al punto y luego lo
  //desplaza hasta el punto indicado. DONE
- rotar(100,80) //el puntero debe cambiar su orientación, en dirección
  //al punto 100,80 DONE

