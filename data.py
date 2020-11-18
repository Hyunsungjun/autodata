import requests
from bs4 import BeautifulSoup

def query_sender():

    base = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?'
    serviceKey = 'serviceKey=cOY3jxbzwQcYdzgHVwNDXf88P%2BhmrSYegSrkP0TQChlG9T4hZAy3pBk9%2F6mbbbubukPNTAXCisEC5hkpyhVi6w%3D%3D'
    #날짜 바꾸기
    starttime = 20200310
    endtime = 20201116
    start = f'&startCreateDt={starttime}'
    end = f'&endCreateDt={endtime}'
    url = base + serviceKey + start + end
    # print(url)
    corona = requests.get(url)
    # corona.encoding
    print(corona.status_code)
    print(corona.encoding)
    #utf-8이 떠야되는데 None이 뜸 
    # print(corona)
    # print(BeautifulSoup(corona).prettify())
    
    
query_sender()
