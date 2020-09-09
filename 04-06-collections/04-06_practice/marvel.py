from collections import namedtuple, defaultdict
import csv
import pprint

Hero = namedtuple('Hero', 'sex first_seen')

def get_superheroes(file):
    superheroes = defaultdict(list)

    with open(file, encoding='utf-8') as fin:
        for line in csv.DictReader(fin):
            try:
                name = line['name'].split()[0]
                sex = line['SEX'].split()[0]
                first_seen = line['FIRST APPEARANCE']
            except IndexError:
                continue

            hero = Hero(sex=sex, first_seen=first_seen)
            superheroes[name].append(hero)

    return superheroes


data = get_superheroes('marvel-wikia-data.csv')


