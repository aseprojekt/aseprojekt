import json
import matplotlib.pyplot as plt

if __name__ == '__main__':
    DataFileName = 'dataMay-31-2017.json'

    with open(DataFileName, 'r') as DataFile:
        collectedData = json.load(DataFile)['data']

    names_occ, company_occ, city_occ = {}, {}, {}
    for record in collectedData:
        name = record[3]
        if name not in names_occ:
            names_occ[name] = 1
        else:
            names_occ[name] += 1

        city = record[2]
        if city not in city_occ:
            city_occ[city] = 1
        else:
            city_occ[city] += 1

        company = record[1]
        if name not in company_occ:
            company_occ[company] = 1
        else:
            company_occ[company] += 1

    plt.title('Names')
    plt.bar(*zip(*names_occ.items()))
    plt.xticks(rotation=90, fontsize=5)
    plt.show()

    plt.title('Cities')
    plt.bar(*zip(*city_occ.items()))
    plt.xticks(rotation=90, fontsize=5)
    plt.show()

    plt.title('Companies')
    plt.bar(*zip(*company_occ.items()))
    plt.xticks(rotation=90, fontsize=5)
    plt.show()
