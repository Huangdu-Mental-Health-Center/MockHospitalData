import unittest

# from marshmallow.mock_hospital.mock_class import Doctor, Hospital
# from marshmallow.mock_hospital.mock_xlsx import query as xlsx_query
# from marshmallow.mock_hospital.mock_api import get_doctor_list as api_query


class Test_testQuerytest(unittest.TestCase):

    def test_db_single_query_if_success(self):
        from marshmallow.mock_hospital.mock_db import query as db_query
        hospital_result = db_query("老刘")
        print(hospital_result.doctor_list_dict_str)
        self.assertTrue(len(hospital_result.doctor_list_dict_str) == 1)

    def test_db_multi_query_if_success(self):
        from marshmallow.mock_hospital.mock_db import query as db_query
        hospital_result = db_query("王")
        print(hospital_result.doctor_list_dict_str)
        self.assertTrue(len(hospital_result.doctor_list_dict_str) == 2)

    def test_db_query_if_no_match(self):
        from marshmallow.mock_hospital.mock_db import query as db_query
        hospital_result = db_query("114514")
        print(hospital_result.doctor_list_dict_str)
        self.assertTrue(len(hospital_result.doctor_list_dict_str) == 0)

    def test_xlsx_multi_query_if_success(self):
        from marshmallow.mock_hospital.mock_xlsx import query as xlsx_query
        hospital_result = xlsx_query("大")
        print(hospital_result.doctor_list_dict_str)
        self.assertTrue(len(hospital_result.doctor_list_dict_str) == 3)

    def test_xlsx_single_query_if_success(self):
        from marshmallow.mock_hospital.mock_xlsx import query as xlsx_query
        hospital_result = xlsx_query("大楹")
        print(hospital_result.doctor_list_dict_str)
        self.assertTrue(len(hospital_result.doctor_list_dict_str) == 1)

    def test_xlsx_query_if_no_match(self):
        from marshmallow.mock_hospital.mock_xlsx import query as xlsx_query
        hospital_result = xlsx_query("114514")
        print(hospital_result.doctor_list_dict_str)
        self.assertTrue(len(hospital_result.doctor_list_dict_str) == 0)

    def test_api_single_query_if_success(self):
        from marshmallow.mock_hospital.mock_api import query as api_query
        hospital_result = api_query("老邓")
        print(hospital_result.doctor_list_dict_str)
        self.assertTrue(len(hospital_result.doctor_list_dict_str) == 1)

    def test_api_multi_query_if_success(self):
        from marshmallow.mock_hospital.mock_api import query as api_query
        hospital_result = api_query("小")
        print(hospital_result.doctor_list_dict_str)
        self.assertTrue(len(hospital_result.doctor_list_dict_str) == 3)

    def test_api_single_query_if_no_match(self):
        from marshmallow.mock_hospital.mock_api import query as api_query
        hospital_result = api_query("114514")
        print(hospital_result.doctor_list_dict_str)
        self.assertTrue(len(hospital_result.doctor_list_dict_str) == 0)

if __name__ == '__main__':
    unittest.main()
