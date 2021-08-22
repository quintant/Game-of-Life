

import pygame
from random import randint


class Lifeforms:
    def __init__(self) -> None:
        self.lifes = set()

    def add(self, x, y):
        self.lifes.add((x//4,y//4))

    def simulate(self):
        trash = set()
        pos_dead = set()
        to_live = set()
        for life in self.lifes:
            lx, ly = life
            neighbours = 0
            left = (lx-1, ly)
            right = (lx+1, ly)
            up = (lx, ly-1)
            down = (lx, ly+1)
            ur = (lx+1, ly-1)
            ul = (lx-1, ly-1)
            dr = (lx+1, ly+1)
            dl = (lx-1, ly+1)

            if left in self.lifes:
                neighbours += 1
            else:
                pos_dead.add(left)

            if right in self.lifes:
                neighbours += 1
            else:
                pos_dead.add(right)

            if up in self.lifes:
                neighbours += 1
            else:
                pos_dead.add(up)

            if down in self.lifes:
                neighbours += 1
            else:
                pos_dead.add(down)
            
            ##############################
            if ur in self.lifes:
                neighbours += 1
            else:
                pos_dead.add(ur)

            if ul in self.lifes:
                neighbours += 1
            else:
                pos_dead.add(ul)

            if dr in self.lifes:
                neighbours += 1
            else:
                pos_dead.add(dr)

            if dl in self.lifes:
                neighbours += 1
            else:
                pos_dead.add(dl)

            
            if neighbours < 2 or neighbours > 3:
                trash.add(life)


        for dead in pos_dead:
            lx, ly = dead
            neighbours = 0
            left = (lx-1, ly)
            right = (lx+1, ly)
            up = (lx, ly-1)
            down = (lx, ly+1)
            ur = (lx+1, ly-1)
            ul = (lx-1, ly-1)
            dr = (lx+1, ly+1)
            dl = (lx-1, ly+1)

            if left in self.lifes:
                neighbours += 1


            if right in self.lifes:
                neighbours += 1


            if up in self.lifes:
                neighbours += 1


            if down in self.lifes:
                neighbours += 1

            
            if ur in self.lifes:
                neighbours += 1


            if ul in self.lifes:
                neighbours += 1


            if dr in self.lifes:
                neighbours += 1

            if dl in self.lifes:
                neighbours += 1

            if neighbours == 3:
                to_live.add(dead)
        
        for life in trash:
            self.lifes.remove(life)

        self.lifes = self.lifes.union(to_live)


    def rc(self):
        return (50, 255, 50)   

    def display(self, screen):
        for life in self.lifes:
            for x in range(4):
                for y in range(4):
                    screen.set_at(
                        (
                            4*life[0]+x, 
                            4*life[1]+y
                        ),
                        self.rc()
                    )


    