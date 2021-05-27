# 这是什么

用于应付 SOA 大项目中教师的模拟医院数据来源要求而编写的模拟数据来源和信息整合系统。

## 目录结构

``` text
│   .gitignore
│   main.py                                         描述此系统对从不同来源的数据整合的过程，提供查询接口。
│   README.md
│   requirements.txt
│   stop_service.py
│
├───demo_img
│       request.png
│
├───doc
│       desciption.md
│
└───marshmallow
    └───mock_hospital
        │   mock_api.py                              模拟调用医院提供的 Web API 的过程
        │   mock_class.py                            模拟时使用的医院和医生类
        │   mock_db.py                               模拟调用医院只读数据库的过程
        │   mock_xlsx.py                             模拟调用医院提供的 Excel 表格的过程
        │
        ├───assets                                   模拟数据来源，源码树中未提供
        │       hospital_api.json                    模拟医院提供的 Web API 的数据
        │       医院A_上海.xlsx                       模拟医院提供的 Excel 表格的数据
        │       医院C_北京.db                         模拟医院提供的只读数据库
        │       医院C_北京.db                         模拟医院提供的只读数据库
        │       hospital_departments.json            模拟各个医院的科室列表
        │       hospitals.json                       模拟医院列表
        │
        ├───tool
                generate_hospital_sqlite.py         生成数据库的代码，源码树中未提供

```

## 按照姓名查询医生

### 载点

`/query`

### 参数

* `doctor_name`: 查询医生姓名

### 返回数据格式

可以概括为

```json
{
    "count": **,
    "success": *******,
    "data":[
        {
            ...
        },
        ...
    ]
}
```

### 样例

```json
// doctor_name:小王
{
    "count": 2,
    "data": [
        {
            "department": "心血管内科",
            "expert_in": "擅长冠心病、高血压、心律失常、心功能不全、高脂血症以及慢性疾病管理。",
            "hospital_name": "医院A",
            "hospital_region": "上海",
            "intro": "主持国家自然科学基金面上项目1项、省部级科研课题3项，参与国家及省部级科研课题10余项。",
            "name": "小王",
            "professional_title": "主治医师"
        },
        {
            "department": "呼吸内科",
            "expert_in": "擅长呼吸危重症的救治以及慢性气道疾病（哮喘、慢阻肺）、淋巴管平滑肌瘤病的诊治。",
            "hospital_name": "医院C",
            "hospital_region": "北京",
            "intro": "医院C呼吸与危重症医学科副主任医师。 ",
            "name": "小王",
            "professional_title": "副主任医师"
        }
    ],
    "success": true,
    "totalPage": 1
}
```

```json
// doctor_name:小
// hospital_name:医院A
{
    "count": 4,
    "data": [
        {
            "department": "心血管内科",
            "expert_in": "擅长冠心病、高血压、心律失常、心功能不全、高脂血症以及慢性疾病管理。",
            "hospital_name": "医院A",
            "hospital_region": "上海",
            "intro": "主持国家自然科学基金面上项目1项、省部级科研课题3项，参与国家及省部级科研课题10余项。",
            "name": "小王",
            "professional_title": "主治医师"
        },
        {
            "department": "心血管外科",
            "expert_in": "擅长心胸外科常见病、多发病的诊治，尤其在微创心胸外科手术和围手术期重症监护领域具有突出的技术优势及专业特长。",
            "hospital_name": "医院A",
            "hospital_region": "上海",
            "intro": "发表论文30余篇，其中以第一及通讯作者发表SCI论文4篇，参编参译专著2部。",
            "name": "小崔",
            "professional_title": "主治医师"
        },
        {
            "department": "心血管外科",
            "expert_in": "以冠心病介入及中西医结合治疗为主要专业特色，在业内率先探索针刺麻醉与心血管介入相结合。",
            "hospital_name": "医院A",
            "hospital_region": "上海",
            "intro": "中国医师协会中西医结合医师分会心血管病学专业委员会秘书长及全国多个学会常务委员。",
            "name": "小曾",
            "professional_title": "主治医师"
        },
        {
            "department": "神经内科",
            "expert_in": "中西医结合卒中救治、记忆障碍、顽固性头痛头晕失眠、运动神经元病、疑难杂症的诊治。",
            "hospital_name": "医院A",
            "hospital_region": "上海",
            "intro": "神经内科行政主任，医学博士，主任医师，留美学者，博士生导师。",
            "name": "小邓",
            "professional_title": "主任医师"
        }
    ],
    "success": true,
    "totalPage": 1
}
```

## 按照名字模糊查询医院

### 载点

`/query_hospital`

### 参数

* `hospital_name`: 医院名字

### 返回样例

```json
{
    "count": 1,
    "data": [
        {
            "hosIntro": "医院 B，是中华人民共和国一家跨国企业控股医院，也是中国大陆规模最大的互联网医院。",
            "hosName": "医院 B",
            "hosPic": "https://static.leiphone.com/uploads/new/article/740_740/201708/598fc025a6ccf.jpg",
            "hosType": "二级乙等",
            "position": "上海市田林路 397 号腾云大厦",
            "telephone": "86-21-54569512"
        }
    ],
    "success": true
}
```