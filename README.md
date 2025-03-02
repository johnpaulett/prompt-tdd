# Test Driven Prompt Engineering with pytest

This is an example of taking an iterative approach to prompt development using pytest to document. Use this repository as a template, customizing the prompt and the client for your use case, documenting what expected responses look like to enable easier productization of your prompt via an executable test suite.

## Why?

Prompt Engineering with LLMs has massively lowered the barriers for domain experts to prototype and create intelligent systems.

During iterative prompt development, the prompt author qualatively evaluates the prompt output.

Unfortunately, this evaluation is typically lost if the input and outputs are not documented, easily re-runnable and comparable.

When handing off to appliction engineers who lack domain knowledge, future prompt changes become dangerous. The prompt is effectively
treated as a brittle black box.

By Test-Driven Prompt Development, capturing inputs and outputs along the way you:

1. Make handoff to application engineers easier, since they can be confident they are not breaking expected behaviour
2. Make evaluation of newer model versions or alternative models easier since their is a test suite that can be repeatedly run.

## Install

Uses [`uv`](https://docs.astral.sh/uv/getting-started/installation/) to manage dependencies

Install pytest

```
make init
```

## How to Use

By default, src/promp_tdd is using ollama with a mistral-small model (`ollama pull mistral-small`) via the ollama OpenAI compatibility API. You can adjust this to use another model via ollama (can set `PROMPT_MODEL` enviromment variable to change), change to use OpenAI itself, or rewrite to use any other LLM API.

Edit `src/prompt_tdd/prompt.py` (includes an example using ollama via the OpenAI API) and `tests/test_prompt.py`.

Run the full test suite:

```
make test
```

If you want another ollama model, after pulling (`ollama pull phi4`)

```
PROMPT_MODEL=phi4 make test
```

Alternatively, watch for changes and only run the relevant changed tests:

```
make watch
```

## Learn more

- pytest marks

- [pytest parametrization](https://docs.pytest.org/en/7.1.x/example/parametrize.html) allows for

## Future

- Enhance fuzy matching of results (ROGUE / BLEU)

## Development

Only run tests on the non-LLM harnesses:

```
make test-local
```

Clean out the virtualenv and cache files:

```
make clean
```
