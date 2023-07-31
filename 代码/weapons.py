from datetime import datetime, timedelta
from random import randint

#定义代表通用武器的类Weapon。  所有其他武器类都以该类为基类。
class Weapon:
    #初始化时设置了如下私有实例属性：
    #  _damage_min: 物理伤害的最小值。
    #  _damage_max: 物理伤害的最大值。
    #  _category: 该武器的类别，例如“大马士革刀”。
    #  _name: 默认引用空串，表明这是普通武器。  如果引用其他字符串，则表明该武器
    # 是有名字的武器。
    def __init__(self, dmin=0, dmax=0, ctg='Void Blade', name='', **kwargs):
        self._damage_min = int(dmin)
        self._damage_max = int(dmax)
        self._category = ctg
        self._name = name
        super().__init__(**kwargs)

    #该保护类属性为最近一次掷骰子的时间。
    _time = datetime.now()

    #该私有类属性为一个取值0～100的骰子，对应物理伤害。
    __dice = 0

    #该保护类属性用于掷骰子。
    @classmethod
    def _roll_dice(cls):
        cls.__dice = randint(0, 100)
        cls._time = datetime.now()

    #该保护类属性基于骰子点数计算物理伤害。
    def _physical_damage(self):
        return (self._damage_min * (100-self.__dice) \
                + self._damage_max * self.__dice) // 100

    #该公有类属性用于计算该武器某次攻击时产生的伤害。
    def damage(self):
        #如果最近一次掷骰子距离现在的时间超过了一秒，则重新掷骰子。
        time_interval = datetime.now() - self._time
        if time_interval > timedelta(seconds=1):
            self._roll_dice()
        #返回伤害值。
        return self._physical_damage()

    #该公有类属性返回该武器的描述。
    def description(self):
        if self._name:
            s = self._name + "'s " + self._category + "\n"
        else:
            s = self._category + "\n"
        s = s + "physical damage: " + str(self._damage_min) + "-"\
                + str(self._damage_max) + "\n"
        print(s)


#定义代表火焰武器的类FireWeapon。
class FireWeapon(Weapon):
    #初始化时设置了如下私有实例属性：
    #  _fire_min: 火焰伤害的最小值。
    #  _fire_max: 火焰伤害的最大值。
    def __init__(self, fmin=0, fmax=0, **kwargs):
        self._fire_min = fmin
        self._fire_max = fmax
        super().__init__(**kwargs)

    #该私有类属性为一个取值0～100的骰子，对应火焰伤害。
    __dice = 0

    #该保护类属性用于掷骰子。
    @classmethod
    def _roll_dice(cls):
        cls.__dice = randint(0, 100)
        super()._roll_dice()

    #该保护类属性基于骰子点数计算火焰伤害。
    def _fire_damage(self):
        return (self._fire_min * (100-self.__dice) \
                + self._fire_max * self.__dice) // 100

    #该公有类属性用于计算该武器某次攻击时产生的伤害。
    def damage(self):
        #如果最近一次掷骰子距离现在的时间超过了一秒，则重新掷骰子。
        time_interval = datetime.now() - self._time
        if time_interval > timedelta(seconds=1):
            self._roll_dice()
        #返回伤害值。
        return self._physical_damage() + self._fire_damage()

    #该公有类属性返回该武器的描述。
    def description(self):
        if self._name:
            s = self._name + "'s " + self._category + "\n"
        else:
            s = self._category + "\n"
        s = s + "physical damage: " + str(self._damage_min) + "-"\
                + str(self._damage_max) + "\n"
        s = s + "fire damage: " + str(self._fire_min) + "-"\
                + str(self._fire_max) + "\n"
        print(s)


#定义代表冰冻武器的类ColdWeapon。
class ColdWeapon(Weapon):
    #初始化时设置了如下私有实例属性：
    #  _cold_min: 冰冻伤害的最小值。
    #  _cold_max: 冰冻伤害的最大值。
    def __init__(self, cmin=0, cmax=0, **kwargs):
        self._cold_min = cmin
        self._cold_max = cmax
        super().__init__(**kwargs)

    #该私有类属性为一个取值0～100的骰子，对应冰冻伤害。
    __dice = 0

    #该保护类属性用于掷骰子。
    @classmethod
    def _roll_dice(cls):
        cls.__dice = randint(0, 100)
        super()._roll_dice()

    #该保护类属性基于骰子点数计算冰冻伤害。
    def _cold_damage(self):
        return (self._cold_min * (100-self.__dice) \
                + self._cold_max * self.__dice) // 100

    #该公有类属性用于计算该武器某次攻击时产生的伤害。
    def damage(self):
        #如果最近一次掷骰子距离现在的时间超过了一秒，则重新掷骰子。
        time_interval = datetime.now() - self._time
        if time_interval > timedelta(seconds=1):
            self._roll_dice()
        #返回伤害值。
        return self._physical_damage() + self._cold_damage()

    #该公有类属性返回该武器的描述。
    def description(self):
        if self._name:
            s = self._name + "'s " + self._category + "\n"
        else:
            s = self._category + "\n"
        s = s + "physical damage: " + str(self._damage_min) + "-"\
                + str(self._damage_max) + "\n"
        s = s + "cold damage: " + str(self._cold_min) + "-"\
                + str(self._cold_max) + "\n"
        print(s)


#定义代表闪电武器的类LightningWeapon。
class LightningWeapon(Weapon):
    #初始化时设置了如下私有实例属性：
    #  _lightning_min: 闪电伤害的最小值。
    #  _lightning_max: 闪电伤害的最大值。
    def __init__(self, lmin=0, lmax=0, **kwargs):
        self._lightning_min = lmin
        self._lightning_max = lmax
        super().__init__(**kwargs)

    #该私有类属性为一个取值0～100的骰子，对应闪电伤害。
    __dice = 0

    #该保护类属性用于掷骰子。
    @classmethod
    def _roll_dice(cls):
        cls.__dice = randint(0, 100)
        super()._roll_dice()

    #该保护类属性基于骰子点数计算闪电伤害。
    def _lightning_damage(self):
        return (self._lightning_min * (100-self.__dice) \
                + self._lightning_max * self.__dice) // 100

    #该公有类属性用于计算该武器某次攻击时产生的伤害。
    def damage(self):
        #如果最近一次掷骰子距离现在的时间超过了一秒，则重新掷骰子。
        time_interval = datetime.now() - self._time
        if time_interval > timedelta(seconds=1):
            self._roll_dice()
        #返回伤害值。
        return self._physical_damage() + self._lightning_damage()

    #该公有类属性返回该武器的描述。
    def description(self):
        if self._name:
            s = self._name + "'s " + self._category + "\n"
        else:
            s = self._category + "\n"
        s = s + "physical damage: " + str(self._damage_min) + "-"\
                + str(self._damage_max) + "\n"
        s = s + "lightning damage: " + str(self._lightning_min) + "-"\
                + str(self._lightning_max) + "\n"
        print(s)


#定义代表魔法武器的类MagicWeapon。
class MagicWeapon(FireWeapon, ColdWeapon, LightningWeapon):
    #初始化时没有设置任何私有实例属性：
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #该保护类属性用于掷骰子。
    @classmethod
    def _roll_dice(cls):
        super()._roll_dice()

    #该公有类属性用于计算该武器某次攻击时产生的伤害。
    def damage(self):
        #如果最近一次掷骰子距离现在的时间超过了一秒，则重新掷骰子。
        time_interval = datetime.now() - self._time
        if time_interval > timedelta(seconds=1):
            self._roll_dice()
        #返回伤害值。
        return self._physical_damage() + self._fire_damage()\
                + self._cold_damage() + self._lightning_damage()

    #该公有类属性返回该武器的描述。
    def description(self):
        if self._name:
            s = self._name + "'s " + self._category + "\n"
        else:
            s = self._category + "\n"
        s = s + "physical damage: " + str(self._damage_min) + "-"\
                + str(self._damage_max) + "\n"
        s = s + "fire damage: " + str(self._fire_min) + "-"\
                + str(self._fire_max) + "\n"
        s = s + "cold damage: " + str(self._cold_min) + "-"\
                + str(self._cold_max) + "\n"
        s = s + "lightning damage: " + str(self._lightning_min) + "-"\
                + str(self._lightning_max) + "\n"
        print(s)

