import requests

api_key = "ff46a9f316ed27c327458ebc62c36d03"


def get_data(cityname, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    no_values = 8 * forecast_days
    filtered_data = filtered_data[:no_values]
    return filtered_data


if __name__ == "__main__":
    data=get_data("Nuneaton",3)
    print(data)
