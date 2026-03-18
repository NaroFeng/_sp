# 🧬 Evolution Engine (The Compiler of Intent)

> **"編譯不再是翻譯語法，而是翻譯意圖。"**

Evolution Engine 是一個實驗性的**下一代智能編譯與自動進化框架**。
傳統軟體開發流程是：`人類思考 -> 撰寫抽象程式碼 (C/Python) -> 電腦編譯機器碼`。
而在這個專案中，我們提倡：`人類建立防呆語意 (Intent) -> AI 提取本地知識庫並推理約束 -> 自動結構成極致效能的底層機器碼`。

這不僅僅是一個 AI 輔助腳本，它是一套具備 **形式化驗證 (Formal Verification)**、**漂移控制 (Drift Control)** 與 **硬核熱切換 (Hard-Wired Hot-Swapping)** 的全新編譯流水線。

---

## 🚀 核心理念 (Core Philosophy)

### 1. Intent-Based Compilation (基於意圖的編譯)
開發者不再需要手刻 Boilerplate 或處理繁瑣的記憶體配置。你只需要撰寫 `.seed.c` 檔案，透過標籤宣告需要的環境與限制，引擎便會自動從 `skills/`（本地演化知識庫）中提取對應的最佳化程式碼模塊（如 O(1) 演算法），並與你的意圖進行交織。

### 2. 雙層協作架構 (Architect & Crystallizer)
本系統將 AI 的角色拆分為二，帶來極大的邏輯穩定度：
- **The Architect (設計端)**：撰寫附帶 `<meta>` 與 `<constraint>` 標籤的種子文件，賦予程式嚴格的物理規則（如：`static_memory`, `no_malloc`）。
- **The Crystallizer (執行端)**：被閹割了「發散思維」的底層編譯者，它在將意圖轉化為 C 語言時，必須嚴格服從 Architect 的約束，產出最具硬體親和性 (Machine Proximity) 的代碼。

### 3. Stability & Drift Control (穩定度與漂移控制)
為了防範 AI 產生幻覺或不可控的代碼突變，系統內建了 **5% 演化漂移 (Evolution Drift) 限制**。任何更新如果與上一代（基準快照）邏輯落差過大，系統會強制煞車阻斷編譯，並要求人工審查。此外，所有的更迭都會鉅細靡遺地被記載進 `/logs/evolution_history.md` 當中。

### 4. Hard-Wired Evolution (全靜態注入進化)
為了追求極致運算效能，系統揚棄了 C 語言在 Runtime 載入並解析 JSON 的傳統做法。當外部變數改變時，`validator.py` 會檢查安全極限，接著引擎會將配置轉化為 `static const` 硬刻進 C 檔案，並透過 `hot_swap.py` 即時傳送 `SIGTERM` 讓舊進程完美收斂並無縫熱替換為新進程。

---

## 📂 專案結構與文件說明

- **`engine.py`**: 進化框架的中樞控制器，負責協調解析、驗證、組裝與編譯。
- **`.seed.c` 檔案**: 使用者唯一需要撰寫的源碼格式，包含 `<meta>`, `<constraint>`, `<injection>` 與 `<body>`。
- **`parser.py` & `validator.py`**: 防呆過濾器，確保種子意圖邏輯沒有衝突（如：要求最高速度卻使用慢速 IO），並兼具 Config 的防護閘門。
- **`ai_module.py`**: The Crystallizer 核心，負責將意圖與本地技能包編織成嚴謹的 C 語言。
- **`watch.py`**: 監控 5% 變動率的防熵衛兵。
- **`hot_swap.py`**: 用於背景監控設定檔與 Seed 變化的常駐精靈，自動實現進程熱切換與代碼汰換。
- **`logger.py`**: 記錄器。

---

## 🛠️ 快速啟動 (Quick Start)

### 1. 單次進化編譯
使用預設提供的 `Makefile` 進行一鍵意圖啟動與編譯：
```bash
make run SEED=v3.seed.c
```

### 2. 啟用熱切換常駐進化服務
監控 `config/app.json` 的數值變動，體驗無需關閉程式即可完成靜態優化更新的全自動流程：
```bash
python hot_swap.py
```

> *"唯有將人類的思考從語法架構中解放，才能將電腦的效能從冗餘設計中釋放。"*
