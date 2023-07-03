# 數字求解自動化

此腳本使用 Selenium 和自定義求解器自動解決紐約時報網站上的「Digits」遊戲中的謎題。

## 先決條件

在運行腳本之前，請確保已安裝以下項目：

- Python 3.x
- Selenium 库
- Chrome WebDriver
- solver 文件夾

## 入門

1. 克隆存儲庫或下載腳本。
2. 使用 pip 安裝所需的依賴項：

   ```shell
   pip install selenium
   ```

3. 下載 Chrome WebDriver 可執行文件，並將其位置添加到系統的 PATH 環境變量中。

好的！這是命令行界面的文檔：

## 用法

```plaintext
solveAuto [-h] [[-start S] [-level L] | [-daily]]
```

### 可選參數

- `-h, --help`：顯示幫助消息並退出。

- `-start S, --startLevel S`：指定開始解決謎題的起始級別。該值應為整數。

- `-level L, --levelToPlay L`：指定要玩的級別總數。該值應為整數。

- `-daily, --dailyOnly`：僅解決每日謎題。如果提供此標誌，工具將忽略 `--startLevel` 和 `--levelToPlay` 選項，僅解決每日謎題。

## 示例

1. 解決從第 5 級開始的 10 級：
   ```plaintext
   python solver/util/solveAuto --startLevel 5 --levelToPlay 10
   ```

2. 僅解決每日謎題：
   ```plaintext
   python solver/util/solveAuto --dailyOnly
   ```

注意：如果未提供任何參數，工具將使用默認設置（從第 1 級到第 20 級）。

## 功能

該腳本自動執行以下操作：

1. 導航至紐約時報網站上的「Digits」遊戲。

2. 使用 `TimeShift.js` 腳本操縱遊戲的時間（僅限 solveMany.py）。

3. 點擊「Play」按鈕開始謎題。

4. 通過在數字按鈕和運算符上執行必要的點擊來解決每個謎題。

5. 處理腳本卡住的情況，例如按鈕或元素無法點擊。

6. 在完成一組謎題集合時，進

入下一個謎題或返回謎題選擇界面。

7. 打印當前謎題編號和日期以供參考（僅限 solveMany.py）。

## 自定義

如果您想修改或擴展腳本的功能，可以探索以下函數：

- `click_element(element_id, error_message)`：處理點擊由其 ID 識別的元素。如果該元素無法點擊，它會提示用戶進行輸入。

- `combine_numbers(step_list, buttons)`：通過在數字按鈕上執行必要的點擊並更新按鈕的狀態，處理數字的合併。

- `next_puzzle_button_click()`：處理點擊「Next Puzzle」按鈕以進入下一個謎題。

- `back_to_puzzles_button_click()`：在完成一組謎題時處理點擊「Back to Puzzles」按鈕。

根據您的特定需求，請隨意修改代碼。

## 許可證

本腳本使用 [MIT 許可證](LICENSE.md) 提供。

請注意，文檔假定您已根據「先決條件」部分中提到的方式設置了必要的環境和依賴項。
