<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Значок Digits Solver"
        width="500"
       />
    </picture>
<p>

[English](README_en.md)
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • Русский

Добро пожаловать в Digits Solver - идеального помощника по Python для победы в умопомрачительной игре [Digits](https://www.nytimes.com/games/digits), разработанной The New York Times. Окунитесь в увлекательный мир числовых задач и освойте искусство стратегической манипуляции. С помощью Digits Solver вы будете стратегически изменять набор начальных цифр с использованием математических операций, чтобы достичь неуловимой целевой цифры. Его мощный алгоритм и тщательный анализ позволяют быстро раскрыть каждую головоломку, предоставляя пошаговые решения с неизменной точностью. Поднимите свою мастерство в решении головоломок и раскройте тайны, скрытые в цифрах. Приготовьтесь к захватывающему путешествию, чтобы стать мастером Digits!

[![Python application](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![PyLint Score](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![python badge](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&color=pink)
[![License](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Демонстрация
Посмотрите алгоритм в действии, нажав зеленую кнопку запуска после перенаправления:

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

Вы также можете посмотреть это быстрое решение, использующее

 алгоритм Digits Solver:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*Примечание: Демонстрация демонстрирует функцию [solve_auto](solveAuto.md). Продолжайте чтение для получения дополнительной информации.*

## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Примеры](#примеры)
- [Альтернативное использование](#альтернативное-использование)
- [Утилитарные модули](#утилитарные-модули)
- [Содействие](#содействие)
- [Лицензия](#лицензия)
- [Благодарности](#благодарности)

## Установка

Вы можете получить копию программы Digits Solver, используя один из следующих методов:

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/yuchuehw/DigitsSolver.git
   ```

2. **Загрузка zip-файла**:
   - Перейдите на вкладку [Release](https://github.com/yuchuehw/DigitsSolver/releases) в репозитории GitHub.
   - Загрузите последний выпуск zip-файла.
   - Извлеките содержимое zip-файла в нужное место.

После получения программы вы можете перейти к разделу [Использование](#использование), чтобы запустить программу Digits Solver.

## Использование

Чтобы запустить программу Digits Solver, откройте терминал и перейдите в каталог, где вы загрузили или склонировали репозиторий DigitsSolver. После того, как вы окажетесь в соответствующем каталоге, выполните следующую команду в терминале (замените значения в угловых скобках на ваши входные данные; см. раздел [Примеры](#примеры) для получения дополнительной информации):

```bash


python solver <starting_digits> <target_digit> [-os] [-h]
```

- `<starting_digits>`: Список целых чисел, разделенных пробелами, представляющих исходные цифры.
- `<target_digit>`: Целевая цифра, которую необходимо получить.
- `-os` или `--onesolution` (необязательно): Если указано, программа найдет только одно решение. В противном случае она найдет все возможные решения.
- `-h` или `--help` (необязательно): Если используется, будет отображено меню справки.

## Примеры

1. Найти все решения для головоломки с цифрами:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Найти только одно решение для головоломки с цифрами:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```


3. Обратите внимание, что исходные цифры всегда идут перед целевыми цифрами. Вот пример головоломки с 8 исходными цифрами:
   ```bash
   python solver 2 3 5 7 11 13 17 19 323 -os
   ```

## Вывод

Программа выведет количество найденных решений и отобразит каждое решение в следующем формате:

```
Решение найдено:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

Мы нашли 1 решение(й)
```

## Альтернативное использование

Digits Solver также можно импортировать как модуль Python и использовать программно. Вы можете добавить больше функциональности, чем мы предоставили. Вот минимальный пример того, как его использовать как импорт:

```python
from solver.solver import DigitSolver

solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
# False в круглых скобках необязателен. False решает все решение. True решает одно решение.
# используйте solve.printer = some_function, чтобы переопределить поведение вывода по умолчанию.
solution_count = solver.solve(False)
print(f"Мы нашли {solution_count} решение(й)")
```

## Утилитарные модули

Мы также включили несколько дополнительных программ на языке Python, которые дополняют программу решения. Они находятся внутри папки solver/util. Вы можете узнать больше о том, как их использовать здесь:

- [Как использовать pretty_solve.py](prettySolve.md): Предоставляет визуально улучшенную версию программы решения.
- [Как использовать filter.py](filter.md): Позволяет отфильтровать решения на основе определенных условий.

## Содействие

Если вы обнаружили ошибку или хотите предложить новую функцию, пожалуйста, создайте [новый Issue](https://github.com/yuchuehw/DigitsSolver/issues) в репозитории GitHub. Мы будем рады принять ваши отзывы и предложения.

Если вы хотите внести свой вклад в разработку Digits Solver, пожалуйста, прочтите наш [руководство по вкладу](CONTRIBUTING.md).

## Лицензия

Этот проект лицензируется под лицензией MIT. Подробную информацию смотрите в файле [LICENSE](LICENSE.md).

## Благодарности

Digits Solver был разработан yuchueh. Мы также благодарим всех участников, которые внесли свой вклад в проект. Вы можете найти имена всех участников в разделе [Участники](https://github.com/yuchuehw/DigitsSolver/graphs/contributors) репозитория GitHub.
