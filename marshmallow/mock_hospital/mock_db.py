import sqlite3
from marshmallow.mock_hospital.mock_class import Doctor, Hospital


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
