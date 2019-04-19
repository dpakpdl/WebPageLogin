import json
import pandas


def get_data_from_file(filename):
    with open(filename, 'r') as in_file:
        data = json.load(in_file)
    return data


def get_properties_from_data(data, searchname):
    all_data = data.get('map', {}).get('properties', [])
    # print (all_data)
    result = list()
    for element in all_data:
        for elem in element:
            if type(elem) == list:
                for el in elem:
                    if type(el) == dict:
                        result.append(get_data_from_single_data(el))
    # print(result)
    with open('files/input.json', 'w+') as outfile:
        json.dump(result, outfile)

    pandas.read_json("files/input.json").to_excel("files/"+ searchname+"_output.xlsx")


def get_data_from_single_data(data):
    street_address = data.get('streetAddress')
    zipcode = data.get('zipcode')
    city = data.get('city')
    price = data.get('price')
    currency = data.get('currency')
    bathrooms = data.get('bathrooms', '')
    bedrooms = data.get('bedrooms', '')
    living_area = data.get('livingArea')
    home_type = data.get('homeType')
    return {
        'streetAddress': street_address,
        'zipcode': zipcode,
        'city': city,
        'price': str(price) + '' + currency + '/mo',
        'bathrooms': str(int(bathrooms)) + ' ba' if bathrooms else "",
        'bedrooms': str(int(bedrooms)) + ' bds' if bedrooms else "",
        'livingArea': str(living_area) + '/sqft',
        'homeType': home_type
    }


if __name__ == "__main__":
    searchname = 'anoka_county_mn'
    filename = 'files/anoka_county_mn.json'
    json_result = get_data_from_file(filename)
    # print(json_result)
    get_properties_from_data(json_result, searchname)
