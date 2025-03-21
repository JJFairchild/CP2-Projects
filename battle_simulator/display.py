import matplotlib.pyplot as plt
import numpy as np

def visualize(chars):
    names = []
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

    sex_counts = {
        'Health': np.array(healths),
        'Strength': np.array(strengths),
        'Defense': np.array(defenses),
        'Speed': np.array(speeds),
    }
    width = 0.6  # the width of the bars: can also be len(x) sequence


    fig, ax = plt.subplots()
    bottom = np.zeros(len(names))

    for sex, sex_count in sex_counts.items():
        p = ax.bar(names, sex_count, width, label=sex, bottom=bottom)
        bottom += sex_count

        ax.bar_label(p, label_type='center')

    ax.set_title('Character statistics')
    ax.legend()

    plt.show()

visualize([])