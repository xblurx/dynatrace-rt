#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rq import Queue
from redis import Redis
from models import PnetEvent, SKKEvent
from flask import request, make_response, Flask
from tasks import make_pnet_request, make_skk_request

app = Flask(__name__)
redis = Redis()
skk_queue = Queue("skk_queue", connection=redis)
pnet_queue = Queue("pnet_queue", connection=redis)


@app.route("/problem", methods=["POST"])
def webhook():
    try:
        print(request.data)
        # skk_event = SKKEvent().make_event()
        pnet_event = PnetEvent(request.data).make_event()

        # skk_queue.enqueue(make_skk_request, skk_event)
        pnet_queue.enqueue(make_pnet_request, pnet_event)
    except AttributeError:
        return make_response("ERROR", 500)
