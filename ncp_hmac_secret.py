import os
import hashlib
import hmac
import base64
import time


def make_signature(
        method="GET",
        path="/photos/puppy.jpg?query1=&query2",
        timestamp=str(int(time.time() * 1000))
):
    access_key = os.getenv("NCP_ACCESS")  # access key id
    secret_key = os.getenv("NCP_SECRET")  # secret key
    secret_key = bytes(secret_key, 'UTF-8')

    message = method + " " + path + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    return base64.b64encode(
        hmac.new(
            secret_key,
            message,
            digestmod=hashlib.sha256
        ).digest()
    ).decode('UTF-8')


if __name__ == '__main__':
    x_ncp_timestamp = str(int(time.time() * 1000))
    print(make_signature(timestamp=x_ncp_timestamp))
