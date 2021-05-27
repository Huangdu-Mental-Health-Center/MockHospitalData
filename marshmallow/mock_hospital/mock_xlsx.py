import pandas as pd
from marshmallow.mock_hospital.mock_class import Doctor, Hospital


hospital_name = "医院A"
hospital_region = "上海"
xlsx_name = hospital_name + "_" + hospital_region + ".xlsx"

df = pd.read_excel("./marshmallow/mock_hospital/assets/" + xlsx_name, engine='openpyxl')
df_all = df.to_dict('records')
doctor_list_dict = []
for doctor_tuple in df_all:
    doctor_list_dict.append(Doctor(doctor_tuple, hospital_name, hospital_region).__dict__)
hospital_all = Hospital(
    hospital_name,
    hospital_region,
    doctor_list_dict)


def get_all() -> Hospital:
    return hospital_all


def query(doctor_name: str) -> Hospital:
    temp_doctor_list_dict = []
    doctor: Doctor
    for doctor in doctor_list_dict:
        if doctor["name"].find(doctor_name) != -1:
            temp_doctor_list_dict.append(Doctor(doctor, hospital_name, hospital_region).__dict__)
    hospital = Hospital(
        hospital_name,
        hospital_region,
        temp_doctor_list_dict)
    return hospital
