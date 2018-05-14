import random
random.seed(31200)
import json
import os
import sys
from sys import platform

if platform == "linux" or platform == "linux2":
	# this is linux
	os.environ['SUMO_HOME'] = '/usr/share/sumo'
	try:
	    import traci
	    import traci.constants as tc
	except ImportError:
	    if "SUMO_HOME" in os.environ:
	        print(os.path.join(os.environ["SUMO_HOME"], "tools"))
	        sys.path.append(
	            os.path.join(os.environ["SUMO_HOME"], "tools")
	        )
	        import traci
	        import traci.constants as tc
	    else:
	        raise EnvironmentError("Please set SUMO_HOME environment variable or install traci as python module!")

elif platform == "win32":
    os.environ['SUMO_HOME'] = 'C:\\Program Files (x86)\\DLR\\Sumo'

    try:
        import traci
        import traci.constants as tc
    except ImportError:
        if "SUMO_HOME" in os.environ:
            print(os.path.join(os.environ["SUMO_HOME"], "tools"))
            sys.path.append(
                os.path.join(os.environ["SUMO_HOME"], "tools")
            )
            import traci
            import traci.constants as tc
        else:
            raise EnvironmentError("Please set SUMO_HOME environment variable or install traci as python module!")


else:
    sys.exit("platform error")


setting_memo = "one_run"
PATH_TO_CONF = os.path.join("conf", setting_memo)

sumoBinary = r"/usr/bin/sumo-gui"
sumoCmd = [sumoBinary,
           '-c',
           r'./hello.sumocfg']
sumoCmd_pretrain = [sumoBinary,
                    '-c',
                    r'./hello.sumocfg']

sumoBinary_nogui = r"/usr/bin/sumo"
sumoCmd_nogui = [sumoBinary_nogui,
                 '-c',
                 r'./hello.sumocfg']
sumoCmd_nogui_pretrain = [sumoBinary_nogui,
                          '-c',
                          r'./hello.sumocfg']




traci.start(sumoCmd)