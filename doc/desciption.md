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
    "data":[                                            // 按医院分组
        {
            "doctor_list_dict_str": [                   // 医院下医生信息数组
                {
                    "department": "******",
                    "expert_in": "******",
                    "intro": "****",
                    "name": "****",
                    "professional_title": "********"
                },
                ...
            ],
            "hospital_name": "**",                      // 医院信息 -- 医院名称
            "hospital_region": "**"                     // 医院信息 -- 医院地区
        },
        ...
    ]
}
```

### 样例

以医院为单位。

```json
{
    "count": 2,
    "success": true,
    "data": [
        {
            "doctor_list_dict_str": [
                {
                    "department": "心血管内科",
                    "expert_in": "擅长冠心病、高血压、心律失常、心功能不全、高脂血症以及慢性疾病管理。",
                    "intro": "rrrr",
                    "name": "小王",
                    "professional_title": "主治医师"
                }
            ],
            "hospital_name": "医院A",
            "hospital_region": "上海"
        },
        {
            "doctor_list_dict_str": [
                {
                    "department": "呼吸内科",
                    "expert_in": "gggg",
                    "intro": "gg",
                    "name": "小王",
                    "professional_title": "住院医师"
                }
            ],
            "hospital_name": "医院C",
            "hospital_region": "北京"
        }
    ]
}
```

一个医院重名的在一个医院下。

```json
{
    "count": 2,
    "success": true,
    "data": [
        {
            "doctor_list_dict_str": [
                {
                    "department": "超声诊断科",
                    "expert_in": "从事超声工作20余年，在腹部超声；甲状腺、乳腺等浅表超声；盆腔超声；颈部血管及下肢血管超声；心脏超声；介入超声诊治方面有着丰富的经验。",
                    "intro": "pppp",
                    "name": "大张",
                    "professional_title": "主任医师"
                },
                {
                    "department": "心血管外科",
                    "expert_in": "不擅长心胸外科常见病、多发病的诊治，尤其在微创心胸外科手术和围手术期重症监护领域具有突出的技术优势及专业特长。",
                    "intro": "tttt",
                    "name": "大张",
                    "professional_title": "住院医师"
                }
            ],
            "hospital_name": "医院A",
            "hospital_region": "上海"
        }
    ]
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