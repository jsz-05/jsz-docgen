import random
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return None

def get_synonyms(word, pos):
    synsets = wn.synsets(word, pos=pos)
    lemmas = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            lemmas.add(lemma.name())
    return lemmas

def paraphrase(sentence):
    tagged_sentence = pos_tag(word_tokenize(sentence))
    paraphrased_sentence = []
    for word, treebank_tag in tagged_sentence:
        wordnet_pos = get_wordnet_pos(treebank_tag)
        if wordnet_pos:
            synonyms = get_synonyms(word, wordnet_pos)
            if synonyms:
                paraphrased_sentence.append(random.choice(list(synonyms)))
            else:
                paraphrased_sentence.append(word)
        else:
            paraphrased_sentence.append(word)
    return ' '.join(paraphrased_sentence)
