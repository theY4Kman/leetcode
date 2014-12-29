No solution came right to mind, so I'm gonna go with naive: generate a dictionary of all possible transformations of all words in the dictionary, a separate dictionary for the end word, then traverse all possibilities until we can transform into the end word.

Well, it *seems* correct, but as expected, it's INCREDIBLY slow. I changed the transformation generation to only generate the words used in the dictionary, start, and end words. Still slow.

Then, I thought about sorting the words to prevent duplicates in the transformations dict. But since only one character can be changed at a time, this falls flat. For example, "TEA" would get put into the dict as "AET". However, "ATE" would also be put in as "AET", and you can't transform "TEA" into "ATE" with one-character substitutions.

Before I figured out that flaw, I also thought about simply removing one character from each position in each transition word, so "ATE" would get transformed into "AT", "AE", "TE". This suffers from the same flaw, though, as a word can resolve into a transformation that doesn't work with one-character substitution: "ASS" becomes "AS", and "HAS" becomes "AS".

Hmmm, should've checked before jumping to conclusions: generating the transformations is instant, following paths through them explodes in its breadth.

So, I added a check to immediately kill any path follow whose length is larger than the shortest path we've seen. Answer is instant. Aye! Let's see how it stands up to enormous dictionaries. I'm scared.

With just three letters in each word, it has trouble finding one valid path in order to cut off longer attempts. I have a feeling I'm going to have to assign priorities to each transformation.
