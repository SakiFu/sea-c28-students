#!/usr/bin/env python

import io
import random


def get_text():
    f = io.open('sherlock.txt', 'r')
    text = f.readlines()
    text.punctuation.replace("'", "")
    [x.lower() for x in text]
    text = " ".join(text)
    words = text.split()
    return words


def trigram(words):
    pairs = {}

    for i in range(len(words)):
        pair = tuple(words[i:i + 2])
        pairs.setdefault(pair, []).append(words[i + 2])
    return pairs


def build_text(words, pairs):
    new_text = []
    for i in range(len(words)):
        random_pair = random.sample(pairs, 1)[0]
        nextword = random.sample(pairs[random_pair], 1)[0]
        new_text.extend((" ".join(random_pair), nextword))

    new_text = " ".join(new_text)
