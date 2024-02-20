def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    letters = letter_count(text)
    reported = report(book_path, words, letters)
    print(reported)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letter_dict = {}
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict

def report(book_path, words, letters):
    report_output = f"=== This is the report of {book_path} ===\n"
    report_output += f"There are {words} words found in this book!\n"
    sorted_report = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    for letter, count in sorted_report.items():
        report_output += f"The '{letter}' letter was found {count} times!\n"
    return report_output

main()