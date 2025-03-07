import json

import pytest

from prompt_tdd.client import execute


def example_one(content, model=None):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a simple bot that will echo my message as a JSON"
                " responses with a message key. Do not include any surrounding"
                " content to the JSON ouput."
            ),
        },
        {"role": "user", "content": "blue"},
        {"role": "assistant", "content": '{"message": "blue"}'},
        {"role": "user", "content": content},
    ]

    # This prompt should return JSON
    response = execute(messages, model=model)
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pytest.fail(f"Expected JSON, got: {response}")


def example_two(content):
    messages = [
        {
            "role": "system",
            "content": "You are a geography bot that answer a location question. Only return the answer.",
        },
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "Paris"},
        {"role": "user", "content": f"What is the capital of {content}?"},
    ]

    return execute(messages)
