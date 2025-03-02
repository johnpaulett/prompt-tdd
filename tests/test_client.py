# Test the prompt harness itself, not the connection to an LLM
from unittest.mock import ANY, patch

import pytest
from openai.types.chat.chat_completion import (
    ChatCompletion,
    ChatCompletionMessage,
    Choice,
)

from prompt_tdd.client import execute, get_client

from .factories import ChatCompletionFactory, ChatCompletionMessageFactory

pytestmark = pytest.mark.local


@patch("prompt_tdd.client.OpenAI", autospec=True)
def test_get_client(mock_openai):
    client = get_client()
    assert client == mock_openai.return_value

    mock_openai.assert_called_once_with(
        base_url="http://localhost:11434/v1", api_key=ANY
    )


@patch("prompt_tdd.client.get_client", autospec=True)
def test_execute(mock_client, monkeypatch):
    # ensure env var is cleared
    monkeypatch.delenv("PROMPT_MODEL", raising=False)

    mock_client.return_value.chat.completions.create.return_value = (
        ChatCompletionFactory.build(
            messages=[ChatCompletionMessageFactory.build(content="Los Angeles Dodgers")]
        )
    )

    messages = [
        {"role": "user", "content": "Who won the world series in 2024?"},
    ]

    execute(messages)

    mock_client.return_value.chat.completions.create.assert_called_once_with(
        model="mistral-small",  # default model
        temperature=0.0,
        messages=messages,
    )


@patch("prompt_tdd.client.get_client", autospec=True)
def test_execute_env_var(mock_client, monkeypatch):
    # ensure env var is cleared
    monkeypatch.setenv("PROMPT_MODEL", "llama3.3")

    mock_client.return_value.chat.completions.create.return_value = (
        ChatCompletionFactory.build(
            messages=[ChatCompletionMessageFactory.build(content="Texas Rangers")]
        )
    )

    messages = [
        {"role": "user", "content": "Who won the world series in 2023?"},
    ]

    execute(messages)

    mock_client.return_value.chat.completions.create.assert_called_once_with(
        model="llama3.3",
        temperature=0.0,
        messages=messages,
    )
