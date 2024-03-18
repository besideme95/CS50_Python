vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

def main():
   prompt = input('Input: ')
   f = body(prompt)
   print(f'Output: {f}')

def body(x):
  final_sentences = ''
  for word in x:
    new_word = ''
    for letter in word:
       if letter not in vowels:
         new_word += letter
       else:
         new_word += ''
    final_sentences += new_word
  return final_sentences

main()


