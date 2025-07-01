
from PIL import Image
import pytesseract
import json

def extract_words(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='eng')
    lines = text.strip().split('\n')
    word_list = []

    for line in lines:
        if ':' in line:
            parts = line.split(':')
            word = parts[0].strip()
            meaning = parts[1].strip()
            word_list.append({'word': word, 'meaning': meaning})

    with open("word_data.json", "w", encoding="utf-8") as f:
        json.dump(word_list, f, ensure_ascii=False, indent=2)

    return word_list
