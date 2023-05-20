# Parcial-Final-POO
## Nombre: Daniel Enrique Martinez Medina

![img.png](img.png)

En este UML se han añadido los siguientes patrones de diseño:

- Patrón Observer: para que el sistema de información pueda estar al tanto de los cambios en los turnos y se actualice automáticamente cuando haya cambios en ellos.
- Patrón de Fábrica Abstracta: para facilitar la creación de objetos de tipo Conductor y Asistente sin depender de una implementación específica.
- Patrón Estrategia: para cambiar fácilmente entre diferentes algoritmos para calcular las rutas de recolección sin cambiar el código en la clase Ruta.

La implementacion en python contiene un menú iterativo con dos opciones: calcular la cantidad de un objeto en un día específico y salir del menú.

Los test estan dentro de test/test.py
Para ejecutarlos se puede poner en la consola: pytest test/test.py