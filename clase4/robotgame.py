import rgkit.rg

class Robot:
    def act(self, game):
        self.numAdyacentesContrario = 0
        self.numAdyacentesPropios = 0
        self.vidaContrario = 0
        self.vidaPropia = 0

        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rgkit.rg.dist(loc, self.location) <= 1:
                    self.numAdyacentesContario+=1;
                    self.vidaContrario+=bot.hp
            else:
                if rgkit.rg.dist(loc, self.location) <= 1:
                    self.numAdyacentesPropios+=1;
                    self.vidaPropia+=bot.hp
        if self.numAdyacentesContario > 3:
            return ['suicide']
        if self.numAdyacentesContario > self.numAdyacentesPropios:
            return ['move', rgkit.rg.toward(self.location, rgkit.rg.CENTER_POINT)]
        else:
            for loc, bot in game.robots.iteritems():
                if bot.player_id != self.player_id:
                    if rgkit.rg.dist(loc, self.location) <= 1:
                        return ['attack', loc]
        if self.location == rgkit.rg.CENTER_POINT:
            return ['guard']
        return ['move', rgkit.rg.toward(self.location, rgkit.rg.CENTER_POINT)]