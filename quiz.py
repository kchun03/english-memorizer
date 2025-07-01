
import random
import json

def load_words():
    with open("word_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def make_quiz(mode, count=10):
    words = load_words()
    questions = random.sample(words, min(count, len(words)))
    quiz = []

    for item in questions:
        if mode == 1:
            quiz.append((item['word'], item['meaning']))
        elif mode == 2:
            quiz.append((item['meaning'], item['word']))
        elif mode == 3:
            if random.choice([True, False]):
                quiz.append((item['word'], item['meaning']))
            else:
                quiz.append((item['meaning'], item['word']))
    return quiz
