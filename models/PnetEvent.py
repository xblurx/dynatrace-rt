#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PnetEvent:
    def __init__(
        self,
        Tags,
        State,
        ProblemID,
        ProblemURL,
        ProblemTitle,
        ProblemDetailsText,
        ImpactedEntity,
    ):
        self.CLASS = "hardcode"
        self.msg = ImpactedEntity
        self.mc_tool = "hardcode"
        self.mc_object = ProblemID
        self.mc_host = "hardcode"
        self.mc_priority = "hardcode"
        self.mc_object_uri = ProblemURL
        self.mc_parameter = ProblemTitle
        self.mc_service = self._map_service(Tags)
        self.mc_object_class = "hardcode"
        self.severity = self._map_severity(State)
        self.mc_long_message = ProblemDetailsText

    def _map_severity(self, state):
        severity_map = {"OPEN": "MINOR", "MERGED": "OK", "RESOLVED": "OK"}
        self.severity = severity_map[state]
        return self.severity

    def _map_service(self, tags):
        service_map = {}  # management zone to pnet service map
        self.service = service_map[tags]
        return self.service

    def make_event(self):
        pnet_event = [
            {
                "attributes": {
                    "msg": self.msg,
                    "CLASS": self.CLASS,
                    "mc_host": self.mc_host,
                    "mc_tool": self.mc_tool,
                    "severity": self.severity,
                    "mc_object": self.mc_object,
                    "mc_service": self.mc_service,
                    "mc_priority": self.mc_priority,
                    "mc_parameter": self.mc_parameter,
                    "mc_object_uri": self.mc_object_uri,
                    "mc_long_message": self.mc_long_message,
                    "mc_object_class": self.mc_object_class,
                }
            }
        ]
        return pnet_event
