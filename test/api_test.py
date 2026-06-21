"""Test the Aquarium environment with a random agent."""
from gymnasium.spaces import Box, Discrete
from pettingzoo.test import api_test, parallel_api_test

from marl_aquarium.aquarium_v0 import env, parallel_env

# Verify action space types match the continuous_actions flag
_disc_env = parallel_env()
_cont_env = parallel_env(continuous_actions=True)
_sample_agent = _disc_env.possible_agents[0]
assert isinstance(_disc_env.action_space(_sample_agent), Discrete), "Default should be Discrete"
assert isinstance(_cont_env.action_space(_sample_agent), Box), "continuous_actions=True should be Box"
del _disc_env, _cont_env, _sample_agent

# Discrete mode conformance (default)
parallel_api_test(parallel_env(), num_cycles=1_000_000)
api_test(env(), num_cycles=1_000_000, verbose_progress=True)

# Continuous mode conformance
parallel_api_test(parallel_env(continuous_actions=True), num_cycles=1_000_000)
api_test(env(continuous_actions=True), num_cycles=1_000_000, verbose_progress=True)
