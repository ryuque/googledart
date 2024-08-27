# -*- coding: utf-8 -*-
import sys
from googlesearch import search

def google_search(website, textfile):
    # テキストファイルから検索クエリを読み込む
    with open(textfile, 'r', encoding='utf-8') as file:
        queries = file.readlines()
    
    # 検索結果を保存するファイル
    output_file = 'search_results.txt'
    
    with open(output_file, 'w') as output:
        for query in queries:
            query = query.strip()
            search_query = f"site:{website} {query}"
            print(f"Searching for: {search_query}")
            try:
                # 検索を実行し、上位5件のURLを取得
                for result in search(search_query, num_results=20):
                    output.write(result + '\n')
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
    
    print(f"Search results saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 googledart.py <website> <textfile>")
        print("There is no mention of the target site")
    else:
        website = sys.argv[1]

        textfile = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else 'common.txt'
        google_search(website, textfile)
