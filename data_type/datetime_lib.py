import datetime
import time


if __name__ == "__main__":
    print(datetime.MAXYEAR)
    print(datetime.MINYEAR)
    print(datetime.date(2020, 10, 1))
    print(datetime.datetime.now())
    print(datetime.time(18, 50, 24))
    print(datetime.tzinfo())
    print(datetime.timezone)

    a = datetime.time(18, 56, 24)

    print(datetime.timedelta.max)
    print(datetime.timedelta.min)
    print(datetime.timedelta.resolution)

    today = datetime.datetime.today()
    yesterday = datetime.datetime.today() + datetime.timedelta(days=-1)
    print(today, yesterday)
    print(today + datetime.timedelta(days=-1) * 5)

    g = datetime.timedelta(days=-3)
    b = datetime.timedelta(days=-2)
    print(g, b)
    print(g.total_seconds())
    print(datetime.datetime.today())
    print(datetime.date.fromtimestamp(time.time()))
    print(time.time())

    print(datetime.datetime.fromisoformat("2019-09-09"))
    print(datetime.date.fromisoformat("2019-09-09"))
    # print(datetime.date.fromisocalendar(2020, 09, 09))
    # 返回(2020, 40, 4) -》 （year, week, day）
    print(datetime.date.isocalendar(datetime.date(2020, 10, 1)))

    print(datetime.date.max)
    print(datetime.date.min)
    print(datetime.date.resolution)

    # date类比较有用的方法
    d = datetime.date(2020, 9, 21)
    print(d)
    print(d.replace(year=2020, month=10, day=1))
    print(d.timetuple())
    # 公元1年1月1日对应的序列号为1，d.toordinal返回日期d对应的序号
    print(d.toordinal())
    # 返回一个数字,表示星期几,星期一为0
    print(d.weekday())
    # 返回一个数字,表示星期几,星期一为1
    print(d.isoweekday())
    # 返回YYYY-MM-DD格式
    print(d)
    print(d.isoformat())


