"""
GET: data muncul jika url dibuka dengan browser
POST:
"""
import requests
import json
import bs4


url = 'https://www.idx.co.id/umbraco/Surface/Helper/GetStockChart?indexCode=TLKM&period=1W'
try:
    result = requests.get(url)
    if result.status_code == 200 :
        data = json.loads(result.text)
        chart_data = data['ChartData']
        # print(chart_data)
        f = open('data.csv','w')
        f.write("#Tanggal;Nilai\n")

        for d in chart_data:
            tgl = d['Date']
            val = d['Close']
            # print(tgl,' - ',val)
            f.write('{};{}\n'.format(tgl,val))
        f.close()

except Exception as ex:
    print(ex)

