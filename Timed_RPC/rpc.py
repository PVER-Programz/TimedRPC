from pypresence import Presence
import time
from activities import *

client_id = "948182088568422422"
now = time.time

RPC = Presence(client_id=client_id)
RPC.connect()

def shedule(start, end, act, showStart=False, showEnd=False):
	if showStart: start_time=start
	else: start_time=None
	if showEnd: end_time=end
	else: end_time=None
	if time.time() > start and time.time() < end:
		RPC.update(**act, start=start_time, end=end_time)
		print(f'''
			--- REFRESH LOG ---
	Refresh timestamp: {now()}
	Current Status: {act['large_image']}
	Start at: {start}
	Elapsed: {now()-start}
	End at: {end}
	Left: {end-now()}
			''')
		time.sleep(20)

while True:
	shedule(1643779800, 1643784600, yt, showStart=False, showEnd=False)
	shedule(1643784600, 1643788800, redt, showStart=False, showEnd=False)
	shedule(1643788800, 1643790600, stare, showStart=False, showEnd=False)
	shedule(1643790600, 1643793000, eat, showStart=False, showEnd=False)
	shedule(1643793000, 1643797800, bot, showStart=False, showEnd=False)
	
	shedule(1643797800, 1643800200, sleep, showStart=False, showEnd=False)
	shedule(1643800200, 1643803200, mfs, showStart=False, showEnd=False)
	shedule(1643803200, 1643805600, afk, showStart=False, showEnd=False)
	shedule(1646829000, 1646830800, eat, showStart=False, showEnd=False)
	shedule(1646830800, 1646833500, dnd, showStart=False, showEnd=False)
	
	shedule(1646833500, 1646835300, stare, showStart=False, showEnd=False)
	shedule(1646835300, 1646837400, mfs, showStart=False, showEnd=False)
	shedule(1646837400, 1646839800, yt, showStart=False, showEnd=False)
	shedule(1646839800, 1646841600, redt, showStart=False, showEnd=False)

	shedule(1646841600, 1646843400, eat, showStart=False, showEnd=False)
	shedule(1646843400, 1646845200, afk, showStart=False, showEnd=False)
	shedule(1646845200, 1646847000, bot, showStart=False, showEnd=False)

	shedule(1646847000, 9999999999, sleep, showStart=False, showEnd=False)


print(dir(RPC.update))