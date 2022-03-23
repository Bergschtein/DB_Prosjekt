
import utilities
from datetime import date


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

            if valg == 1:
                print("Kaffesmaking")
                brenneri = input('Brenneri: ')
                kaffenavn = input('Kaffenavn: ')
                poeng = input('Poeng: ')
                smaksnotat = input('Smaksnotat: ')
                utilities.H1(brenneri, kaffenavn, poeng, smaksnotat, bruker)

            elif valg == 2:
                utilities.H2()

            elif valg == 3:
                utilities.H3()

            elif valg == 4:
                utilities.H4()

            elif valg == 5:
                utilities.H5()
            
            elif valg == 6:
                bruker = 0
                print("Vi smakes.")            

main()