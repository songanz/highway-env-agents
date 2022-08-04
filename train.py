# Setup submodule path
import sys
import os
highway_env_path = os.path.join(os.getcwd(), "highway-env")
sys.path.append(highway_env_path)
stable_baselines3_path = os.path.join(os.getcwd(), "stable-baselines3")
sys.path.append(stable_baselines3_path)

import time

import gym
import highway_env

import stable_baselines3
from stable_baselines3.common.callbacks import CheckpointCallback, CallbackList, EvalCallback
from stable_baselines3.common.logger import configure
from stable_baselines3.common.monitor import Monitor

if __name__=="__main__":
    # todo: set arg parser
    env_name = "highway-v0"
    algo_name = 'DQN'

    env = gym.make(env_name)
    model_ = getattr(stable_baselines3, algo_name)
    model = model_("MlpPolicy", env, verbose=1)

    base_folder = os.path.join("./outputs/stable_baseline_3/", env_name, algo_name)
    log_dir = os.path.join(base_folder, time.strftime('%Y-%m-%d_%H-%M-%S'))
    model_path = os.path.join(log_dir, 'model/')
    os.makedirs(model_path, exist_ok=True)
    eval_path = os.path.join(log_dir, 'eval/')
    os.makedirs(eval_path, exist_ok=True)

    logger = configure(eval_path, ['stdout', 'csv', 'tensorboard'])
    model.set_logger(logger)

    checkpoint_callback = CheckpointCallback(save_freq=1000, save_path=model_path, name_prefix='rl_model')
    env_eval = Monitor(env, eval_path)
    eval_callback = EvalCallback(env_eval, best_model_save_path=model_path, log_path=eval_path, n_eval_episodes=5, eval_freq=50)
    callback = CallbackList([checkpoint_callback, eval_callback])
    model.learn(total_timesteps=int(1e7), callback=callback)
