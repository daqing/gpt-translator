# GPT-Translator

Translate markdown files using OpenAI's GPT-4 model.

# Usage

```
$ python main.py --base-lang en --target-lang zh-CN --input ./demo/example.en.md --output ./example.zh-CN.md
```

This will translate `./demo/example.en.md` into simplified chinese and save to `./example.zh-CN.md`.

Remember to set the `OPENAI_API_KEY` environment variable in order to use the GPT-4 model.
