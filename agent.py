import re

from client import OpenAIClient
from tools import AVAILABLE_TOOLS

user_prompt = input("Chat with Deepseek: ")

prompt_history = f"User: {user_prompt}\n"

client = OpenAIClient()

for i in range(5):
    res = client.generate(prompt_history)

    action = re.search(r"Action: (.*)", res).group(1)

    if action.startswith("Finish"):
        answer = re.search(r"Finish\[(.*)\]", action).group(1)
        print(f"Answer: {answer}")
        break
    else:
        tool_call = re.search(r"(\w+)\(", res).group(1)
        tool_arg = re.search(r"\((.*)\)", res).group(1)
        kwargs = dict(re.findall(r'(\w+)="([^"]*)"', tool_arg))

    if tool_call in AVAILABLE_TOOLS:
        observation = AVAILABLE_TOOLS[tool_call](**kwargs)
    else:
        observation = f"没有工具：{tool_call}，检查你的回答，保证工具合法且格式正确。"

    observation_str = f"Observation: {observation}\n"
    prompt_history += observation_str

    if i >= 5:
        print("达到最大循环次数，停止对话。")
        break
