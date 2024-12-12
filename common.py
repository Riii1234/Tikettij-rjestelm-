# -------------------------------------------------------------------
def avaa_tiedosto(tiedosto :str):
    """Tekee sanakirjan avatusta tiedostosta"""
    sanakirja = {}

    # Luo tiedoston, jos sitä ei vielä ole ja palauttaa tyhjän sanakirjan
    try:  
        with open(tiedosto, "x") as tied:
            return sanakirja
        
    # Lukee tiedoston tiedot sanakirjaan, jos se on olemassa
    except:  
        with open(tiedosto) as tied:
            for rivi in tied:
                sanakirja2 = {}
                # Tiedot riviltä ID:tä lukuunottamatta
                asiat = rivi[9:].split(";")
                laskuri = 1
                for asia in asiat[::2]:
                    # Kuvaus ja tieto
                    sanakirja2[asia] = asiat[laskuri].strip()
                    laskuri += 2
                # rivi[:8] on ID
                sanakirja[rivi[:8]] = sanakirja2

    return sanakirja
# -------------------------------------------------------------------
def id_lukumaara(sanakirja :dict):
    """Laskee montako ID:tä sanakirjassa on jo olemassa uuden ID:n luomista varten"""
    laskuri = 0

    for id in sanakirja:
        laskuri += 1

    return laskuri
# -------------------------------------------------------------------
def luo_uusi_id(tunnus :str, montako :int):
    """Luo uuden ID:n tunnuksesta (asiakas, laite, tiketti tai teknikko) ja riippuen ID:ein määrästä"""
    id = tunnus + str(montako)

    while len(id) < 8:
        id = id[:3] + str(0) + id[3:]

    return id
# -------------------------------------------------------------------
def tallenna_tiedostoon(sanakirja: dict, tallennettava_id :str, tiedosto: str):
    """Tallentaa tiedostoon yhden ID:n ja sen tiedot"""

    with open(tiedosto, "a") as tied:
        # Id ja sanakirja tiedoista (tiedot) sanakirjassa
        for id, tiedot in sanakirja.items():
            if id == tallennettava_id:
                tied.write(f"{tallennettava_id};")
                rivi = ""
                # Kuvaus on esim "nimi", "email" ja tieto on sitä vastaava tieto
                for kuvaus, tieto in tiedot.items():
                    rivi += f"{kuvaus};{tieto};"
                rivi = rivi[:-1]
                tied.write(rivi + "\n")
# -------------------------------------------------------------------
def tallenna_tiedosto(sanakirja: dict, tiedosto: str):
    """Korvaa tiedoston tiedot sanakirjalla, joka sisältää kaikki ID:t ja niiden tiedot"""

    with open(tiedosto, "w") as tied:
        # Id ja sanakirja tiedoista (tiedot) sanakirjassa
        for id, tiedot in sanakirja.items():
                tied.write(f"{id};")
                rivi = ""
                # Kuvaus on esim "nimi", "email" ja tieto on sitä vastaava tieto
                for kuvaus, tieto in tiedot.items():
                    rivi += f"{kuvaus};{tieto};"
                rivi = rivi[:-1]
                tied.write(rivi + "\n")
# -------------------------------------------------------------------
def hae_tiedot(id_tai_tieto: str, avain: str, tiedosto: str, haku_valinta):
    """Hakee ID:n tai valitun tiedon kaikki tiedot"""

    sanakirja = avaa_tiedosto(tiedosto)
    # ID on sanakirjan avain ja tiedot ovat sanakirjana
    for id, tiedot in sanakirja.items():

        if haku_valinta == "id":
            if id_tai_tieto == id:
                return tiedot

        elif haku_valinta == "tieto":
            if tiedot[avain] == id_tai_tieto:
                return tiedot
    return ""
# ------------------------------------------------------------------- 
def hae_tieto_lista(avain: str, tiedosto: str, haku_valinta: str, id_lista: list):
    """Hakee avaimen kaikki tiedot"""

    sanakirja = avaa_tiedosto(tiedosto)
    lista = []

    for id, tiedot in sanakirja.items():

        if haku_valinta == "erilaiset":
            if tiedot[avain] not in lista:
                lista.append(tiedot[avain])

        elif haku_valinta == "id_lista":
            if id in id_lista:
                lista.append(tiedot[avain])

    return lista
# -------------------------------------------------------------------
def hae_tietoja(tieto, avain, tiedosto):
    """Hakee kaikkien täsmäävien ID:n ja tiedot"""

    sanakirja = avaa_tiedosto(tiedosto)
    lista = []

    for id, tiedot in sanakirja.items():
        
        if tiedot[avain] == tieto:
            lista.append(id)
            lista.append(tiedot)

    return lista
# -------------------------------------------------------------------
def hae_id_tiedolla(tieto: str, milla_tiedolla: str, tiedosto: str):
    """ID:n haku tiedolla"""

    sanakirja = avaa_tiedosto(tiedosto)

    for id, tiedot in sanakirja.items():
        if tiedot[milla_tiedolla] == tieto:
            return id
# -------------------------------------------------------------------
def hae_tieto_id(annettu_id: str, mika_tieto: str, tiedosto: str):
    """Tiedon haku ID:llä"""

    sanakirja = avaa_tiedosto(tiedosto)

    for id, tiedot in sanakirja.items():
        if annettu_id == id:
            return tiedot[mika_tieto]
    return "-"
# -------------------------------------------------------------------
def hae_id(tiedot_lista: list, tiedosto: str, tieto: str):
    """Hakee ID:n entryn tiedolla sanakirjasta"""

    # Haetaan entryn tieto get() metodilla
    entryn_tieto = tiedot_lista[0].get()

    sanakirja = avaa_tiedosto(tiedosto)

    for id,tiedot in sanakirja.items():
        if entryn_tieto == tiedot[tieto]:
            haettava_id = id
            return haettava_id
        else:
            haettava_id = ""

    return haettava_id
# -------------------------------------------------------------------
def lisaa_tiedot_sanakirjaan(tiedot_lista: list, tieto_nimikkeet: list):
    """Tekee kahdesta listasta sanakirjan"""

    sanakirja = {}
    i = 0
    while i < len(tiedot_lista):
        sanakirja[tieto_nimikkeet[i]] = tiedot_lista[i]
        i = i + 1

    return sanakirja
# -------------------------------------------------------------------
def lue_tiedot(tiedot):
    """Lue tiedot entryistä listaan"""

    tiedot_lista = []
    for i in tiedot:
        tieto = i.get()
        tiedot_lista.append(tieto)

    return tiedot_lista
# -------------------------------------------------------------------
def aseta_valikko(valikko, tieto_lista):
    """Asettaa tiedot valikkoon"""

    valikko.configure(values = tieto_lista)
    valikko.set(tieto_lista[0])
# -------------------------------------------------------------------