# Cosmic Evasion

* **Video Demo:** https://youtu.be/-db5b_puPJM
* **GitHub Repository:**  https://github.com/WavySnow/Cosmic-Evasion
## Description
**Cosmic Evasion** is an interactive 2D arcade game built in Python using the Pygame library. Players pilot a spaceship through deep space to dodge an endless barrage of falling asteroids while their survival score climbs in real time. Moving beyond simple geometric placeholders, the game incorporates custom sprite assets, automated background removal, and a multi-layered parallax starfield to create a polished retro arcade experience.

## Key Features
* **Dual-Scheme 2D Controls:** Supports both `WASD` and `Arrow keys` via continuous key-state polling (`pygame.key.get_pressed()`) for smooth 4-directional movement locked safely inside the 800x600 window boundaries.
* **Custom Sprite Processing:** Includes a custom `load_sprite()` pipeline that dynamically strips white backgrounds from image files, crops transparent padding using `get_bounding_rect()`, and scales assets cleanly.
* **Parallax Starfield Background:** Generates 80 background stars across three distinct speed and brightness tiers (`1`, `2`, and `3` px/frame) to simulate depth and forward motion in space, which continues animating even on the Game Over screen.
* **Procedural Asteroid Spawning:** Spawns asteroids at randomized horizontal positions and sizes (`35px` to `70px`) every 30 frames, automatically removing off-screen obstacles to maintain steady performance.
* **Forgiving Hitbox Collision & Instant Reset:** Uses slightly deflated `pygame.Rect` bounding boxes (`inflate(-10, -10)` for the ship and `inflate(-8, -8)` for asteroids) for fair collision detection, triggering a "GAME OVER" overlay with a one-button `[SPACE]` restart and `[ESC]` quit option.

## Repository Files
* `main.py` *(replace with your exact `.py` filename)*: Contains the complete Pygame initialization, custom `load_sprite()` image-processing helper, parallax star generator, main 60 FPS game loop, collision logic, and UI rendering.
* `Assets/`: Directory containing the visual game sprites:
  * `Halo ship.jpeg`: Player spaceship sprite (processed at runtime to remove its white background and scaled to `50x60`).
  * `Asteroid.png`: Base asteroid hazard sprite (dynamically scaled to random sizes as obstacles spawn).
* `README.md`: Project documentation detailing functionality, file structure, design choices, and future enhancements.

## Design Considerations & Challenges
* **Runtime Image Cleanup:** Because the player ship (`Halo ship.jpeg`) came with a solid white background, I wrote a pixel-iteration loop inside `load_sprite()` that converts near-white pixels (`RGB > 240`) into transparent alpha pixels and trims excess transparent borders before scaling.
* **Fair Collision Detection:** Raw rectangular hitboxes around irregularly shaped sprites often cause frustrating "ghost hits" on empty corners. To make the controls feel responsive and fair, I used Pygame's `.inflate()` method with negative values on both the player and asteroid rects so collisions only trigger when the visible sprites actually overlap.
* **Memory Management:** Iterating over a copy of the active obstacle list (`for asteroid in asteroids[:]`) allowed asteroids that pass below the bottom of the screen (`top > HEIGHT`) to be safely removed without skipping items or leaking memory during long runs.

## Future Improvements
* **Progressive Difficulty Scaling:** Gradually decrease the `spawn_counter` threshold or increase asteroid fall speed as the player's score rises so survival becomes progressively harder over time.
* **Audio & Visual Feedback:** Add background space synth music, explosion animations on impact, and thruster particle effects behind the ship.
* **High Score Persistence:** Store the player's highest score in a local file so records carry over across game sessions.
