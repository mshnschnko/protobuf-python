from typing import TypeVar, Any, Type
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.message import DecodeError

T = TypeVar('T')

def parseDelimited(data: Any, cls: Type[T]) -> tuple[Type[T], int]:
    """
    \brief Расшифровывает сообщение,
    предваренное длиной из массива байтов.
        
    \param data Массив данных.
    \param cls Тип сообщения.

    \return Возвращает кортеж из
    расшифрованного сообщения и количество байт,
    которое потребовалось для расшифровки.
    """
    if data is None or len(data) == 0:
        return None, 0
    l, p = _DecodeVarint32(data, 0)
    if l + p > len(data):
        return None, 0
    message = cls()
    try:
        message.ParseFromString(data[p:p+l])
    except DecodeError:
        raise ValueError
    return message, p + l