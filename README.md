#### Download repo:  
`git clone https://github.com/xblurx/dynatrace-rt.git`
#### Create venv:
`python3 -m venv venv`
#### Activate venv:
`source venv/bin/activate`
#### Install dependencies:
`pip install -r requirements.txt`
#### Collect dependencies in wheels folder:
`pip wheel -r requirements.txt  --wheel-dir ./wheel`  
### To start webhook:
#### Copy env flask app variable:
`export FLASK_APP=~/webhook_listener.py`
#### Run flask:  
`nohup flask run &`
#### Run custom host/port:
`nohup python3 webhook_listener.py &`


