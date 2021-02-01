#### Create venv:
`python3 -m venv venv`
#### Install dependencies:
`pip install -r requirements.txt`
#### Copy env flask app variable:
`export FLASK_APP=/opt/pnet_skk_integration/dynatrace-rt/webhook_listener.py`
#### Collect dependencies in wheels folder:
`pip wheel -r requirements.txt  --wheel-dir ./wheel`
