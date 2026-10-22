# House Rules

Every place where the game deliberately differs from, or adds to, the 2014 rules (SRD 5.1). Each rule shows what the 2014 rules do, what we do instead, and what is still undecided.

**Status key:** **Decided** = settled and ready to build · **Needs numbers** = idea settled, values not chosen yet · **Open** = idea not settled yet

---

## Dice

### Unique rolls — Decided
- **2014 rules:** no position (a tabletop game).
- **Ours:** every roll uses fresh randomness. The dice state is never stored in a save, so reloading and retrying gives a new result.
- **How it's built:** only the host rolls. Each result is written to the session log so a fight can be replayed for debugging. Tests use a fixed-sequence dice service.

---

## Party and combat

### Party size and roster — Decided
- **2014 rules:** no limit.
- **Ours:** up to 5 active party members; a roster of up to 10.

### Battle size and reinforcements — Needs numbers
- **2014 rules:** every combatant is on the field from the start.
- **Ours:** at most 5 combatants per side on the field at once, with no limit on total enemies. When an enemy dies, the next one comes in.
- **To decide:** where reinforcements enter, whether they roll initiative on arrival or take the dead enemy's place in the order, and whether the 5-per-side limit also applies to summons and allies.

### Low-man mode — Needs numbers
- **2014 rules:** none.
- **Ours:** for each party slot deliberately left empty, the party gets a stat bonus. Slots not yet unlocked and dead characters don't count.
- **To decide:** which stats, how big the bonus is per empty slot, and whether it is set at the start of a fight or updates live.

### Staged fights — Decided (built per encounter)
- **2014 rules:** up to the Dungeon Master.
- **Ours:** some battles have events or triggers that must be completed to move the fight into its next stage.

### Combat grid — Decided
- **2014 rules:** squares by default; hexes as an optional variant.
- **Ours:** hexes, 5 ft per hex, with height. Used in combat only; free movement while exploring.

---

## Experience

### XP sources — Needs numbers
- **2014 rules:** XP comes from defeating monsters (by challenge rating) and from milestones the Dungeon Master chooses.
- **Ours:** combat, events, discovery, learning new recipes, and special XP consumables.
- **To decide:** how much XP each non-combat source gives.

### XP falls off with level gap — Needs numbers
- **2014 rules:** a monster gives the same XP whatever the party's level.
- **Ours:** the further a character's level is above the monster's, the less XP it gives, with a minimum of 1.
- **To decide:** the falloff curve, and whether it uses each character's own level or the party's average.

### Steeper levelling curve — Needs numbers
- **2014 rules:** a fixed XP table (300 XP for level 2 … 355,000 for level 20).
- **Ours:** the XP needed per level rises steeply, to stop low-level farming.
- **To decide:** the table itself. It should be tuned alongside the falloff rule and the size of the world.

### Spawned child monsters — Decided
- **2014 rules:** summoned or spawned creatures give XP like any other.
- **Ours:** creatures spawned during a fight give **no XP and no loot**. Creatures that wander in and join the fight count normally.
- **Why:** so a monster that keeps spawning children can't be used to farm XP or items.

### No XP, no loot — Decided
- **2014 rules:** none.
- **Ours:** a monster only drops items if it gives XP. With the minimum of 1 XP from the level-gap rule, this means spawned children never drop loot.

---

## Characters and progression

### Custom subclasses and skill trees — Decided (content to be designed)
- **2014 rules:** each class has its own subclasses. The free rules (SRD 5.1) include one per class.
- **Ours:** our own subclasses and skill trees on top of the 2014 classes. Tree nodes can branch, lock out alternatives (either/or), level up, or evolve into a new skill that keeps the old one's effect.

### Stat growth — Decided: 2014 rule unchanged
- **2014 rules:** ability scores only increase at set levels (usually 4, 8, 12, 16 and 19; Fighters also at 6 and 14, Rogues also at 10), by +2 total or through a feat.
- **Ours:** the same. The original idea of per-level stat growth is dropped.

### Short rests per long rest — Decided
- **2014 rules:** no limit; a short rest just takes 1 hour.
- **Ours:** the party gets a limited number of short rests between long rests, set by difficulty: **5 − difficulty level**.

  | Difficulty | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | Short rests per long rest | 4 | 3 | 2 | 1 | 0 |

- On difficulty 5, classes that recover on a short rest (e.g. Warlock spell slots, Fighter's Second Wind and Action Surge, Monk ki) only recover on long rests. Worth checking in balance testing.

### Item level requirements — Needs numbers
- **2014 rules:** none (only some items need attunement).
- **Ours:** some items have level requirements.

---

## The Jester's curses (spirit fights)

Full story: [story/jester.md](story/jester.md).

### Hidden permanent curse — Decided
- **2014 rules:** none.
- **Ours:** a character who dies in a spirit fight permanently loses 1 from their main stat. It stacks up to −6, can't be removed, and is never shown in the interface.
- **Main stat:** for classes with more than one key ability (e.g. Paladin: STR and CHA; Monk: DEX and WIS), the curse hits whichever ability adds more to that character's damage. A finesse-weapon Paladin's would be DEX, for example.
- **Locked:** the stat is chosen at the first curse and every later stack hits the same ability, so changing build can't spread or dodge the curse.

### Restless debuff (spirit-fight exhaustion) — Decided
- **2014 rules:** none.
- **Ours:** each spirit-fight death gives the character one stack of a visible debuff. With N stacks, the character's **first N short rests after each long rest give them no benefit**. The rests still count down for the rest of the party as normal.
- **Example:** on difficulty 1 (4 short rests), a character with 1 stack gets nothing from the first short rest but benefits from the other 3. With 4 stacks they get nothing from any short rest.
- **Removal:** semi-permanent, like the proficiency penalty: removed by a cleansing task.
- **To decide:** whether one cleansing task removes all stacks or one at a time; whether stacks cap at 4 (the most that matters on difficulty 1); and the debuff's in-game name ("Restless" is a placeholder).

### Visible proficiency penalty — Decided
- **2014 rules:** none.
- **Ours:** −2 to a random proficiency, shown in the interface. Semi-permanent: it is removed by a special questline, probably unique to each painting's fight.

---

## Crafting — Needs numbers
- **2014 rules:** simple crafting by time and gold (and tool proficiency).
- **Ours:** craft potions, poisons, ammo and gear. Gear is basic, or enchanted by adding a compound, with the benefit depending on where the compound is added.
- **To decide:** recipes, costs, time, and how enchanting slots work.
