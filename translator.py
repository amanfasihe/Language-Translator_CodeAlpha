from googletrans import Translator

def show_menu():
    print("\n===== Language Translation Tool =====")
    print("Type 'exit' to quit\n")

def translate_text(text, dest_lang):
    translator = Translator()
    result = translator.translate(text, dest=dest_lang)
    return result.text

def main():
    show_menu()

    while True:
        text = input("\nEnter text: ")

        if text.lower() == "exit":
            print("Goodbye!")
            break

        lang = input("Enter target language code (en, ur, fr, de, es, ar): ")

        try:
            translated = translate_text(text, lang)
            print("Translated:", translated)
        except Exception as e:
            print("Error occurred:", e)

main()