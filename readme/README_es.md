<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Ícono de Digits Solver"
        width="500"
       />
    </picture>
<p>

[English](README_en.md)
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • Español
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)

Bienvenido a Digits Solver, el compañero definitivo en Python para conquistar el desafiante juego de rompecabezas [Digits](https://www.nytimes.com/games/digits), desarrollado por The New York Times. Sumérgete en un cautivador mundo de desafíos numéricos y domina el arte de la manipulación estratégica. Con Digits Solver, manipularás estratégicamente un conjunto de dígitos iniciales utilizando operaciones matemáticas para alcanzar el esquivo dígito objetivo. Su potente algoritmo y análisis meticuloso te permiten desentrañar rápidamente cada rompecabezas, ofreciendo soluciones paso a paso con una precisión inquebrantable. Mejora tus habilidades para resolver rompecabezas y descubre los secretos ocultos entre los dígitos. ¡Prepárate para un emocionante viaje para convertirte en un maestro de Digits!

[![Aplicación Python](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![Puntuación de PyLint](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Insignia de Python](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![se aceptan contribuciones](https://img.shields.io/badge/contribuciones-bienvenidas-brightgreen.svg?style=flat&color=pink)
[![Licencia](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![Estilo de código: black](https://img.shields.io/badge/estilo%20de%20código-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Demo
Observa el algoritmo en acción haciendo

 clic en el botón verde de ejecución después de ser redirigido:

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-morado.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

También puedes ver esta ejecución rápida que utiliza

el algoritmo Digits Solver:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-morado.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*Nota: La demostración muestra la función [solve_auto](solveAuto.md). Continúa leyendo para obtener más información.*

## Tabla de contenido

- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplos](#ejemplos)
- [Uso Alternativo](#uso-alternativo)
- [Módulos Utilitarios](#módulos-utilitarios)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Agradecimientos](#agradecimientos)

## Instalación

Puedes obtener una copia del programa Digits Solver utilizando uno de los siguientes métodos:

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/yuchuehw/DigitsSolver.git
   ```

2. **Descargar el Archivo Zip**:
   - Ve a la pestaña [Release](https://github.com/yuchuehw/DigitsSolver/releases) en el repositorio de GitHub.
   - Descarga el archivo zip de la última versión.
   - Extrae el contenido del archivo zip en la ubicación deseada.

Después de obtener el programa, puedes proceder a la sección de [Uso](#uso) para ejecutar el programa Digits Solver.

## Uso

Para ejecutar el programa Digits Solver, abre la terminal y navega hasta el directorio donde has descargado o clonado el repositorio DigitsSolver. Una vez que te encuentres en el directorio adecuado, ejecuta el siguiente comando en la terminal (reemplaza los valores entre corchetes por tu entrada; consulta la sección de [Ejemplos](#ejemplos) para obtener más detalles):

```bash
python solver <dígitos_iniciales> <dígito_objetivo> [-os] [-h]
```

- `<dígitos_iniciales>`: Una lista de enteros separados por espacios que representan los dígitos iniciales.
- `<dígito_objetivo>`: El dígito objetivo que se debe obtener.
- `-os` o `--onesolution` (opcional): Si se especifica, el programa encontrará solo una solución. De lo contrario, encontrará todas las soluciones posibles.
- `-h` o `--help` (opcional): Si se usa, se mostrará el menú de ayuda.

## Ejemplos

1. Encontrar todas las soluciones para el rompecabezas de dígitos:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Encontrar solo una solución para el rompecabezas de dígitos:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```


3. Observa que

 los `dígitos_iniciales` siempre van antes de los `dígitos_objetivo`. Este es un ejemplo de un rompecabezas con 8 `dígitos_iniciales`:
   ```bash
   python solver 2 3 5 7 11 13 17 19 323 -os
   ```

## Salida

El programa mostrará el número de soluciones encontradas y mostrará cada solución en el siguiente formato:

```
Solución encontrada:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

Encontramos 1 solución(es)
```

## Uso Alternativo

El Digits Solver también se puede importar como un módulo de Python y utilizar programáticamente. Eres libre de agregar más funcionalidades de las que hemos proporcionado. Aquí tienes un ejemplo mínimo de cómo utilizarlo como una importación:

```python
from solver.solver import DigitSolver

solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
# False en el paréntesis es opcional. False resuelve todas las soluciones. True resuelve una solución.
# usa solve.printer = alguna_función para reemplazar el comportamiento de salida predeterminado.
cantidad_soluciones = solver.solve(False)
print(f"Encontramos {cantidad_soluciones} solución(es)")
```

## Módulos Utilitarios

También hemos incluido algunos programas adicionales en Python que complementan el programa del solucionador. Se encuentran dentro de la carpeta `solver/util`. Puedes leer más sobre cómo utilizarlos aquí:

- [Cómo utilizar pretty_solve.py](prettySolve.md): Proporciona una versión visualmente mejorada del programa del solucionador.
- [Cómo utilizar solve_auto.py](solveAuto.md): Solucionador automático completo de Digits con Selenium

Siéntete libre de explorar estos archivos y utilizarlos para casos de uso o escenarios específicos.

*La carpeta de Apéndice incluye 450 problemas utilizados en los juegos de NYT. Siéntete libre de usar esos problemas para las pruebas del programa.*

## Contribuciones

¡Las contribuciones al programa Digits Solver son bienvenidas! Si encuentras algún problema o tienes sugerencias para mejoras, por favor, abre un issue o envía una pull request en el repositorio de GitHub.

Cuando contribuyas, asegúrate de seguir las mejores prácticas, mantener la calidad del código y proporcionar descripciones claras de tus cambios.

## Licencia

El programa Digits Solver tiene licencia bajo la [Licencia MIT](https://choosealicense.com/licenses/mit/). Eres libre de usar, modificar y distribuir este programa para fines personales o comerciales. Consulta el archivo [LICENSE](LICENSE.md) para obtener más detalles.

## Agradecimientos

Agradecimientos especiales al autor de [timeshift.js](https://github.com/plaa/TimeShift-js) por su contribución a este proyecto. Se han utilizado partes de su código en la implementación del módulo `solver.util`.
