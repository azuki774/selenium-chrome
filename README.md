# selenium-chrome
以下のライブラリが構築されたDockerイメージ
- google-chrome-stable
- python3-selenium
- selenium
- webdriver-manager
- BeautifulSoup4

## 動作
- デフォルトでは初めに `src/main.py` が実行される。
    - CMD ["filename.py"] を渡すと最初に起動するpyファイルが変更できる。
- driverは、
    ``` bash
    import driver

    driver = driver.get_driver()
    ```
    で読み込む。

- デフォルトの `/src/main.py` は GitHub のホームページからタイトルを取り出して表示するサンプル。
