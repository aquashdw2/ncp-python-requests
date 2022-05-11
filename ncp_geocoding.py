import os
from urllib.parse import quote_plus
import requests


def geocode(query: str, cord: tuple = None):
    request_domain = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?"
    if query:
        request_domain += f"query={quote_plus(query)}"
    if cord:
        cord_string = f"{cord[0]},{cord[1]}"
        request_domain += f"coordinate={quote_plus(cord_string)}"
    print(request_domain)
    response = requests.get(
        request_domain,
        headers={
            "X-NCP-APIGW-API-KEY-ID": os.getenv("X_NCP_APIGW_API_KEY_ID"),
            "X-NCP-APIGW-API-KEY": os.getenv("X_NCP_APIGW_API_KEY"),
        },
    )
    return response.json()


def reverse(long=128.12345, lat=37.98776):
    request_domain = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
    request_domain += f"?coords={long},{lat}&output=json"

    response = requests.get(
        request_domain,
        headers={
            "X-NCP-APIGW-API-KEY-ID": os.getenv("X_NCP_APIGW_API_KEY_ID"),
            "X-NCP-APIGW-API-KEY": os.getenv("X_NCP_APIGW_API_KEY"),
        },
    )
    return response.json()


if __name__ == '__main__':
    print(geocode("내정로 55"))
    # print(reverse(long=127.1152768, lat=37.3660181))
