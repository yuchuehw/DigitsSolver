<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Digits Solver icon"
        width="500"
       />
    </picture>
<p>

[English](README_en.md)
 • 繁體中文
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)

歡迎使用 Digits Solver，這是一款最終版的 Python 伴侶，可助你征服由《紐約時報》開發的令人著迷的[Digits](https://www.nytimes.com/games/digits)數字益智遊戲。沉浸在引人入勝的數字挑戰世界中，精通策略操控的藝術。使用 Digits Solver，你將透過數學運算巧妙操縱一組起始數字，以達到追逐已遠的目標數字。其強大的演算法和細緻的分析能力讓你能夠迅速解開每個謎題，提供逐步解決方案，確保絕對精確度。提升你的解謎能力，揭開數字背後隱藏的秘密。準備好展開一段令人興奮的旅程，成為Digits大師吧！

[![Python應用程式](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![PyLint分數](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![python徽章](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![歡迎貢獻](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&color=pink)
[![許可證](https://img.shields.io/github/license/y

uchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![程式碼風格：black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## 示範
點擊綠色運行按鈕查看演算法的實際運作：

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

你也可以觀看這個使用 Digits Solver 演算法的速解過程：

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*備註：此示範展示了 [solve_auto](solveAuto.md) 功能。繼續閱讀以獲取更多信息。*

## 目錄

- [安裝](#安裝)
- [用法](#用法)
- [範例](#範例)
- [替代用法](#替代用法)
- [Util 模組](#Util-模組)
- [貢獻](#貢獻)
- [許可證](#許可證)
- [鳴謝](#鳴謝)

## 安裝

你可以使用以下方法之一來獲取 Digits Solver 程式的副本：

1. **複製存儲庫**:
   ```bash
   git clone https://github.com/yuchuehw/DigitsSolver.git
   ```

2. **下載 Zip 檔案**:
   - 前往 GitHub 存儲庫的 [Release](https://github.com/yuchuehw/DigitsSolver/releases) 標籤。
   - 下載最新版本的 zip 檔案。
   - 將 zip 檔案的內容解壓縮到你想要的位置。

獲取程式之後，你可以繼續閱讀 [用法](#usage) 部分來運行 Digits Solver 程式。

## 用法

要運行 Digits Solver 程式，打開終端並導航到你下載或複製 DigitsSolver 存儲庫的目錄。一旦你在適當的目錄中，請在終端中執行以下命令（使用尖括號中的值替換；請參閱[範例](#example) 部分以獲取更多詳細信息）：

```bash
python solver <starting_digits> <target_digit> [-os] [-h]
```

- `<starting_digits>`：一個用空格分隔的整數列表，表示起始數字。


- `<target_digit>`：需要達到的目標數字。
- `-os` 或 `--onesolution`（可選）：如果指定，程序將只找到一個解。否則，它將找到所有可能的解。
- `-h` 或 `--help`（可選）：如果使用，將顯示幫助菜單。

## 範例

1. 尋找數字謎題的所有解：
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. 尋找數字謎題的一個解：
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```


3. 注意，起始數字必須位於目標數字之前。這是一個包含 8 個起始數字的謎題示例：
   ```bash
   python solver 2 3 5 7 11 13 17 19 323 -os
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

Digits Solver 也可以作為 Python 模組進行導入並以程式方式使用。你可以自由地添加比我們提供的功能更多的功能。這是一個使用導入的最小示例：

```python
from solver.solver import DigitSolver

solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
# 括號中的 False 是可選的。False 解決所有解，True 解決一個解。
# 使用 solve.printer = some_function 覆蓋默認的輸出行為。
solution_count = solver.solve(False)
print(f"我們找到了 {solution_count} 個解")
```

## Util 模組

我們還包含了幾個額外的 Python 程式，它們與 solver 程式互補。它們位於 solver/util 文件夾中。你可以在這裡閱讀有關如何使用它們的更多信息：

- [如何使用 pretty_solve.py](prettySolve.md)：提供了一個視覺增強版的 solver 程式。
- [如何使用 solve_auto.py](solveAuto.md)：使用 Selenium 的完全自動化 Digits solver

隨意探索這些文件並根據特定的用例或場景使用它們。

*附錄文件夾中包含了 NYT Games 使用的 450 個問題。歡迎使用這些問題進行程式測

試。*

## 貢獻

如果你對 Digits Solver 感興趣，我們歡迎各種形式的貢獻！你可以通過以下方式幫助我們：

- 回報問題：如果你在使用過程中遇到任何問題，請在 [GitHub 存儲庫的 Issues](https://github.com/yuchuehw/DigitsSolver/issues) 頁面中報告問題。
- 提供改進建議：如果你有任何改進或建議，請通過 GitHub Issues 分享你的想法。
- 修復錯誤：如果你發現錯誤並且可以解決它，請通過 Pull Request 向我們提交修復錯誤的代碼。
- 添加功能：如果你想要添加新功能，請通過 Pull Request 向我們提交你的想法和代碼。

感謝你的貢獻！我們非常期待與你合作。

## 許可證

Digits Solver 使用 MIT 許可證。有關詳細信息，請參閱 [LICENSE](LICENSE.md) 文件。

## 鳴謝

特別感謝 [timeshift.js](https://github.com/plaa/TimeShift-js) 的作者對此項目的貢獻。他們的部分代碼已在 solver.util 模組的實現中使用。
