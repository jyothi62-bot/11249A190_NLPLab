import nltk
from nltk.corpus import brown
from nltk import UnigramTagger
from nltk.tag import brill, brill_trainer
nltk.download('brown')
tagged_sentences = brown.tagged_sents(categories='news')
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]
baseline_tagger = UnigramTagger(train_data)
templates = brill.brill24()
trainer = brill_trainer.BrillTaggerTrainer(
    baseline_tagger,
    templates,
    trace=1
)
for max_rules in [10, 30]:
    brill_tagger = trainer.train(
        train_data,
        max_rules=max_rules
    )

    baseline_acc = baseline_tagger.accuracy(test_data)
    brill_acc = brill_tagger.accuracy(test_data)

    improvement = (brill_acc - baseline_acc) * 100

    print("\nMaximum rules:", max_rules)
    print("Baseline accuracy:", baseline_acc)
    print("Brill accuracy:", brill_acc)
    print("Improvement (percentage points):", improvement)

    print("Learned rules:")
    for rule in brill_tagger.rules()[:5]:
        print(rule)
sentence = "They will fish for hours near the river bank"
tokens = nltk.word_tokenize(sentence)
print("\nBaseline tagging:", baseline_tagger.tag(tokens))
print("Brill tagging:", brill_tagger.tag(tokens))
