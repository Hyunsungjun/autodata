import requests
from pyprnt import prnt

searching = input()
url = f'https://dapi.kakao.com/v2/local/search/address.json?query={searching}'
headers = {
    "Authorization": "KakaoAK 2d3a7e374ebf2788385a939041bdae61"
}
places = requests.get(url, headers = headers).json()['documents']
prnt(places)
