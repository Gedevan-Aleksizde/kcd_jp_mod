#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from pathlib import Path
import configparser
import requests
import re

# https://drive.google.com/uc?export=download&id=1Au-s4FIU3Ju3aNrIGGi8UIg0nKiBsQks
# path_local = Path.home().joinpath('SteamLibrary/steamapps/common/KingdomComeDeliverance/mods/ZZZ_JPMod')

print(__file__)
path_local = Path(__file__).parent
# configparser はセクションのない ini ファイルを読み込めないのでダミーを追加
with path_local.joinpath('config.ini').open('r') as f:
    conf = configparser.ConfigParser()
    conf.read_string('[S]\n' + f.read())
    conf = dict(conf['S'])
    for k in conf.keys():
        conf[k] = conf[k].replace('\\', '/')
url_jpfont = "https://drive.google.com/uc?export=download&id=1x4TiJeE_aQoRLXGu1G9rO3UDvjKyKO8R"
path_pak = path_local.joinpath(conf['savefilepath']).joinpath(conf['dlfilename'])
path_bak_bakup = path_local.joinpath(conf['savefilepath']).joinpath(conf['dlfilename'] + '.bak')
path_jpfont = path_local.joinpath(conf['jpmodpath'])

match_str = 'https://drive\.google\.com/uc\?export=download&amp;id=.+?</div>'

print(path_local)
print(path_jpfont)

if __name__ == '__main__':
    if conf['jpmodaction'] == 'Enable':
        if path_jpfont.exists():
            pass
        else:
            print('日本語フォントファイルが存在しません. ダウンロードしますか?')
            while True:
                q = input('yes/no')
                ans = q[0].lower()
                if q == '' or not ans in ['y', 'yes', 'n', 'no']:
                    print('yes か no で入力してください.')
                else:
                    break
            if ans in ['y', 'yes']:
                print('フォントファイルをダウンロードします.')
                font = requests.get(url_jpfont)
                if font.status_code >= 400:
                    raise(BaseException('ファイルのダウンロードに失敗しました: ' + url_jpfont))
                else:
                    path_jpfont.write_bytes(font.content)
                    print('フォントのインストールが完了しました.')
            elif ans in ['n', 'no']:
                pass
            else:
                pass

    print('翻訳ファイルのダウンロードリンクを取得します.')
    r = requests.get(conf['sheetsurl'])
    if r.status_code >= 400:
        raise(BaseException('ファイルのダウンロードリンク取得に失敗しました: ' + r.status_code))

    # TODO: API で落としたほうが健全か?
    # ダウンロードリンクが3つ書かれて, 上から順に1つ目がIDつきという前提
    links_pak = re.findall(match_str, r.text)
    if len(links_pak) >= 1:
        download_url = links_pak[0][:-6].replace('&amp;', '&')
        print('翻訳ファイルをダウンロードします.')
        pak = requests.get(download_url)
        if pak.status_code >= 400:
            raise(BaseException('翻訳ファイルのダウンロード中にエラーが発生しました: ' + download_url))
        if path_pak.exists():
            print('翻訳ファイルが既に存在するため English_xml.bak にバックアップを取ります.')
            path_pak.rename(path_bak_bakup)
        path_pak.write_bytes(pak.content)
        print('更新処理が完了しました.')
    else:
        raise(BaseException('pak ファイルのダウンロードリンクが見つかりません: ' + conf['sheeturl1']))