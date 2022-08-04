# highway-env&agents
A collection of environments for *autonomous driving* and *RL agents* for decision making

## 1. Installation
1. Builder docker using docker file
```sh
cd docker
./build_docker.sh
```
2. After successfully build the docker 

in docker folder, run: 
```sh
./run_container.sh
```
## 2. The environments
Please check the readme of sub module highway-env

## 3. The RL agents
This repo include two popular RL library as sub modules:
1. stable_baselines3
2. rl_agents

Please refer to the readme of the original sub modules

## 4. Examples
### 4.1 Simple Usage
```python
import gym
import highway_env

env = gym.make("highway-v0")
obs = env.reset()

done = False
while not done:
    action = env.action_space.sample() # for simple usage, you can just sample action space
    obs, reward, done, info = env.step(action)
    env.render()
```

### 4.2 Training
1. stable_baselines3
Please check script `train_stable_baselines3.py` which is setup using stable_baselines3
2. rl_agents
Please check bash script `train_rl_agents.sh` for setting up training using rl_agents

### 4.3 Plot training curve
1. stable_baselines3
Please check script `plot.py`, and write your own
2. rl_agents
TBD

### 4.4 Load trained policy
1. stable_baselines3
Please check script `ani.py`, and write your own
2. rl_agents
TBD

## Reference 
[Gym Documentation](https://www.gymlibrary.ml/)