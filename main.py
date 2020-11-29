import marshmallow.mock_hospital.mock_db as mock_db
import marshmallow.mock_hospital.mock_xlsx as mock_xlsx
import marshmallow.mock_hospital.mock_api as mock_api
import requests
import json
from flask import Flask, request
from gevent.pywsgi import WSGIServer
import json
from threading import Thread

app = Flask(__name__)


def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

# print(mock_xlsx.get_all().__dict__)
# print(mock_xlsx.query("大张").__dict__)

# print(mock_db.get_all().__dict__)
# print(mock_db.query("老刘").__dict__)

# r = requests.get("http://127.0.0.1:15000/get_all")
# print(json.loads(r.text))

# r = requests.get("http://127.0.0.1:15000/query?doctor_name=老赵")
# print(json.loads(r.text))


@app.route('/query', methods=['GET'])
def get_doctor_list():
    doctor_name = request.args.get('doctor_name')
    result_list = []
    xlsx_dict = mock_xlsx.query(doctor_name).__dict__
    db_dict = mock_db.query(doctor_name).__dict__
    api_resp = requests.get(
        "http://127.0.0.1:15000/query?doctor_name=" + doctor_name)
    api_dict = json.loads(api_resp.text)
    print(xlsx_dict)
    print(api_dict)
    print(db_dict)
    result_list.append(xlsx_dict)
    result_list.append(api_dict)
    result_list.append(db_dict)
    result = {"data": []}
    for i in result_list:
        if len(i["doctor_list_dict_str"]) != 0:
            result["data"].append(i)
    return result


@app.route('/exit', methods=['GET'])
def to_exit():
    exit()


def main():
    port_num = 14000
    main_server = WSGIServer(('0.0.0.0', port_num), app)
    print("Mock Data:\nThis service will serve at {}\n".format(port_num))
    main_server.serve_forever()


if __name__ == '__main__':
    t = Thread(target=mock_api.main)
    t.start()
    main()
