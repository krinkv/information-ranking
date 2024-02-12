import contextualSpellCheck
import spacy

nlp = spacy.load("en_core_web_sm")

nlp.add_pipe("contextual spellchecker")


def context_spellcheck(sentence):
    doc = nlp(sentence)
    return doc._.outcome_spellCheck


def context_spellcheck_suggestions(sentence):
    doc = nlp(sentence)
    return doc._.suggestions_spellCheck
