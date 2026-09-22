# Fruit Fly Crib Sesh

A 3D meme scene built with Three.js, rendered like a PlayStation 1 game
(240-line framebuffer, vertex snapping, 15-bit dithered colour). A sculpted fly
sits on a purple couch in a G-funk living room that floats in a swirling 90s
shadow realm, blunt at its mouth, headphones on, a Zune on the coffee table.
Next to it a low-poly homage to a certain Grove Street resident is smoking his
own. The room was assembled in Blender from CC0 kits (see Credits) and
exported as `assets/room.glb`. The third puff starts BONES —
IfYouHadAZuneIHateYou (ft. Spooky Black), from the free TeamSESH release
*Garbage*, at the opening hits and lets a long stretch play before it
fades. The corner readout lights up with the puffs.

Press **"Press to give the fly a hit"** and:

- a puff of smoke rolls off the blunt and hazes around the fly,
- the brain readout lights up from the centre outward, and a puff of smoke
  drifts across it too,
- a small firework pops out of the fly's head, and its eyes glow,
- the third puff flashes a rainbow line. The first time it says
  "Certified Baked", then "Fly High", then "Addicted!", and the
  synapses stay above a thousand for about half a minute.

Puffs stack. The meter shows how lit the fly is and slowly comes down.
The three dots under the button count toward the line.

## Run
    ./run.sh
then open http://localhost:8765. Drag to orbit, scroll to zoom.
Needs internet for the Three.js CDN. The song is a local file, so it does
not go through YouTube. The third puff, or the ▶ play control, starts at
the bass hits and plays for a while before fading (browsers block sound
until that click).

Append `?demo` to the URL to load already lit, with a rainbow line up.

## Files
- `index.html`: the whole scene, UI and effects.
- `assets/fly_model.js`: the fly model embedded as base64 so the page works
  from disk. `assets/fly.glb` is the same model as a plain file.
- `assets/room.glb`: the living room, the lowrider outside the window and the
  seated smoker, built by a headless Blender script from the kits below.
- `screenshot.png`: what it looks like. `seat_diagnostic.png`: the Blender
  check render used to line the smoker up with the couch.
- `assets/ifyouhadazuneihateyou.mp3`: BONES — IfYouHadAZuneIHateYou
  (ft. Spooky Black), TeamSESH, from *Garbage* (2014). BONES gives the
  catalog away. ℗ TeamSESH.
- `assets/opening.mp3`: a long stretch of that song, starting at the first
  bass hit. The third puff starts it, then it fades out.
- `data/raw/`: two small annotation tables from the public MaleCNS v1.0 fruit
  fly connectome (HHMI Janelia FlyEM / Cambridge / Google, CC-BY 4.0), kept as
  a downloaded prop. The page never reads them. The brain readout is a random
  point cloud with a colour animation, not a neuron model.

## Credits
- Fly model: "Spy Fly" by sunburn on OpenGameArt, CC-BY 3.0
  (https://opengameart.org/content/spy-fly). Decimated, recoloured, and the
  spy camera removed in Blender.
- Furniture, walls, boombox, lava lamp, plants: Kenney "Furniture Kit", CC0
  (https://kenney.nl/assets/furniture-kit). Recoloured.
- Lowrider outside the window: Kenney "Car Kit", CC0
  (https://kenney.nl/assets/car-kit).
- The smoker: "PS2 Styled Characters" by Wobble Blocks on OpenGameArt, CC0
  (https://opengameart.org/content/ps2-styled-characters). Retextured (white
  tank top, jeans) and posed in Blender. A fan homage, not a game rip.
- Wall and floor textures: "N64 Texture Pack" by n64guy on OpenGameArt, CC0
  (https://opengameart.org/content/n64-texture-pack). Tinted.
