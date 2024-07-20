

from examples.parent_a import ParentA
from examples.parent_b import ParentB


def main():
    child = Child()
    child.child_method()
    child.parent_b_method()
    child.parent_a_method(2, 3)


class Child(ParentA, ParentB):

    def child_method(self):
        return 'this is child method'

    def another(self):
        pass

    def __init__(self, cookies: str):
        self.cookies = cookies
