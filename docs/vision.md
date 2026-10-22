# Vision

_Reorganised from the original design notes (`legacy/README.md`). Where a later decision in [PROJECT_PLAN.md](PROJECT_PLAN.md) changes an original idea, it is marked **Decided since**. Unresolved points are collected in [Open questions](#13-open-questions)._

## 1. The game in one paragraph

An open-world fantasy RPG with dungeons, complex stories and turn-based combat. Challenging side quests, special bosses and hidden secrets reward players who explore. The story has thousands of possible paths, the ending is not predetermined, and the player's choices matter a lot.

## 2. What the game is about

- **Choices that matter**: branching stories with no fixed ending.
- **A world worth exploring**: a large open world, unique dungeons, hidden secrets.
- **A party you build**: up to 5 heroes in play, played solo or with friends.
- **Challenge**: hard side quests, special bosses and staged fights.

## 3. World and exploration

- A large open-world map with many unique dungeons.
- Every area opens up for exploration after a few introductory quests.
- Large cities to explore.
- **Biomes:** city, swamp, plains, mountains, desert, tundra, jungle, volcanic, beach, rivers, oceans, islands (tropical and arctic), plus some specialty realms.
- **Dungeons** are either:
  - preset quest dungeons, or
  - randomly generated dungeons that match their area (a desert spawns a cave or desert dungeon, not an ice dungeon).
- **Hidden layer:** the region's map hides symbols in each area, and some symbols combine into a larger meaning. See [story/jester.md](story/jester.md).

## 4. Story and choices

- A new game starts with an opening that depends on the character's **background**.
- During the opening, questions and options shape the character's early proficiencies. Levelling starts as a natural part of the story rather than a menu.
- The character then appears in the starting setting and the story begins. Each story can go thousands of ways, and the ending is not predetermined.
- The signature hidden storyline is **The Jester and the six Houses**: see [story/jester.md](story/jester.md).

## 5. Party

- **Up to 5 heroes active** in a party.
- **Roster of up to 10 characters**, with 5 active at a time.
- Pre-built NPC allies are available to recruit.
- Each hero class has its own look, abilities and skill trees.
- **Low-man mode:** for each party slot deliberately left empty, the party gets a stat bonus. Slots not yet unlocked and dead characters don't count. See [house-rules.md](house-rules.md).
- **Players:** up to 5 people together, or 1 person playing up to 5 heroes.
  - **Decided since:** co-op only (no PvP). Each player controls one character and the host controls any others. Players join by direct IP (which covers LAN) or Steam. Solo play is fully supported.

## 6. Characters and progression

- **Classes:** **Decided since:** the 12 classes from the 2014 rules (SRD 5.1), with our own subclasses and skill trees on top.
- Each class starts from a preset template that provides base skills and abilities. More skills and abilities unlock with level and are chosen by the player.
- Original idea: each template has base stats that grow per level, not always the same stat every level.
  - **Decided since:** stats follow the 2014 rules and only increase at set levels (usually 4, 8, 12, 16 and 19).
- Some items have level requirements.

## 7. Skill trees

- Each choice in a tree branches into options that expand on the node before it.
- Players don't have to keep going down a path.
- Some nodes are either/or: picking one path locks the other.
- Skills can grow in two ways:
  - **Level up:** the same skill becomes stronger.
  - **Evolve:** the skill becomes a new skill that replaces it, keeping the original's effect and adding a new feature.
- **Decided since:** skill trees sit on top of the 2014 class progression.

## 8. Combat

- **Decided since:** like Baldur's Gate 3. Exploration is real time with free movement. Combat is turn-based on a hex grid (5 ft per hex, with height).
- Every character, hero or enemy, has an initiative rating that sets the turn order.
- On a turn, characters can use **items, attacks, abilities and specials**.
- **Battle size:** at most 5 per side on the field at once, but the number of enemies is not limited. When an enemy dies, the next one comes in.
- **Staged fights:** some battles have special events or triggers that must be completed to move the fight into its next stage.
- **Dice:** every roll is unique. Reloading a save and trying again gives a new result.

## 9. Experience and rewards

- **XP sources:** combat, events, discovery, learning new recipes, and special XP consumables.
- **XP scales with level gap:** a level 1 monster is always a level 1 monster. The further above it a character is, the less XP it gives, but it always gives at least 1.
- **Spawned child monsters** give no XP and no rewards. These are creatures spawned during a fight, not creatures that wander in and join it.
- **A monster must give XP to drop items.**
- To stop low-level farming, the XP needed for each level rises steeply.

Details and numbers: [house-rules.md](house-rules.md).

## 10. Crafting

- Craft potions, poisons, ammo and gear.
- **Basic gear:** basic armour types, weapon types and shield types.
- **Enchanted gear:** basic gear with a compound added to it. The benefit depends on where the compound is added.

## 11. Menus

**Start screen:** New Game, Load Game, Settings.

**New Game** opens a second menu:
- Single player or multiplayer (online or LAN)
- Difficulty
- Expansion
- Story
- Name
- Race
- Class
- Background

**Load Game** lists saved games with the save name, time played and main character's name.

**Settings:**
- Colour and brightness
- Sound levels
- Subtitles
- _(more to come)_

## 12. Look and presentation

- Original idea: a 3D isometric view, similar to Diablo 2.
- **Decided since:** full 3D in Panda3D with a camera that can rotate and zoom, closer to Baldur's Gate 3.

## 13. Open questions

- **Q1 — "Expansion" and "Story" in the New Game menu.** Are these separate campaigns, or DLC to switch on and off?
- **Q2 — Difficulty levels.** Decided so far: 5 levels; short rests per long rest = 5 − difficulty (4 down to 0). What else changes between them (enemy stats, AI, XP, death rules)?
- **Q3 — Specialty realms.** What are they (planes, dream worlds, the spirit-fight realm)?
- **Q4 — Death.** What happens when a hero dies outside the spirit fights: revival, permanent death, or a difficulty setting?
- **Q5 — Pre-built NPC allies and the roster of 10.** Can the roster mix player-made heroes and pre-built allies freely?
