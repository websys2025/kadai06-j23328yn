# 気象庁 天気予報データ API
# 機能：日本の天気予報情報をJSON形式で取得
# 使い方：地域コードを指定し天気予報情報を取得（千葉県の場合：120000）
# 統計データからデータ部を取得する方法が分からなかった
import requests
import pandas as pd

API_URL="https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json" #エンドポイント
params={
    "lang":"J"
}
response = requests.get(API_URL, params=params)
# Process the response
data=response.json()

print(data)