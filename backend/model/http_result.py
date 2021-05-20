from flask import jsonify


class HttpResult():

    @classmethod
    def success_result(cls, data):
        response = dict()
        response['data'] = data
        response['success'] = True
        response['code'] = 1
        return jsonify(response)

    @classmethod
    def error_result(cls):
        response = dict()
        response['data'] = None
        response['success'] = False
        response['code'] = -1
        return jsonify(response)
