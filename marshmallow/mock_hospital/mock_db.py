import sqlite3
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


hospital_name = "医院C"
hospital_region = "北京"
db_name = hospital_name + "_" + hospital_region + ".db"
conn = sqlite3.connect("./marshmallow/mock_hospital/assets/" + db_name)
c = conn.cursor()
c.execute('SELECT * FROM doctor')
result = c.fetchall()
conn.close()
docker_list_dict = []
for doctor_tuple in result:
    docker_list_dict.append(Doctor(doctor_tuple).__dict__)
hospital_all = Hospital(
    hospital_name,
    hospital_region,
    docker_list_dict)


def query(doctor_name: str) -> Hospital:
    conn = sqlite3.connect("./marshmallow/mock_hospital/assets/" + db_name)
    c = conn.cursor()
    query = (doctor_name,)
    c.execute('SELECT * FROM doctor WHERE name=?', query)
    result = c.fetchall()
    conn.close()
    docker_list_dict = []
    for doctor_tuple in result:
        docker_list_dict.append(Doctor(doctor_tuple).__dict__)
    hospital = Hospital(
        hospital_name,
        hospital_region,
        docker_list_dict)
    return hospital


def get_all() -> Hospital:
    return hospital_all


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
