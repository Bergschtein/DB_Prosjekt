import sqlite3 as sql
from datetime import date
from pprint import pprint
from tabulate import tabulate #Trenger installering "pip install tabulate", ikke i bruk enda.
class Bruker:
    def __init__(self, epost, passord, fornavn, etternavn) -> None:
        self.epost = epost
        self.passord = passord
        self.fornavn = fornavn
        self.etternavn = etternavn
        
    def leggTilBruker(self):
        con = sql.connect("KaffeDB.db")
        cursor = con.cursor()
        cursor.execute( """ INSERT INTO Bruker(epost, passord, fornavn, etternavn ) 
                            VALUES (:epost, :passord, :fornavn, :etternavn )""", {'epost':self.epost,'passord':self.passord,'fornavn':self.fornavn,'etternavn':self.etternavn})
        con.commit()
        con.close()
    def getId(self):
        con = sql.connect("KaffeDB.db")
        cursor = con.cursor()
        cursor.execute( """ SELECT brukerID FROM Bruker WHERE epost = :epost """, {'epost':self.epost})
        brukerId = cursor.fetchone()[0]
        con.close()
        return brukerId
        
        return 
    def getEpost(self):
        return self.epost
    def getFornavn(self):
        return self.fornavn
    def getEtternavn(self):
        return self.etternavn
    
def meny():
    print("(1) Legg til kaffesmaking (H1)")
    print("(2) Toppliste, antall smakte kaffe(H2)")
    print("(3) Bang 4 your buck")
    print("(4) Søk etter kaffe basert på beskrivelse")
    print("(5) Søk etter kaffe basert på land og foredlingsmetode (H5)")
    print("(6) Avslutt")
    
    valg = int(input("Valg:"))

    return valg


def registrering():
    fornavn = input("Fornavn: ")
    etternavn = input("Etternavn:")
    epost = input("Epost: ")
    passord = input("Passord: ")
    bruker = Bruker(epost, passord, fornavn, etternavn)
    bruker.leggTilBruker()
    return bruker


def login(epost, passord):

    con = sql.connect("KaffeDB.db")
    cursor = con.cursor()
    cursor.execute("""SELECT *
                        FROM Bruker
                        WHERE Bruker.epost = :epost AND Bruker.passord = :passord""", {'epost':epost,'passord':passord})                   
    result = cursor.fetchone()

    if result: #Hvis brukeren finnes kjøres dette
        bruker = Bruker(result[1], result[2], result[3], result[4])
        return bruker
    else:
        return 0


def H1(brenneri, kaffenavn, poeng, smaksnotat, bruker):
    today = date.today()
    datoto = ("{}.{}.{}".format(today.day,today.month,today.year))
    
    con = sql.connect("KaffeDB.db")
    cursor = con.cursor()
    cursor.execute("""SELECT fkID
                        FROM (FerdigbrenntKaffe AS fk INNER JOIN Brenneri ON fk.brenneriID = Brenneri.brenneriID )
                        WHERE Brenneri.navn = :brenneri AND fk.navn = :kaffenavn """, {'brenneri':brenneri, 'kaffenavn':kaffenavn})                   
    result = cursor.fetchone()
    fkID = result[0] 

    # Må fikse datogreia
    cursor.execute( """ INSERT INTO Innlegg(smaksnotat, poeng, smaksdato, brukerID, fkID)
                            VALUES (:smaksnotat, :poeng, :smaksdato, :brukerID, :fkID )""", {'smaksnotat':smaksnotat,'poeng':poeng,'smaksdato':datoto,'brukerID':bruker.getId(),'fkID':fkID })
    con.commit()
    
    

    con.close()

def H2():
    con = sql.connect("KaffeDB.db")
    cursor = con.cursor()
    #Fikse oppdaterbart årstall
    cursor.execute("""SELECT COUNT(DISTINCT Innlegg.fkid) AS AntallKaffe, Bruker.fornavn, Bruker.etternavn
                        FROM (Innlegg INNER JOIN Bruker ON Innlegg.brukerID = Bruker.brukerID)
                        WHERE Innlegg.smaksdato LIKE '%.2022'
                        GROUP BY Innlegg.brukerID 
                        ORDER BY AntallKaffe DESC;
                        """)

    result = cursor.fetchall()
    
    for i in range (len(result)):
        print("{}. Antall unike innlegg: {}, Fullt navn: {} {}".format(i+1,result[i][0],result[i][1],result[i][2]))
        print(" ")
   

def H3():
    con = sql.connect("KaffeDB.db")
    cursor = con.cursor()
    cursor.execute("""SELECT brenneri.navn, fk.navn, fk.kgPris, avg(innlegg.poeng) AS gjennomsnittscore
                        FROM ((Brenneri INNER JOIN FerdigbrenntKaffe AS fk ON Brenneri.brenneriID = fk.brenneriID) 
                        INNER JOIN Innlegg ON fk.fkID = Innlegg.fkID)
                        GROUP BY brenneri.navn, fk.navn
                        ORDER BY gjennomsnittscore DESC, kgPris ASC;""")                   
    result = cursor.fetchall()
    for i in range(len(result)):
        print(" ")
        print("{}. Brennerinavn: {}, Kaffenavn: {}, Pris: {}, Gjennomsnittsscore: {}".format(i+1,result[i][0],result[i][1],result[i][2],result[i][3]))
    con.close()

def H4():
    søkeord = input("Søkeord: ")
    søkeord = søkeord.strip()
    con = sql.connect("KaffeDB.db")
    cursor = con.cursor()
    cursor.execute("""SELECT DISTINCT Brenneri.navn, fk.navn 
                        FROM ((Brenneri INNER JOIN FerdigbrenntKaffe AS fk ON Brenneri.brenneriID = fk.brenneriID) 
                                        INNER JOIN Innlegg ON fk.fkID = Innlegg.fkID)
                        WHERE fk.beskrivelse LIKE :søkeord1 OR Innlegg.smaksnotat LIKE :søkeord2;""", {'søkeord1':"%"+søkeord+"%", 'søkeord2':"%"+søkeord+"%"})           
    result = cursor.fetchall()
    
    for i in range (len(result)):
        print(" ")
        print("{}. Brenneri: {}, Kaffenavn: {}".format(i+1,result[i][0],result[i][1]))
        print(" ")

#ToDo: Få inn data så denne kan sjekkes
def H5():
    con = sql.connect("KaffeDB.db")
    cursor = con.cursor()
    cursor.execute(""" SELECT brenneri.navn, fk.navn
                        FROM ((((FerdigbrenntKaffe AS fk INNER JOIN brenneri ON fk.brenneriID = brenneri.brenneriID)
                        INNER JOIN parti ON fk.partiID = parti.partiID) 
                        INNER JOIN Foredlingsmetode AS fm ON parti.fmID = fm.fmID)
                        INNER JOIN gård ON parti.gårdID = gård.gårdID)
                        WHERE (gård.land = 'Colombia' OR gård.land = 'Rwanda') AND LOWER(fm.navn) <> 'vasket';
                    """)                   
    result = cursor.fetchall()
    for i in range (len(result)):
        print(" ")
        print("{}. Brenneri: {}, Kaffenavn: {}".format(i+1,result[i][0],result[i][1]))
        print(" ")