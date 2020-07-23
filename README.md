# rokuyou_icalendar

概要
---
イベントに六曜を含んだiCalendar形式のテキストを出力する

機能
---
- 指定した期間のiCalendarを出力する

開発環境
---
- Windows 8.1
- Python 3.8.5 x64

必要なもの
---
- Python 3.6以上 64bit版
- 新暦、旧暦変換 qreki.py( https://github.com/fgshun/qreki_py )
    - 導入についてはURL先を参照
- 外部からアクセス可能なWebサーバー(github.ioなど)

使い方
---
1. `rokuyou_icalendar.py` をテキストエディタで開き、下記変数を任意の値に設定(体裁は維持してください)
    - `start_day`
    - `emd_day`
    - `file_name`
1. 任意のディレクトリでこのプログラムを実行( `py rokuyou_icalendar.py` など)
1. 実行した際のディレクトリにファイルが生成されていることを確認( デフォルトは `upat_6Yo_cal.ics` )
1. 上記のファイルをwebサーバー上に配置し、スマートフォン等から照会してください

Screenshots(iOS)
---
![sample1](https://github.com/upat/rokuyou_icalendar/images/sc1.png)
![sample2](https://github.com/upat/rokuyou_icalendar/images/sc2.png)

使用上の注意
---
iOSのカレンダーアプリ(サードパーティ含む)で読めることしか確認していません

参考文献
---
- https://github.com/fgshun/qreki_py
- https://qiita.com/TomOse/items/31b5fb4782f06d19af79
- http://www.asahi-net.or.jp/~ci5m-nmr/iCal/ref.html
- Googleカレンダー

ライセンス
---
MIT Licence
