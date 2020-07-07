This is a script to fetch the Japanese translation mod files of Kingdom Come: Deliverance (KCD).

KCD 有志翻訳 mod の翻訳ファイルを取得するスクリプトです. 従来のものは実質  Windows でしか使えませんでしたが Linux 系でも翻訳ファイルを取得できるようにしました.

# 要件 (Requirements)
* KCD本体 (steam版, Epic Games版)
* Python 3.x (>= 3.7 recommended)

私は試してないですがこのサイトによるとEpic Games版でもできるとのこと https://automaton-media.com/articles/newsjp/20200214-113773/

`python3` で呼び出せるようにパスが通っている状態にしてください.
現時点では Python 組み込みのモジュールしか使っていないので多分 Python をインストールするだけでいけるはず

# 使い方 (Usage)

1. 以下を参考に, 「最新データ自動更新Mod」をインストール
https://wikiwiki.jp/kcd0/%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%8C%96MOD
(正確にはフォルダ構成を真似し, `config.ini` を置くだけでもよい)

2. このリポジトリをダウンロードしフォルダ以下2つを入れる
	* `update_with_id.sh`
	* `update_witout_id.sh`
ターミナルを開いて mod ディレクトリに移動し以下を実行.

```
# update with IDs:
./update_with_id.sh
# update without IDs:
./update_without_id.sh
```
sh ファイルは py ファイルを呼び出してるだけなので直接 *.py を実行してもいい
