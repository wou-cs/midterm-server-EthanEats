from flask import Flask, request


app = Flask(__name__)


@app.route("/api/calcs/<num>", methods=["GET"])
def calcs(num):
    try:
        num = int(num)
        if num < 1:
            return '{"Error": "Integer is non-positive"}', 404, {'Content-Type': 'application/json'}

        h = hex(num)
        d = num - 1

        return f'{{ "hex" : "{h}", "dec" : {d}}}', 200, {'Content-Type': 'application/json'}   


    except:
        return '{"Error": "Integer is invalid"}', 400, {'Content-Type': 'application/json'}

