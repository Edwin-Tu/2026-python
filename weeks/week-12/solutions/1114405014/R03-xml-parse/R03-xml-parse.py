# R03. XML 解析基礎（6.3）
# 主題：xml.etree.ElementTree
# 方法：find / findall / get / text / iter
# XML（eXtensible Markup Language）是常見的資料交換格式
# ElementTree 是 Python 內建的 XML 解析模組

# 匯入 xml.etree.ElementTree，慣例縮寫為 ET
import xml.etree.ElementTree as ET

# ── 範例 XML ─────────────────────────────────────────────────────────
# 使用三引號字串定義一個 RSS 2.0 格式的 XML 範例
# RSS 是常見的新聞訂閱格式，這裡簡化結構作為教學用途
xml_data = """
<rss version="2.0">
  <channel>
    <title>Planet Python</title>
    <item>
      <title>討論 Python 型別提示</title>
      <link>https://example.com/1</link>
      <author>Alice</author>
    </item>
    <item>
      <title>asyncio 最佳實踐</title>
      <link>https://example.com/2</link>
      <author>Bob</author>
    </item>
  </channel>
</rss>
"""

# ── 解析字串 ─────────────────────────────────────────────────────────
# fromstring() 將 XML 字串解析為 Element 物件（根元素）
root = ET.fromstring(xml_data)
# tag 屬性存放標籤名稱，如 'rss'
print("根標籤：", root.tag)           # rss
# attrib 屬性存放標籤的所有屬性，回傳 dict
print("屬性：",   root.attrib)        # {'version': '2.0'}

# ── find / findall ────────────────────────────────────────────────────
# find() 尋找第一個符合條件的子元素，回傳 Element 或 None
# 路徑使用類似檔案系統的語法，預設從當前元素的子元素開始找
channel = root.find("channel")
# 可以串接 find() 來深入巢狀結構
# channel.find("title") 找到 <channel> 下的第一個 <title>
print("頻道名稱：", channel.find("title").text)

# findall() 尋找所有符合條件的子元素，回傳 list
# 可以使用 XPath 語法，如 "channel/item" 表示 channel 下的所有 item
for item in root.findall("channel/item"):
    # 從每個 item 中取出子元素的 text 屬性
    title  = item.find("title").text   # 文章的標題文字
    author = item.find("author").text  # 作者名稱
    # 格式化輸出，方便閱讀
    print(f"  [{author}] {title}")

# ── iter：遍歷所有同名標籤 ───────────────────────────────────────────
# iter(tag) 回傳一個迭代器，深度優先（depth-first）遍歷所有子孫元素
# 不指定 tag 則遍歷所有元素
print("\n所有 <title>：")
for elem in root.iter("title"):
    # 不論巢狀多深，所有名為 <title> 的元素都會被找到
    print(" ", elem.text)

# ── 從檔案解析 ───────────────────────────────────────────────────────
# 如果 XML 存在檔案中，使用 ET.parse() 而非 fromstring()
# tree = ET.parse("data.xml")    # 解析整個檔案
# root = tree.getroot()          # 取得根元素
# 之後的操作與 fromstring() 完全一樣

# ── 取得屬性 .get() ───────────────────────────────────────────────────
# Element.get(key, default=None) 用來取得元素的屬性值
# 類似 dict.get()，如果屬性不存在可回傳預設值
version = root.get("version")
print("\nRSS 版本：", version)        # 2.0
# 第二個參數是屬性不存在的預設回傳值
print("不存在的屬性：", root.get("missing", "預設值"))
