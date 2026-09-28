import random
import time
from typing import Any

from arcengine import FrameData, GameAction, GameState
from agents.agent import Agent


class MyAgent(Agent):
    """Random agent — picks a random action each step.

    Modify this class to implement your own agent strategy!
    """

    # The base Agent normally stops after 80 actions. This demo removes
    # that cap, so the run ends only after the game reaches WIN.
    MAX_ACTIONS = float('inf')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # Mix the current time and game ID to vary the random action stream.
        seed = int(time.time() * 1000000) + hash(self.game_id) % 1000000
        random.seed(seed)

    def is_done(self, frames: list[FrameData], latest_frame: FrameData) -> bool:
        # GAME_OVER is not terminal: choose_action will RESET and try again.
        return latest_frame.state is GameState.WIN

    def choose_action(self, frames: list[FrameData], latest_frame: FrameData) -> GameAction:
        if latest_frame.state in [GameState.NOT_PLAYED, GameState.GAME_OVER]:
            # Start a new attempt before making a move.
            action = GameAction.RESET
        else:
            # Once in progress, choose uniformly from every non-reset action.
            action = random.choice([a for a in GameAction if a is not GameAction.RESET])

        if action.is_simple():
            # Simple actions need no coordinates; reasoning is only metadata.
            action.reasoning = f"RNG told me to pick {action.value}"
        elif action.is_complex():
            # Complex actions need a position. This baseline guesses on a
            # 64×64 grid instead of reading the frame.
            action.set_data({
                "x": random.randint(0, 63),
                "y": random.randint(0, 63),
            })
            action.reasoning = {
                "desired_action": f"{action.value}",
                "my_reason": "RNG said so!",
            }
        return action
