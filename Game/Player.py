import statistics 
class Player:
    def __init__(self, talent, map_skill, weapon_skill, utility_usage, game_sense, communication, mood, motivation, nationality, name, surname, age):
        self.talent = talent
        self.map_skill = map_skill
        self.weapon_skill = weapon_skill
        self.utility_usage = utility_usage
        self.game_sense = game_sense
        self.communication = communication
        self.mood = mood
        self.motivation = motivation
        self.nationality = nationality
        self.name = name
        self.surname = surname
        self.age = age
    def get_m(self):
        data=[0,0,0,0,0,0,0,0]
        data=[self.talent, self.map_skill, self.weapon_skill, self.utility_usage, self.game_sense, self.communication, self.mood, self.motivation]
        return statistics.mean(data)