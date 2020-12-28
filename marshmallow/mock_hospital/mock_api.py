from flask import Flask, request
from gevent.pywsgi import WSGIServer
import json
from marshmallow.mock_hospital.mock_class import Doctor, Hospital


with open("./marshmallow/mock_hospital/assets/hospital_api.json", encoding='utf8') as mock_hospital_json_str:
    mock_hospital_data = json.loads(mock_hospital_json_str.read())
    doctor_list_dict = []
    mock_hospital_data: dict
    doctor: dict
    for doctor in mock_hospital_data["data"]:
        doctor_list_dict.append(Doctor(doctor).__dict__)
    hospital_all = Hospital(
        mock_hospital_data["hospital_name"],
        mock_hospital_data["hospital_region"],
        doctor_list_dict)

app = Flask(__name__)


@app.route('/query', methods=['GET'])
def get_doctor_list():
    doctor_name = request.args.get('doctor_name')
    return_dict_list = []
    for doctor in mock_hospital_data["data"]:
        this_doctor_name: str
        this_doctor_name = doctor["name"]
        if this_doctor_name.find(doctor_name) != -1:
            return_dict_list.append(Doctor(doctor).__dict__)
    hospital = Hospital(mock_hospital_data["hospital_name"],
                        mock_hospital_data["hospital_region"], return_dict_list)
    return hospital.__dict__


@app.route('/get_all', methods=['GET'])
def get_hospital():
    return json.dumps(hospital_all.__dict__)


@app.route('/exit', methods=['GET'])
def to_exit():
    exit()


def main():
    port_num = 15000
    main_server = WSGIServer(('0.0.0.0', port_num), app)
    print("Mock Source: API\nThe service will serve at {}\n".format(port_num))
    main_server.serve_forever()


if __name__ == '__main__':
    main()
