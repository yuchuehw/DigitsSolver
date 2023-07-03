<p align="center">
    <picture>
      <img 
        src="new_logo.png" 
        alt="VueTube 图标"
        width="500"
       />
    </picture>
<p>

Digits Solver 是一个使用 Python 编写的程序，通过找到可应用于一组起始数字以获得目标数字的数学运算来解决一个数字拼图游戏。

[![Python 应用](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![PyLint 分数](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Python 徽章](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![欢迎贡献](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&color=pink)
[![许可证](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![代码风格：black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## 演示
您可以在此处观看算法的运行示例（在重定向后点击绿色运行按钮）：

[![Replit](https://img.shields.io/badge/演示-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

您还可以观看使用此算法的速通演示：

[![Replit](https://img.shields.io/badge/演示-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*注意：演示使用了 solveAuto 功能，继续阅读了解更多信息*
## 目录
- [用法](#用法)
- [示例](#示例)
- [替代用法](#替代用法)
- [贡献](#贡献)
- [许可证](#许可证)


## 用法

要运行 Digits Solver 程序，请执行以下命令：

```bash
git clone https://github.com/yuchue

hw/DigitsSolver
cd ./DigitSolver
python solver <起始数字> <目标数字> [-os] [-h]
```

- `<起始数字>`：用空格分隔的整数列表，表示起始数字。
- `<目标数字>`：需要获得的目标数字。
- `-os` 或 `--onesolution`（可选）：如果指定了此参数，程序将仅查找一个解决方案。否则，它将查找所有可能的解决方案。
- `-h` 或 `--help`（可选）：如果使用该参数，将显示帮助菜单。

## 示例

1. 查找数字拼图的所有解决方案：
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. 仅查找数字拼图的一个解决方案：
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```

## 输出

程序将输出找到的解决方案数，并以以下格式显示每个解决方案：

```
找到解决方案：
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

我们找到了 1 个解决方案
```

## 替代用法
Digits Solver 也可以作为 Python 模块导入并以编程方式使用。以下是一个示例：

```python
from solver.solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
solution_count = solver.solve(False)
print(f"我们找到了 {solution_count} 个解决方案")
```

## 其他文件

我还包含了一些其他的 Python 程序，它们与 solver 程序相辅相成。您可以在下面找到有关如何使用每个程序的详细说明：

- [如何使用 pretty_solve.py](reference/prettySolve.md)：提供了一个视觉增强版的 solver 程序。
- [如何使用 solve_auto.py](reference/solveAuto.md)：具有 Selenium 的全自动 Digits solver

请随意探索这些文件，并根据特定的用例或场景利用它们。

*apendix 文件夹包含了用于程序测试的 450 个问题，欢迎使用这些问题进行测试*

## 贡献

欢迎对 Digits Solver 程序进行贡献！如果您发现任何问题或有改进建议，请在 GitHub 存储库上打开一个 issue 或提交一个 pull request。

在进行贡献时，请确保遵循最佳实践、保持代码质量，并提供对您的更改的清晰描述。


## 许可证

Digits Solver 程序根据 [MIT 许可证](https://choosealicense.com/licenses/mit/) 授权。您可以自由使用、修改和分发此程序，无论是用于个人还是商业目的。详细信息请参阅 [LICENSE

](LICENSE.md) 文件。

## 致谢

特别感谢 [timeshift.js](https://github.com/plaa/TimeShift-js) 的作者对本项目的贡献。他们的部分代码已在 solver/util 模块的实现中得到利用。
```

Please replace the original content in your README.md file with the translated content above.
