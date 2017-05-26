import random
from psychopy import visual

stim_text = {'RED': 'red', 'BLUE': 'blue', 'PINK': 'pink', 'BLACK': 'black', 'GREEN': 'green'}


def prepare_trial(trial_type, win, text_size):
    text = random.choice(stim_text.keys())
    if trial_type == 'congruent':
        color = stim_text[text]
    elif trial_type == 'incongruent':
        possible_colors = stim_text.values()
        possible_colors.remove(stim_text[text])
        color = random.choice(possible_colors)
    else:
        raise Exception('Wrong trigger type')

    stim = visual.TextStim(win, color=color, text=text, height=2*text_size)
    return {'trial_type': trial_type, 'text': text, 'color': color, 'stim': stim}


def prepare_part(trials_congruent, trials_incongruent, win, text_size):
    trials = ['congruent'] * trials_congruent + ['incongruent'] * trials_incongruent
    random.shuffle(trials)
    return [prepare_trial(trial_type, win, text_size) for trial_type in trials]


def prepare_exp(data, win, text_size):
    training_trials = prepare_part(data['Training_trials_congruent'], data['Training_trials_incongruent'], win,
                                   text_size)
    experiment_trials = prepare_part(data['Experiment_trials_congruent'], data['Experiment_trials_incongruent'], win,
                                     text_size)
    return training_trials, experiment_trials
