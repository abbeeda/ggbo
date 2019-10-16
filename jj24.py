import time
localtime = time.asctime( time.localtime(time.time()) )
print("当前时间：",localtime)
print(time.strftime("%j", time.localtime()) )
