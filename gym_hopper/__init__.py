from gym.envs.registration import register


register(
    id="hopper-sac-v0",
    entry_point="gym_hopper.envs:GymHopperSAC",
    timestep_limit=10000)

register(
    id="hopper-pc-v0",
    entry_point="gym_hopper.envs:GymHopperPC",
    timestep_limit=10000)

