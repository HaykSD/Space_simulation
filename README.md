# Space Simulator with Pygame

![Simulator Screenshot](https://github.com/HaykSD/Space_simulation/assets/60398571/17005a26-83d8-4e25-bd9e-38e392caf8a7)

This is a space simulator created with Pygame that allows you to explore the movements and interactions of celestial bodies in a virtual space. You can add, modify, and observe planets as they traverse their trajectories.

## Features

1. **Planet Creation**: You can create new planets by clicking the right mouse button on the screen. Each planet is represented by a colorful orb.🌍

2. **Planet Size Adjustment**: Scroll your mouse wheel to adjust the current planet size. This feature lets you experiment with the relative sizes of celestial bodies.✅

3. **Applying Forces**: To apply forces to a planet, hold the left mouse button and move the cursor in the desired direction. A direction vector will be displayed, and when you release the button, the planet will continue moving in that direction and can interact with other planets.☄️

4. **Interactions**: Planets interact with each other in this simulation. They can be attracted or repelled based on their positions and masses.🎇🪄🧲

5. **Planet collisions**: Result in the formation of a new, larger planet.☢️

6. **Automatic Deletion**: To keep the simulation manageable, planets that move too far away from the screen are automatically deleted.❌


## Getting Started

To run the simulator, you'll need Python and Pygame installed on your system. You can install Pygame using pip:

```bash
git clone https://github.com/HaykSD/Space_simulation.git
cd Space_simulation
pip3 install -r requirements.txt
```

## Running command
```bash
python3 space_sim.py
