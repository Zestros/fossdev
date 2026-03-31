def reverse_text(text):
    return text[::-1]


def main():
    text = input("Enter text: ")
    print(reverse_text(text))


if __name__ == "__main__":
    main()