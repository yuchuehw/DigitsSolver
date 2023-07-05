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
 • [繁體中文](README_zh-TW.md)
 • 简体中文
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)

欢迎使用 Digits Solver，这是一款最终版的 Python 伴侣，可助你征服由《纽约时报》开发的令人着迷的[Digits](https://www.nytimes.com/games/digits)数字益智游戏。沉浸在引人入胜的数字挑战世界中，精通策略操控的艺术。使用 Digits Solver，你将透过数学运算巧妙操纵一组起始数字，以达到追逐已远的目标数字。其强大的演算法和细致的分析能力让你能够迅速解开每个谜题，提供逐步解决方案，确保绝对精确度。提升你的解谜能力，揭开数字背后隐藏的秘密。准备好展开一段令人兴奋的旅程，成为Digits大师吧！

[![Python應用程式](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![PyLint分數](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![python徽章](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![歡迎貢獻](https://img.shields.io/badge/歡迎-貢獻-brightgreen.svg?style=flat&color=pink)
[![許可證](https://img.shields.io/badge/許可證-MIT-yellow.svg)](LICENSE.md)
[![程式碼風格：black](https://img.shields.io/badge/程式碼風格-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## 示范
点击绿色运行按钮查看演算法的实际运作：

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

你也可以观看这个使用 Digits Solver 演算法的速解过程：

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*备注：此示范展示了 [solve_auto](solveAuto_zh-CN.md) 功能。继续阅读以获取更多信息。 *

## 目录

- [安装](#安装)
- [用法](#用法)
- [范例](#范例)
- [替代用法](#替代用法)
- [Util 模组](#Util-模组)
- [贡献](#贡献)
- [许可证](#许可证)
- [鸣谢](#鸣谢)

## 安装

你可以使用以下方法之一来获取 Digits Solver 程式的副本：

1. **复制存储库**:
   ```bash
   git clone https://github.com/yuchuehw/DigitsSolver.git
   ```

2. **下载 Zip 档案**:
   - 前往 GitHub 存储库的 [Release](https://github.com/yuchuehw/DigitsSolver/releases) 标签。
   - 下载最新版本的 zip 档案。
   - 将 zip 档案的内容解压缩到你想要的位置。

获取程式之后，你可以继续阅读 [用法](#usage) 部分来运行 Digits Solver 程式。

## 用法

要运行 Digits Solver 程式，打开终端并导航到你下载或复制 DigitsSolver 存储库的目录。一旦你在适当的目录中，请在终端中执行以下命令（使用尖括号中的值替换；请参阅[范例](#example) 部分以获取更多详细信息）：

```bash
python solver <starting_digits> <target_digit> [-os] [-h]
```

- `<starting_digits>`：一个用空格分隔的整数列表，表示起始数字。


- `<target_digit>`：需要达到的目标数字。
- `-os` 或 `--onesolution`（可选）：如果指定，程序将只找到一个解。否则，它将找到所有可能的解。
- `-h` 或 `--help`（可选）：如果使用，将显示帮助菜单。

## 范例

1. 寻找数字谜题的所有解：
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. 寻找数字谜题的一个解：
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```


3. 注意，起始数字必须位于目标数字之前。这是一个包含 8 个起始数字的谜题示例：
   ```bash
   python solver 2 3 5 7 11 13 17 19 323 -os
   ```

## 输出

程序将输出找到的解的数量并以以下格式显示每个解：

```
找到解：
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

我们找到了 1 个解
```

## 替代用法

Digits Solver 也可以作为 Python 模组进行导入并以程式方式使用。你可以自由地添加比我们提供的功能更多的功能。这是一个使用导入的最小示例：

```python
from solver.solver import DigitSolver

solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
# 括号中的 False 是可选的。 False 解决所有解，True 解决一个解。
# 使用 solve.printer = some_function 覆盖默认的输出行为。
solution_count = solver.solve(False)
print(f"我们找到了 {solution_count} 个解")
```

## Util 模组

我们还包含了几个额外的 Python 程式，它们与 solver 程式互补。它们位于 solver/util 文件夹中。你可以在这里阅读有关如何使用它们的更多信息：

- [如何使用 pretty_solve.py](prettySolve.md)：提供了一个视觉增强版的 solver 程式。
- [如何使用 solve_auto.py](solveAuto_zh-CN.md)：使用 Selenium 的完全自动化 Digits solver

随意探索这些文件并根据特定的用例或场景使用它们。

*附录文件夹中包含了 NYT Games 使用的 450 个问题。欢迎使用这些问题进行程式测

试。 *

## 贡献

如果你对 Digits Solver 感兴趣，我们欢迎各种形式的贡献！你可以通过以下方式帮助我们：

- 回报问题：如果你在使用过程中遇到任何问题，请在 [GitHub 存储库的 Issues](https://github.com/yuchuehw/DigitsSolver/issues) 页面中报告问题。
- 提供改进建议：如果你有任何改进或建议，请通过 GitHub Issues 分享你的想法。
- 修复错误：如果你发现错误并且可以解决它，请通过 Pull Request 向我们提交修复错误的代码。
- 添加功能：如果你想要添加新功能，请通过 Pull Request 向我们提交你的想法和代码。

感谢你的贡献！我们非常期待与你合作。

## 许可证

Digits Solver 使用 MIT 许可证。有关详细信息，请参阅 [LICENSE](LICENSE.md) 文件。

## 鸣谢

特别感谢 [timeshift.js](https://github.com/plaa/TimeShift-js) 的作者对此项目的贡献。他们的部分代码已在 solver.util 模组的实现中使用。
