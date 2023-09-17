import translators as tt

print('Enter your text:')
mytext = input()
mytstext = tt.translate_text(mytext, translator='bing', to_language='de')
#mytstext = 'Blumentopf'
print(mytstext)