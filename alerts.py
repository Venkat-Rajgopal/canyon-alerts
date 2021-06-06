import requests, re, json
from pprint import pprint


url = 'https://www.canyon.com/en-de/gravel-bikes/adventure/grizl/grizl-cf-sl-6/2711.html?dwvar_2711_pv_rahmenfarbe=GY%2FBK'

urls = { '1' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-7/2370.html?dwvar_2370_pv_rahmenfarbe=SR%2FBK',
         '2' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-7/2370.html?dwvar_2370_pv_rahmenfarbe=GN%2FBK',
         '3' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-6/2369.html?dwvar_2369_pv_rahmenfarbe=SR%2FBK',
         '4' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-6/2369.html?dwvar_2369_pv_rahmenfarbe=GN%2FBK',
         '71by' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-7-1by/2707.html?dwvar_2707_pv_rahmenfarbe=SR%2FBK',
        'Grizl_1' : 'https://www.canyon.com/en-de/gravel-bikes/adventure/grizl/grizl-cf-sl-6/2711.html?dwvar_2711_pv_rahmenfarbe=GN%2FBU',
        'Grizl_2' : 'https://www.canyon.com/en-de/gravel-bikes/adventure/grizl/grizl-cf-sl-6/2711.html?dwvar_2711_pv_rahmenfarbe=GY%2FBK'
}


r = requests.get(url)
s = re.search(r'window\.deptsfra=(.*);', r.text).group(1)
data = json.loads(s)

results = {i['value'] : i['availability']['shippingInfo'] for i in data['productDetail']['variationAttributes'][1]['values']}
pprint(results)

def get_results(url):
    r = requests.get(url)
    s = re.search(r'window\.deptsfra=(.*);', r.text).group(1)
    data = json.loads(s)
    results = {i['value'] : i['availability']['shippingInfo'] for i in data['productDetail']['variationAttributes'][1]['values']}
    pprint(results)

    return results


for key, value in urls.items():
    print(key, value)
    result = get_results(url=value)
    

