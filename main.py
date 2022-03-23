
import utilities
from datetime import date

# utilities.login('maya.papaya534@stud.ntnu.no', 'maya')
# utilities.H1("Jacobsen & Svart", "Vinterkaffe 2022", 8, "jojoj")




#M fikse at slik at epost og navn ikke er case sensitivt. Nå er det potensielt et slitsomt system
#Printe tabellene finere, med tittler og sånn. 
#Mer data i db. Flere gårder og kaffer



def main():
    print("Velkommen til KaffeDB")
    bruker = 0
    while not bruker:
        svar = int(input("Logg inn (1), registrere ny bruker (2) eller avslutt (3): "))
        if svar == 1:
            epost = input("Epost: ").lower()
            passord = input("Passord: ")
            bruker = utilities.login(epost, passord)
            if bruker == 0:
                print("Epost-passord-kombinasjonen finnes ikke.")
        elif svar == 2:
            bruker = utilities.registrering()

        elif svar == 3:
            break



    
    while bruker:
        if bruker != 0 and bruker != 1: 
            valg = utilities.meny()

        #Ikke helt ferdig tror jeg
        #Flytte input til utilities?
            if valg == 1:
                print("Kaffesmaking")
                brenneri = input('Brenneri: ')
                kaffenavn = input('Kaffenavn: ')
                poeng = input('Poeng: ')
                smaksnotat = input('Smaksnotat: ')
                utilities.H1(brenneri, kaffenavn, poeng, smaksnotat, bruker)

        #Trenger oppdaterbart årstall
            elif valg == 2:
                utilities.H2()

        #Denne funker
            elif valg == 3:
                utilities.H3()

        #Problemer med å få brukerinput til spørringen, ikke strengt tatt nødvendig.
            elif valg == 4:
                utilities.H4()

        #Fyll databsen med info slik at denne kan testes.
            elif valg == 5:
                utilities.H5()
            

            elif valg == 6:
                bruker = 0
                print("Vi smakes.")            

        
        

# utilities.H5()



main()