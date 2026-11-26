from datetime import datetime
from zoneinfo import ZoneInfo
import urllib.parse
import urllib.request

TOKEN = "8985673964:AAESQvUiNgf_GmVN0OwrV-a-83fMx-JVjK8"
CHAT_ID = "9228138679"

taipei_now = datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")

message = (
    "🎉 主動通知測試成功！\n"
    "這是我的 Telegram 作業。\n"
    f"發送時間：{taipei_now}"
)

url = (
    f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    f"?chat_id={CHAT_ID}&text={urllib.parse.quote(message)}"
)

with urllib.request.urlopen(url) as response:
    print("Status:", response.status)
點擊右上角綠色的 「Commit changes...」，在彈出視窗再點一次 「Commit changes」 儲存檔案。   接著點專案上方選單的 「Actions」 分頁。   若看到工作流程列表或提示，點選 「set up a workflow yourself」（或搜尋 Python application 點 Configure）。   檔名保持 .github/workflows/blank.yml（或 python-app.yml），將內容全部清空並貼上以下設定（加入 workflow_dispatch，讓我們可以按按鈕手動測試）：YAMLname: Telegram Notify

on:
  workflow_dispatch:

jobs:
  send-notification:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Run notification script
        run: python notify.py
