from flask import Flask, render_template
from myapi import search_tweets_bp, deepl_translate_bp


app = Flask(__name__, static_folder='../dist/static', template_folder='../dist')

# 独自APIの機能は分割して実装し、myapiパッケージとしてまとめる
# 各独自APIのBlueprintをアプリに登録
app.register_blueprint(search_tweets_bp)
app.register_blueprint(deepl_translate_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
