import pandas as pd
from collections import Counter
import copy

def remove_analyzers(chars, analyzers):
    return [char for char in chars if char['name'] not in analyzers and char['name'] != '-']

def analyze(chars): # Master function for analyzing things
    props = ['health', 'strength', 'defense', 'speed', 'level'] # Some iterative lists
    analyzers = ['-', 'mean', 'median', 'mode', 'max', 'min']
    
    filler = {'name': '-'} # Profiles that will be filled out and added to 'chars' for display
    mean = {'name': 'Mean'}
    median = {'name': 'Median'}
    mode = {'name': 'Mode'}
    max = {'name': 'Max'}
    min = {'name': 'Min'}

    for analyzer in analyzers:
        for prop in props:
            sort = []
            for char in chars:
                if char['name'].lower() not in analyzers and char['name'].lower() != '-': # Makes sure that no previously analyzed data is analyzed again
                    sort.append(char[prop])
            sort.sort()
            match analyzer: # Decides what to do with the data, then adds it to one of the above profiles depending on the analyzer.
                case 'mean':
                    mean[prop] = sum(sort)/len(sort)
                case 'median':
                    median[prop] = sort[int(len(sort)/2)]
                case 'mode':
                    counts = Counter(sort)
                    mode[prop] = counts.most_common(1)[0][0]
                case 'max':
                    max[prop] = sort[-1]
                case 'min':
                    min[prop] = sort[0]
                case '-':
                    filler[prop] = '-'

    display = copy.deepcopy(chars)
    for i in [filler, mean, median, mode, min, max]: # Adds the profiles to chars
        display.append(i)
    df = pd.DataFrame(display) # Displays the data frame.
    print(df)