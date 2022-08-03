import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    matplotlib.use('TkAgg')

    path = "/home/songanz/Documents/Git_repo/highway-env&agents/outputs/stable_baseline_3/highway-v0/DQN/2022-08-03_03-26-45/eval/evaluations.npz"
    data = np.load(path)
    # print(data.files)
    # print(data['results'])
    x = np.arange(0, len(data['results']), 1)
    y = np.mean(data['results'], 1)
    ci = np.std(data['results'], axis=1)

    fig, ax = plt.subplots()

    ll = ax.plot(x, y, label="DQN", color='r')
    ax.fill_between(x, (y-ci), (y+ci), color='r', alpha=.1)

    ax.legend()
    ax.set_xlabel('Total Timesteps')
    ax.set_ylabel('Mean Cumulative Reward (over 5 evaluation)')
    plt.show()