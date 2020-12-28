import pandas as pd
from marshmallow.mock_hospital.mock_class import Doctor, Hospital


hospital_name = "医院A"
hospital_region = "上海"
xlsx_name = hospital_name + "_" + hospital_region + ".xlsx"

df = pd.read_excel("./marshmallow/mock_hospital/assets/" + xlsx_name)
df_all = df.to_dict('records')
doctor_list_dict = []
for doctor_tuple in df_all:
    doctor_list_dict.append(Doctor(doctor_tuple).__dict__)
hospital_all = Hospital(
    hospital_name,
    hospital_region,
    doctor_list_dict)


def get_all() -> Hospital:
    return hospital_all


def query(doctor_name: str) -> Hospital:
    df_searched = df.loc[df['name'].isin].to_dict('records')
    doctor_list_dict = []
    for doctor_tuple in df_searched:
        doctor_list_dict.append(Doctor(doctor_tuple).__dict__)
    hospital = Hospital(
        hospital_name,
        hospital_region,
        doctor_list_dict)
    return hospital
