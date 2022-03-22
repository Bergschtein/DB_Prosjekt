

CREATE TABLE Bruker (
                    brukerID INTEGER PRIMARY KEY AUTOINCREMENT,
                    epost VARCHAR UNIQUE NOT NULL, 
                    passord VARCHAR NOT NULL, 
                    fornavn TEXT NOT NULL, 
                    etternavn TEXT NOT NULL);
CREATE TABLE Innlegg (
                    innleggID INTEGER PRIMARY KEY AUTOINCREMENT,
                    smaksnotat TEXT, 
                    poeng INTEGER CHECK( poeng >= 0 AND poeng <= 10), 
                    smaksdato TEXT, 
                    brukerID INTEGER, 
                    fkID INTEGER,
                    CONSTRAINT FK_BrukerID FOREIGN KEY (brukerID) 
                    REFERENCES Bruker(brukerID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                    CONSTRAINT FK_FerdigbrenntKaffe FOREIGN KEY (fkID) 
                    REFERENCES FerdigbrenntKaffe(fkID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE);

CREATE TABLE Brenneri (
                    brenneriID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    navn VARCHAR UNIQUE, 
                    region VARCHAR);

CREATE TABLE FerdigbrenntKaffe (
                    fkID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    partiID INTEGER, 
                    brenneriID INTEGER ,
                    navn TEXT, 
                    brenningsdato TEXT, 
                    brenningsgrad TEXT CHECK(brenningsgrad IN ('lys', 'middels', 'mørk')), 
                    beskrivelse TEXT,
                    kgPris REAL,
                    CONSTRAINT FK_Parti FOREIGN KEY (partiID) 
                    REFERENCES Parti(partiID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                    CONSTRAINT FK_Brenneri FOREIGN KEY (brenneriID) 
                    REFERENCES Brenneri(brenneriID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE);


CREATE TABLE Parti (
                    partiID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    gårdID INTEGER, 
                    fmID INTEGER, 
                    innhøstingsår INTEGER, 
                    betalingPerKg REAL,
                    CONSTRAINT FK_Gård FOREIGN KEY (gårdID) 
                    REFERENCES Gård(gårdID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                    CONSTRAINT FK_Foredlingsmetode FOREIGN KEY (fmID) 
                    REFERENCES Foredlingsmetode(fmID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE);
CREATE TABLE Foredlingsmetode (
                    fmID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    navn TEXT UNIQUE, 
                    beskrivelse TEXT);
CREATE TABLE Bønne (
                    bønneID INTEGER PRIMARY KEY AUTOINCREMENT,
                    art TEXT NOT NULL UNIQUE,
                    navn VARCHAR);                    
CREATE TABLE Gård (
                    gårdID INTEGER AUTO_INCREMENT PRIMARY KEY,  
                    navn TEXT , 
                    HoH INTEGER, 
                    region TEXT, 
                    land TEXT);                                        
CREATE TABLE Dyrke (
                    gårdID INTEGER, 
                    bønneID INTEGER,
                    CONSTRAINT PK_Dyrke PRIMARY KEY (gårdID, bønneID),
                    CONSTRAINT FK_Gård FOREIGN KEY (gårdID) 
                    REFERENCES Gård(gårdID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                    CONSTRAINT FK_Bønne FOREIGN KEY (bønneID) 
                    REFERENCES Bønne(bønneID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE);                                                            
CREATE TABLE Innhold (
                    partiID INTEGER, 
                    bønneID INTEGER,
                    CONSTRAINT PK_Innhold PRIMARY KEY (partiID , bønneID)
                    CONSTRAINT FK_Parti FOREIGN KEY (partiID) 
                    REFERENCES Parti(partiID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                    CONSTRAINT FK_Bønne FOREIGN KEY (bønneID) REFERENCES Bønne(bønneID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE);                                                                                                                                                                       



INSERT INTO Bruker 
                VALUES (1,'maya.papaya534@stud.ntnu.no', 'maya', 'maya', 'papaya'); 
INSERT INTO Bruker 
                VALUES (2, 'nora.åsen626@outlook.no', 'nora', 'nora', 'åsen'); 
INSERT INTO Bruker 
                VALUES (3, 'isak.fisak806@gmail.com', 'isak', 'isak', 'fisak'); 

-- Til brukerhistorien
INSERT INTO Innlegg 
                VALUES (1, 'Wow - en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, '20.02.2020', 1, 1); 

INSERT INTO Innlegg 
                VALUES (2, 'Denne er god as', 8, '20.02.2022', 2, 1); 

INSERT INTO Innlegg 
                VALUES (3, 'meh', 3, '18.02.2022', 2, 2);    

INSERT INTO Innlegg 
                VALUES (4, 'Fantastisk, florale tendenser', 9, '18.02.2022', 2, 3);    


INSERT INTO Innlegg 
                VALUES (5, 'God', 7, '20.02.2022', 3, 1); 

INSERT INTO Innlegg 
                VALUES (6, 'Funker', 5, '18.02.2022', 3, 2);    

INSERT INTO Innlegg 
                VALUES (7, 'Likte denne', 8, '18.02.2022', 3, 3);    


--- Test av H2
INSERT INTO Innlegg 
                VALUES (8, 'Wow - en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, '20.02.2022', 1, 2); 

INSERT INTO Innlegg 
                VALUES (9, 'Wow - en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, '20.02.2022', 2, 1); 




INSERT INTO FerdigbrenntKaffe 
                VALUES (1, 1, 1, 'Vinterkaffe 2022', '20.01.2022', 'lys' , 'En velsmakende og kompleks kaffe for mørketiden', 600) 
;    

INSERT INTO FerdigbrenntKaffe 
                VALUES (2, 2, 2, 'Sommerkaffe 2022', '20.05.2022', 'middels' , 'En velsmakende og kompleks kaffe for soloppgangen, noen vil si den er floral', 600) 
;    

INSERT INTO FerdigbrenntKaffe 
                VALUES (3, 3, 3, 'Vårkaffe 2022', '20.03.2022', 'mørk' , 'En velsmakende og kompleks kaffe for våren', 200) 
;    






INSERT INTO Brenneri
                VALUES(1, 'Jacobsen & Svart', 'Trondheim')
; 

INSERT INTO Brenneri
                VALUES(2, 'Jacobsen & Hvit', 'Oslo')
; 

INSERT INTO Brenneri
                VALUES(3, 'Jacobsen & Schwartz', 'Berlin')
; 






INSERT INTO Foredlingsmetode
                VALUES (1, 'bærtørket', 'Tørker kaffebærne... ')
;            
INSERT INTO Foredlingsmetode
                VALUES (2, 'vasket', 'Skiller fruktkjøttet fra bønnen umiddelbart etter innhøsting... ')
;




INSERT INTO Parti
                VALUES (1, 1, 1, '2021', 8)
;


INSERT INTO Parti
                VALUES (2, 2, 2, '2022', 10)
;


INSERT INTO Parti
                VALUES (3, 1, 3, '2021', 9)
;




INSERT INTO Gård
                VALUES (1, 'Nombre de Dios', 1500, 'Santa Ana', 'El Salvador')
;
INSERT INTO Gård
                VALUES (2, 'Nombre de Tres', 500, 'Banan', 'Mexico')
;
INSERT INTO Gård
                VALUES (3, 'Nombre de Quattro', 1000, 'Santa Maria', 'El Kalvador')
;
INSERT INTO Gård
                VALUES (4, 'Nombre de fem på spansk', 1000, 'Et sted i Rwanda', 'Rwanda')
;




INSERT INTO Bønne(art, navn)
                VALUES ('coffea arabica', 'Bourbon')
;                
INSERT INTO Bønne(art, navn) 
                VALUES ('coffea robusta', 'Baboon')
;               
INSERT INTO Bønne(art, navn) 
                VALUES ('coffea liberica', 'Kakoon')
;


INSERT INTO Innhold 
                VALUES (1,1)
;                                    
INSERT INTO Innhold 
                VALUES (2,1)
; 
INSERT INTO Innhold 
                VALUES (2,2)
; 