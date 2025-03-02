import os

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam


def get_client():
    # Use the OpenAI compat for ollama, could use other prompt APIs
    #   https://ollama.com/blog/openai-compatibility
    return OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    )


def execute(messages: list[ChatCompletionMessageParam]) -> ChatCompletion:
    client = get_client()

    model = os.getenv("PROMPT_MODEL", "mistral-small")

    response = client.chat.completions.create(
        model=model,
        temperature=0.0,  # No randomness, can change
        messages=messages,
    )

    return response.choices[0].message.content
