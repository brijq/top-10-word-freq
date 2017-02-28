"""
I would like you to produce a small serverlet that accepts as input a body of text, such as that from a book,
and returns the top ten most-used words along with how many times they occur in the text.You are free to choose
an appropriate language of your choice, and you can use whatever frameworks also are convenient if you like.
When you are done push it to a https://github.com repository.
"""


wordstring = '''Friendship is a rainbow at the end of a rain shower,
Friendship is a sweeping cool breeze on a warm summers day,
Friendship is a warm fuzzy kitten lying across my feet,
Friendship is dancing fire on a cold winters night.
Source: http://www.familyfriendpoems.com/poem/poem-about-friendship-what-is-it'''

wordlist = wordstring.split()

# adding all the words in wordlist to enter wordfreq
wordfreq = []               
for word in wordlist:     
  if word not in wordfreq:
    wordfreq.append(word)

# Make a list of (count, unique) tuples.
counts = []
for unique in wordfreq:
  count = 0              # Initialize the count to zero.
  for word in wordlist:  # Iterate over the words.
    if word == unique:   # Is this word equal to the current unique?
      count += 1         # If so, increment the count
  counts.append((count, unique))

counts.sort()            # Sorting the list puts the lowest counts first.
counts.reverse()         # Reverse it, putting the highest counts first.


# Print the ten words with the highest counts.
for i in range(min(10, len(counts))):
  count, word = counts[i]
  print('%s %d' % (word, count))

