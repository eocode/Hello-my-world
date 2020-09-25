# Sample Test passing with nose and pytest
import hello_my_world.hello as h

def test_pass():
    assert h.hello() == "Hello world"
