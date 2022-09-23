# translate text.txt into japanese
# write translation on next line in file - didnt work, think its encoding issue from being japanese?
# install translate

from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open("./test.txt", mode="r") as source_file:
        source_text = source_file.read()
        translation = translator.translate(source_text)
        print(f"Original Text: {source_text}")
        print(f"Translation: {translation}")
        # Write disabled due to encode error
        # with open("text-ja.txt", mode="w") as my_file_ja:
        #     my_file_ja.write(translation)
except IOError:
    print("You messed up")
