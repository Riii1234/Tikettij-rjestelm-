from tiketit import uusi_tiketti
from teknikot import uusi_teknikko, vaihda_valmiusastetta
from haku import haku

#valinta = input("Mitä haluat tehdä: (tiketti/teknikko/valmiusaste/haku)")
valinta = "haku"

if valinta == "tiketti":
    uusi_tiketti()

elif valinta == "teknikko":
    uusi_teknikko()

elif valinta == "valmiusaste":
    vaihda_valmiusastetta()

elif valinta == "haku":
    haku()


