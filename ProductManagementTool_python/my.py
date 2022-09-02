import logging


#ロガーの生成
logger = logging.getLogger('mylog')

#出力レベルの設定
logger.setLevel(logging.DEBUG)

#ハンドラの設定
handler = logging.FileHandler('./logs/logfile.log')

#フォーマッタの生成
fmt = logging.Formatter('%(asctime)s%(message)s')
handler.setFormatter(fmt)

#ハンドラをloggerに追加
logger.addHandler(handler)

debug_msg = 'debug message'
error_msg = 'error_message'

def main():
    logger.debug('[START] My System Start')
    print('[SUCCESS] py -m  myproject')