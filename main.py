from clipboard_manager import ClipboardManager as pp

# クリップボードの履歴から特定のキーワードを含むアイテムを検索
keywords = ["Python", "Machine Learning"]
for keyword in keywords:
    history_items = pp.search_history(keyword)
    print(f"{keyword}に関するクリップボードの履歴:")
    for item in history_items:
        print(item)
