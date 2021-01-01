import marshmallow.mock_hospital.mock_db as mock_db
import marshmallow.mock_hospital.mock_xlsx as mock_xlsx
import marshmallow.mock_hospital.mock_api as mock_api
import requests
import json
from flask import Flask, request
from gevent.pywsgi import WSGIServer
import json
from threading import Thread
from flask import Response

app = Flask(__name__)


def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


with open("./marshmallow/mock_hospital/assets/hospitals.json", encoding='utf8') as hospital_list_json:
    mock_hospital_list = json.loads(hospital_list_json.read())


@app.route('/query', methods=['GET'])
def get_doctor_list_by_name():
    response = {
        "data": [],
        "count": -1,
        "success": False,
    }
    try:
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

        for i in result_list:
            if len(i["doctor_list_dict_str"]) != 0:
                response["data"].append(i)
        temp_count = 0
        for i in response["data"]:
            temp_count += len(i["doctor_list_dict_str"])
        response["count"] = temp_count
        response["success"] = True
    except Exception as e:
        print(e.with_traceback)
        response = {
            "data": [],
            "count": -1,
            "success": False,
        }
    return response


@app.route('/query_hospital', methods=['GET'])
def get_hospital_list_by_name():
    response = {
        "data": [],
        "count": -1,
        "success": False,
    }
    need_pagination = False
    pagination_page_size = -1
    pagination_page_num = -1
    query_dict = request.args
    try:
        pagination_page_size = int(query_dict["itemCountOnOnePage"])
        pagination_page_num = int(query_dict["pageIndex"])
        need_pagination = True
    except KeyError:
        pass
    except ValueError:
        # not an int
        return Response(dict({
            "msg": "Invaild pagination request."
        }), status=400)
    try:
        list_to_append = []
        hospital_name = request.args.get('hospital_name')
        for hospital in mock_hospital_list["hospital_list"]:
            this_hospital_name: str
            this_hospital_name = hospital["hosName"]
            if this_hospital_name.find(hospital_name) != -1:
                list_to_append.append(hospital)
        if need_pagination:
            pagination_start = (pagination_page_num - 1) * pagination_page_size
            pagination_end = pagination_page_num * pagination_page_size
            list_to_append = list_to_append[pagination_start:pagination_end]
        response["data"] = list_to_append
        response["count"] = len(response["data"])
        response["success"] = True
    except Exception as e:
        print(e.with_traceback)
        response = {
            "data": [],
            "count": -1,
            "success": False,
        }
        return Response(response, status=500, mimetype='application/json')
    return response


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
