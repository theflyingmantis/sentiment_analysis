def readFile(fileName):
    """
     * Code for reading a file.  you probably don't want to modify anything here,
     * unless you don't like the way we segment files.
    """
    contents = []
    f = open(fileName)
    for line in f:
      contents.append(line)
    f.close()
    result = segmentWords('\n'.join(contents))
    return result
def segmentWords(s):
    """
     * Splits lines on whitespace for file reading
    """
    return s.split()

def filterStopWords(words):
    """
    * TODO
    * Filters stop words found in self.stopList.
    """
    contents = []
    final_words = []
    f = open('../data/english.stop')
    for line in f:
      contents.append(line)
    stop = segmentWords('\n'.join(contents))
    f.close()
    for w in words:
      if w not in stop:
        final_words.append(w)
    return final_words


# from collections import Counter
# cnt=Counter()
# l=["a","b","a","b","c"]
# cnt["a"]+=2
# cnt["b"]=1

# for k in cnt:
#   print cnt[k]
# k=readFile('random_file.txt')
# print filterStopWords(k)

from sets import Set
engineers = Set()
engineers.add('a')
engineers.add('a')
engineers.add('b')
for k in engineers:
  print k
# print engineers

