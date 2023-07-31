import typing

#该全局变量的标注说明它应该引用Tuple[int, str]类型的对象。
a: typing.Tuple[int, str]

#该赋值语句不会报错，因为符合标注。
a = (0, 'a')
#该赋值语句会报错，因为值的类型为List[object]。
a = [0, 'a']
#该赋值语句会报错，因为值的类型为Tuple[int]。
a = (0,)
#该赋值语句会报错，因为值的类型为Tuple[int, str, None]。
a = (0, 'a', None)
#该赋值语句会报错，因为值的类型为Tuple[float, bytes]。
a = (0.0, b'a')

