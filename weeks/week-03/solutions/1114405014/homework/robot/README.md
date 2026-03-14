# Mars Robot Simulator

本專案實作一個模擬火星探測機器人的系統。

機器人在有限大小的網格地圖上移動，依照指令：

- L：左轉
- R：右轉
- F：前進

當機器人移動超出地圖邊界時會掉落（LOST），並在最後安全位置留下 **scent（氣味）**，避免之後的機器人重複掉落。

本專案採用 **TDD（Test-Driven Development）** 開發核心邏輯。

---

# 專案架構

```
homework/
│
├── robot_core.py
├── robot_game.py
│
├── tests/
│   ├── test_robot_core.py
│   └── test_robot_scent.py
│
├── TEST_LOG.md
├── TEST_CASES.md
├── AI_USAGE.md
└── README.md
```

---

# 核心規則

機器人狀態：

`(x, y, direction, lost)`

| 欄位     | 說明         |
|----------|--------------|
| x        | X 座標       |
| y        | Y 座標       |
| direction| N / E / S / W |
| lost     | 是否掉落     |

---

# 指令說明

| 指令 | 行為      |
|------|-----------|
| L    | 左轉 90°  |
| R    | 右轉 90°  |
| F    | 向前移動一格 |

方向循環：

```
N → E → S → W
```

---

# scent 機制

當機器人掉落時會記錄：

`(x, y, direction)`

後續機器人在相同位置與方向執行 `F` 時：

- 忽略該指令

避免再次掉落。

---

# TDD 開發流程

本專案遵循：

```
Red → Green → Refactor
```

詳細過程請參閱：

[TEST_LOG.md](TEST_LOG.md)


---

# 單元測試

本專案使用 `unittest`。

測試內容包含：

- 方向旋轉
- 前進移動
- 邊界判斷
- LOST 處理
- scent 機制
- 非法指令

執行測試：

```bash
python -m unittest discover -s tests -p "test_*.py" -v

測試結果：

Ran 18 tests
OK
pygame 視覺化

robot_game.py 提供簡單的視覺化操作。

功能：

顯示網格地圖

顯示機器人位置

顯示方向

顯示 scent

鍵盤操作：

鍵	功能
L	左轉
R	右轉
F	前進
N	建立新機器人
C	清除 scent
ESC	離開
執行方式
安裝套件
pip install pygame
啟動遊戲
python robot_game.py
Python 版本

建議：

Python 3.9+

本專案測試環境：

Python 3.9

---

# 七、AI_USAGE.md 建議補充

建議加入這段：

```markdown
## 拒絕的 AI 建議

AI 曾建議先實作 pygame 視覺化介面，但我選擇先完成
`robot_core.py` 與所有單元測試。

原因：

- 核心邏輯應先被測試驗證
- UI 不應影響核心測試
- 符合 TDD 開發原則