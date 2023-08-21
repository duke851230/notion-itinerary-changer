# Itinerary Producer


## 本程式的目的
因為平常就會用 Notion 的 Board view 來排行程，單用來排行程或整理店家資訊是非常好用的。但它有個缺點就是對手機版介面支援不夠好，不是很方便觀看。  
所以以前的我都會在把確定下來的行程填寫到 Excel 中並印出來，但這個工作蠻花時間的，而且一旦行程又有變動修改起來格外複雜，因此萌生了撰寫此程式的動機，讓我之後能輕鬆的產出行程表。


## 成果展示
### 下圖為 Notion 的 Board view 中排好的行程
用 notion 來排行程確實很方便，但如果出去玩時，要用手機來觀看就不是那麼方便了。

![notion_database](https://gitlab.com/duke-try-new-things/python/itinerary-producer/-/raw/dev/docs/pictures/notion_database.png?inline=false)

### 下圖為輸出的 Excel 行程表格式
經過轉換的行程表，能以顏色區分行程的類型，並增加了時間軸，讓行程更一目了然，且 Excel 也可輕易的列印出來或轉換成 PDF。

![excel](https://gitlab.com/duke-try-new-things/python/itinerary-producer/-/raw/4c1b835021829a5497f6e7495352cf7feda5ece2/docs/pictures/excel.png?inline=false)


## 如何使用？
一、參考別人的教學 https://shaoku.cc/productivity/notion-api-practice/ ，建立自己的 notion integration，並將其 share 到自己的 notion board view 行程表頁面
- 行程表卡片必須至少有 Name, Date, Type, Start_at, End_at 欄位  
![card](https://gitlab.com/duke-try-new-things/python/itinerary-producer/-/raw/dev/docs/pictures/activity_card.png?ref_type=heads&inline=false)
- 能吃的 Type 目前只有以下這些  
![type](https://gitlab.com/duke-try-new-things/python/itinerary-producer/-/raw/dev/docs/pictures/activity_type.png?ref_type=heads&inline=false)
- 或是直接從我的 notion 下載範本即可（https://efficient-wound-e70.notion.site/5656c60dec224795a36c3658af2fdbcf?pvs=4）

二、先將專案 clone 到本地端

三、將 python 環境裝好，並將 requirements.txt 的套件裝上

四、修改配置檔，將 config.toml.example 更名為 config.toml，並修改裡面的值

![config](https://gitlab.com/duke-try-new-things/python/itinerary-producer/-/raw/dev/docs/pictures/config.png?ref_type=heads&inline=false)
- TOKEN：為 notion integration 的 secret
- DATABASE_ID：從 notion board view 的網址上能找到  
![notion_url](https://gitlab.com/duke-try-new-things/python/itinerary-producer/-/raw/dev/docs/pictures/notion_url.png?ref_type=heads&inline=false)
- EXCEL_BASIC_DIR：產出的 Excel 要放在哪
- SCHEDULE_TIMELINE_START_AT：Excel 行程表最左邊時間軸的起始時間
- SCHEDULE_TIMELINE_END_AT：Excel 行程表最左邊時間軸的結束時間
- SCHEDULE_TIMELINE_INTERVAL：Excel 行程表最左邊時間軸的時間跨度（單位：分鐘）
- MINIMAL_INTERVAL：Excel 行程時間分割的最小粒度（單位：分鐘），若設為 10 分鐘，notion board view 中設置的時間最小單位就只能以 10 分鐘來填寫  
![time_restriction](https://gitlab.com/duke-try-new-things/python/itinerary-producer/-/raw/dev/docs/pictures/time.png?ref_type=heads&inline=false)

五、執行程式，執行 produce_schedule.sh（或把裡面的指令複製出來執行）
