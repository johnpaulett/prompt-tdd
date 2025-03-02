from typing import Optional

import factory
from openai.types.chat.chat_completion import (
    ChatCompletion,
    ChatCompletionMessage,
    Choice,
)


class ChatCompletionMessageFactory(factory.Factory):
    class Meta:
        model = ChatCompletionMessage

    role = "assistant"
    content = factory.Faker("sentence")


class ChoiceFactory(factory.Factory):
    class Meta:
        model = Choice

    finish_reason = "stop"
    index = factory.Sequence(lambda n: n)
    message = factory.SubFactory(ChatCompletionMessageFactory)


class ChatCompletionFactory(factory.Factory):
    class Meta:
        model = ChatCompletion

    choices = factory.List([factory.SubFactory(ChoiceFactory)])
    object = "chat.completion"
    id = factory.Faker("uuid4")
    model = factory.Faker("word")
    created = factory.Faker("random_int")

    @classmethod
    def build(cls, messages: Optional[list[ChatCompletionMessage]], **kwargs):
        if messages:
            kwargs["choices"] = [
                ChoiceFactory.build(message=message) for message in messages
            ]

        return super().build(**kwargs)
