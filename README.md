# TsiolkovskyRocketEqSim
Rocket Equation Simulator
This program lets you explore rocket motion using either the ideal Tsiolkovsky rocket equation or a more realistic simulation that includes gravity and air drag. It features interactive user input and animated plots to help you visualize how rockets perform under different conditions.

Features:

Two simulation modes:
Tsiolkovsky Rocket Equation: Calculates and animates the ideal change in velocity (Δv) for a rocket in a vacuum, ignoring gravity and drag.
Realistic Simulation: Numerically simulates a rocket launch with gravity, air resistance, and mass loss, animating altitude, velocity, and acceleration over time.
Interactive input: Prompts the user for all relevant rocket parameters, with sensible defaults.
Animated visualization: Uses Matplotlib to animate the results for both modes.
How to Use:

Run the script.
Choose a simulation mode:
Enter 1 for the ideal Tsiolkovsky rocket equation.
Enter 2 for the realistic simulation with gravity and drag.
Enter rocket parameters as prompted (or press Enter to use defaults).
View the animated results in a pop-up window.
Requirements:

Python 3.x
numpy
matplotlib
What is Simulated?

In Tsiolkovsky mode, the program calculates Δv using the formula Δv = ve * ln(mi / mf), where ve is exhaust velocity, mi is initial mass, and mf is final mass. The animation shows velocity ramping up to Δv.
In realistic mode, the program simulates the rocket's ascent, accounting for gravity, air drag (with user-settable drag coefficient and cross-sectional area), decreasing mass due to fuel burn, and thrust from exhaust velocity and mass flow rate. It animates altitude, velocity, and acceleration over time.
Educational Value:

This tool is ideal for students and enthusiasts who want to:

Understand the difference between ideal and real rocket motion
Visualize the impact of gravity and drag on rocket performance
Experiment with different rocket parameters interactively
Enjoy exploring rocket science!
