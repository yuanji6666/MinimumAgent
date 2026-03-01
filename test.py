import re

tool_arg = 'arg_name="arg", another_arg="another_value"'
a = re.findall(r'(\w+)="([^"]*)"', tool_arg)

print(dict(a))
