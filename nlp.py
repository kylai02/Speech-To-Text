import spacy
from string import punctuation


nlp=spacy.load('en_core_web_sm')

def get_keywords(text):
    result = []
    pos_tag = ['NOUN']
    doc = nlp(text.lower())

    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            result.append(token.text)
    return result

new_text = """
When it comes to evaluating the performance of keyword extractors, you can use some of the standard metrics in machine learning: accuracy, precision, recall, and F1 score. However, these metrics don't reflect partial matches. they only consider the perfect match between an extracted segment and the correct prediction for that tag.
Fortunately, there are some other metrics capable of capturing partial matches. An example of this is ROUGE.
"""


print(get_keywords(new_text))