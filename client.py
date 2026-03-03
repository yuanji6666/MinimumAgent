import os

from openai import OpenAI, OpenAIError

from system_prompt import SYSTEM_PROMPT


class OpenAIClient:
    base_url: str
    api_key: str

    def __init__(self, apiKey=None, baseUrl=None):
        # allow callers to override but fall back to env vars
        self.api_key = apiKey or os.getenv("OPENAI_API_KEY")
        self.base_url = baseUrl or os.getenv("OPENAI_API_BASE_URL")
        # if neither provided, OpenAI will also look at its own env var names
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )

    # generate answer by model
    def generate(
        self,
        user_prompt="",
        system_prompt=SYSTEM_PROMPT,
        model="deepseek/deepseek-v3.2-251201",
    ):

        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]

            print(f"{model} is generating...")
            print(f"{user_prompt}")

            res = self.client.chat.completions.create(model=model, messages=messages)

            ansStr = res.choices[0].message.content

            print(f"{model} generation completed.\n{ansStr}")

        except OpenAIError as e:
            print(f"{model} generation failed.\nError: {e}")
            return "model generation failed"

        else:
            return ansStr
