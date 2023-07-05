# Digits Solver Automation（数字の解決自動化）

このスクリプトは、Seleniumとカスタムソルバーを使用して、New York TimesのウェブサイトのDigitsゲームのパズルを自動で解くものです。

## 前提条件

スクリプトを実行する前に、以下の項目がインストールされていることを確認してください：

- Python 3.x
- Seleniumライブラリ
- Chrome WebDriver
- solverフォルダ

## はじめに

1. リポジトリをクローンするか、スクリプトをダウンロードしてください。
2. pipを使用して必要な依存関係をインストールしてください：

   ```shell
   pip install selenium
   ```

3. Chrome WebDriverの実行可能ファイルをダウンロードし、その場所をシステムのPATH環境変数に追加してください。

はい！以下はコマンドラインインターフェースのドキュメンテーションです：

## 使用法

```plaintext
python solver/util/solve_auto [-h] [[-start S] [-level L] | [-daily]]
```

### オプション引数

- `-h, --help`: ヘルプメッセージを表示して終了します。

- `-start S, --startLevel S`: パズルの解決を開始するレベルを指定します。値は整数である必要があります。

- `-level L, --levelToPlay L`: プレイするレベルの総数を指定します。値は整数である必要があります。

- `-daily, --dailyOnly`: 毎日のパズルのみを解決します。このフラグが指定された場合、ツールは`--startLevel`および`--levelToPlay`オプションを無視し、毎日のパズルのみを解決します。

## 例


1. レベル5から始まる10レベルを解決する：
   ```plaintext
   python solver/util/solve_auto --startLevel 5 --levelToPlay 10
   ```

2. 毎日のパズルのみを解決する：
   ```plaintext
   python solver/util/solve_auto --dailyOnly
   ```

注：引数が指定されていない場合、ツールはデフォルトの設定（レベル1からレベル20までの範囲）を使用します。


## 機能

このスクリプトは以下のアクションを自動化します：

1. New York Timesのウェブサイト上のDigitsゲームへの移動。

2. `TimeShift.js`スクリプトを使用してゲームの時間を操作します。（solveMany.pyのみ）

3. "Play"ボタンをクリックしてパズルを開始します。

4. 必要なクリック操作

を実行し、各パズルを解きます。

5. ボタンや要素がクリックできない場合など、スクリプトが停止する場合の処理。

6. パズルセットが完了した場合、次のパズルに進むかパズル選択画面に戻る処理。

7. 参照のために現在のパズル番号と日付を印刷します。（solveMany.pyのみ）

## カスタマイズ

スクリプトの機能を変更または拡張したい場合は、以下の関数を調査してみてください：

- `click_element(element_id, error_message)`: IDで識別される要素をクリックします。要素がクリックできない場合は、ユーザーに入力を求めます。

- `combine_numbers(step_list, buttons)`: 必要なクリック操作を実行して数字を組み合わせ、ボタンの状態を更新します。

- `next_puzzle_button_click()`: "Next Puzzle"ボタンをクリックして次のパズルに進みます。

- `back_to_puzzles_button_click()`: パズルセットが完了した場合に、"Back to Puzzles"ボタンをクリックします。

特定の要件に応じてコードを変更してください。

## ライセンス

このスクリプトは[MITライセンス](LICENSE.md)のもとで提供されています。

ドキュメンテーションでは、すでに「前提条件」セクションで説明した環境と依存関係の設定が済んでいることを前提としています。
