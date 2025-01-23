import datetime

def get_weekday(year, month, day):
    try:
        date = datetime.date(year, month, day)
        weekdays = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
        return weekdays[date.weekday()]
    except ValueError:
        return "無効な日付です。正しい日付を入力してください。"

# 入力例
year = int(input("生まれた年を入力してください（例: 2000）:"))
month = int(input("生まれた月を入力してください（例: 7）:"))
day = int(input("生まれた日を入力してください（例: 14）:"))

weekday = get_weekday(year, month, day)
print(f"{year}年{month}月{day}日は{weekday}です。")
