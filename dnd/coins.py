from __future__ import annotations


CP_VALUE_IN_GP = 0.01

PP_VALUE_IN_CP = 1000
GP_VALUE_IN_CP = 100
EP_VALUE_IN_CP = 50
SP_VALUE_IN_CP = 10
CP_VALUE_IN_CP = 1

class Coins:
    def __init__(self, cp = 0, sp = 0, ep = 0, gp = 0, pp = 0) -> None:
        self.cp = self.convert_to_cp_(cp, sp, ep, gp, pp)
    
    def add(self, cp = 0, sp = 0, ep = 0, gp = 0, pp = 0) -> None:
        self.cp += self.convert_to_cp_(cp, sp, ep, gp, pp)

    def remove(self, cp = 0, sp = 0, ep = 0, gp = 0, pp = 0) -> bool:
        owed = self.convert_to_cp_(cp, sp, ep, gp, pp)
        if self.cp < owed:
            return False
        self.cp -= owed
        return True

    def convert_to_cp_(cp, sp, ep, gp, pp) -> int:
        return (pp * PP_VALUE_IN_CP + gp * GP_VALUE_IN_CP + ep * EP_VALUE_IN_CP + 
                sp * SP_VALUE_IN_CP + cp * CP_VALUE_IN_CP)
    
    def split(self) -> tuple[int, int, int, int, int]:
        cp_left = self.cp

        def take(cp_left, coin_value):
            if cp_left > 0:
                coins = cp_left // coin_value
                return (coins, cp_left - (coins * coin_value)) 

        pp, cp_left = take(cp_left, PP_VALUE_IN_CP)
        gp, cp_left = take(cp_left, GP_VALUE_IN_CP)
        ep, cp_left = take(cp_left, EP_VALUE_IN_CP)
        sp, cp_left = take(cp_left, SP_VALUE_IN_CP)
        cp, cp_left = take(cp_left, CP_VALUE_IN_CP)

        return pp, gp, ep, sp, cp

    def __str__(self) -> str:
        pp, gp, ep, sp, cp = self.split()
        return (
            f"{pp} PP, {gp} GP, {ep} EP, {sp} SP, {cp} CP\n"
            f"Total GP value: {self.cp * CP_VALUE_IN_GP}"
        )
