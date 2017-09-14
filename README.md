チラ裏オタクブログ( http://healuniv.hatenablog.jp )のゴミ実験のために使ったデータとかソースコードとかをまとめました．jupyter notebookとか全然整理してないので訳わからん実行結果残ってたりするけど許してちょんまげ．

## 何が入っているのか？
- csv for alg:学習・テストデータ
   - feature_learn:学習データ（特徴量）
   - preference_learn_notitle:学習データ（嗜好）
   - feature_test: テストデータ（特徴量）
- feature.tsv:過去視聴したアニメに関する制作会社，監督，シリーズ構成の情報
- preference.tsv:過去視聴したアニメの嗜好に関する情報
- feature_autumn2017.csv: 2017年秋アニメに関する制作会社，監督，シリーズ構成の情報
- データ成形プロセス.ipynb:データ成形に使ったコード等まとめ

## 嗜好データに関して
嗜好は1~5の5段階で評価．

## ToDo
- 早く.csvファイルを作る
- アルゴリズムの実装
- 実験
