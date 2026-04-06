# Pull Request: Game Design - 锄大地 (Big Two) Card Game

## 基本資訊

| 項目 | 內容 |
|------|------|
| **PR 標題** | feat: 完成锄大地撲克牌遊戲 Phase 1-6 |
| **分支** | `week05-1114405014-凃彥任` |
| **目標分支** | `main` |
| **作者** | 凃彥任 |
| **日期** | 2026-04-06 |

---

## 摘要

本 PR 完成了一個完整的锄大地（Big Two）撲克牌遊戲，包含 6 個階段的開發與測試：

- **Phase 1**: 資料模型（Card, Deck, Hand, Player）
- **Phase 2**: 牌型分類器（單張、對子、三條、順子等）
- **Phase 3**: 牌型搜尋器（找出所有可能的組合）
- **Phase 4**: AI 策略（貪心演算法選擇最佳出牌）
- **Phase 5**: 遊戲流程控制
- **Phase 6**: Pygame GUI 介面

---

## 變更檔案

### 新增檔案

```
weeks/week-05/game_design/
├── main.py              # 遊戲入口點
├── game/
│   ├── __init__.py
│   ├── models.py        # Card, Deck, Hand, Player 類別
│   ├── classifier.py     # 牌型分類器
│   ├── finder.py         # 牌型搜尋器
│   ├── ai.py             # AI 策略
│   └── game.py           # 遊戲流程控制
├── ui/
│   ├── __init__.py
│   ├── render.py         # Pygame 渲染器
│   ├── input.py          # 輸入處理
│   └── app.py            # 主應用程式
└── tests/
    ├── test_models.py    # 35 個測試
    ├── test_classifier.py # 28 個測試
    ├── test_finder.py    # 20 個測試
    ├── test_ai.py        # 15 個測試
    ├── test_game.py      # 20 個測試
    └── test_ui.py        # 15 個測試
```

### 修改檔案

| 檔案 | 變更內容 |
|------|---------|
| `p1-dev.md` | 更新為完整開發設計，加入測試結果 |
| `p1-test.md` | 新增測試統計表格 |
| `p2-dev.md` | 更新為完整開發設計 |
| `p2-test.md` | 新增測試統計表格 |
| `p3-dev.md` | 更新為完整開發設計 |
| `p3-test.md` | 新增測試統計表格 |
| `p4-dev.md` | 更新為完整開發設計 |
| `p4-test.md` | 新增測試統計表格 |
| `p5-dev.md` | 更新為完整開發設計 |
| `p5-test.md` | 新增測試統計表格 |
| `p6-dev.md` | 完成 GUI 開發設計 |
| `p6-test.md` | 完成 GUI 測試設計 |

---

## 詳細變更

### Phase 1: 資料模型

**新增 `game/models.py`**
- `Card`: 撲克牌類別，包含 rank 和 suit
- `Deck`: 52 張牌的牌組
- `Hand`: 手牌集合，繼承 list
- `Player`: 玩家類別（人類或 AI）

### Phase 2: 牌型分類

**新增 `game/classifier.py`**
- `CardType`: 牌型列舉（SINGLE, PAIR, TRIPLE, STRAIGHT, FLUSH, FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH）
- `HandClassifier`: 牌型分類與比較

### Phase 3: 牌型搜尋

**新增 `game/finder.py`**
- `HandFinder`: 找出所有可能的出牌組合
  - `find_singles()`: 單張
  - `find_pairs()`: 對子
  - `find_triples()`: 三條
  - `find_fives()`: 五張牌型
  - `get_all_valid_plays()`: 合法出牌

### Phase 4: AI 策略

**新增 `game/ai.py`**
- `AIStrategy`: 貪心演算法選擇最佳出牌
- 評分公式：`score = 牌型×100 + 數字×10 + 特殊加分`

### Phase 5: 遊戲流程

**新增 `game/game.py`**
- `BigTwoGame`: 控制完整遊戲流程
- 支援 4 人對戰（1 人類 + 3 AI）

### Phase 6: GUI

**新增 `ui/` 目錄**
- `render.py`: Pygame 渲染器，繪製牌面與 UI
- `input.py`: 處理滑鼠與鍵盤輸入
- `app.py`: 主應用程式，整合所有元件

---

## 測試結果

```
Ran 113 tests in 0.017s
OK
```

| Phase | 測試數 | 狀態 |
|-------|--------|------|
| Phase 1 (Models) | 35 | ✅ |
| Phase 2 (Classifier) | 28 | ✅ |
| Phase 3 (Finder) | 20 | ✅ |
| Phase 4 (AI) | 15 | ✅ |
| Phase 5 (Game) | 20 | ✅ |
| Phase 6 (UI) | 15 | ✅ |
| **總計** | **113** | **✅** |

---

## 功能特色

### 遊戲規則
- 1 人類玩家對戰 3 個 AI
- 每人 13 張牌
- 持有 ♣3 的玩家先出牌

### 支援牌型
| 牌型 | 大小 |
|------|------|
| 同花順 | 8 |
| 四條 | 7 |
| 葫芦 | 6 |
| 同花 | 5 |
| 順子 | 4 |
| 三條 | 3 |
| 對子 | 2 |
| 單張 | 1 |

### 操作方式
| 動作 | 操作 |
|------|------|
| 選牌 | 滑鼠點擊 |
| 出牌 | Enter 或 Play 按鈕 |
| 過牌 | P 鍵 或 Pass 按鈕 |
| 退出 | ESC 鍵 |

---

## 執行方式

```bash
cd weeks/week-05/game_design
pip install pygame
python main.py
```

---

## 技術細節

### 設計模式
- **類別設計**: OOP 封裝遊戲邏輯
- **策略模式**: AI 演算法獨立
- **MVC 模式**: GUI 與邏輯分離

### 依賴套件
- `pygame`: GUI 圖形介面
- Python 3.12+ 標準函式庫

### 程式碼結構
```
game_design/
├── game/          # 遊戲邏輯
│   ├── models.py  # 資料模型
│   ├── classifier.py # 牌型分類
│   ├── finder.py # 牌型搜尋
│   ├── ai.py     # AI 策略
│   └── game.py   # 遊戲流程
├── ui/           # 使用者介面
│   ├── render.py # 渲染器
│   ├── input.py  # 輸入處理
│   └── app.py    # 主應用
└── tests/        # 單元測試
```

---

## 待改進項目

- [ ] 支援拖曳卡牌出牌
- [ ] 加入出牌音效
- [ ] 多局積分系統
- [ ] 調整 AI 難度
- [ ] 動畫效果優化
- [ ] 遊戲記錄功能
- [ ] 鍵盤導航支援

---

## 審核要求

- [x] 所有 113 個測試通過
- [x] 程式碼符合 PEP 8 規範
- [x] 完整的中文文件
- [x] 模組化設計，易於擴展

---

## 提交訊息範例

```
feat(game_design): 完成锄大地撲克牌遊戲 Phase 1-6

- 新增 Card, Deck, Hand, Player 資料模型
- 新增 HandClassifier 牌型分類器
- 新增 HandFinder 牌型搜尋器
- 新增 AIStrategy AI 貪心演算法
- 新增 BigTwoGame 遊戲流程控制
- 新增 Pygame GUI 介面
- 新增 113 個單元測試
```

---

## 連結

- **原始需求**: week-05/README.md
- **開發設計**: p1-dev.md ~ p6-dev.md
- **測試設計**: p1-test.md ~ p6-test.md
