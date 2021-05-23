import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('https://a-z-animals.com/animals/mammals/', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
bsObject = BeautifulSoup(html, "html.parser")

mammals_page_url = []
for cover in bsObject.find_all('div', {'class' : 'col-lg-4 col-md-6'}) :
    link = cover.select('a')[0].get('href')
    mammals_page_url.append(link)
print(len(mammals_page_url))

mammals = []

for link in mammals_page_url :
    page_req = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'})
    page_html = urlopen(page_req).read()
    page_bsObject = BeautifulSoup(page_html, "html.parser")

    mammals_dataset = ["" for i in range(100)]

    i = 0
    for characteristics in page_bsObject.find_all('dt', {'class' : 'col-sm-6 text-md-right'}) :
        mammals_dataset[i] = (characteristics.text)
        i = i + 2

    i = 1
    for characteristics in page_bsObject.find_all('dd', {'class' : 'col-sm-6'}) :
        mammals_dataset[i] = (characteristics.text)
        i = i + 2

    mammals_longevity_weight = {"longevity" : '', "weight" : ''}
    if "Lifespan" in mammals_dataset and "Weight" in mammals_dataset :
        longevity_index = mammals_dataset.index("Lifespan") + 1
        weight_index = mammals_dataset.index("Weight") + 1

        mammals_longevity_weight["longevity"] = mammals_dataset[longevity_index]
        mammals_longevity_weight["weight"] = mammals_dataset[weight_index]

        mammals.append(mammals_longevity_weight)


for mammal in mammals :
    # longevity casting - avg
    longevity = mammal['longevity']
    longevity.replace(' ', '')
    flag = False
    for char in longevity:
        if char.isdigit():
            flag = True
    if flag:
        if longevity.find('months') != -1:
            if len(re.findall('\d*\.?\d+', longevity)) > 1:
                longevity = str(
                    (float(re.findall('\d*\.?\d+', longevity)[1]) + float(re.findall('\d*\.?\d+', longevity)[0])) / 24)
            else:
                longevity = str(float(re.findall('\d*\.?\d+', longevity)[0]) * (1 / 12))
        elif longevity.find('years') != -1 or longevity.find('yrs') != -1:
            if len(re.findall('\d*\.?\d+', longevity)) > 1:
                longevity = str(
                    (float(re.findall('\d*\.?\d+', longevity)[1]) + float(re.findall('\d*\.?\d+', longevity)[0])) / 2)
            else:
                longevity = re.findall('\d*\.?\d+', longevity)[0]
        mammal['longevity'] = longevity
    else:
        mammals.remove(mammal)
        continue
        # weight casting - max
    weight = mammal['weight']
    weight = weight.replace(',', '')
    weight = weight.replace(' ', '')
    flag = False
    for char in weight:
        if char.isdigit():
            flag = True
    if flag:
        if weight.find('(') != -1:
            weight = weight[0:weight.index('(')]
        if weight.find('lbs') != -1 or weight.find('Lbs') or weight.find('pound'):
            if len(re.findall('\d*\.?\d+', weight)) > 1:
                weight = str(float(re.findall('\d*\.?\d+', weight)[1]) * 0.453592)
            else:
                weight = str(float(re.findall('\d*\.?\d+', weight)[0]) * 0.453592)
        elif weight.find('kg') != -1:
            if len(re.findall('\d*\.?\d+', weight)) > 1:
                weight = str(float(re.findall('\d*\.?\d+', weight)[1]))
            else:
                weight = re.findall('\d*\.?\d+', weight)[0]
        elif weight.find('g') != -1:
            if len(re.findall('\d*\.?\d+', weight)) > 1:
                weight = str(float(re.findall('\d*\.?\d+', weight)[1]) * 0.001)
            else:
                weight = str(float(re.findall('\d*\.?\d+', weight)[0]) * 0.001)
        elif weight.find('ton') != -1:
            if len(re.findall('\d*\.?\d+', weight)) > 1:
                weight = str(float(re.findall('\d*\.?\d+', weight)[1]) * 1000)
            else:
                weight = str(float(re.findall('\d*\.?\d+', weight)[0]) * 1000)
        elif weight.find('oz') != -1 or weight.find('ounce'):
            if len(re.findall('\d*\.?\d+', weight)) > 1:
                weight = str(float(re.findall('\d*\.?\d+', weight)[1]) * 0.0283495)
            else:
                weight = str(float(re.findall('\d*\.?\d+', weight)[0]) * 0.0283495)
        mammal['weight'] = weight
    else:
        mammals.remove(mammal)
        continue

f = open("data8_avg_max.txt", 'w', encoding="utf-8")
for mammal in mammals :
    f.write("{\'longevity\' : \'" +  mammal['longevity'] + "\', " + "\'weight\' : \'" +  mammal['weight']  + "\'}\n")
    print(mammal)

