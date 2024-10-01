def correct_sentence(text):

    text = text.split()
    if len(text) > 1:
        title = text[0].title() + " "
        split = str(title + text[-1])
    else:
        title = text[0].title()
        split = str(title)
    if split.endswith("."):
        return f"{split}"
    else:
        result = split + "."
        return f"{result}"
print(correct_sentence("greeting, firends"))
print(correct_sentence("hello"))
print(correct_sentence("Greeting. Firends"))
print(correct_sentence("Greeting, firends."))
print(correct_sentence("greeting, firends."))