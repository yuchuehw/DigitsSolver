# Automatización del Solucionador de Digits

Este script automatiza la resolución de puzzles en el juego Digits en el sitio web de New York Times utilizando Selenium y un solucionador personalizado.

## Prerrequisitos

Antes de ejecutar el script, asegúrate de tener instalado lo siguiente:

- Python 3.x
- Biblioteca Selenium
- Controlador de Chrome
- Carpeta del solucionador

## Empezando

1. Clona el repositorio o descarga el script.
2. Instala las dependencias requeridas usando pip:

   ```shell
   pip install selenium
   ```

3. Descarga el ejecutable del controlador de Chrome WebDriver y agrega su ubicación a la variable de entorno PATH de tu sistema.

¡Claro! Aquí está la documentación para la interfaz de línea de comandos:


## Uso

```plaintext
solver/util/solve_auto [-h] [[-start S] [-level L] | [-daily]]
```

### Argumentos opcionales

- `-h, --help`: Muestra el mensaje de ayuda y sale.

- `-start S, --startLevel S`: Especifica el nivel de inicio para comenzar a resolver los puzzles. El valor debe ser un número entero.

- `-level L, --levelToPlay L`: Especifica el número total de niveles a jugar. El valor debe ser un número entero.

- `-daily, --dailyOnly`: Resuelve solo los puzzles diarios. Si se proporciona esta opción, la herramienta ignorará las opciones `--startLevel` y `--levelToPlay` y resolverá solo el puzzle diario.

## Ejemplos

1. Resolver 10 niveles comenzando desde el nivel 5:
   ```plaintext
   python solver/util/solve_auto --startLevel 5 --levelToPlay 10
   ```

2. Resolver solo puzzles diarios:
   ```plaintext
   python solver/util/solve_auto --dailyOnly
   ```

Nota: Si no se proporcionan argumentos, la herramienta utilizará la configuración predeterminada (comenzar desde el nivel 1 hasta el nivel 20).


## Funcionalidad

El script automatiza las siguientes acciones:

1. Navegar al juego Digits en el sitio web de New York Times.

2. Manipular el tiempo del juego usando el script `TimeShift.js`. (solo solveMany.py)

3. Hacer clic en el botón "Jugar" para comenzar un puzzle.

4. Resolver cada puzzle realizando los clics necesarios en los botones de números y operadores.

5. Manejar casos en los que el script se bloquea, como cuando los botones o elementos no son clicables.

6. Avanzar al siguiente puzzle o regresar a la pantalla de selección de puzzles cuando se completa un conjunto de puzzles.

7. Imprimir el número y la fecha del puzzle actual como referencia. (solo solveMany.py)

## Personalización

Si deseas modificar o ampliar la funcionalidad del script, puedes explorar las siguientes funciones:

- `click_element(element_id, error_message)`: Maneja el clic en un elemento identificado por su ID. Si el elemento no es clicable, solicita la entrada del usuario.

- `combine_numbers(step_list, buttons)`: Maneja la combinación de números realizando los clics necesarios en los botones de números y actualizando el estado de los botones.

- `next_puzzle_button_click()`: Maneja el clic en el botón "Siguiente Puzzle" para pasar al siguiente puzzle.

- `back_to_p

uzzles_button_click()`: Maneja el clic en el botón "Volver a los Puzzles" cuando se completa un conjunto de puzzles.

Siéntete libre de modificar el código según tus requisitos específicos.

## Licencia

Este script se proporciona bajo la [Licencia MIT](LICENSE.md).

Ten en cuenta que la documentación asume que ya has configurado el entorno necesario y las dependencias mencionadas en la sección "Prerrequisitos".
