from googletrans import Translator

with open('figures.txt', 'w', encoding='utf-8') as f:
    with open('figures1.txt', 'r', encoding='utf-8') as f1:
        text = f1.read()
    f.write(Translator().translate(text, src='en', dest='ru').text)
