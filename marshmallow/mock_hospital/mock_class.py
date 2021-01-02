from typing import List, Union


class Doctor:
    def __init__(self, name: str, department: str, professional_title: str, intro: str, expert_in: str, hospital_name: str, hospital_region: str):
        self.name = name
        self.department = department
        self.professional_title = professional_title
        self.intro = intro
        self.expert_in = expert_in
        self.hospital_name = hospital_name
        self.hospital_region = hospital_region

    def __init__(self, doctor: Union[dict, tuple], hospital_name: str, hospital_region: str):
        if type(doctor) == dict:
            self.name = doctor["name"]
            self.department = doctor["department"]
            self.professional_title = doctor["professional_title"]
            self.intro = doctor["intro"]
            self.expert_in = doctor["expert_in"]
            self.hospital_name = hospital_name
            self.hospital_region = hospital_region
        elif type(doctor) == tuple:
            self.name = doctor[0]
            self.department = doctor[1]
            self.professional_title = doctor[2]
            self.intro = doctor[3]
            self.expert_in = doctor[4]
            self.hospital_name = hospital_name
            self.hospital_region = hospital_region
        else:
            raise Exception


class Hospital:
    def __init__(self, hospital_name: str, hospital_region: str, doctor_list_dict_str: List[str]):
        self.hospital_name = hospital_name
        self.hospital_region = hospital_region
        self.doctor_list_dict_str = doctor_list_dict_str
