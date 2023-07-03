<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Icono de Digits Solver"
        width="500"
       />
    </picture>
<p>

[English](README.md)
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • Español
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)


Bienvenido a Digits Solver, un programa Python indispensable diseñado para conquistar el juego de Digits desarrollado por The New York Times. Sumérgete en el cautivador mundo de los desafíos numéricos mientras manipulas estratégicamente un conjunto de dígitos iniciales utilizando operaciones matemáticas para alcanzar el esquivo dígito objetivo. Con su poderoso algoritmo y análisis meticuloso, Digits Solver te permite desentrañar rápidamente cada rompecabezas, ofreciendo soluciones paso a paso con una precisión inquebrantable. Eleva tus habilidades para resolver acertijos y desbloquea los secretos ocultos entre los dígitos. Experimenta el compañero definitivo para dominar el juego Digits.

[![Aplicación de Python](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![Puntuación PyLint](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Insignia de Python](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![Contribuciones bienvenidas](https://img.shields.io/badge/contribuciones-welcome-brightgreen.svg?style=flat&color=pink)
[![Licencia](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![Estilo de código: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Demo
Puedes ver el algoritmo en acción aquí (haz clic en el botón de ejecución verde después de redirigido):

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

También puedes ver esta ejecución rápida que utiliza este algoritmo:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*nota: la demo utiliza las características de solveAuto, sigue leyendo para obtener más información*
## Tabla de contenidos
- [Uso](#uso)
- [Ejemplos](#ejemplos)
- [Uso alternativo](#uso-alternativo)
- [Contribuir](#contribuir)
- [Licencia](#licencia)


## Uso

Para ejecutar el programa Digits Solver, ejecuta el siguiente comando:

```bash
git clone https://github.com/yuchuehw/DigitsSolver
cd ./DigitSolver
python solver <starting_digits> <target_digit>

 [-os] [-h]
```

- `<starting_digits>`: Una lista de enteros separados por espacios que representan los dígitos iniciales.
- `<target_digit>`: El dígito objetivo que se debe obtener.
- `-os` o `--onesolution` (opcional): Si se especifica, el programa encontrará solo una solución. De lo contrario, encontrará todas las soluciones posibles.
- -`h` o `--help` (opcional): Si se usa, se mostrará el menú de ayuda.

## Ejemplos

1. Encontrar todas las soluciones para el puzzle de dígitos:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Encontrar solo una solución para el puzzle de dígitos:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```

## Salida

El programa mostrará la cantidad de soluciones encontradas y mostrará cada solución en el siguiente formato:

```
solución encontrada:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

encontramos 1 solución(es)
```

## Uso alternativo
Digits Solver también se puede importar como un módulo de Python y utilizarse de forma programática. Aquí tienes un ejemplo:
```python
from solver.solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
cantidad_soluciones = solver.solve(False)
print(f"encontramos {cantidad_soluciones} solución(es)")
```
## Otros archivos

También he incluido algunos programas Python adicionales que complementan el programa solver. Puedes encontrar instrucciones detalladas sobre cómo usar cada uno de estos programas a continuación:

- [Cómo usar pretty_solve.py](reference/prettySolve.md): Proporciona una versión visualmente mejorada del programa solver.
- [Cómo usar solve_auto.py](reference/solveAuto.md): Resolutor de Digits completamente automático con Selenium.

No dudes en explorar estos archivos y utilizarlos para casos de uso o escenarios específicos.

*La carpeta de anexos incluye 450 problemas utilizados en los juegos del NYT. Siéntete libre de utilizar estos problemas para probar el programa*

## Contribuir

¡Se aceptan contribuciones al programa Digits Solver! Si encuentras algún problema o tienes sugerencias de mejora, por favor abre un problema o envía una solicitud de extracción en el repositorio de GitHub.

Al contribuir, por favor asegúrate de seguir las mejores prácticas, mantener la calidad del código y proporcionar descripciones claras de tus cambios.

## Licencia

El programa Digits Solver está bajo la licencia [MIT](https://choosealicense.com/licenses/mit/). Eres libre de usar, modificar y distribuir este programa para fines personales o comerciales. Por favor consulta el archivo [LICENSE](LICENSE.md) para más detalles.

## Reconocimientos

Agradecimientos especiales al autor de [timeshift.js](https://github.com/plaa/TimeShift-js) por su contribución a este proyecto. Se han utilizado porciones de su código en la implementación del módulo solver.util.
