# MockHospitalData

This repo contains mock data apis to use with this project.

## Prerequisites

``` bash
pip install -r ./requirements.txt
```

## Usage

0. Put yout assets into `marshmallow/mock_hospital/assets/`.
1. Fire up two terminals.
2. In the first terminal, cd into `cd ./marshmallow/mock_hospital/` and `python ./mock_api.py`.
3. In the second terminal, `python ./main.py`.
4. Send a request to `127.0.0.1:14000/query?doctor_name=` with your name.

![request](./demo_img/request.png)
