# translate text.txt into japanese
# write translation on next line in file - didnt work, think its encoding issue from being japanese?
# install translate

from translate import Translator

try:
    with open("./test.txt", mode="r+") as source_file:
        source_text = source_file.read()
        translator = Translator(to_lang="ja")
        translation = translator.translate(source_text)
        print(f"Original Text: {source_text}")
        print(f"Translation: {translation}")
except IOError:
    print("You messed up")
