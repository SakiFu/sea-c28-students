#!/usr/bin/env python

from io import open
import random


def get_text(filename):

    f = open(filename, 'r')
    text = f.readlines()
    [x.lower() for x in text]
    text = " ".join(text)
    words = text.split()
    return words


def trigram(words):
    pairs = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        pairs.setdefault(pair, []).append(words[i + 2])
    return pairs


def build_text(words, pairs):
    new_text = []
    for i in range(300):
        random_pair = random.sample(pairs, 1)[0]
        nextword = random.sample(pairs[random_pair], 1)[0]
        new_text.extend((" ".join(random_pair), nextword))
    new_text2 = " ".join(new_text)
    return new_text2


if __name__ == "__main__":
    words = get_text('sherlock.txt')
    pairs = trigram(words)
    new_text2 = build_text(words, pairs)

    print new_text2
