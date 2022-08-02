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

env = gym.make("highway-v0")

done = False
while not done:
    action = ... # Your agent code here
    obs, reward, done, info = env.step(action)
    env.render()