#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import base64
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

with open("config/config.yaml") as fin:
    config = yaml.safe_load(fin)


def make_pnet_request(payload):
    url = config["pnet_api"]["url"]
    username = config["pnet_api"]["username"]
    password = config["pnet_api"]["password"]
    base64string = (
        base64.encodebytes(f"{username}:{password}".encode()).decode().strip()
    )
    headers = {
        "Authorization": f"basic {base64string}",
        "Content-Type": "application/json",
    }
    session = requests.Session()
    retries = Retry(
        total=5, backoff_factor=0.1, status_forcelist=[403, 500, 502, 503, 504]
    )
    session.mount("http://", HTTPAdapter(max_retries=retries))
    try:
        response = session.post(url=url, headers=headers, json=payload, verify=False)
        return response.status_code
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def make_skk_request(payload):
    # do something
    pass
