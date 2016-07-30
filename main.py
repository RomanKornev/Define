# -*- coding: utf-8 -*-
from textblob import TextBlob, Word

def define(query):
    query = query.strip().lower()
    results = []
    if query:
        for synset in Word(query).get_synsets()[:5]:
            results.append({
                "Title": synset._definition,
                "SubTitle": ', '.join(n.replace('_', ' ') for n in synset._lemma_names),
                "IcoPath":"Images/app.png"
            })
    if not results:
        results.append({
                "Title": 'Not found',
                "SubTitle": '',
                "IcoPath":"Images/app.png"
            })
    return results

from wox import Wox

class Define(Wox):
    def query(self, query):
        return define(query)

if __name__ == "__main__":
    Define()