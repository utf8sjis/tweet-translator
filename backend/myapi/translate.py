from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

from api import DeeplAPI, get_keys


class DeeplTranslate(Resource):
    """
    リクエストのパラメータをもとにDeepLのAPIを叩き、
    取得した情報を整形して返す独自のAPI。
    DeepLのAPIは自作のapiパッケージのモジュールから
    DeeplAPIクラスをインポートして使っている
    """
    def post(self):
        input_data = request.json

        config = get_keys()
        deepl_api = DeeplAPI(config['DEEPL_API_KEY'])

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
