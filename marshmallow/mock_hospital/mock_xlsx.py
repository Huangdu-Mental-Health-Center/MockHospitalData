import pandas as pd
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


hospital_name = "医院A"
hospital_region = "上海"
xlsx_name = hospital_name + "_" + hospital_region + ".xlsx"

df = pd.read_excel("./marshmallow/mock_hospital/assets/" + xlsx_name)
df_all = df.to_dict('records')
docker_list_dict = []
for doctor_tuple in df_all:
    docker_list_dict.append(Doctor(doctor_tuple).__dict__)
hospital_all = Hospital(
    hospital_name,
    hospital_region,
    docker_list_dict)


def get_all() -> Hospital:
    return hospital_all


def query(doctor_name: str) -> Hospital:
    df_searched = df.loc[df['name'] == doctor_name].to_dict('records')
    docker_list_dict = []
    for doctor_tuple in df_searched:
        docker_list_dict.append(Doctor(doctor_tuple).__dict__)
    hospital = Hospital(
        hospital_name,
        hospital_region,
        docker_list_dict)
    return hospital
