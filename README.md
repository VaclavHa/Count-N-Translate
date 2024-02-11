# Count 'N' Translate
Count 'N' Translate is a Python-based tool that combines the power of language translation with a detailed analysis of letter occurrences within translated texts. 
It leverages the googletrans library to translate text from one language to another and then analyzes the translated text to count the frequency of each letter. 
This project is inspired by the creative coding challenges found in "Impractical Python Projects."

## Features 
Translation: Utilize Google Translate to convert text from one language to another.
Letter Counting: Analyze translated texts to count the occurrence of each letter, providing insights into letter frequency.
Support for Multiple Languages: Translate between numerous languages supported by the Google Translate API.

## Getting started

Before you begin, ensure you have the following installed:

Python 3.x
Pip for Python 3

## Installation
To install required libs use:
- pip install -r requirements.txt

## Usage
To use Count 'N' Translate, run the script with the sentence and the target language code as arguments. Here's an example:
- python count_n_translate.py --sentence "Your sentence here." --code_of_lang "de"

For a list of all supported language codes, use:
- python count_n_translate.py --list-languages

## Acknowledgments
Google Translate API for enabling the translation features.
"Impractical Python Projects" for the inspiration behind this project.
