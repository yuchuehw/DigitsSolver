<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Digits Solver icon"
        width="500"
       />
    </picture>
<p>

English
 • 繁體中文
 • [简体中文](https://github.com/yuchuehw/DigitsSolver/readme/README_zh-CN.md)
 • [日本語](https://github.com/yuchuehw/DigitsSolver/readme/README_ja.md)
 • [Español](https://github.com/yuchuehw/DigitsSolver/readme/README_es.md)
 • [Français](https://github.com/yuchuehw/DigitsSolver/readme/README_fr.md)
 • [Italiano](https://github.com/yuchuehw/DigitsSolver/readme/README_it.md)
 • [Deutsche](https://github.com/yuchuehw/DigitsSolver/readme/README_de.md)
 • [Русский](https://github.com/yuchuehw/DigitsSolver/readme/README_ru.md)

Digits Solver 是一個使用 Python 開發的程式，它通過尋找可以應用於一組起始數字以獲得目標數字的數學運算來解決數字拼圖遊戲。

[![Python application](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![PyLint 分數](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![python 徽章](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![歡迎貢獻](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&color=pink)
[![許可證](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![代碼風格：black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Demo
你可以在這裡查看算法運行的示例（在重定向後點擊綠色運行按鈕）：

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

你也可以觀看使用此算法的速通影片：

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*注意：演示使用了 solveAuto 功能，繼續閱讀以獲取更多信息*

## 目錄
- [用法](#用法)
- [示例](#示例)
- [替代用法](#替代用法)
- [貢獻](#貢獻)


- [許可證](#許可證)


## 用法

要運行 Digits Solver 程式，請執行以下命令：

```bash
git clone https://github.com/yuchuehw/DigitsSolver
cd ./DigitSolver
python solver <起始數字> <目標數字> [-os] [-h]
```

- `<起始數字>`：用空格分隔的整數列表，表示起始數字。
- `<目標數字>`：需要獲得的目標數字。
- `-os` 或 `--onesolution`（可選）：如果指定，程序將只找到一個解。否則，它將找到所有可能的解。
- `-h` 或 `--help`（可選）：如果使用，將顯示幫助菜單。

## 示例

1. 查找數字拼圖的所有解：
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. 只找到數字拼圖的一個解：
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```

## 輸出

程序將輸出找到的解的數量並以以下格式顯示每個解：

```
找到解：
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

我們找到了 1 個解
```

## 替代用法
Digits Solver 也可以作為 Python 模塊被導入並以編程方式使用。以下是一個示例：

```python
from solver.solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
solution_count = solver.solve(False)
print(f"我們找到了 {solution_count} 個解")
```
## 其他文件

我還包含了一些補充的 Python 程式，它們與 solver 程式相輔相成。你可以在下面找到如何使用每個程式的詳細說明：

- [如何使用 pretty_solve.py](reference/prettySolve.md)：提供了一個視覺增強版的 solver 程式。
- [如何使用 solve_auto.py](reference/solveAuto.md)：使用 Selenium 的全自動 Digits solver

隨意探索這些文件，並根據特定的使用案例或情境使用它們。

*附錄文件夾中包含 450 個用於 NYT 遊戲的問題。歡迎使用這些問題進行程序測試*

## 貢獻

歡迎對 Digits Solver 程式進行貢獻！如果您發現任何問題或有改進建議，請在 GitHub

 存儲庫上打開一個 issue 或提交一個 pull request。

在進行貢獻時，請確保您遵循最佳實踐，保持代碼質量，並提供對您的更改的清晰描述。


## 許可證

Digits Solver 程式根據 [MIT 許可證](https://choosealicense.com/licenses/mit/) 授權。您可以自由使用、修改和分發此程式，無論是用於個人還是商業目的。詳細信息請參閱 [LICENSE](LICENSE.md) 文件。

## 致謝

特別感謝 [timeshift.js](https://github.com/plaa/TimeShift-js) 的作者對此項目的貢獻。他們的部分代碼已在 solver.util 模組的實現中使用。
