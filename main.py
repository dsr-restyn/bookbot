def main():
    with open("books/frankenstein.txt") as f:
        char_counts = {}
        text = f.read()
        words = text.split()
        for char in text:
            if char.isalpha() == False:
                continue
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        print(f"--- Begin report of {f.name} ---")
        print(f"{len(words)} words found in the text")
        print("                                 ")
        for char, count in char_counts.items():
            print(f"The '{char}' character was found {count} times")


if __name__ == "__main__":
    main()