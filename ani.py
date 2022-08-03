# Setup submodule path
import sys
import os
highway_env_path = os.path.join(os.getcwd(), "highway-env")
rl_agents_path = os.path.join(os.getcwd(), "rl-agents")
stable_baselines3_path = os.path.join(os.getcwd(), "stable-baselines3")
sys.path.append(highway_env_path)
sys.path.append(rl_agents_path)
sys.path.append(stable_baselines3_path)

import time

import gym
import highway_env

import stable_baselines3
from stable_baselines3.common.vec_env import DummyVecEnv

if __name__ == "__main__":
    # todo: set arg parser
    env_name = "highway-v0"
    algo_name = "DQN"  # must be the same with the alto you used to train
    model_path = "/home/songanz/Documents/Git_repo/highway-env&agents/outputs/stable_baseline_3/highway-v0/DQN/2022-08-03_03-26-45/model/best_model.zip"

    env = gym.make(env_name)
    env = DummyVecEnv([lambda: env])
    obs = env.reset()

    model_ = getattr(stable_baselines3, algo_name)
    model = model_("MlpPolicy", env, verbose=1)
    model.load(model_path)

    done = False
    while not done:
        rl_action, _ = model.predict(obs)
        obs, reward, done, info = env.step(rl_action)
        env.render()
