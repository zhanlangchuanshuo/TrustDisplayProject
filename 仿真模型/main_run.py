from window import Window  
import playingGame as pg 

def main_run():
	settings, center, suppliers, manufacturers = pg.initParticipant()

	# 创建窗口
	win = Window(settings, center, suppliers, manufacturers)
	win.execute()

main_run()

