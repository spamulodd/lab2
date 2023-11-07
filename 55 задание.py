class Text:

  def __init__(self, text):
    self.text = text

  def get_char_count(self):
    return len(self.text)

  def get_letter_count(self):
    return len([x for x in self.text if x.isalpha()])

  def get_space_count(self):
    return self.text.count(' ')

  def get_char_without_spaces(self):
    return len([x for x in self.text if not x.isspace()])

  def get_words(self):
    return self.text.split()

  def get_sentences(self):
    return self.text.split('.')

text = Text("Hello world. This is some text with spaces.")

print(text.get_char_count())
print(text.get_letter_count())
print(text.get_space_count())
print(text.get_char_without_spaces())
print(text.get_words())
print(text.get_sentences())