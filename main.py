import argparse
import sys
from collections import defaultdict
from pprint import pprint as pp

from googletrans import Translator

SUPPORTED_LANG_CODES = {
    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn',
    'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka',
    'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it',
    'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms',
    'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru',
    'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta',
    'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
}


def count_letters(sentence: str) -> dict:
    """
    Counts the occurrence of each letter in a given sentence.

    This function iterates through the input sentence, filtering out non-letter characters,
    and counts the occurrences of each letter, regardless of case. The result is a dictionary
    where keys are letters and values are lists of occurrences of that letter.

    Parameters:
    - sentence (str): The input sentence to analyze.

    Returns:
    - dict: A dictionary with letters as keys and lists of these letters as values.
    """

    sentence = sentence.strip().lower()
    d = defaultdict(list)
    for char in sentence:
        if char.isalpha():
            d[char].append(char)
    return d


def translate(sentence: str, code_of_lang: str) -> str:
    """
    Translates the given sentence to a specified language using the googletrans library.

    This function takes a sentence and a two-letter language code (as per ISO 639-1 standards),
    and returns the translated sentence in the specified language.

    Note: The accuracy of the translation and the availability of languages depend on the
    googletrans library and the Google Translate API it interfaces with.

    Parameters:
    - sentence (str): The sentence to translate.
    - code_of_lang (str): The two-letter code of the target language (e.g., 'de' for German).

    Returns:
    - str: The translated sentence.
    """

    translator = Translator()
    text_to_translate = translator.translate(sentence, dest=f'{code_of_lang}')

    return str(text_to_translate.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translate text and count letter occurrences.')
    parser.add_argument('--sentence', type=str, help='The sentence to translate and analyze.')
    parser.add_argument('--code_of_lang', type=str, help='The two-letter code of the target language for translation.')
    parser.add_argument('--list-languages', action='store_true', help='List all supported language codes and exit.')
    args = parser.parse_args()

    if args.list_languages:
        print("Supported language codes:")
        for code in sorted(SUPPORTED_LANG_CODES):
            print(code)
        sys.exit(0)
    elif args.sentence and args.code_of_lang:
        if args.code_of_lang not in SUPPORTED_LANG_CODES:
            print(f"Error: '{args.code_of_lang}' is not a supported language code.")
            sys.exit(1)

        input_s = args.sentence
        language_code = args.code_of_lang

        print(f"Entered sentence: {input_s}")
        letter_dict = count_letters(input_s)
        pp(letter_dict, indent=2, width=150)

        print()

        translation = translate(input_s, language_code)
        print(f"Translated sentence: {translation}")
        new_trans = count_letters(translation)
        pp(new_trans, indent=2, width=150)
    else:
        parser.print_help()
        print(
            "\nError: Please provide both a sentence and a language code for translation,\
             or use --list-languages to list all supported languages.")
        sys.exit(1)
