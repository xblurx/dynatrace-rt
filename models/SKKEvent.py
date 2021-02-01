#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SKKEvent:
    def __init__(
        self,
        PID,
        Tags,
        State,
        ProblemID,
        ProblemURL,
        ProblemTitle,
        ProblemDetailsText,
        ImpactedEntity,
    ):
        """
        Возможные параметры из интеграции оповещений в Dynatrace.
        Используем не все, те которые используем должны совпадать в интеграции Dynatrace.
        :param PID: str, Unique system identifier of the reported problem
        :param Tags: array, Comma separated list of tags that are defined for all impacted entities
        :param State: str, Problem state. Possible values are OPEN or RESOLVED or in some cases MERGED when the problem has been merged into another problem.
        :param ProblemID: int, Display number of the reported problem
        :param ProblemURL: str, URL of the problem within Dynatrace
        :param ProblemTitle: str, Short description of the problem
        :param ProblemDetailsText: str, All problem event details including root cause as a text-formatted string
        :param ImpactedEntity: str, Entity impacted by the problem (or x impacted entities when there are multiple).
        """
        self.message = f"Проблема: {ProblemTitle} на {ImpactedEntity} с тегами {Tags}. Суть проблемы: {ProblemDetailsText}"
        self.external_id3 = PID
        self.problem_id = ProblemID

    def make_event(self):
        """
        external-id1: str, Идентификатор МРФ (недоступен, либо хардкодить,
        либо создавать custom alerting на конкретный мрф, чтобы этот параметр передавался в случае события
        external-id3: str, Идентификатор системы (попробовал указывать в него PID, если не прокатывает, см выше)
        template-id: str, Идентификатор шаблона для отправки сообщения
        message-id: array, Массив идентификаторов сообщений
        recipient": телефон получателя. Прописывать его здесь - неправильно, нужно инжектировать извне, но это долго
        """
        return {
            "external-id1": "kc",
            "external-id3": self.external_id3,
            "messages": [
                {
                    "recipient": "Номер получателя",
                    "template-id": "1172",
                    "message-id": self.problem_id,
                    "variables": {"smsmsg": self.message},
                }
            ],
        }
