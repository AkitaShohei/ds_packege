import pyperclip_plus as pp

# 日報のテンプレートをクリップボードにコピー
pp.copy("今日の活動:\n\n")

# 実際の活動を入力
activities = "Python勉強\n食事\n寝る"
pp.copy(activities + "\n\n")

# 日報をまとめてクリップボードにコピー
pp.copy(pp.paste() + activities)
