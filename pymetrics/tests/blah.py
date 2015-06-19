from pymetrics.registry import registry, name
from pymetrics.counter import Counter
from pymetrics.timer import Timer

c1 = Counter(name('blah', 'somethhig'))
registry.register(c1)

c1.inc()

t = Timer(name('blah', 'example'))
registry.register(t)

context = t.time()
try:
    None
finally:
    context.stop()


with t.time():
    None
