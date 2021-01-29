import base64
import datetime
import requests
import sys
import time
import traceback


def send(data, retries=1):
    if retries <= 5:
        username = "api_send2"
        password = "Qwerty123!"
        base64string = (
            base64.encodebytes(("{0}:{1}".format(username, password)).encode())
            .decode()
            .replace("\n", "")
        )
        pnet_api = "http://10.29.140.106:80/bppmws/api/Event/create?routingId=sks06sr001.ks.rt.ru&routingIdType=SERVER_NAME"
        headers = {
            "Authorization": "basic {}".format(base64string),
            "Content-Type": "application/json",
        }
        with requests.Session() as session:
            try:
                response = session.post(
                    url=pnet_api, headers=headers, json=data, verify=False
                )
                status = response.status_code == 200
            except:
                status = False
                retries += 1
                time.sleep(300)
                send(data, retries)
        return status
    else:
        sys.exit(1)


def make_event(data, retry=False, retry_filename=""):
    escalation_cancelled = False
    if "NOTE: Escalation cancelled" in data:
        data = "\n".join(data.split("\n")[1:])
        escalation_cancelled = True
    info = data.split("[_____]")
    tags = {
        tag.split(":")[0]: tag.split(":")[1]
        for tag in info[1].split(", ")
        if ":" in tag
    }
    params = {s.split("[_]")[0]: s.split("[_]")[1] for s in info[0].split("[___]")}
    # params['msg'] = 'Вы можете динамически изменять параметры в теле скрипта'
    # params['severity'] = 'CRITICAL'
    params["date_reception"] = datetime.datetime.now().timetuple()
    params["date_reception"] = int(time.mktime(params["date_reception"]))
    params["severity"] = (
        severity_map[params["severity"]] if not escalation_cancelled else "OK"
    )
    params_send = send([{"attributes": params}])
    return params_send


if __name__ == "__main__":
    severity_map = {
        "OK": "OK",
        "INFO": "INFO",
        "WARNING": "WARNING",
        "MINOR": "MINOR",
        "MAJOR": "MAJOR",
        "CRITICAL": "CRITICAL",
    }
    with open(
        "C:/Users/Aleksandr.Vishnyakov/Desktop/Integration Script/command.txt"
    ) as fin:
        data = fin.readline()
        try:
            make_event(data)
        except:
            msg = f"Could not get params: 4\n{traceback.format_exc()}"
