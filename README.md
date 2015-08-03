Usage
-----

基本的には crontab を使って OS (uso) 起動時に, `./auto_reboot.sh` を実効している.

1. 温度データを取得する. 取得したデータは同じ階層の `data/` に保存される.

        $ ./logger.sh
		
2. logger.sh がエラー終了した際に, 10 分後に再起動する.

        $ ./restart.sh ./logger.sh
