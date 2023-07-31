from datetime import datetime, timezone, timedelta


#定义Clock类，其实例代表处于某时区的本地时钟。  由于该类实现了__get__，所以该类的实例
# 都是描述器。
class Clock:
    #实例属性tz储存着该时钟所在时区。
    def __init__(self, h):
        h = int(h)
        delta = timedelta(hours=h)
        self.tz = timezone(delta)

    #读取该时钟时返回“hh:mm:ss”格式的本地时间。
    def __get__(self, instance, owner=None):
        t = datetime.now(self.tz)
        return str(t.hour) + ':' + str(t.minute) + ':' + str(t.second)


#定义WorldClock类，其每个类属性以一个城市命名，引用一个处于该城市所在时区的时钟描述器。
class WorldClock:
    honolulu = Clock(-11)    #西11区，火奴鲁鲁。
    hawaii = Clock(-10)    #西10区，夏威夷。
    juneau = Clock(-9)    #西9区，朱诺。
    los_angeles = Clock(-8)    #西8区，洛杉矶。
    mexico_city = Clock(-7)    #西7区，墨西哥城。
    chicago = Clock(-6)    #西6区，芝加哥。
    washington = Clock(-5)    #西5区，华盛顿。
    buenos_aires = Clock(-4)    #西4区，布宜诺斯艾利斯。
    brasilia = Clock(-3)    #西3区，巴西利亚。
    greenland = Clock(-2)    #西2区，格陵兰岛。
    conakry = Clock(-1)    #西1区，科纳克里。
    london = Clock(0)    #UTC时间，伦敦。
    berlin = Clock(1)    #东1区，柏林。
    cairo = Clock(2)    #东2区，开罗。
    moscow = Clock(3)    #东3区，莫斯科。
    abu_dhabi = Clock(4)    #东4区，阿布扎比。
    new_delhi = Clock(5)    #东5区，新德里。
    almaty = Clock(6)    #东6区，阿拉木图。
    singapore = Clock(7)    #东7区，新加坡。
    beijing = Clock(8)    #东8区，北京。
    tokyo = Clock(9)    #东9区，东京。
    melbourne = Clock(10)    #东10区，墨尔本。
    honiara = Clock(11)    #东11区，霍尼亚拉。
    wellington = Clock(12)    #东12区，惠灵顿。

