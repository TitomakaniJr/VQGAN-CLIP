import random
import re
import sys
import os

templates = []
templates_filename = 'templates.txt'

# Below is all the data needed to parse the different word types
# {type}s - The object that will hold all data parsed from the given files
# {type}s_dir - The directory where all the files of a given word type are stored
# {type}_files - A list of files which should be parsed for the word type. With this you can create your own word files
# and control exactly what dataset you want to include during generation. Files should have a single entry on each line

actors = []
actors_dir = "actors\\"
actor_files = [
    'batman.txt',
    'spongebob.txt',
    'starwars.txt'
]

adjectives = []
adjectives_dir = "adjectives"
adjective_files = [
    'adjectives.txt'
]

nouns = []
nouns_dir = "nouns"
noun_files = [
    'nouns.txt'
]

mediums = []
medium_dir = "mediums"
medium_files = [
    'mediums.txt'
]

objects = []
objects_dir = "objects"
object_files = [
    'objects.txt'
]

places = []
places_dir = "places"
place_files = [
    'places.txt'
]

styles = []
styles_dir = "styles"
style_files = [
    'styles.txt'
]

times = []
times_dir = "times"
time_files = [
    'times.txt'
]

verbs = []
verbs_dir = "verbs"
verb_files = [
    'verbs.txt'
]
    
def InitGenerator():
    ReadTemplates(templates_filename)
    
    # TODO: Create word list struct list and loop over that instead of doing all these in-line calls
    ReadWordList(actors_dir, actor_files, actors)
    ReadWordList(adjectives_dir, adjective_files, adjectives)
    ReadWordList(nouns_dir, noun_files, nouns)
    ReadWordList(medium_dir, medium_files, mediums)
    ReadWordList(objects_dir, object_files, objects)
    ReadWordList(places_dir, place_files, places)
    ReadWordList(styles_dir, style_files, styles)
    ReadWordList(times_dir, time_files, times)
    ReadWordList(verbs_dir, verb_files, verbs)

def GeneratePrompt():
    prompt = ParseSentence(random.choice(templates))
    return prompt

# Parse a given sentence, replacing any prompt tokens with valid data
def ParseSentence(sentence):
    output = ''
    
    for word in sentence.split(' '):
        if not output == '':
            output += ' '
            
        # Replace word type tokens with valid data
        if word == 'ACTOR':
            output += random.choice(actors)
        elif word == 'ADJECTIVE':
            output += random.choice(adjectives)
        elif word == 'NOUN':
            output += random.choice(nouns)
        elif word == 'MEDIUM':
            output += random.choice(mediums)
        elif word == 'OBJECT':
            output += random.choice(objects)
        elif word == 'PLACE':
            output += random.choice(places)
        elif word == 'STYLE':
            output += random.choice(styles)
        elif word == 'TIME':
            output += random.choice(times)
        elif word == 'VERB':
            output += random.choice(verbs)
        else:
            output += word

    return output

# Parse all world lists for a given word type
def ReadWordList(file_dir, filenames, list):
    for filename in filenames:
        with open(GetLocalPath(os.path.join(file_dir, filename)), 'r') as f:
            for line in f:
                word = line.strip()
                list.append(word)
            
# Parse all random templates
def ReadTemplates(filename):
    with open(GetLocalPath(filename), 'r') as f:
        for line in f:
            line = line.strip()
            templates.append(line)
            
def GetLocalPath(filename):
    return os.path.join(os.path.dirname(__file__), filename)
    
if __name__ == '__main__':
    InitGenerator()
    GeneratePrompt()
    
    
    
    
    
