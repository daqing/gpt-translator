split_string = "\n\n"
format = "markdown"

def translate_text(full_text, input_lang, target_lang, client):
    system_prompt = f"You are a translation tool. You receive a text snippet from a file in the following format:\n{format}\n\n. The file is also written in the language:\n{input_lang}\n\n. As a translation tool, you will solely return the same string in {target_lang} without losing or amending the original formatting. Your translations are accurate, aiming not to deviate from the original structure, content, writing style and tone."

    results = []

    split_text = full_text.split(split_string)

    for text in split_text:
        messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": text}]

        completion = client.chat.completions.create(
                model="gpt-4-0613",
                messages=messages
                )

        results.append(completion.choices[0].message.content)

    return split_string.join(results)
