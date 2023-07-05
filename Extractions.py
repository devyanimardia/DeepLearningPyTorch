import spacy
import textacy.extract

nlp = spacy.load('en_core_web_lg') #This is the model

#Text to examine

text = """London is the capital and most populous city of England and  the United Kingdom.  
Standing on the River Thames in the south east of the island of Great Britain, 
London has been a major settlement  for two millennia.  It was founded by the Romans, 
who named it Londinium.
"""

doc = nlp(text)

statements = textacy.extract.semistructured_statements(doc, entity="London", cue=("be"))
print("Here are the things I know about London:")

for statement in statements:
    subject, verb, fact = statement
    print(f' - {fact}')
