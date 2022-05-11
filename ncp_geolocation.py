import os
import time

import requests

from ncp_hmac_secret import make_signature


def geolocation(request_ip):
    request_domain = "https://geolocation.apigw.ntruss.com"
    request_uri = f"/geolocation/v2/geoLocation?ip={request_ip}&ext=t&responseFormatType=json"

    req_timestamp = str(int(time.time() * 1000))
    access_key = os.getenv("NCP_ACCESS")
    signature = make_signature(
        method="GET",
        path=request_uri,
        timestamp=req_timestamp
    )

    response = requests.get(
        request_domain + request_uri,
        headers={
            "x-ncp-apigw-timestamp": req_timestamp,
            "x-ncp-iam-access-key": access_key,
            "x-ncp-apigw-signature-v2": signature,
        },
    )

    return response.json()


if __name__ == "__main__":
    print(geolocation("210.57.252.50"))
