from misc import generate_random_text

def analyze_text(s):
    """
    Analyzes the given text and performs the following tasks:
    а) Determines the number of lowercase letters in the text.
    б) Finds the first word that contains the letter 'v' and its position.
    в) Prints the text with words starting with 's' removed.

    Args:
        s (str): The text to be analyzed.

    Returns:
        None
    """
    lowercase_letters = sum(c.islower() for c in s)
    print(f"Количество строчных букв: {lowercase_letters}")

    words = s.split()
    for i, word in enumerate(words):
        if 'v' in word.lower():
            print(f"Первое слово, содержащее букву 'v': {word}, его номер: {i+1}")
            break

    new_s = ' '.join(word for word in words if not word.lower().startswith('s'))
    print(f"Строка без слов, начинающихся на 's': {new_s}")