from core.hello_world import greet
def test_hello():
    assert greet("bob") == "hello bob"
