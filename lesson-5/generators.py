from functools import reduce

sentences = ["This is a sentence", "This is another sentence", "This is a third sentence"]

sorted_sentences = list(sorted(
  reduce(
    lambda acc, sentence: acc + sentence,
    map(
      lambda sentence: list(filter(
        lambda word: len(word) < 5,
        sentence.split(" ")
      )),
      sentences
    )
  ),
  key=lambda word: word.lower()
))

print(sorted_sentences)