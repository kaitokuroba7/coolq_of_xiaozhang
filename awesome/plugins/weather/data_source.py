# async def get_weather_of_city(city: str) -> str:
import requests


async def get_weather_of_city(city: str) -> str:
    ErrorList = ['TimeoutError', 'ConnectionError', 'HTTPError', 'TooManyRedirects', 'OtherError']
    url = 'http://jisutqybmf.market.alicloudapi.com/weather/query'
    appcode = '374414f80e62455ba0711fa9894a05d4'
    headers = {'Authorization': 'APPCODE ' + appcode}
    try:
        content = requests.get(url=url, params={'city': city}, headers=headers)
    except requests.exceptions.Timeout:
        return 'TimeoutError'
    except requests.exceptions.ConnectionError:
        return 'ConnectionError'
    except requests.exceptions.HTTPError:
        return 'HTTPError'
    except requests.exceptions.TooManyRedirects:
        return 'TooManyRedirects'
    except:
        return 'OtherError'
    else:
        if content.status_code == 200 and content.json():
            demo = content.json()
            if demo in ErrorList:
                print(demo)
            else:
                test = demo.get("result")
                # 获取城市
                city = test.get('city')
                # 获取天气
                weather = test.get('weather')
                # 获取气温
                temp = test.get('temp')
                high_temp = test.get('temphigh')
                low_temp = test.get('templow')
                winddirect = test.get('winddirect')
                windpower = test.get('windpower')
                for index in test.get('index'):
                    if index['iname'] == '空调指数':
                        air_value = index['detail']
                    if index['iname'] == '运动指数':
                        sport_value = index['detail']
                    if index['iname'] == '紫外线指数':
                        ziwai_value = index['detail']
                    if index['iname'] == '感冒指数':
                        cold_value = index['detail']
                    if index['iname'] == '穿衣指数':
                        clo_value = index['detail']

                return f'{city}的天气是{weather},气温是{temp}度,最高气温是{high_temp}度,' \
                       f'最低气温是{low_temp}度,风向为{winddirect},风力为{windpower},{clo_value}' \
                       f'{cold_value}' \
                       # f'{sport_value}{ziwai_value}{cold_value}{clo_value}', demo
        else:
            return ''


