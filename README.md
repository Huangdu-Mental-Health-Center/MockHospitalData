# MockHospitalData

This repo contains mock data apis to use with this project.

* Test data available at `./marshmallow/mock_hospital/assets`.

## Prerequisites

``` bash
pip install -r ./requirements.txt
```

## Usage

0. Put yout assets into `./marshmallow/mock_hospital/assets/`.
1. Fire up a terminal.
2. Run `python ./main.py` to bring up the service.
3. Send a request to `127.0.0.1:14000/query?doctor_name=` with your name.
4. If you want to exit, run `python ./stop_service.py` in another terminal.

![request](./demo_img/request.png)
