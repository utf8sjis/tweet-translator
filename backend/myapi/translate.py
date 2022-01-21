from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

import config
from api import DeeplAPI


class DeeplTranslate(Resource):
    """
    メソッド: POST, URI: /api/translate
    ツイート文と目的言語のデータをもとにDeepLのAPIにアクセスして翻訳を行い、
    取得した翻訳データから訳文を抜き出して返す独自のAPI
    DeepLのAPIは自作のapiパッケージのモジュールから
    DeeplAPIクラスをインポートして使っている
    """
    def post(self):
        input_data = request.json

        deepl_api = DeeplAPI(config.DEEPL_API_KEY)

        translated_text = deepl_api.translate(
            input_data['tweetText'],
            input_data['translateLang'])
        result_data = {
            'text': translated_text
        }

        return jsonify(result_data)

deepl_translate_bp = Blueprint(
    'deepl_translate', __name__, url_prefix='/api/translate')
deepl_translate = Api(deepl_translate_bp)
deepl_translate.add_resource(DeeplTranslate, '')
