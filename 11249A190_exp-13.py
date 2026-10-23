def perplexity(prob, n):
    return prob ** (-1 / n) if prob > 0 else float("inf")
# Test sentence
sentence = "the fox runs away"
n = len(sentence.split())
# Sentence probabilities
uni_p = 0.1304
bi_p = 0.000147
tri_p = 0.000272
# Calculate perplexity
uni_pp = perplexity(uni_p, n)
bi_pp = perplexity(bi_p, n)
tri_pp = perplexity(tri_p, n)

# Observation Table
print("Model\t\tSentence Probability\tPerplexity")
print("-" * 50)

print("Unigram\t\t", uni_p, "\t\t", round(uni_pp, 2))
print("Bigram\t\t", bi_p, "\t\t", round(bi_pp, 2))
print("Trigram\t\t", tri_p, "\t\t", round(tri_pp, 2))