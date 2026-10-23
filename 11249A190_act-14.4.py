start_p = {'DT': 0.6, 'NN': 0.3, 'VB': 0.1}
trans_p = {
    'DT': {'DT': 0.05, 'NN': 0.85, 'VB': 0.10},
    'NN': {'DT': 0.10, 'NN': 0.30, 'VB': 0.60},
    'VB': {'DT': 0.40, 'NN': 0.50, 'VB': 0.10}
}
emit_p = {
    'DT': {'a': 0.5, 'the': 0.5},
    'NN': {'cat': 0.4, 'dog': 0.4, 'runs': 0.2},
    'VB': {'runs': 0.7, 'plays': 0.3}
}
words = ['a', 'cat', 'runs']
states = ['DT', 'NN', 'VB']
V = [{}]
backpointer = [{}]
for state in states:
    V[0][state] = (
        start_p[state] * emit_p[state].get(words[0], 0)
    )
    backpointer[0][state] = None
for t in range(1, len(words)):
    V.append({})
    backpointer.append({})

    for state in states:
        emission = emit_p[state].get(words[t], 0)

        candidates = [
            (
                V[t - 1][previous] *
                trans_p[previous][state] *
                emission,
                previous
            )
            for previous in states
        ]

        V[t][state], backpointer[t][state] = max(
            candidates, key=lambda item: item[0]
        )
last_state = max(states, key=lambda s: V[-1][s])
path = [last_state]

for t in range(len(words) - 1, 0, -1):
    path.append(backpointer[t][path[-1]])

path.reverse()

print("Viterbi values:")
for t, word in enumerate(words):
    print(word, V[t])
print("Best tag sequence:", list(zip(words, path)))
print("Best path probability:", V[-1][last_state])
