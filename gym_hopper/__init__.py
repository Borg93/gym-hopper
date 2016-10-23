from gym.envs.registration import register


register(
    id="hopper-v0",
    entry_point="gym_hopper.envs:GymHopper",
    timestep_limit=1000)
