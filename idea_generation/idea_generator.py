import random
import re
import sys
import os

templates = []
templates_filename = 'templates.txt'

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
    ReadWordList(objects_dir, object_files, objects)
    ReadWordList(places_dir, place_files, places)
    ReadWordList(times_dir, time_files, times)
    ReadWordList(verbs_dir, verb_files, verbs)

def GenerateIdea():
    idea = ParseSentence(random.choice(templates))
    return idea

def ParseSentence(sentence):
    output = ''
    
    for word in sentence.split(' '):
        if not output == '':
            output += ' '
            
        if word == 'ACTOR':
            output += random.choice(actors)
        elif word == 'ADJECTIVE':
            output += random.choice(adjectives)
        elif word == 'NOUN':
            output += random.choice(nouns)
        elif word == 'OBJECT':
            output += random.choice(objects)
        elif word == 'PLACE':
            output += random.choice(places)
        elif word == 'TIME':
            output += random.choice(times)
        elif word == 'VERB':
            output += random.choice(verbs)
        else:
            output += word

    return output
    
def ReadWordList(file_dir, filenames, list):
    for filename in filenames:
        with open(GetLocalPath(os.path.join(file_dir, filename)), 'r') as f:
            for line in f:
                word = line.strip()
                list.append(word)
            
def ReadTemplates(filename):
    with open(GetLocalPath(filename), 'r') as f:
        for line in f:
            line = line.strip()
            templates.append(line)
            
def GetLocalPath(filename):
    return os.path.join(os.path.dirname(__file__), filename)
    
if __name__ == '__main__':
    InitGenerator()
    GenerateIdea()
    
    
    
    
    
