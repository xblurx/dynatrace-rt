#### Create venv:
`python3 -m venv venv`
#### Copy env flask app variable:
`export FLASK_APP=/opt/pnet_skk_integration/dynatrace-rt/webhook_listener.py`
#### Collect dependencies in wheels folder:
`pip wheel -r requirements.txt  --wheel-dir ./wheel`