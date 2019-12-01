from datetime import datetime
import time


def log(msg, *, dt=datetime.utcnow()):
    print(f'{dt}:{msg}')


def log_sol(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print(f'{dt}:{msg}')


log("message 1")
time.sleep(2)
log("message 2")


log_sol("message 1")
time.sleep(2)
log_sol("message 2")
