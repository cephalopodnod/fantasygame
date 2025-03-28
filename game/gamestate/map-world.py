class Chunk:
    import math
    CHUNK_HEIGHT = 250
    CHUNK_WIDTH = 250
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)

    def remove_cell(self, cell):
        self.cells.remove(cell)

    def get_cell_from_player(self, x, y):
        cell_x = math.floor(x / Cell.CELL_WIDTH)
        cell_y = math.floor(y / Cell.CELL_HEIGHT)
        cell_x = max(0, min(cell_x, Chunk.CHUNK_WIDTH - 1))
        cell_y = max(0, min(cell_y, Chunk.CHUNK_HEIGHT - 1))
        return (cell_x, cell_y)
    
    def get_chunk_cells(self, center_x, center_y, radius):
        cells = []
        for cell in self.cells:
            if (cell.x - center_x)**2 + (cell.y - center_y)**2 <= radius**2:
                cells.append(cell)
        return cells

class Cell:
    CELL_HEIGHT = 50
    CELL_WIDTH = 50
    # biomes: forest, desert, mountain, swamp, tundra, plains, jungle, volcanic, island, ocean, river, lake, city
    # terrain: grass, sand, rocks, snow, ice, lava, water, trees, buildings, roads, bridges, dirt, mud, cliff, mountains, hills, farm
    def __init__(self, x, y, biome, terrain):
        self.x = x
        self.y = y
        self.biome = biome
        self.terrain = terrain
        self.dungeons = []
        self.enemies = []
        self.interactables = []
        self.npcs = []

    def add_dungeon(self, dungeon):
        self.dungeons.append(dungeon)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_interactable(self, interactable):
        self.interactables.append(interactable) 

    def add_npc(self, npc):
        self.npcs.append(npc)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def remove_interactable(self, interactable):
        self.interactables.remove(interactable)

    def remove_npc(self, npc):
        self.npcs.remove(npc)



        


