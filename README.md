# Tweet Translator
Twitter APIとDeepL APIを使用して、ツイートの検索とその翻訳を一画面で行うシンプルなSPA

![](/tweet-translator.gif)

Herokuへのデプロイを想定して実装を行っている（現在はAPIの制限等があるため公開は行っていない）

# root

## Pipfile, Pipfile.lock
使用しているPythonライブラリの管理をpipenvで行うためのファイル。

* Flask: ウェブアプリケーションフレームワーク
* Flask-RESTful: Flask上でREST APIを実装するライブラリ
* Tweepy: Twitter API用のライブラリ
* deepl: DeepL API用のライブラリ
* Gunicorn: WSGIを実装するHTTPサーバーのライブラリ。Flaskをサーバ上で動かす

## Procfile
Herokuでサーバを立てるためにHeroku側で実行するコマンドを指定するファイル。

## requirements.txt
Heroku上にインストールするPythonライブラリのリストを指定するファイル。

## runtime.txt
Herokuで走らせるPythonのバージョンを指定するファイル。

# backend
Pythonで記述。フレームワークにはFlaskを使用。REST APIを実装し、クライアントからのリクエストに応える。

## main.py
サーバ上でアプリを走らせるためのエントリポイントとなるプログラム。

## config.py（未追跡）
APIキー等を管理するモジュール

## myapi
自作のREST APIのモジュールをまとめたパッケージ

## api
外部APIとやり取りするクラスなどをまとめたパッケージ

# frontend
Vue CLIを使ったVue.jsのフロントエンド開発場所。ビルドするとコードをdistディレクトリに展開する。以下のファイルは基本的にVue CLIが自動的に生成するテンプレートが元になっている。

## .browserslistrc
CSSで付与するベンダープレフィクスに関して、サポートするブラウザの範囲を指定するファイル。

## .editorconfig
コーディングスタイルに関する設定ファイル。

## .eslintrc.js
ESLint関連の設定ファイル。

## babel.config.js
Babel関連の設定ファイル。

## package.json, package-lock.json
使用しているJavaScriptライブラリの管理をnpmで行うためのファイル。Vue CLIが自動的に生成するため、今回使用しなかったライブラリも含まれている（VuexやSassなど）。

* Vue.js: UI設計のJavaScriptフレームワーク
* Vuetify: マテリアルデザインに則ったUIデザインのフレームワーク。コンポーネントを提供する
* axios: Ajaxで非同期通信を行うライブラリ
* ESLint: JavaScriptの静的コード分析ツール。保守性の低いコードや危ないコードを指摘してくる
* Babel: JavaScriptトランスコンパイラ。古いJavaScriptの書き方に変換する

## vue.config.js
Vue関連の設定ファイル。

## public
index.htmlやfaviconの配置場所。index.htmlにVueで作成したアプリが展開される。

## src
Vueのソース。main.jsをエントリポイントとし、App.vueとそれに依存するコンポーネントを置く。

# dist
frontendでビルドしたコードを展開する場所。Flaskではここをレスポンスのテンプレートのフォルダとしている。


