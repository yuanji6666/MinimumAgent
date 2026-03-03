from hello_agents import HelloAgentsLLM, SimpleAgent, ReActAgent

from openai import OpenAI, OpenAIError

from dotenv import load_dotenv

from system_prompt import SYSTEM_PROMPT


load_dotenv()

llm = HelloAgentsLLM()


class OpenAIClient:
    client = SimpleAgent('str', llm, SYSTEM_PROMPT)
    def generate(self, user_prompt):
        return self.client.run(user_prompt)





