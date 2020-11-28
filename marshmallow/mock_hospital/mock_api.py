from json import encoder
from flask import Flask, request, Response
import random
from gevent.pywsgi import WSGIServer
import json
from typing import List, Union


class Doctor:
    def __init__(self, name: str, department: str, professional_title: str, intro: str, expert_in: str):
        self.name = name
        self.department = department
        self.professional_title = professional_title
        self.intro = intro
        self.expert_in = expert_in

    def __init__(self, doctor: Union[dict, tuple]):
        if type(doctor) == dict:
            self.name = doctor["name"]
            self.department = doctor["department"]
            self.professional_title = doctor["professional_title"]
            self.intro = doctor["intro"]
            self.expert_in = doctor["expert_in"]
        elif type(doctor) == tuple:
            self.name = doctor[0]
            self.department = doctor[1]
            self.professional_title = doctor[2]
            self.intro = doctor[3]
            self.expert_in = doctor[4]
        else:
            raise Exception


class Hospital:
    def __init__(self, hospital_name: str, hospital_region: str, doctor_list_dict_str: List[str]):
        self.hospital_name = hospital_name
        self.hospital_region = hospital_region
        self.doctor_list_dict_str = doctor_list_dict_str


with open("./assets/hospital_api.json", encoding='utf8') as mock_hospital_json_str:
    mock_hospital_data = json.loads(mock_hospital_json_str.read())
    docker_list_dict = []
    mock_hospital_data: dict
    doctor: dict
    for doctor in mock_hospital_data["data"]:
        docker_list_dict.append(Doctor(doctor).__dict__)
    hospital_all = Hospital(
        mock_hospital_data["hospital_name"],
        mock_hospital_data["hospital_region"],
        docker_list_dict)

app = Flask(__name__)


@app.route('/query', methods=['GET'])
def get_doctor_list():
    doctor_name = request.args.get('doctor_name')
    return_dict_list = []
    for doctor in mock_hospital_data["data"]:
        if doctor["name"] == doctor_name:
            return_dict_list.append(Doctor(doctor).__dict__)
    hospital = Hospital(mock_hospital_data["hospital_name"],
                        mock_hospital_data["hospital_region"], return_dict_list)
    return hospital.__dict__


@app.route('/get_all', methods=['GET'])
def get_hospital():
    return json.dumps(hospital_all.__dict__)


def main():
    port_num = 15000
    main_server = WSGIServer(('0.0.0.0', port_num), app)
    print("Will serve at {}".format(port_num))
    main_server.serve_forever()


if __name__ == '__main__':
    main()
