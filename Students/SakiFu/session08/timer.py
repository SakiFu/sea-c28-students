
import time


class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args, **kwargs):
        self.end = time.clock()
        self.elapse = self.end - self.start
        state = "this code took {:.6f} seconds".format(self.elapse)
        print state


with Timer() as t:
    for i in range(100000):
        i = i ** 20
