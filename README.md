# File_Manipulator
指定したファイルの内容を読み込み、変更・複製・置き換え等をした新しいファイルを作成する。
## 機能とコマンド
・文字のレバース　`reverse`（新しいファイルを作成）
  例）hello ⇒　olleh

・ファイルのコピー　`copy`（新しいファイルの作成）

・指定ファイルの文字列を指定数だけ繰り返して変更を加える。　`duplicate-contents`　(新しいファイルを作成)

・文字の置き換え　`replace-string`　（ファイル内容の変更）
　例）　hello world ⇒　good world
 
・マークダウンファイルからhtmlファイルへの変換　`markdown`（新しいファイルを作成）
  例）　test.md ⇒ test.html

## コマンドごとの使用方
リバースコマンド（reverse）<br />
python3 file_manipulator.py reverse ファイル名 新しいファイル名
<br />例）`python3 file_manipulator.py reverse test1.txt test2.txt`

コピーコマンド（copy）<br />
python3 file_manipulator.py copy ファイル名 新しいファイル名
<br />例）`python3 file_manipulator.py copy test1.txt test2.txt`

繰り返しコマンド（duplicate-contents）<br />
python3 file_manipulator.py duplicate-contents ファイル名 繰り返し回数
<br />例）`python3 file_manipulator.py duplicate-contents test1.txt 3`

文字置き換えコマンド（replace-string）<br />
python3 file_manipulator.py replace-string ファイル名 置き換え前の文字 置き換え後の文字
<br />例）`python3 file_manipulator.py repalce-string test1 hello good`

マークダウンファイルからhtmlファイルへの変換（markdown）<br />
python3 file_manipulator.py markdown ファイル名 新しいhtmlファイル名
<br />例）`python3 file_manipulator.py markdown test.md test.htmle`



