# AI 使用說明

## 允許使用 AI 的時機

- 不懂如何寫測試時
- 實現遇到 Python 語法問題時
- ASCII 視覺化時
- 需要重構代碼時

## 禁止使用 AI 的地方

- 完整複製 AI 生成的代碼
- 跳過 TDD 三階段流程
- 使用 `as any` 或 `@ts-ignore` 等方式壓制錯誤

## 推薦作法

1. 先自己寫測試 (Stage 1: RED)
2. 看測試失敗
3. AI 協助實現最小化代碼 (Stage 2: GREEN)
4. 自己重構代碼 (Stage 3: REFACTOR)
5. 確認所有測試通過

## TDD 三階段流程

### Stage 1: RED - 資料讀取
- 先寫測試案例
- 測試失敗是正常的
- 逐步實現資料讀取功能

### Stage 2: GREEN - 戰鬥模擬
- 實現最小化代碼通過測試
- 使用 Week 02 技能: sorted(), Counter, defaultdict, namedtuple

### Stage 3: REFACTOR - 重構與視覺化
- 新增 ASCII 視覺化報告
- 保持所有測試通過
- 提升代碼可讀性

## 學習資源

- Week 02: Python 資料結構與排序
- Week 07: 檔案 I/O 與 EOF 處理
- TDD: Red → Green → Refactor
