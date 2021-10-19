import requests
import nltk

from nltk import RegexpParser
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from nltk.tag.stanford import StanfordPOSTagger

if __name__ == "__main__":
  sentiment0 = """$BTC.X This will crash in short term. am bullish long run."""
  sentiment1 = """$BTC.X will rally to $60k!"""

  porter = PorterStemmer()

  with open("bear.txt", "r") as f:
    bearish = [line.replace("\n", "") for line in f.readlines()]      

  with open("bull.txt", "r") as f:
    bullish = [line.replace("\n", "") for line in f.readlines()]      

  # sentFiltered = [word for word in sentiment1.split() if word not in stopwords.words('english')]
  # print(sentFiltered)

  st = StanfordPOSTagger(model_filename="/home/lan/stanford-postagger/models/english-bidirectional-distsim.tagger", path_to_jar="/home/lan/stanford-postagger/stanford-postagger.jar")

  sentTokens = word_tokenize(" ".join(sentiment1.split(" ")))
  sentTagged = st.tag(sentTokens)

  chunkPattern = """Chunk: {<NNP><RB>}"""

  chunker = RegexpParser(chunkPattern)
  output = chunker.parse(sentTagged)
  output.draw()

# sentiments = requests.get("http://localhost:5000/api/v1/sentiments")
# for sent in sentiments.json():
#   print(sent["content"])