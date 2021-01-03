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

with open("./marshmallow/mock_hospital/assets/hospital_departments.json", encoding='utf8') as hospital_department_list_json:
    mock_hospital_department_list = json.loads(
        hospital_department_list_json.read())


@app.route('/query', methods=['GET'])
def get_doctor_list_by_name():
    response = {
        "data": [],
        "count": -1,
        "success": False,
        "totalPage": 1
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
        doctor_name = request.args.get('doctor_name')
        doctor_name_filter_enabled = True if doctor_name else False
        department_name = request.args.get('department_name')
        department_name_filter_enabled = True if department_name else False
        hospital_name = request.args.get('hospital_name')
        hospital_name_filter_enabled = True if hospital_name else False
        region_name = request.args.get('region_name')
        region_name_filter_enabled = True if region_name else False

        result_list = []
        xlsx_dict = mock_xlsx.get_all().__dict__
        db_dict = mock_db.get_all().__dict__
        api_resp = requests.get(
            "http://127.0.0.1:15000/get_all")
        api_dict = json.loads(api_resp.text)
        all_result = xlsx_dict["doctor_list_dict_str"] + \
            api_dict["doctor_list_dict_str"] + db_dict["doctor_list_dict_str"]
        result_list = all_result
        if doctor_name_filter_enabled:
            temp_list = []
            for doctor in result_list:
                if doctor["name"].find(doctor_name) != -1:
                    temp_list.append(doctor)
            result_list = temp_list
        if department_name_filter_enabled:
            temp_list = []
            for doctor in result_list:
                if doctor["department"] == department_name:
                    temp_list.append(doctor)
            result_list = temp_list
        if hospital_name_filter_enabled:
            temp_list = []
            for doctor in result_list:
                if doctor["hospital_name"] == hospital_name:
                    temp_list.append(doctor)
            result_list = temp_list
        if region_name_filter_enabled:
            temp_list = []
            for doctor in result_list:
                if doctor["hospital_region"] == region_name:
                    temp_list.append(doctor)
            result_list = temp_list
        total_count = len(result_list)
        if need_pagination:
            pagination_start = (pagination_page_num - 1) * pagination_page_size
            pagination_end = pagination_page_num * pagination_page_size
            result_list = result_list[pagination_start:pagination_end]
            response["totalPage"] = (total_count // pagination_page_size) + 1
        response["data"] = result_list
        response["count"] = total_count
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
        "totalPage": 1
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
        total_count = len(list_to_append)
        if need_pagination:
            pagination_start = (pagination_page_num - 1) * pagination_page_size
            pagination_end = pagination_page_num * pagination_page_size
            list_to_append = list_to_append[pagination_start:pagination_end]
            response["totalPage"] = (total_count // pagination_page_size) + 1
        response["data"] = list_to_append
        response["count"] = total_count
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


@app.route('/query_hospital_department', methods=['GET'])
def get_hospital_department_list_by_name():
    response = {
        "data": [],
        "count": -1,
        "success": False,
        "totalPage": 1
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
        for hospital in mock_hospital_department_list["hospital_department_list"]:
            this_hospital_name: str
            this_hospital_name = hospital["hosName"]
            if this_hospital_name.find(hospital_name) != -1:
                list_to_append.append(hospital)
        total_count = len(list_to_append)
        if need_pagination:
            pagination_start = (pagination_page_num - 1) * pagination_page_size
            pagination_end = pagination_page_num * pagination_page_size
            list_to_append = list_to_append[pagination_start:pagination_end]
            response["totalPage"] = (total_count // pagination_page_size) + 1
        response["data"] = list_to_append
        response["count"] = total_count
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
