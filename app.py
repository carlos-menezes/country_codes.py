from requests_html import HTMLSession
import json

session = HTMLSession()

data = []

r = session.get('https://en.wikipedia.org/wiki/ISO_3166-1')
table = r.html.find('.wikitable')[1]
rows = table.find('tr')

for row in rows[1:]:
    countries = row.find('tr')[0]
    countryName = countries.find('td')[0].text
    alpha2 = countries.find('td')[1].text
    alpha3 = countries.find('td')[2].text
    numeric = countries.find('td')[3].text
    independent = countries.find('td')[5].text

    if independent == "Yes":
        independent = True
    else:
        independent = False

    data.append({
        "country": countryName,
        "alpha2-code": alpha2,
        "alpha3-code": alpha3,
        "numeric": numeric,
        "independent": independent
    })

with open('country-codes.json', "w") as f:
    json.dump(data, f)