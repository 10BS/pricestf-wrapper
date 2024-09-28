from datetime import datetime

import requests


class Price:
    def __init__(self, token=None, verify=True) -> None:
        self.verify = verify
        self.token = token
        if token is None:
            self.__get_token()

    def __get_token(self) -> str:
        get_token = self.__make_request("POST", "auth/access")
        access_token: str = get_token["accessToken"]
        self.token = access_token
        return self.token

    def __make_request(self, method, url, params=None, data=None):
        headers = {}
        base_url = r"https://api2.prices.tf/"
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        response = requests.request(
            method=method,
            url=base_url + url,
            params=params,
            data=data,
            headers=headers,
        )
        if response.ok:
            return response.json()
        elif self.token is not None and response != 200:
            self.__get_token()

    def get_price(
        self,
        sku: str,
        page: int = 1,
        limit: int = 100,
        order: str = "DESC",
        from_date=datetime.today(),
    ) -> dict:
        if order not in ["ASC", "DESC"]:
            raise ValueError("Order must be either ASC or DESC")
        return self.__make_request(
            method="GET",
            url=f"history/{sku}",
            params={
                "page": page,
                "limit": limit,
                "order": order,
                "from": from_date,
            },
        )
