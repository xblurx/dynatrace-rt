#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rq import Queue
from redis import Redis
from flask import request, make_response, Flask
from models import PnetEvent, SKKEvent
from tasks import make_pnet_request, make_skk_request

app = Flask(__name__)
redis = Redis()
skk_queue = Queue("skk_queue", connection=redis)
pnet_queue = Queue("pnet_queue", connection=redis)


@app.route("/webhook", methods=["GET"])
def index():
    return make_response("OK", 200)


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        skk_event = SKKEvent().make_event()
        pnet_event = PnetEvent(request.data).make_event()

        skk_queue.enqueue(make_skk_request, skk_event)
        pnet_queue.enqueue(make_pnet_request, pnet_event)
        return make_response("OK", 200)
    except AttributeError:
        return make_response("ERROR", 500)


if __name__ == "__main__":
    app.run(host="10.242.152.115", debug=True, use_reloader=True)
