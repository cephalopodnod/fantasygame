# Project Plan — fantasygame (working title)

_Last updated: 2026-10-21_

## 1. Decisions

| Area | Decision |
|---|---|
| Rules base | D&D 5e **2014** rules (SRD 5.1) as the foundation |
| Rules on top | Our own **skill trees** and **subclasses** layered over the 2014 classes, plus house rules (low-man bonus, XP/anti-farming, Jester curses) |
| Setting | Classic fantasy, with room for custom items and creatures. Original world, still to be created (no map yet) |
| Engine | Python + **Panda3D** (3D) |
| Feel | **Like Baldur's Gate 3**: real-time exploration, turn-based combat with initiative, 3D camera, dialogue with skill checks, environmental interactions |
| Combat grid | **Hex grid**, 5 ft per hex, with height levels — **combat only**; free movement while exploring |
| Dice | **Every roll is fresh and unique.** Reloading a save and retrying gives a new result |
| Multiplayer | **Co-op only**, up to 5 players. Each player controls one character; the host controls any party members nobody else is playing. Join by **direct IP and Steam** |
| Solo | Fully playable solo (the player is the host and controls the whole party) |
| Classes | All 12 classes from the 2014 rules |
| Art | You make the final art; we plan around **placeholders** until then |
| Platform | **Windows first**; sold on **Steam** eventually |
| Goal | Commercial release, ~40 hrs/week, deep systems, good graphics |
| Legacy code | Rewrite from scratch; reuse only content that is accurate and complete (§10) |
| Developer | Minimal game-programming experience; priority is building it right for the long term rather than fast |

## 2. Constraints that follow

### 2.1 Licensing (commercial release)
The 2014 rules can be shipped commercially **only through SRD 5.1** (CC‑BY‑4.0, credit required).

SRD 5.1 gives us all 12 classes (levels 1–20) with **one subclass each**, nine races (one subrace each), one background (Acolyte), one feat (Grappler), most spells, equipment, conditions and a large monster list.

Everything else — extra subclasses, skill trees, backgrounds, feats, the world, its gods and names — is **original work**. No "D&D" or other trademarks in the game or store page. This lines up with your plan: SRD for the base, your own subclasses and skill trees on top.

**Rule:** every data record carries `"source": "SRD 5.1"` or `"source": "original"`. A test fails if anything is missing a source.

### 2.2 Engine
Panda3D: a mature 3D engine with a C++ core and a Python API. It has shipped commercial games, loads glTF models from Blender, supports modern (PBR) lighting through `panda3d-simplepbr`, and packages Windows builds with its own `build_apps` tool. We go straight to Panda3D rather than prototyping in something simpler and switching later.

**Python version:** your PyCharm project is set to 3.14. Pin the project to the newest Python version Panda3D publishes Windows wheels for (checked in Phase 0).

### 2.3 What "like Baldur's Gate 3" means for the systems
- **Exploration** happens in real time. Characters move freely; the camera follows the party.
- **Combat** starts when a fight triggers: everyone snaps to the nearest hex, initiative is rolled, and turns are taken in order. Consecutive party members can act at the same time in co-op, to keep players from waiting.
- **Verticality:** hexes have a height. High ground, falling, jumping and line of sight over height all matter.
- **Surfaces and reactions:** fire, grease, water, ice, poison clouds on hexes, and objects that react to them (the legacy burning/exploding/conducting barrels fit here).
- **Dialogue with skill checks:** this is also how the Jester paintings work (tiered Perception results).
- **Party control:** in solo, switch between characters freely. In co-op, each player has one character; the host has the rest.

### 2.4 Co-op networking
- One **host** runs the real game (the authoritative simulation). Other players' copies send commands ("move to hex", "cast Fire Bolt here") and display what the host sends back.
- Solo play is the same: a host running inside your own game with no one else connected. One code path, so solo and co-op can't drift apart.
- If a player drops, the host takes over their character until they rejoin.
- **Two connection methods behind one interface ("transport"):**
  - Direct IP over TCP — built first. The host may need to forward a port; Steam removes that problem.
  - Steam networking (relay and friend invites) — added later through a Python binding to Steam's C API.

## 3. Choices that are hard to change later

These are fixed from the start, because getting them wrong means rewriting large parts of the game.

| # | Choice | Why it matters |
|---|---|---|
| 1 | **Game logic never imports the engine.** Rules and simulation are plain Python | Lets the host run without graphics, makes everything testable, and stops engine code leaking into rules |
| 2 | **Everything happens through commands and events** | Required for co-op; also gives undo-free replays, logs and debugging |
| 3 | **One dice service, on the host, with fresh randomness for every roll** | Every roll is unique: the dice state is never saved, so reloading and retrying gives a new result (no save-scumming the same outcome). Each roll's result is written to the session log, so a fight can still be replayed exactly for debugging. Tests can plug in a fixed-sequence dice service. Only the host rolls; other players receive the results |
| 4 | **Everything a character can do comes from data, as "features" made of "effects"** | Classes, SRD subclasses, your custom subclasses, skill-tree nodes, feats, items, curses and house rules all use the same system. Adding a skill tree later is new data, not new code |
| 5 | **Content lives in data files checked by schemas** | Invalid data is caught when the game loads, not mid-fight |
| 6 | **Network transport behind an interface** | Direct IP now, Steam later, with no game-code changes |
| 7 | **Art is referenced by ID through an asset manifest** | Swapping a placeholder for your final model is a data change. Fixed scale (1 unit = 1 m) and fixed bone/animation names from day one |
| 8 | **Save files carry a version number and an upgrade step** | Old saves keep working as the game changes — essential once players have them |
| 9 | **Type hints everywhere, checked by a type checker, plus tests** | Catches mistakes early in a codebase that will grow for years |

## 4. Tech stack

| Purpose | Choice |
|---|---|
| Language | Python (version pinned to Panda3D support), with type hints checked by `pyright` |
| Environment and dependencies | `uv` with `pyproject.toml` |
| 3D engine | Panda3D, `panda3d-simplepbr`, `panda3d-gltf` |
| Art pipeline | Blender → glTF (`.glb`); free CC0 placeholder packs until your art is ready |
| Data | JSON in `data/`, checked by `pydantic` models |
| Saves | Versioned JSON |
| Networking | `asyncio` TCP with a small typed message protocol; Steam transport later |
| Tests | `pytest`, plus a headless combat simulator for balance |
| Lint / format | `ruff` |
| CI | GitHub Actions running tests, lint and type checks on each push |
| Hex maths | Our own module, axial/cube coordinates (Red Blob Games' "Hexagonal Grids" guide) |

## 5. Architecture

```
data/ (JSON: classes, subclasses, skill trees, races, spells, items, monsters, world, story)
   │  loaded + checked by
   ▼
content/    schemas and loading; the asset manifest
   ▼
rules/      dice, abilities, checks, saves, features/effects, spells, conditions, character build
   ▼
sim/        game state, hex grid + height, exploration, combat turns, surfaces, AI, dialogue state
   ▼
host/       owns the sim; takes commands, sends events; runs inside the game for solo
   ▲  commands      │ events          (via a transport: in-process / TCP / Steam)
   │                ▼
client/     Panda3D: rendering, camera, input, UI, audio, animation
```

`rules/`, `sim/` and `host/` never import Panda3D.

## 6. Repository layout

```
fantasygame/
├── src/fantasygame/
│   ├── content/  rules/  sim/  host/  net/  client/
│   └── __main__.py                 (python -m fantasygame)
├── data/            classes/ subclasses/ skilltrees/ races/ spells/ items/ monsters/ world/ story/
├── assets/          models/ textures/ audio/ fonts/  +  manifest.json
├── tools/           srd_import.py, later a map/encounter editor
├── tests/
├── docs/            PROJECT_PLAN.md, vision.md, house-rules.md, story/, world/
├── legacy/          old prototype, reference only
├── pyproject.toml
└── README.md
```

## 7. Phases

Estimates assume 40 hrs/week and include learning time, since this is your first large game project. They will be revised at the end of Phase 3.

### Phase 0 — Foundation and learning (3–4 weeks)
- Work through the official Panda3D manual's basics (scene graph, tasks, models, camera, input) in a throwaway `sandbox/` folder.
- Set up the repo layout, `pyproject.toml`, `uv`, `ruff`, `pyright`, `pytest`, GitHub Actions, root `.gitignore`. Delete the old root `__pycache__/`.
- New `README.md`. Move the vision from the legacy README to `docs/vision.md` and the Jester story to `docs/story/jester.md`.
- **Engine test scene:** a hex-grid floor with height, a rotating/zooming camera, and one placeholder glTF character with modern lighting, packaged into a Windows build.
- **Done when:** `python -m fantasygame` opens that scene, and the packaged `.exe` runs on another Windows machine.

### Phase 1 — Rules engine (8–10 weeks)
- `tools/srd_import.py`: pull SRD 5.1 data (for example from the D&D 5e API, which serves SRD content) into `data/`, tagged with its source.
- Schemas for every data type.
- Dice service; ability scores; proficiency; skills; checks and saves; advantage/disadvantage.
- **Features and effects system** (choice 4 in §3): class features, the SRD subclasses, feats and items all expressed as data.
- Character creation: point-buy, standard array, race, background, class. All 12 classes, levels 1–20.
- Spell slots (including Warlock pact magic), conditions, rests, hit dice, levelling.
- **Skill-tree format:** define it now, with one small sample tree, so later trees are just data.
- **Done when:** tests build correct level 1, 5 and 10 characters of every class, matched against the SRD tables.

### Phase 2 — Combat without graphics (8–10 weeks)
- Hex grid: coordinates, distance, height, line of sight, cover, difficult terrain, pathfinding.
- Initiative, turns, action / bonus action / reaction / movement, attacks, damage types, resistances, critical hits, opportunity attacks, death saves, concentration, shoving, jumping, falling.
- Spell areas on hexes (cone, line, sphere, cube); surfaces (fire, grease, water, ice) and how they interact.
- House rules: at most 5 combatants per side on the field with reinforcements stepping in; low-man bonus; XP rules.
- Basic monster AI.
- Session log of commands and dice results, with replay; a headless simulator that can run thousands of fights.
- **Done when:** a level-3 party of 4 against a goblin war band plays out in the simulator, replays identically from its session log, and gives different rolls when the same fight is started again from a save.

### Phase 3 — 3D client (10–12 weeks)
- Camera (rotate, zoom, follow), real-time exploration movement, switching to combat and snapping to hexes.
- Hex highlighting, movement and range previews, area-of-effect previews, height indicators.
- Selecting characters, issuing orders, initiative bar, health bars, combat log, basic hotbar.
- UI approach chosen here (Panda3D's built-in GUI or a custom UI layer).
- Placeholder models and animations through the asset manifest.
- **Done when:** the Phase 2 goblin fight is playable with mouse and keyboard, including exploring into it.

### Phase 4 — Co-op (6–8 weeks)
- Host/client over direct-IP TCP: lobby, character assignment (one per player, host controls the rest), the host saves the game.
- Simultaneous turns for consecutive party members; dropped players handed to the host and back on rejoin.
- Checks that every copy of the game agrees with the host (state hashes).
- **Done when:** two Windows PCs finish the goblin fight together, and solo still works through the in-process host.

### Phase 5 — Vertical slice (5–7 months)
- One town, one hand-built dungeon, one wilderness area, with placeholder art at a consistent scale.
- Dialogue system with skill checks, quests, shops, inventory and equipment, loot, interactive objects (doors, chests, levers, reacting barrels), versioned save/load, main menu and settings (display, sound, subtitles — from the vision).
- All 12 classes playable to level 5; the first custom subclass and the first full skill tree.
- **Done when:** 45–60 minutes of play you'd show to testers.

### Phase 6 — The Jester (2–3 months, can overlap Phase 7)
- Examine system with tiered Perception results and bonus skill checks per painting.
- The six Houses as factions with questlines; spirit fights; hidden permanent curses (stacking to −6) and visible semi-permanent penalties with their removal quests; hidden map symbols; the Jester encounter.
- **Done when:** all six paintings can be found and examined, and their consequences survive saving and loading.

### Phase 7 — World and depth (12+ months)
- **World-building** (can start any time as a writing track): world name, map, regions, gods, history, how the six Houses fit.
- Open world in chunks, biomes from the vision, procedural dungeons themed by biome.
- Crafting (potions, poisons, ammo, gear; basic and enchanted).
- More custom subclasses and skill trees; roster of 10 with 5 active; pre-built companions.
- Levels 6–20 content and balance; your final art replacing placeholders.

### Phase 8 — Steam and release (4–6 months)
- Steam transport (relay, friend invites), Steamworks integration (achievements and cloud saves if wanted), Steam store page, Early Access decision.
- Performance, accessibility, credits with the CC‑BY credit line, review that no non-SRD content ships.

**Rough timeline:** vertical slice about 12–15 months from now; Early Access about 2–2.5 years; 1.0 about 3–4 years. Doing all the art yourself is the factor most likely to stretch this. Placeholders keep it from blocking the programming.

## 8. Placeholder art plan
- Free CC0 packs (e.g. Quaternius, KayKit, Kenney) for characters, monsters and dungeon pieces until your models are ready.
- Fixed conventions from day one: 1 unit = 1 metre; one hex = 5 ft (1.524 m) across its flats; Y-forward, Z-up (Panda3D's default); a shared humanoid skeleton and standard animation names (`idle`, `walk`, `run`, `attack_melee`, `cast`, `hit`, `die`, …).
- Every model is referenced by an ID in `assets/manifest.json`, so replacing one is a file swap.

## 9. Risks

| Risk | Mitigation |
|---|---|
| Learning curve (first large game) | Phase 0 learning time; small "done when" goals; tests from day one |
| Art volume, all done by one person | Placeholders never block code; one consistent art style; final art scheduled from Phase 5 on |
| Shipping non-SRD content by accident | Source tag on every record, enforced by a test |
| Co-op bugs | Engine-free simulation run only on the host, session logs with recorded dice results, replay tests from Phase 2 |
| Steam networking from Python | Transport interface from Phase 4; the Steam binding is isolated in one module |
| Python speed | Heavy lifting in Panda3D's C++ core; profiling from Phase 3 |
| Scope | Nothing in Phase 7 starts until the vertical slice is fun |

## 10. What we reuse from `legacy/`

| Keep (as reference, moved into docs or rebuilt as data) | Drop |
|---|---|
| Vision → `docs/vision.md` | Class level tables (several are wrong; replaced by the SRD import) |
| Jester story, Houses, Perception tiers → `docs/story/jester.md`, later `data/story/` | 2024 races, backgrounds and origin feats in `createCharacter.py` |
| Event-bus idea (`BusManager`) → the event system | Custom 0–99 stat / MP / element system |
| Reacting barrels; chest, door and lever ideas → surfaces and interactive objects | Guns and modern creatures (may return later as custom content) |
| Dungeon room types (Entrance, Hall, Stairs, Boss, Locked, Treasure, Junk) | Feat text copied from non-SRD sources |
| Goblin variants and loot chances → rebuilt as 2014 stat blocks | MySQL code |

## 11. Open questions (not blocking)
- **Game name and world name:** needed before the Steam page (Phase 8); "fantasygame" is the working title.
