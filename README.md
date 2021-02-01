copy env flask app variable:  
`export FLASK_APP=/opt/pnet_skk_integration/dynatrace-rt/webhook_listener.py`
collect dependencies in wheels folder:  
`pip wheel -r requirements.txt  --wheel-dir ./wheel`