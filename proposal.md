# Project Proposal: Cosmic Evasion

## Description
**Cosmic Evasion** is an interactive 2D arcade game built in python where players maneuver a space rocket to survive an increasingly dense feild of asteroids. This project explores real time user interactivity and procedural asset generation, demonstrating how programming fundamentals combine to create engaging digital arts and media experiences.

## Key Features
 **Dynamic Rocket Controls**
   Handled by utilizing Pygame's keyboard event listeners to capture responsive players movement across 2D plane (supporting both 'WASD' and 'Arrow keys') while locking the sprits boundries safely inside the screen edges.
 **Procedurally Generate Hazards**
   Built using a tracking system that spawns astroids obstacles at random cordinates above the viewport, utilizing time base increments to increase downward volocity as playtime increases.
 **Collision Tracking and State Management**
   Managed by monitoring axis-aligned bounding boxes around active objects, instantly triggering a game-over screen overlay and score calculation upon detection.
## Challenges
Learning how to use standard Pygame clocks to keep the block movements consistent at 60 frames per second.
Tracking and safely updating lists of falling rectangles so that obstacles can be added and removed from memory without crashing the game.
Structuring conditional if/else states to toggle between the active game loop and a static text menu upon a collision.

## Project Outcomes

## Ideal Outcome
A fully functional game that gets harder over time, featuring a live score display on a black background, fluid keyboard responses, and an instant game-over reset routine.

## Minimal Viable Outcome
 A screen where a player box can be moved left and right to avoid falling obstacle boxes, displaying a final score when a collision is recorded.

## Timeline Milestones

Week 1
  1. Initialize the base window setup, set up the game loop, and draw a solid black background.
  2. Implement a player box sprite with responsive dual WASD and Arrow key controls.

Week 2
  1. Add a timer system that spawns falling red rectangles at random horizontal positions at the top of the window.
  2. Implement boundary restrictions to prevent the player box from slipping off the screen edges.

Week 3 (Final)
  1. Code collision detection using rect bounding boxes that triggers a text-based "GAME OVER" screen overlay.
  2. Implement a live score tracker and add spacebar listener logic to completely reset the game metrics back to default values.