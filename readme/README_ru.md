<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Значок Digits Solver"
        width="500"
       />
    </picture>
<p>

[English](README.md)
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • Русский

Добро пожаловать в Digits Solver, незаменимую программу на языке Python, разработанную для покорения игры Digits, созданной The New York Times. Погрузитесь в увлекательный мир числовых задач и стратегически манипулируйте набором начальных цифр с использованием математических операций, чтобы достичь желаемой целевой цифры. Благодаря своему мощному алгоритму и тщательному анализу, Digits Solver позволяет быстро раскрыть каждую головоломку, предоставляя пошаговые решения с непоколебимой точностью. Поднимите свои навыки решения головоломок и раскройте тайны, скрытые в цифрах. Ощутите истинного спутника для овладения игрой Digits.

[![Приложение на Python](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![Рейтинг PyLint](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Значок Python](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![Приветствуются вклады](https://img.shields.io/badge/Вклады-приветствуются-brightgreen.svg?style=flat&color=pink)
[![Лицензия](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![Стиль кода: black](https://img.shields.io/badge/Стиль%20кода-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Демонстрация
Вы можете увидеть алгоритм в действии здесь (нажмите на зеленую кнопку "run" после перенаправления):

[![Replit](https://img.shields.io/badge/ДЕМО-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

Также вы можете посмотреть это быстрое решение, которое использует этот алгоритм:

[![Replit](https://img.shields.io/badge/ДЕМО-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*Примечание: Демонстрация использует функции solveAuto. Читайте дальше для получения дополнительной информации.*
## Содержание
- [

Использование](#использование)
- [Примеры](#примеры)
- [Альтернативное использование](#альтернативное-использование)
- [Внесение вклада](#внесение-вклада)
- [Лицензия](#лицензия)


## Использование

Для запуска программы Digits Solver выполните следующую команду:

```bash
git clone https://github.com/yuchuehw/DigitsSolver
cd ./DigitSolver
python solver <startende_zahlen> <ziel_zahl> [-os] [-h]
```

- `<startende_zahlen>`: Пробелом разделенный список целых чисел, представляющих начальные цифры.
- `<ziel_zahl>`: Целевая цифра, которую необходимо получить.
- `-os` или `--onesolution` (опционально): Если указано, программа найдет только одно решение. В противном случае, будут найдены все возможные решения.
- `-h` или `--help` (опционально): Если использовать, будет показано меню справки.

## Примеры

1. Найти все решения для головоломки с цифрами:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Найти только одно решение для головоломки с цифрами:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```

## Вывод

Программа выведет количество найденных решений и отобразит каждое решение в следующем формате:

```
Найдено решение:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

Мы нашли 1 решение(й)
```

## Альтернативное использование
Digits Solver также может быть импортирован как модуль Python и использован программно. Вот пример:

```python
from solver.solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
количество_решений = solver.solve(False)
print(f"Мы нашли {количество_решений} решение(й)")
```

## Другие файлы

Я также добавил несколько дополнительных программ на языке Python, которые дополняют программу solver. Вы можете найти подробные инструкции по использованию каждой из этих программ ниже:

- [Как использовать pretty_solve.py](reference/prettySolve.md): Предоставляет визуально улучшенную версию программы solver.
- [Как использовать solve_auto.py](reference/solveAuto.md): Полностью автоматический Digits Solver с использованием Selenium.

Не стесняйтесь изучать эти файлы и использовать их для конкретных случаев или сценари

ев использования.

*Приложена папка "appendix" со 450 задачами, использованными в NYT Games. Вы можете использовать эти задачи для тестирования программы.*

## Внесение вклада

Приветствуются вклады в программу Digits Solver! Если вы нашли какие-либо проблемы или у вас есть предложения по улучшению, пожалуйста, создайте проблему (issue) или отправьте запрос на внесение изменений (pull request) в репозитории на GitHub.

При внесении изменений, пожалуйста, убедитесь, что вы следуете bew лучшим практикам, поддерживаете качество кода и предоставляете четкие описания ваших изменений.

## Лицензия

Программа Digits Solver лицензирована под [MIT License](https://choosealicense.com/licenses/mit/). Вы можете свободно использовать, изменять и распространять эту программу в личных или коммерческих целях. Пожалуйста, ознакомьтесь с файлом [LICENSE](LICENSE.md) для получения дополнительной информации.

## Благодарности

Особая благодарность автору [timeshift.js](https://github.com/plaa/TimeShift-js) за их вклад в этот проект. Часть их кода была использована в реализации модуля solver.util.
