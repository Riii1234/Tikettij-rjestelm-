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
                count = 1
                for asia in asiat[::2]:
                    # Kuvaus ja tieto
                    sanakirja2[asia] = asiat[count].strip()
                    count += 2
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
def hae_tiedot_id(annettu_id: str, tiedosto: str):
    """Yhden ID:n tietojen haku tiedostosta"""

    sanakirja = avaa_tiedosto(tiedosto)

    # ID on sanakirjan avain ja tiedot ovat sanakirjana
    for id, tiedot in sanakirja.items():
        if annettu_id == id:
            return tiedot
# ------------------------------------------------------------------- 
def hae_tiedot(annettu_tieto: str, milla_tiedolla: str, tiedosto: str):
    """Yhden tiedon tietojen haku"""

    sanakirja = avaa_tiedosto(tiedosto)

    for id, tiedot in sanakirja.items():
        if tiedot[milla_tiedolla] == annettu_tieto:
            return tiedot
# ------------------------------------------------------------------- 
def hae_tiedot_kaikkien(milla_tiedolla: str, tiedosto: str):
    """Kaikkien tietojen haku tiedolla (ei ID)"""

    sanakirja = avaa_tiedosto(tiedosto)
    lista = []

    for id, tiedot in sanakirja.items():
        lista.append(tiedot[milla_tiedolla])

    return lista
# -------------------------------------------------------------------
def hae_tiedot_kaikkien_erit(milla_tiedolla: str, tiedosto: str):
    """Kaikkien tietojen haku tiedolla (ei ID), vain yksilölliset tiedot"""

    sanakirja = avaa_tiedosto(tiedosto)
    lista = []

    for id, tiedot in sanakirja.items():
        if tiedot[milla_tiedolla] not in lista:
            lista.append(tiedot[milla_tiedolla])

    return lista
# -------------------------------------------------------------------
def hae_mahd_tieto_kaikki(idt: list, mika_tieto: str, tiedosto: str):
    """Useamman ID:n yhden tiedon haku ID:eillä (Jos id täsmää)"""

    sanakirja = avaa_tiedosto(tiedosto)
    lista = []

    for id, tiedot in sanakirja.items():
        if id in idt:
            lista.append(tiedot[mika_tieto])

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
# -------------------------------------------------------------------
def hae_tietoja(mika_tieto, tieto_nimike, tiedosto):
    """Kaikkien täsmäävien tiedot"""

    sanakirja = avaa_tiedosto(tiedosto)
    lista = []

    for id, tiedot in sanakirja.items():
        
        if tiedot[tieto_nimike] == mika_tieto:
            lista.append(id)
            lista.append(tiedot)

    print("hae_tietoja - lista", lista)

    return lista
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