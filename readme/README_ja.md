<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Digits Solver アイコン"
        width="500"
       />
    </picture>
<p>

English
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)

Digits Solverへようこそ。これは、The New York Timesが開発した数独パズルゲーム[Digits](https://www.nytimes.com/games/digits)を攻略するための究極のPython補助ツールです。数字のチャレンジに飛び込み、戦略的な操作の技術を習得する魅惑的な世界に没入してください。Digits Solverを使用すると、数学の演算を使って一連の初期数字を戦略的に操作し、目標とする数字に到達することができます。その強力なアルゴリズムと緻密な分析により、各パズルを迅速に解き明かし、一歩一歩確実な解答を提供します。パズル解決の腕前を高め、数字に隠された秘密を解き放ちましょう。Digitsのマスターになるためのエキサイティングな旅の準備をしてください！

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

## デモ
リダイレクト後、緑色の実行ボタンをクリックしてアルゴリズムを動作させる様子をご覧ください：

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

また、Digits Solverアルゴリズムを使用したスピードランもご覧いただけます：

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*注意：デモでは[solve_auto](solveAuto.md)機能を紹介しています。詳細については続けて読んでください。*

## 目次

- [インストール](#インストール)
- [使用方法](#使用方法)
- [例](#例)
- [代替の使用方法](#代替の使用方法)
- [Utilモジュール](#utilモジュール)
- [貢献方法](#貢献方法)
- [ライセンス](#ライセンス)
- [謝辞](#謝辞)

## インストール

次のいずれかの方法でDigits Solverプログラムのコピーを取得できます：

1. **リポジトリをクローンする**：
   ```bash
   git clone https://github.com/yuchuehw/DigitsSolver.git
   ```

2. **Zipファイルをダウンロードする**：
   - GitHubリポジトリの[Release](https://github.com/yuchuehw/DigitsSolver/releases)タブに移動します。
   - 最新のリリースのzipファイルをダウンロードします。
   - zipファイルの内容を任意の場所に展開します。

プログラムを取得したら、Digits Solverプログラムを実行するために[使用方法](#使用方法)セクションに進むことができます。

## 使用方法

Digits Solverプログラムを実行するには、ターミナルを開き、DigitsSolverリポジトリをダウンロードまたはクローンしたディレクトリに移動します。適切なディレクトリに移動したら、ターミナルで以下のコマンドを実行します（角括弧内の値を入力値で置き換えてください。詳細については[例](#例)セクションを参照してください）：

```bash
python solver <starting_digits> <target_digit> [-os] [-h]
```

- `<starting_digits>`: 初期数字を表す整数

のスペース区切りのリストです。
- `<target_digit>`: 目標とする数字です。
- `-os`または`--onesolution`（オプション）：指定された場合、プログラムは1つの解だけを見つけます。それ以外の場合は、すべての可能な解を見つけます。
- `-h`または`--help`（オプション）：使用すると、ヘルプメニューが表示されます。

## 例

1. 数字パズルのすべての解を見つける：
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. 数字パズルの解を1つだけ見つける：
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```

3. 注意：starting_digitsは常にtarget_digitsの前にあります。これは8つのstarting_digitsを持つパズルの例です：
   ```bash
   python solver 2 3 5 7 11 13 17 19 323 -os
   ```

## 出力

プログラムは見つかった解の数を出力し、各解を次の形式で表示します：

```
解が見つかりました：
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

解が1つ見つかりました
```

## 代替の使用方法

Digits SolverはPythonモジュールとしてインポートしてプログラム内で使用することもできます。提供されたもの以上の機能を追加することができます。以下は、インポートとして使用する最小限の例です：

```python
from solver.solver import DigitSolver

solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
# 括弧内のFalseはオプションです。Falseはすべての解を解きます。Trueは1つの解を解きます。
# solve.printer = some_functionを使用してデフォルトの出力動作を上書きします。
solution_count = solver.solve(False)
print(f"{solution_count} 個の解が見つかりました")
```

## Utilモジュール

solver.utilフォルダ内には、solverプログラムを補完するいくつかの追加のPythonプログラムも含まれています。これらの使用方法については、こちらをご覧ください：

- [pretty_solve.pyの使用方法](prettySolve.md)：solverプログラムの視覚的に向上したバージョンを提供します。
- [solve_auto.pyの使用方法](solveAuto.md)：Seleniumを使用した完全自動のDigitsソルバー

これらのファイルを探索し、特定のユースケースやシナリオに活用してください。

*Appendixフォルダには、NYT Gamesで使用される数独のいくつかのサンプルゲームが含まれています。興味がある場合は、参照してみてください。*

## 貢献方法

Digits Solverはオープンソースプロジェクトであり、コミュニティからの貢献を歓迎しています。バグの報告や機能の提案、コードの改善など、さまざまな形で貢献することができます。[Contribution Guidelines](CONTRIBUTING.md)を参照してください。

## ライセンス

Digits Solver プログラムは [MIT ライセンス](https://choosealicense.com/licenses/mit/) のもとでライセンスされています。このプログラムは個人使用や商用目的で自由に使用、変更、配布することができます。詳細については [LICENSE](LICENSE.md) ファイルをご覧ください。

## 謝辞

このプロジェクトへの貢献について、特に [timeshift.js](https://github.com/plaa/TimeShift-js) の作者に心から感謝いたします。彼らのコードの一部は、solver.util モジュールの実装に利用されています。
