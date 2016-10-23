from io import StringIO
import sys

import gym
from gym import error, spaces, utils
from gym.utils import seeding

class GymHopper(gym.Env):
   def __init__(self):
    print("__init__! yusss")
  def _step(self, action):
    print("step! yusss")
  def _reset(self):
    print("reset! yusss")
  def _render(self, mode='human', close=False):
    print("render! yusss")
