import sys
import os
sys.path.append(os.getcwd())

import multiprocessing


bind = "0.0.0.0:3000"
workers = 1 #multiprocessing.cpu_count() * 2 + 1
