import os
import time

import requests

from ncp_hmac_secret import make_signature


def sms_request(
        content,
        sender_number,
        receiver_list: list,
        subject="title",
        msg_type="SMS",
        content_type="COMM",
        country_code="82",
        specified_msgs: list = None
):
    if specified_msgs is None:
        specified_msgs = []
    else:
        for msg in specified_msgs:
            if "to" not in msg.keys():
                raise KeyError()

    messages = []
    for receiver in receiver_list:
        messages.append({"to": receiver})
    messages.extend(specified_msgs)

    request_body = {
        "type": msg_type,
        "contentType": content_type,
        "countryCode": country_code,
        "from": sender_number,
        "subject": subject,
        "content": content,
        "messages": messages,
    }

    request_domain = "https://sens.apigw.ntruss.com"
    request_uri = f"/sms/v2/services/{os.getenv('NCP_SENS_SERVICE_ID')}/messages"
    mime_type = "application/json; charset=utf-8"
    req_timestamp = str(int(time.time() * 1000))
    access_key = os.getenv("NCP_ACCESS")
    signature = make_signature(
        method="POST",
        path=request_uri,
        timestamp=req_timestamp
    )

    response = requests.post(
        request_domain + request_uri,
        headers={
            "Content-Type": mime_type,
            "x-ncp-apigw-timestamp": req_timestamp,
            "x-ncp-iam-access-key": access_key,
            "x-ncp-apigw-signature-v2": signature,
        },
        json=request_body,
    )

    return response.json()


if __name__ == "__main__":
    print(sms_request("test", "01076506941", ["01076506941"]))
