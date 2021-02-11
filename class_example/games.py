class Game():
    def __init__(self, name, number_of_players, genre, skill_required):
        self.name = name
        self.number_of_players = number_of_players
        self.genre = genre
        self.skill_required = skill_required

    def one_player(self):
        print("Name:", self.name)
        print("Number_of_players:", self.number_of_players, "player")
        print("Genre:", self.genre)
        print("Skill_required:", self.skill_required)

    def two_players(self):
        print("Name:", self.name)
        print("Number_of_players:", self.number_of_players, "players")
        print("Genre:", self.genre)
        print("Skill_required:", self.skill_required)

    def more_than_two_players(self):
        print("Name:", self.name)
        print("Number_of_players:", self.number_of_players, "players")
        print("Genre:", self.genre)
        print("Skill_required:", self.skill_required)


chess = Game("Chess", 2, "strategic board game", "strategy & tactic")
chess.two_players()
print("-"*50)
sudoku = Game("Sudoku", 1, "puzzle & mind sport", "mathematics")
sudoku.two_players()
