import pydart2_api as papi
import world
try:
    import gui
except Exception, e:
    print("-" * 40)
    print("Error while importing pydart2.gui")
    print(e)
    print("-" * 40)


def boo(x):
    print("pydart2.boo is excuted")
    return x * 2


def init():
    papi.init()


def create_world(step, skel_path=None):
    return world.World(step, skel_path)
