# ARC-AGI-3 Kaggle Agent

This project explores agents for the ARC Prize 2026 ARC-AGI-3 Kaggle competition. The goal is to build an agent that can interact with unfamiliar ARC games, learn from the game state and action history, and complete as many levels as possible.

Current work is based on the competition starter notebook. It includes a simple random-action baseline (`MyAgent`) and the Kaggle notebook structure needed for the competition's hidden evaluation rerun.

The next step is to replace the random decisions in `MyAgent.choose_action(...)` with a strategy that reads game frames, selects purposeful actions, and improves through repeated attempts.
