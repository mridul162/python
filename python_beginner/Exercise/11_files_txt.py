word_stats = {}
with open("poem.txt", "r") as f:
    for line in f:
        words = line.split(' ')
        for word in words:
            if word in word_stats:
                word_stats[word] += 1
            else:
                word_stats[word] = 1

# for w, s in word_stats.items():
#     print(f"{w} : {s}")

word_occurrences = list(word_stats.values())
max_count = max(word_occurrences)
print("Max occurrences of any word is: ", max_count)

print("Words with max occurrences are: ")
for word, count in word_stats.items():
    if count == max_count:
        print(word)