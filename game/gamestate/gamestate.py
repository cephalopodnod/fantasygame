# this will handle the different actions and events that can happen in the game, this places them into a queue and handles them in order.
class BusManager(self):
        def __init__(self):
            self.subscribers = {}

        def subscribe(self, event_type, callback):
            if event_type not in self.subscribers:
                self.subscribers[event_type] = []
            self.subscribers[event_type].append(callback)

        def publish(self, event_type, data):
            if event_type in self.subscribers:
                for callback, _ in self.subscribers[event_type]:
                    callback(data)    

# this will manage the current state of the game, including the players, enemies, map, and other game elements. 
class GameState:
    def __init__(self):
        self.players = {}
        self.active_player_id = None
        self.enemies = {}
        self.map = {}
        self.is_running = False
        self.game_time = 0
        self.difficulty = 'normal'
        self.global_items = {} 
        self.bus = BusManager()

    def input_handler(self, key, player_position, interactive_object=None):
        if key in ['W', 'A', 'S', 'D']:
            self.bus.publish('player_move', {"action": "move", "direction": key})
        elif key == 'E':
            self.bus.publish('player_interact', {"action": "interact", "position": player_position, "object": interactive_object})
        elif key == 'Tab':
            self.bus.publish('player_menu', {"action": "open_menu", "player_id": self.active_player_id})
        elif key == 'I':
            self.bus.publish('player_inventory', {"action": "open_inventory", "player_id": self.active_player_id})

    def player_move(self,data):
        print(f"Player {data['player_id']} moved {data['direction']}")
        
    def object_proximity(self,data):
        player_pos = data["player_position"]
        object_pos = data["interactive_object"]["position"]
        if data["action"] == "interact" and player_pos == object_pos:
            self.bus.publish('object_interact', {"action": "interact", "object_id": data["object"]["id"]})
            print(f"Player {self.players[self.active_player_id]} interacted with object {data['object']['id']} at {data['object']['position']}")
    
    def player_interact(self,data): 
        if data['object']['type'] == 'chest':
            self.bus.publish('chest_opened', {"action": "open_chest", "object_id": data["object"]["id"]})
        elif data['object']['type'] == 'door':
            self.bus.publish('door_opened', {"action": "open_door", "object_id": data["object"]["id"]})
        elif data['object']['type'] == 'npc':
            self.bus.publish('npc_interaction', {"action": "talk_to_npc", "object_id": data["object"]["id"]})
        elif data['object']['type'] == 'item':
            self.bus.publish('item_pickup', {"action": "pickup_item", "object_id": data["object"]["id"]})

    def open_chest(self, data):
        print(f"Player opened chest and these items were added to inventory: {', '.join(data['object']['loot']['name'])}")
        for items in data['object']['loot']: 
            self.players[data['player_id']]['inventory'].append(items)

    def open_door(self, data):
        print(f"Player opened door: {data['object_id']}")
        # update to open door in the map, enabling access to next area

    def pickup_item(self, data):
        print(f"Player picked up item: {data['object']['name']}")
        self.players[data['player_id']]['inventory'].append(data['object'])
  







    # def create_character(self):
    #     char = Character()
    #     char.name = input("Enter character name: ")
    #     char.set_race()
    #     char.set_alignment()
    #     char.set_class()
    #     char.set_stats()
    #     char.set_traits()
    #     self.players[char.name] = char

    # def add_character(self, character):
    #     self.players[character.name] = character

            
    # def update_player_position(self, player_id, new_position):
    #     if player_id in self.players:
    #         self.players[player_id]['position'] = new_position
            
    # def update_player_health(self, player_id, health_change):
    #     if player_id in self.players:
    #         current_health = self.players[player_id]['health']
    #         self.players[player_id]['health'] = max(0, min(
    #             current_health + health_change, 
    #             self.players[player_id]['max_health']
    #         ))
            
    # # Enemy management methods
    # def add_enemy(self, enemy_id, enemy_type, position=(0,0), health=50):
    #     self.enemies[enemy_id] = {
    #         'type': enemy_type,
    #         'position': position,
    #         'health': health,
    #         'max_health': health,
    #         'is_active': True
    #     }
        
    # def update_enemy_position(self, enemy_id, new_position):
    #     if enemy_id in self.enemies:
    #         self.enemies[enemy_id]['position'] = new_position
            
    # # Map management methods
    # def set_tile(self, x, y, tile_data):
    #     self.map['tiles'][(x, y)] = tile_data
        
    # def add_spawn_point(self, position):
    #     self.map['spawn_points'].append(position)
        
    # # Game state methods
    # def start_game(self):
    #     self.is_running = True
        
    # def end_game(self):
    #     self.is_running = False
        
    # def update_game_time(self, time_delta):
    #     if self.is_running:
    #         self.game_time += time_delta
            
    # # Item management
    # def add_item(self, item_id, position, item_type):
    #     self.global_items[item_id] = {
    #         'position': position,
    #         'type': item_type,
    #         'is_picked_up': False
    #     }
        
    # def pickup_item(self, item_id, player_id):
    #     if (item_id in self.global_items and 
    #         not self.global_items[item_id]['is_picked_up'] and 
    #         player_id in self.players):
    #         self.global_items[item_id]['is_picked_up'] = True
    #         self.players[player_id]['inventory'].append(item_id)

    # def take_turn(self):
    #     for character in self.fightorder:
    #         if self.fightorder[character] == self.currentturn:
    #             #character can do 1 action(cast spell, use skill, standard action) and do 1 bonus action, there are skills that allow you to do multiple actions or bonus actions.
    #             print(f"{character} can take their turn")
    #     self.currentturn += 1
    #     pass

    # def end_turn(self,character):
    #     if self.currentturn != self.fightsize:
    #         self.currentturn += 1
    #     else:
    #         self.currentturn = 1

