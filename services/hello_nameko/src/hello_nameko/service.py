"""
Nameko Hello World
"""
from nameko.rpc import rpc


class HelloWorldService:
    name = "hello_world"

    @rpc
    def hello(self, name):
        return f"Bem vindo {name}"
