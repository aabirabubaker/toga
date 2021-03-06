import inspect

from .libs import *


class LongRunningTask(NSObject):
    @objc_method
    def performIteration_(self, info) -> None:
        try:
            delay = next(self.__dict__['interface'])
            NSTimer.scheduledTimerWithTimeInterval(
                delay,
                target=self,
                selector=SEL('performIteration:'),
                userInfo=None,
                repeats=False
            )
        except StopIteration:
            pass


def process_callback(callback_result):
    "Handle generators in actions"
    if inspect.isgenerator(callback_result):
        task = LongRunningTask.alloc().init()
        task.__dict__['interface'] = callback_result
        task.performIteration(None)
