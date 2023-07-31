from profile1 import factorial1, factorial2
import cProfile, pstats

#将Profile对象当成上下文管理器。
with cProfile.Profile(builtins=False) as pro:
    #从这里开始收集统计数据。
    factorial2(6)
    pro.create_stats()
    #在这里终止收集统计数据。
    factorial1(6)

#将收集到的统计数据保存到文件。
pro.dump_stats("profile_factorial21")

#创建一个Stats对象，并显示分析结果。
sta = pstats.Stats("profile_factorial21")
sta.strip_dirs()
sta.print_callers()

