import pygame

NEIGHERBOR_OFFSET = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
PHYSICS_TITLES = {"grass", "stone"}

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgridtiles = []
        for i in range(1000):
            self.tilemap[str(-500 + i) + ";10"] = {"type": "grass", "variant": 1, "pos": (-500 + i, 10)}
        for i in range(10):
            self.tilemap["-9;" + str(9 - i)] = {"type": "stone", "variant": 5, "pos": (-9, 9 - i)}
            self.tilemap["9;" + str(9 - i)] = {"type": "stone", "variant": 2, "pos": (9, 9 - i)}
        for i in range(7):
            self.tilemap[str(8 - i) + ";7"] = {"type": "grass", "variant": 1, "pos": (8 - i, 7)}
            self.tilemap[str(-8 + i) + ";4"] = {"type": "grass", "variant": 1, "pos": (-8 + i, 4)}
        for i in range(1000):
            for t in range(10):
                self.tilemap[str(-500 + i) + ";" + str(11 + t)] = {"type": "grass", "variant": 8, "pos": (-500 + i, 11 + t)}
    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHERBOR_OFFSET:
            check_loc = str(tile_loc[0] + offset[0]) + ";" + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile["type"] in PHYSICS_TITLES:
                rects.append(pygame.Rect((tile["pos"][0] * self.tile_size, tile["pos"][1] * self.tile_size, self.tile_size, self.tile_size)))
        return rects
    def render(self, surf, offset):
        for tile in self.offgridtiles:
            surf.blit(self.game.assets[tile["type"]][tile["variant"]], (tile["pos"][0] - offset[0], tile["pos"][1] - offset[1]))

        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile["type"]][tile["variant"]], ((tile["pos"][0] * self.tile_size) - offset[0], (tile["pos"][1] * self.tile_size) - offset[1]))





