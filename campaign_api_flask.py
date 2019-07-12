from flask import Flask, jsonify
from flask.wrappers import Response
from flask.globals import request
from werkzeug.wrappers import ETagRequestMixin, ETagResponseMixin, BaseRequest, BaseResponse

from Manager.manager import Manager
from Reporter.Reporter import Reporter

app = Flask(__name__)


class Response(BaseResponse, ETagResponseMixin):
    pass


class Request(BaseRequest, ETagRequestMixin):
    pass


def checkForm(json):
    keys = json.keys()
    return ('email' in keys and "hashtags" in keys and "mentions" in keys and "startDate" in keys and "endDate" in keys)


# Goes from guinated string to list
def fixCampaing(c):
    c.hashtags = c.hashtags.split("-")
    c.mentions = c.mentions.split("-")
    return c


# -------------------------- manager flask ------------------------------

@app.route('/Campaing', methods=['POST', 'DELETE'])
def api_manager():
    if request.method == 'POST' and 'application/json' == request.headers['Content-Type']:
        if checkForm(request.json):
            idCampaign = Manager().insertCampaign(request.get_json())
            res = Response(status=201)
            res.set_etag(str(idCampaign), weak=False)
            return res
        else:
            return Response(status=412)

    elif request.method == 'DELETE':
        if 'idC' in request.json.keys():
            res = Manager().deleteCampaignporid(request.json['idC'])
            return Response(status=res)
        elif 'email' in request.json.keys():
            res = Manager().deleteCampaignporuser(request.json['email'])
            return Response(status=res)
    else:
        return Response(status=400)


@app.route('/Campaing/<int:idC>', methods=['GET', 'PATCH'])
def api_manager_id(idC):
    if request.method == 'GET':
        campaign = Manager().returnCampaign(idC)
        return (Response(status=404) if campaign == [] else jsonify(fixCampaing(campaign).to_json()))

    elif request.method == 'PATCH':
        if ('columnaAModif' in request.json.keys()) and ('campoColumna' in request.json.keys()):
            res = Manager().modifyCampaign(idC, request.json['columnaAModif'], request.json['campoColumna'])
            return Response(status=res)
        else:
            return Response(status=400)
    else:
        return Response(status=404)


# -------------------------- reporter flask ------------------------------

@app.route('/Reporter/ReporterJSON/<int:idC>', methods=['GET'])
def api_report_json(idC):
    summary = Reporter().reportSummary(idC)
    if summary == 404:
        return Response(status=404)
    elif summary == 412:
        return Response(status=412)
    return jsonify(summary)


@app.route('/Reporter/ReporterRAW/<int:idC>', methods=['GET'])
def api_report_raw(idC):
    data = Reporter().reportRawData(idC)
    if data == 404:
        return Response(status=404)
    elif data == 412:
        return Response(status=412)
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
