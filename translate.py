split_string = "\n\n"
format = "markdown"

def translate_full(full_text, input_lang, target_lang, client):
    system_prompt = f"You are a translation tool. You receive a text snippet from a file in the following format:\n{format}\n\n. The file is also written in the language:\n{input_lang}\n\n. As a translation tool, you will solely return the same string in {target_lang} without losing or amending the original formatting. Your translations are accurate, aiming not to deviate from the original structure, content, writing style and tone."
    code_prompt = "Make sure don't translate code blocks in markdown format, and don't translate image paths in :src field, and do translate the alt field from img tag"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": code_prompt},
        {"role": "user", "content": full_text}
    ]

    completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
            )

    return completion.choices[0].message.content
