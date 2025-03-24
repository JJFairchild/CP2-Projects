import matplotlib.pyplot as plt
import numpy as np

def visualize(chars):
    names = [] # Gets lists of every relevant property
    healths = []
    strengths = []
    defenses = []
    speeds = []

    for char in chars:
        names.append(char['name'])
        healths.append(char['health'])
        strengths.append(char['strength'])
        defenses.append(char['defense'])
        speeds.append(char['speed'])

    type_counts = { # Organizes the lists into things that can be graphed
        'Health': np.array(healths),
        'Strength': np.array(strengths),
        'Defense': np.array(defenses),
        'Speed': np.array(speeds),
    }
    width = 0.6  # the width of the bars: can also be len(x) sequence


    fig, ax = plt.subplots()
    bottom = np.zeros(len(names))

    for type, type_count in type_counts.items(): # Graphs the information into a bar graph.
        p = ax.bar(names, type_count, width, label=type, bottom=bottom)
        bottom += type_count

        ax.bar_label(p, label_type='center')

    ax.set_title('Character statistics')
    ax.legend()

    plt.show()