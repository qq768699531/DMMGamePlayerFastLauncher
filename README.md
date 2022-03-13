# DMMGamePlayerFastLauncher
DMM Game Player のゲームを高速かつセキュアに起動できるランチャー

## 特徴
- **ワンクリックでゲームを起動**
- **管理者権限不要**

## インストール
[Releases](https://github.com/fa0311/DMMGamePlayerFastLauncher/releases) から DMMGamePlayerFastLauncher-Setup.exe をダウンロード<br>
実行してセットアップする

## 使い方
*%AppData%\DMMGamePlayerFastLauncher* にある *DMMGamePlayerFastLauncher.exe* を右クリックしショートカットを作成<br>
作成したショートカットのプロパティのリンク先に *product_id* を追記<br>

例: `%AppData%\DMMGamePlayerFastLauncher\DMMGamePlayerFastLauncher.exe <product_id>`<br>

product_idは存在しないproduct_idが指定された際のエラーにダウンロードされているソフトのproduct_idが表示されるのでそれを参考にして下さい<br>
*%AppData%\DMMGamePlayerFastLauncher\sample* にサンプル用のショートカットを置いています<br>

## 引数
`DMMGamePlayerFastLauncher.exe <product_id>`

| オプション           | エイリアス | デフォルト                                       | 備考                              | タイプ |
|----------------------|------------|--------------------------------------------------|-----------------------------------|--------|
| --help               | -h         | False                                            |                                   | bool   |
| --game-path          |            | False                                            | Falseにすると自動                 |        |
| --dmmgameplayer-path | -dgp-path  | C:/Program Files/DMMGamePlayer/DMMGamePlayer.exe |                                   |        |
| --non-kill           |            | False                                            | DMMGamePlayerが起動したままになる | bool   |
| --debug              |            | False                                            | デバッグモード                    | bool   |
| --login-force        |            | False                                            | ログインを強制する                | bool   |

## ヘルプ

> **セットアップする際、WindowsによってPCが保護されましたと表示される**<br>
> 詳細情報をクリックして実行をクリック

> **ゲームのアイコンに寄せたい**<br>
> ショートカットを右クリック→プロパティ→アイコンの変更→参照

> **アンインストールしたい**<br>
> `%AppData%\DMMGamePlayerFastLauncher` の `unins000.exe` を実行


## 典拠
[Lutwidse/priconner_launch.py](https://gist.github.com/Lutwidse/82d8e7a20c96296bc0318f1cb6bf26ee)

## ライセンス
DMMGamePlayerFastLauncher is under MIT License