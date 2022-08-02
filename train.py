
import sys
import os
highway_env_path = os.path.join(os.getcwd(), "highway-env")
rl_agents_path = os.path.join(os.getcwd(), "rl-agents")
stable_baselines3_path = os.path.join(os.getcwd(), "stable-baselines3")
# add sub module path
sys.path.append(highway_env_path)
sys.path.append(rl_agents_path)
sys.path.append(stable_baselines3_path)

import gym
import highway_env
import stable_baselines3
import rl_agents

env = gym.make("highway-v0")
env.reset()

done = False
while not done:
    action = 0 # Your agent code here
    obs, reward, done, info = env.step(action)
    env.render(mode='rgb_array')