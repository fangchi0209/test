from flask_testing import TestCase
from flask import request, Flask, jsonify
import unittest


class demo(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config["TESTING"] = True

        @app.route("/name", methods=["POST"])
        def name():
            data  = request.get_json()
            check = data["name"]

            if check == "Anna":
                return jsonify({
                    "ok": True
                })
            return jsonify({
                "erro": True
            }),400

        return app

    def test_name(self):
        response = self.client.post("/name", json={"name": "Anna"})

        self.assert200(response)

unittest.main()



