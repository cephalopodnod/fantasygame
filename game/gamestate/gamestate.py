class GameState:
    def __init__(self):
        # Player data
        self.players = {}
        self.active_player_id = None
        
        # Enemy data
        self.enemies = {}
        
        # Map data
        self.map = {
            'width': 100,
            'height': 100,
            'tiles': {},  # Could use coordinates as keys (x,y) and tile data as values
            'spawn_points': []
        }
        
        # Game status
        self.is_running = False
        self.game_time = 0
        self.difficulty = 'normal'
        
        # Inventory/Items
        self.global_items = {}  # Items on the map
        
    # Player management methods
    def add_player(self, player_id, name, position=(0,0), health=100):
        self.players[player_id] = {
            'name': name,
            'position': position,
            'health': health,
            'max_health': 100,
            'inventory': [],
            'score': 0
        }
        if not self.active_player_id:
            self.active_player_id = player_id
            
    def update_player_position(self, player_id, new_position):
        if player_id in self.players:
            self.players[player_id]['position'] = new_position
            
    def update_player_health(self, player_id, health_change):
        if player_id in self.players:
            current_health = self.players[player_id]['health']
            self.players[player_id]['health'] = max(0, min(
                current_health + health_change, 
                self.players[player_id]['max_health']
            ))
            
    # Enemy management methods
    def add_enemy(self, enemy_id, enemy_type, position=(0,0), health=50):
        self.enemies[enemy_id] = {
            'type': enemy_type,
            'position': position,
            'health': health,
            'max_health': health,
            'is_active': True
        }
        
    def update_enemy_position(self, enemy_id, new_position):
        if enemy_id in self.enemies:
            self.enemies[enemy_id]['position'] = new_position
            
    # Map management methods
    def set_tile(self, x, y, tile_data):
        self.map['tiles'][(x, y)] = tile_data
        
    def add_spawn_point(self, position):
        self.map['spawn_points'].append(position)
        
    # Game state methods
    def start_game(self):
        self.is_running = True
        
    def end_game(self):
        self.is_running = False
        
    def update_game_time(self, time_delta):
        if self.is_running:
            self.game_time += time_delta
            
    # Item management
    def add_item(self, item_id, position, item_type):
        self.global_items[item_id] = {
            'position': position,
            'type': item_type,
            'is_picked_up': False
        }
        
    def pickup_item(self, item_id, player_id):
        if (item_id in self.global_items and 
            not self.global_items[item_id]['is_picked_up'] and 
            player_id in self.players):
            self.global_items[item_id]['is_picked_up'] = True
            self.players[player_id]['inventory'].append(item_id)

# Example usage:
if __name__ == "__main__":
    game = GameState()
    
    # Add a player
    game.add_player("player1", "Hero", (10, 10))
    
    # Add an enemy
    game.add_enemy("enemy1", "goblin", (20, 20))
    
    # Set some map tiles
    game.set_tile(10, 10, {"type": "grass", "passable": True})
    
    # Add an item
    game.add_item("item1", (15, 15), "health_potion")
    
    # Start the game
    game.start_game()
    
    # Example of updating state
    game.update_player_position("player1", (11, 11))
    game.update_game_time(1.0)
    
    # Print current state
    print("Players:", game.players)
    print("Enemies:", game.enemies)
    print("Map tiles:", game.map['tiles'])
    print("Game time:", game.game_time)