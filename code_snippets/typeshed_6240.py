from google.protobuf.wrappers_pb2 import StringValue
StringValue(value=some_obj.var_a)

some_string_field_in_proto_Message = StringValue(value=some_obj.var_a) if some_obj.var_a is not None else None 
