import paralleldots
paralleldots.set_api_key('Du4NAEeb7qRi84rUlNjtsIgIWrVCYM3MTP2WaeaXH10')


def ner(text):
    ner = paralleldots.ner(text)
    return ner
