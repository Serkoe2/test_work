import pytest
import requests
import json

Data = (
    ("usd", "12.5"),
    ("eur", "12"),
    ("gbp", "0"),
    ("usd", "-12"),
    ("eur", "2312784801244739012830180472891479182390812904721398748917284972318947289174892174892738129381902478923"),
    ("eur", "-2312784801244739012830180472891479182390812904721398748917284972318947289174892174892738129381902478923"),
)

Load = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
Rates = {
    "usd": Load["Valute"]["USD"]["Value"],
    "eur": Load["Valute"]["EUR"]["Value"],
    "gbp": Load["Valute"]["GBP"]["Value"],
}
Server_url = "http://127.0.0.1:5000/api/getRates/"


@pytest.mark.parametrize('data', Data)
def test_getRates(data):
    body = {
        "rate": data[0],
        "value": float(data[1])
    }
    response = requests.post(Server_url, json=body).json()
    print(response)
    try:
        answer = round(float(data[1]) * Rates[data[0]], 2)
    except Exception as e:
        print(e)
        answer = data[2]
    assert response['result'] == answer


if __name__ == '__main__':
    print(Rates)
