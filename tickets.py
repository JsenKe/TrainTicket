import requests
import re
import TrainCollection


def cli():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
    r = requests.get(url, verify=False)
    # stations = re.findall(r'([A-Z]+)\|([a-z]+)', r.text)
    stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text)
    diction2 = dict(stations)
    diction2 = dict(zip(diction2.keys(), diction2.values()))

    # 需要输入的参数
    date = input("请输入出发日期(yyyy-mm-dd):")
    start = input("请输入出发站:")
    end = input("请输入到达站:")

    # 获取车站代码
    startcode = ''
    endcode = ''

    while True:
        if diction2.__contains__(start):
            startcode = diction2.get(start)
            break
        else:
            start = input("没有这个出发站，请重新输入:")

    while True:
        if diction2.__contains__(end):
            endcode = diction2.get(end)
            break
        else:
            end = input("没有这个到达站，请重新输入:")

    print("搜索信息："+date + ' ' + start + ' 到 ' + end)

    # 查票链接
    url = "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}".format(date, startcode, endcode)
    r = requests.get(url, verify=False)
    rows = r.json()['data']['datas']
    trains = TrainCollection.TrainCollection(rows)
    trains.pretty_print()


if __name__ == '__main__':
    cli()
