from __future__ import annotations
import dataclasses
import typing

@dataclasses.dataclass
class NodeItem:
  data: typing.Any
  next: NodeItem | None

class CustomStack:
    def __init__(self):
        self.__head = None
        self.__length = 0

    def peek(self):
        if self.__head is None:
            return None
        else:
            return self.__head.data

    def append(self, data: typing.Any):
        if self.__head is None:
            self.__head = NodeItem(data=data, next=None)
        else:
            new_elem = NodeItem(data=data, next=self.__head)
            self.__head = new_elem
        self.__length += 1

    def pop(self):
        if self.__head is None:
            return None
        else:
            data = self.__head.data
            next = self.__head.next
            self.__head.next = None
            self.__head = next
            self.__length -= 1
            return data

    def __len__(self):
        return self.__length

    def __repr__(self):
        return self.__head.__repr__()