# LazyTree CLI Tool

一個簡單的命令列工具，用來以 **懶加載（lazy loading）** 的方式瀏覽檔案系統樹狀結構。從指定的根目錄開始，只在使用者展開時載入下一層目錄，避免一次性讀取龐大資料夾結構。

---

## 功能特色

* **懶加載**：只在展開資料夾時才讀取該層內容。
* **導航操作**：

  * 輸入目錄索引即可展開對應資料夾。
  * 使用 `..` 返回上層目錄。
  * 使用 `q` 離開程式。
* **路徑複製**：輸入 `c [index]` 可以顯示完整路徑，方便複製。
* **錯誤處理**：針對權限不足或檔案不存在提供提示。

---

## 安裝與執行

### 1. 複製專案

```bash
git clone <your-repo-url>
cd lazytree
```

### 2. 執行程式

```bash
python lazy_tree.py
```

---

## 使用方法

### 1. 輸入根目錄路徑

程式啟動時會要求輸入根目錄，例如：

```
Enter root path: /home/nick/
```

### 2. 操作指令

* `index` → 展開對應的資料夾
* `c index` → 顯示對應項目的完整路徑
* `..` → 返回上一層
* `q` → 離開程式

### 範例互動

```
Enter root path: /home/nick/

Current path: /home/nick/
[0] Documents/
[1] Downloads/
[2] Pictures/

Options: [index] to open folder, 'c [index]' to copy path, '..' to go up, 'q' to quit
> 1

Current path: /home/nick/Downloads
[0] project.zip
[1] papers/
```

---

## 適用場景

* 下載檔案時快速瀏覽並複製目錄路徑。
* 處理大型或巢狀結構目錄時，避免一次讀取全部造成延遲。
* 簡單 CLI 環境下的替代檔案總管工具。

---

## 後續改進方向

* 加入搜尋功能。
* 支援檔案/資料夾資訊顯示（大小、修改日期）。
* 發展成 GUI 版（例如 PyQt / Tkinter）。
* 背景監聽檔案系統變化，自動更新顯示。

---

## 授權

MIT License
