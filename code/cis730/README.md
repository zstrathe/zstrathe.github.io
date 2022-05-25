## Game-playing Reinforcement Learning Model Project: Python Code

#### Python notebook for training and evaluating models: <a href="https://github.com/zstrathe/zstrathe.github.io/blob/master/code/cis730/cis730_baselines.ipynb">Python Notebook</a>

#### Notebook for viewing TensorBoard (training logs): <a href="https://github.com/zstrathe/zstrathe.github.io/blob/master/code/cis730/cis730_tensorboard.ipynb">Python Notebook</a>

#### Custom Python libraries used:
- <a href="https://github.com/MatPoliquin/baselines-fix.git">https://github.com/MatPoliquin/baselines-fix.git</a> (a fork of OpenAI Baselines that fixes a bug which significantly improves training time)
- <a href="https://github.com/MatPoliquin/stable-retro.git">https://github.com/MatPoliquin/stable-retro.git</a> (a fork of OpenAI Retro that has more game integrations)

#### Code library modifications (<a href="https://github.com/zstrathe/zstrathe.github.io/tree/master/code/cis730/Modified%20Files">link to modified files</a>)
- baselines/run.py: 
    - line 57: added 'MarioBros-Nes' to _game_envs[retro] dict

- baselines/common/retro_wrappers.py:
  -	line 239: added 'MarioDiscretizer'
  -	line 251: added call to MarioDiscretizer when building environment
  -	line 253: modified WarpFrame parameters to specify width, height, and non-greyscale images

- baselines/common/cmd_util.py
  -	line 80: modified initilization of the Gym Retro environment to NOT use the default action space

- retro/data/stable/MarioBros-Nes/data.json
  -	Added "enemies" variable & memory location (for enemies remaining on level)

- retro/data/stable/MarioBros-Nes/updated_scenario_cropping.json
  - Added cropping of the game image

- retro/data/stable/MarioBros-Nes/updated_scenario_reward_func.json
  - Updated scenario for new reward function based on enemies remaining instead of game score

- retro/data/stable/MarioBros-Nes/rom.nes
  - Included ROM for game


---

<h3><a href="/">Back</a></h3>
