import os

if not os.path.exists(os.path.join('proto', 'message_pb2.py')):
    os.system('protoc -Iproto --python_out proto proto/message.proto')