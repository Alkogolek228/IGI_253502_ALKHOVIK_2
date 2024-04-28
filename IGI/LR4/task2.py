import re
import zipfile

class TextAnalyzer:
    """
    A class for analyzing text files.

    Args:
        source_file (str): The path to the source file.
        result_file (str): The path to the result file.

    Attributes:
        source_file (str): The path to the source file.
        result_file (str): The path to the result file.
        zip_file (str): The name of the zip file.

    Methods:
        analyze(): Analyzes the text from the source file.
        save(): Saves the analysis results to the result file.
        archive(): Archives the result file.
        get_info(): Retrieves information about the file in the archive.
    """

    def __init__(self, source_file, result_file):
        self.source_file = source_file
        self.result_file = result_file
        self.zip_file = 'result.zip'

    def analyze(self):
        """
        Analyzes the text from the source file.

        Reads the text from the source file and finds the required information, such as sentences,
        declarative sentences, interrogative sentences, imperative sentences, words, and emoticons.
        """

        with open(self.source_file, 'r') as f:
            text = f.read()

        self.sentences = re.findall(r'[\.!?]', text)
        self.countsentences = re.split(r'[\.!?]', text)
        self.declarative_sentences = [s for s in self.sentences if re.search(r'\.', s)]
        self.interrogative_sentences = [s for s in self.sentences if re.search(r'\?', s)]
        self.imperative_sentences = [s for s in self.sentences if re.search(r'\!', s)]
        self.words = re.findall(r'\b\w+\b', text)
        self.emoticons = re.findall(r'[:;]-*[()\[\]]+', text)

    def save(self):
        """
        Saves the analysis results to the result file.

        Writes the analysis results, such as the number of sentences, declarative sentences,
        interrogative sentences, imperative sentences, average sentence length, average word length,
        and number of emoticons, to the result file.
        """

        with open(self.result_file, 'w') as f:
            f.write(f'Number of sentences: {len(self.countsentences)}\n')
            f.write(f'Number of declarative sentences: {len(self.declarative_sentences)}\n')
            f.write(f'Number of interrogative sentences: {len(self.interrogative_sentences)}\n')
            f.write(f'Number of imperative sentences: {len(self.imperative_sentences)}\n')
            f.write(f'Average sentence length: {sum(len(s) for s in self.countsentences) / len(self.countsentences)}\n')
            f.write(f'Average word length: {sum(len(w) for w in self.words) / len(self.words)}\n')
            f.write(f'Number of emoticons: {len(self.emoticons)}\n')

    def archive(self):
        """
        Archives the result file.

        Archives the result file into a zip file.
        """

        with zipfile.ZipFile(self.zip_file, 'w') as zipf:
            zipf.write(self.result_file)

    def get_info(self):
        """
        Retrieves information about the file in the archive.

        Retrieves information about the file in the archive, such as the compressed file size
        and the uncompressed file size.
        """

        with zipfile.ZipFile(self.zip_file, 'r') as zipf:
            info = zipf.getinfo(self.result_file)
            print(f'Compressed file size: {info.compress_size} bytes')
            print(f'Uncompressed file size: {info.file_size} bytes')

# Usage
#analyzer = TextAnalyzer('source.txt', 'result.txt')
#analyzer.analyze()


def task_2():
    # Create an instance of TextAnalyzer
    analyzer = TextAnalyzer('source.txt', 'result.txt')

    # Analyze the text
    analyzer.analyze()

    # Get all words in the text
    words = analyzer.words

    # Find all pairs of characters where the first is a lowercase letter and the second is an uppercase letter
    pairs = re.findall(r'[a-z][A-Z]', ' '.join(words))
    highlighted_pairs = ['_?_' + pair + '_?_' for pair in pairs]

    # Find the number of words that are less than 7 characters long
    short_words = [word for word in words if len(word) < 7]
    num_short_words = len(short_words)

    # Find the shortest word that ends with 'a'
    words_ending_with_a = [word for word in words if word.endswith('a')]
    shortest_word_ending_with_a = min(words_ending_with_a, key=len)

    # Sort all words in descending order of their length
    words_sorted_by_length = sorted(words, key=len, reverse=True)

    # Print the results
    print(f'Highlighted pairs: {highlighted_pairs}')
    print(f'Number of short words: {num_short_words}')
    print(f'Shortest word ending with "a": {shortest_word_ending_with_a}')
    print(f'Words sorted by length: {words_sorted_by_length}')

    analyzer.save()
    analyzer.archive()
    analyzer.get_info()

