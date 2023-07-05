# 数字求解自动化

此脚本使用 Selenium 和自定义求解器自动解决纽约时报网站上的「Digits」游戏中的谜题。

## 先决条件

在运行脚本之前，请确保已安装以下项目：

- Python 3.x
- Selenium 库
- Chrome WebDriver
- solver 文件夹

## 入门

1. 克隆存储库或下载脚本。
2. 使用 pip 安装所需的依赖项：

   ```shell
   pip install selenium
   ```

3. 下载 Chrome WebDriver 可执行文件，并将其位置添加到系统的 PATH 环境变量中。

好的！这是命令行界面的文档：

## 用法

```plaintext
solver/util/solve_auto [-h] [[-start S] [-level L] | [-daily]]
```

### 可选参数

- `-h, --help`：显示帮助消息并退出。

- `-start S, --startLevel S`：指定开始解决谜题的起始级别。该值应为整数。

- `-level L, --levelToPlay L`：指定要玩的级别总数。该值应为整数。

- `-daily, --dailyOnly`：仅解决每日谜题。如果提供此标志，工具将忽略 `--startLevel` 和 `--levelToPlay` 选项，仅解决每日谜题。

## 示例

1. 解决从第 5 级开始的 10 级：
   ```plaintext
   python solver/util/solve_auto --startLevel 5 --levelToPlay 10
   ```

2. 仅解决每日谜题：
   ```plaintext
   python solver/util/solve_auto --dailyOnly
   ```

注意：如果未提供任何参数，工具将使用默认设置（从第 1 级到第 20 级）。

## 功能

该脚本自动执行以下操作：

1. 导航至纽约时报网站上的「Digits」游戏。

2. 使用 `TimeShift.js` 脚本操纵游戏的时间（仅限 solveMany.py）。

3. 点击「Play」按钮开始谜题。

4. 通过在数字按钮和运算符上执行必要的点击来解决每个谜题。

5. 处理脚本卡住的情况，例如按钮或元素无法点击。

6. 在完成一组谜题集合时，进

入下一个谜题或返回谜题选择界面。

7. 打印当前谜题编号和日期以供参考（仅限 solveMany.py）。

## 自定义

如果您想修改或扩展脚本的功能，可以探索以下函数：

- `click_element(element_id, error_message)`：处理点击由其 ID 识别的元素。如果该元素无法点击，它会提示用户进行输入。

- `combine_numbers(step_list, buttons)`：通过在数字按钮上执行必要的点击并更新按钮的状态，处理数字的合并。

- `next_puzzle_button_click()`：处理点击「Next Puzzle」按钮以进入下一个谜题。

- `back_to_puzzles_button_click()`：在完成一组谜题时处理点击「Back to Puzzles」按钮。

根据您的特定需求，请随意修改代码。

## 许可证

本脚本使用 [MIT 许可证](LICENSE.md) 提供。

请注意，文档假定您已根据「先决条件」部分中提到的方式设置了必要的环境和依赖项。
