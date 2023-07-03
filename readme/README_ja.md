<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Digits Solver アイコン"
        width="500"
       />
    </picture>
<p>

[English](README.md)
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • 日本語
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)
握「Digits」游戏的终极伴侣。

「Digits Solver」へようこそ。この必須のPythonプログラムは、ニューヨークタイムズが開発した[Digits](https://www.nytimes.com/games/digits)パズルゲームを攻略するために設計されました。数字の魅力に浸りながら、数学の演算を駆使して出発点の数字を操作し、目標の数字を見つけ出す戦略を展開してください。強力なアルゴリズムと緻密な分析により、Digits Solverは各パズルを迅速に解き明かし、一歩ずつ確実な解答を提供します。パズル解決のスキルを高め、数字の中に隠された秘密を解き放ちましょう。Digitsゲームのマスターにとって欠かせない最高のパートナーを体験してください。

[![Python アプリケーション](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![PyLint スコア](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Python バッジ](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![貢献歓迎](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&color=pink)
[![ライセンス](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![コードスタイル: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## デモ
アルゴリズムの実行例はこちらでご覧いただけます（リダイレクト後、緑色の実行ボタンをクリックしてください）：

[![Replit](https://img.shields.io/badge/デモ-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

また、このアルゴリズムを使用したスピードラン動画もご覧いただけます：

[![Replit](https://img.shields.io/badge/デモ-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*注意: このデモでは solveAuto 機能を使用しています。詳細は続きを読んでください*
## 目次
- [使用法](#使用法)
- [例](#例)
- [代替使用法](#代替使用法)
- [貢献](#貢献)
- [ライセンス](#ライセンス)


## 使用法

Digits Solver プログラムを実行するには、次のコマンドを実行します:

```bash
git clone https://github.com/yuchuehw/DigitsSolver
cd ./DigitSolver
python solver <starting_digits> <target_digit> [-os] [-h]
```

- `<starting_digits>`: 開始数字を表す整数のリスト（スペース区切り）。
- `<target_digit>`: 獲得する必要がある目標数字。
- `-os` または `--onesolution`（オプション）: 指定された場合、プログラムは1つの解決策のみを見つけます。それ以外の場合は、すべての可能な解決策を見つけます。
- `-h` または `--help`（オプション）: 使用すると、ヘルプメニューが表示されます。

## 例

1. 数字のパズルのすべての解を見つける場合:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. 数字のパズルの1つの解のみを見つける場合:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```

## 出力

プログラムは見つかった解の数を出力し、以下の形式で各解を表示します:

```
解が見つかりました:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

解が 1 つ見つかりました
```

## 代替使用法
Digits Solver は Python モジュールとしてもインポートして、プログラム上で使用することもできます。以下は使用例です:

```python
from solver.solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
solution_count = solver.solve(False)
print(f"解が {solution_count} つ見つかりました")
```

## その他のファイル

solver プログラムを補完するいくつかの追加の Python プログラムも含まれています。これらの各プログラムの使用方法についての詳しい説明は、以下で確認できます：

- [pretty_solve.py の使用方法](reference/prettySolve.md): solver プログラムの視覚的に向上させたバージョンを提供します。
- [solve_auto.py の使用方法](reference/solveAuto.md): Selenium を使用したフルオートマチックな Digits solver

これらのファイルを探索して、特定の使用ケースやシナリオに活用してください。

*apendix フォルダには、NYT Games で使用された450の

問題も含まれています。これらの問題をプログラムのテストに使用しても構いません*

## 貢献

Digits Solver プログラムへの貢献は歓迎します！問題を見つけた場合や改善の提案がある場合は、GitHub リポジトリで問題をオープンしたりプルリクエストを送信したりしてください。

貢献する際には、ベストプラクティスに従い、コードの品質を維持し、変更の説明を明確に提供してください。

## ライセンス

Digits Solver プログラムは [MIT ライセンス](https://choosealicense.com/licenses/mit/) のもとでライセンスされています。このプログラムは個人使用や商用目的で自由に使用、変更、配布することができます。詳細については [LICENSE](LICENSE.md) ファイルをご覧ください。

## 謝辞

このプロジェクトへの貢献について、特に [timeshift.js](https://github.com/plaa/TimeShift-js) の作者に心から感謝いたします。彼らのコードの一部は、solver.util モジュールの実装に利用されています。
