# 〇課題３
# 実行すると
# 「動物名（英語）を入力してください。」
# 「動物名（日本語）を入力してください。」
# と表示されて、任意の回数入力できること
# ※「動物名（英語）を入力してください。」の場合に英語以外を入力するとエラーメッセージ「動物名（英語）は半角英字で入力してください。」と表示され、
# 「動物名（英語）を入力してください。」から再開すること
# 「ファイル出力する」と入力すると
# 以下の形式で、json、csv、xmlファイルを生成するプログラムを作成しなさい。
# なお、出力するファイルの出力先やファイル名はconfigファイルを参照するようにすること


import json
import csv
import os
import re

with open("config.json", "r", encoding="utf-8") as config_file:
    CONFIG = json.load(config_file)

def validate_english_name(name):
    return re.fullmatch(r"[a-zA-Z]+", name) is not None

def save_as_json(data):
    path = os.path.join(CONFIG["output_dir"], CONFIG["json_file"])
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def save_as_csv(data):
    path = os.path.join(CONFIG["output_dir"], CONFIG["csv_file"])
    with open(path, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["英語", "日本語"])
        for eng, jap in data.items():
            writer.writerow([eng, jap])

def save_as_xml(data):
    path = os.path.join(CONFIG["output_dir"], CONFIG["xml_file"])
    with open(path, "w", encoding="utf-8") as xml_file:
        xml_file.write("<Animals>\n")
        for english, japanese in data.items():
            xml_file.write(f"  <{english}>{japanese}</{english}>\n")
        xml_file.write("</Animals>\n")

def main():
    os.makedirs(CONFIG["output_dir"], exist_ok=True)
    animals = {}

    while True:
        english_name = input("動物名（英語）を入力してください: ")
        if english_name.lower() == "ファイル出力する":
            break

        if not validate_english_name(english_name):
            print("動物名（英語）は半角英字で入力してください。")
            continue

        japanese_name = input("動物名（日本語）を入力してください: ")
        animals[english_name] = japanese_name

    save_as_json(animals)
    save_as_csv(animals)
    save_as_xml(animals)
    print("ファイルが出力されました。")

if __name__ == "__main__":
    main()
