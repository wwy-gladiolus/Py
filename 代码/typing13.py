import typing

T = typing.TypeVar("T")

class A(typing.Generic[T]):
    pass

class B(A[int], list[int]):
    pass

print(f"B.__bases__ == {B.__bases__}")
print(f"B.__mro__ == {B.__mro__}")

