import logging

from twitterhal.command_line import init_logging
from twitterhal.gracefulkiller import killer
from twitterhal.runtime import runner

logger = init_logging(logging.DEBUG)


def worker():
    while not killer.kill_now:
        print("worker, gonna sleep 10s")
        killer.sleep(10)


def loop_task():
    print("loop task")


runner.register_worker(worker)
runner.register_loop_task(loop_task, sleep=15)

runner.run()
