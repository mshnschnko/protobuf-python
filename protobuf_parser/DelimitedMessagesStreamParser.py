from protobuf_parser.helpers import parseDelimited

from typing import TypeVar, Type

T = TypeVar('T')

class DelimitedMessagesStreamParser:
    def __init__(self, cls: Type[T]) -> None:
        self.message_type = cls
        self.buffer: bytes = b''

    def parse(self, data: bytes) -> list[Type[T]]:
        messages = list()
        try:
            self.buffer += data
        except TypeError:
            return messages
        else:
            while len(self.buffer) != 0:
                message, bytes_processed = parseDelimited(self.buffer, self.message_type)
                if message:
                    messages.append(message)
                elif bytes_processed == 0:
                    break
                self.buffer = self.buffer[bytes_processed:]
            return messages
