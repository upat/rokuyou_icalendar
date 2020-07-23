#!/usr/bin/env python3
# coding: UTF-8
import os, datetime
from qreki import Kyureki

### ▽▽▽ユーザー設定▽▽▽ ###
# 出力開始年月日
start_day = '2020-07-22'
# 出力終了年月日
end_day = '2021-12-31'
# 出力ファイル名
file_name = 'upat_6Yo_cal.ics'
### △△△ユーザー設定△△△ ###

# コマンド実行ディレクトリへ出力するファイルパス作成
text_path = os.getcwd() + '\\' + file_name

# 日付型へ変換
start_day_dt = datetime.datetime.strptime( start_day, '%Y-%m-%d' )
end_day_dt = datetime.datetime.strptime( end_day, '%Y-%m-%d' )

# ループカウント用
count_day_dt = start_day_dt
# UID作成用
uid_count = 0

# 開始年月日が終了年月日より前か？
if start_day_dt < end_day_dt:
	# iCalendarの先頭部分を作成
	ical_text = 'BEGIN:VCALENDAR\n' + \
				'PRODID:-//upat//JP\n' + \
				'VERSION:2.0\n' + \
				'CALSCALE:GREGORIAN\n' + \
				'METHOD:PUBLISH\n' + \
				'X-WR-CALNAME:rokuyou calendar by upat\n' + \
				'X-WR-TIMEZONE:Asia/Tokyo\n'

	# ファイルへ出力(新規作成 or 上書き)
	with open( text_path, mode='w', encoding='utf-8' ) as f:
		f.write( ical_text )

	# 指定した出力終了年月日に到達するまでループ
	while count_day_dt <= end_day_dt:
		# 日付型から年月日を数値出力→0埋め→文字列変換
		y_str = str ( '{0:04d}'.format( count_day_dt.year ) )
		m_str = str( '{0:02d}'.format( count_day_dt.month ) )
		d_str = str( '{0:02d}'.format( count_day_dt.day ) )
		
		# 六曜データ取得
		rky = Kyureki.from_ymd( count_day_dt.year, count_day_dt.month, count_day_dt.day )
		
		# イベント終了用の日付型作成(翌日)
		count_nextday_dt = count_day_dt + datetime.timedelta( days=1 )
		ny_str = str ( '{0:04d}'.format( count_nextday_dt.year ) )
		nm_str = str( '{0:02d}'.format( count_nextday_dt.month ) )
		nd_str = str( '{0:02d}'.format( count_nextday_dt.day ) )
		
		# iCalendarのイベント部分を作成
		ical_text = 'BEGIN:VEVENT\n' + \
					'DTSTART;VALUE=DATE:' + y_str + m_str + d_str + '\n' + \
					'DTEND;VALUE=DATE:' + ny_str + nm_str + nd_str + '\n' + \
					'DTSTAMP:' + y_str + '0101T000000Z\n' + \
					'UID:' + str( uid_count ) + '@upat\n' + \
					'CREATED:' + y_str + '0101T000000Z\n' + \
					'DESCRIPTION:\n' + \
					'LAST-MODIFIED:' + y_str + '0101T000000Z\n' + \
					'LOCATION:\n' + \
					'SEQUENCE:0\n' + \
					'STATUS:CONFIRMED\n' + \
					'SUMMARY:' + rky.rokuyou + '\n' + \
					'TRANSP:TRANSPARENT\n' + \
					'END:VEVENT\n'

		# 異なるUID作成のためインクリメント
		uid_count = uid_count + 1

		# 既に作成済みのファイルへ出力(追記)
		if os.path.isfile( text_path ):
			with open( text_path, mode='a', encoding='utf-8' ) as f:
				f.write( ical_text )
		else:
			# ファイルが存在しない
			print( 'file not found.' )
			sys.exit()
		
		# 1日進める
		count_day_dt = count_nextday_dt

	# iCalendarの末尾を作成
	ical_text = 'END:VCALENDAR\n'

	# 既に作成済みのファイルへ出力(追記)
	if os.path.isfile( text_path ):
		with open( text_path, mode='a', encoding='utf-8' ) as f:
			f.write( ical_text )
	else:
		# ファイルが存在しない
		print( 'file not found.' )
		sys.exit()
else:
	# 日時指定が不適切
	print( 'process failed.' )
