from profile1 import factorial2
import cProfile, pstats

#创建一个空的Profile对象。
pro = cProfile.Profile(builtins=False)

pro.enable()
#从这里开始收集统计数据。
factorial2(6)
#在这里终止收集统计数据。
pro.disable()

#创建一个Stats对象，并显示分析结果。  注意这里直接以Profile对象为参数。
sta = pstats.Stats(pro)
sta.strip_dirs()
sta.print_callees()

