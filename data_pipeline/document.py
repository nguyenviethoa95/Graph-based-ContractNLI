from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize.texttiling import TextTilingTokenizer
import spacy


class DocumentGraph:
    def __init__(self):
        pass

    def build_graph(self):
        pass

    def preprocess(self):
        pass

    def get_entities(self):
        """
        Use dependency parsing to extract entities
        :return:
        """
        pass

    def get_relations(self):
        pass

    def plot_graph(self):
        pass

    def __len__(self):
        """
        1.  Tokenize a document by whitespace
        2.  Count the number of tokens
        :return:
        """
        # Create a reference variable for Class WhitespaceTokenizer
        tk = WhitespaceTokenizer()

        # Use tokenize method
        tokens = tk.tokenize(self.text)

        # Return document lengths
        return len(tokens)

    def _get_sentence_(self):
        """
        Split text document into sentences by comma -> line break
        :return:
        """
        sentencizer = PunktSentenceTokenizer()
        return sentencizer.tokenize(self.text)

    def _get_paragraph_(self):
        """
        Use the text tilling algorithm to split a document into paragraph.
        :return:
        """
        tokenizer = TextTilingTokenizer()
        return tokenizer.tokenize(self.text)

    def _get_toc_(self):
        """
        Use regular expression to split the title or the enumeration of a document
        Generate a table of content
        :return:
        """
        pass