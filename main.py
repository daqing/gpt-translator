import openai
import os
from translate import translate_text
import argparse

lang_dict = {
    "zh-CN": "chinese_simplified",
    "zh-TW": "chinese_traditional",
    "ru": "russian",
    "de":  "german",
    "es": "spanish",
    "fr": "french",
    "ja": "japanese",
    "pt": "portuguese",
    "vi": "vietnamese",
    "ar": "arabic",
    "en": "english",
}

def translate_file(input_path, output_path, base_lang, target_lang, client):
    with open(input_path, "r") as f:
        file_content = f.read()

        print(f"Translating file {input_path} to {target_lang}...")
        translated_text = translate_text(file_content, base_lang, target_lang, client)

        with open(output_path, "w") as f:
            f.write(translated_text)

def main():
    # Check if OPENAI_API_KEY is set in the environment
    if "OPENAI_API_KEY" not in os.environ:
        print("Please set the OPENAI_API_KEY environment variable.")
        exit(1)

    client = openai.OpenAI()

    # Create the parser
    parser = argparse.ArgumentParser(description="Translate markdown files using OpenAI's GPT-4 model.")

    # Add the arguments
    parser.add_argument('--base-lang', metavar='base_lang', default="en", type=str, help='the base language to translate from')
    parser.add_argument('--target-lang', metavar='target_lang', type=str, help='the target language to translate to')

    parser.add_argument('--input', metavar='input file', type=str, help='path to the input file')
    parser.add_argument('--output', metavar='output file', type=str, help='path to the output file')

    # Parse the arguments
    args = parser.parse_args()

    if args.target_lang is None:
        print("Please specify the target language to translate to")
        exit(1)

    if args.base_lang not in lang_dict:
        print(f"Base language {args.base_lang} not supported. Supported languages: {', '.join(lang_dict.keys())}")
        exit(1)

    if args.target_lang not in lang_dict:
        print(f"Target language {args.target_lang} not supported. Supported languages: {', '.join(lang_dict.keys())}")
        exit(1)

    if args.input is None:
        print("Please specify the path to the input file.")
        exit(1)

    if args.output is None:
        print("Please specify the path to the output file.")
        exit(1)

    translate_file(args.input, args.output, lang_dict[args.base_lang], lang_dict[args.target_lang], client)

# Run the main function
main()
