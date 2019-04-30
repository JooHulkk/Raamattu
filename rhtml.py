filer=open("raamattu.txt", "r") #Remember to add utf8 charset afterwards & save as UTF8 in notepad or equivalent
filew=open("raamattu.html", "w")
kirja = ""
vkirja = ""
splitter = ""
luku = ""
vluku = ""
jae = ""
splitlines = False
kirjat = []
predef_kirjat = ['1Moos', '2Moos', '3Moos', '4Moos', '5Moos', 'Joos', 'Tuom', 'Ruut', '1Sam', '2Sam', '1Kun', '2Kun', '1Aik', '2Aik', 'Esra', 'Neh', 'Est', 'Job', 'Ps', 'Sananl', 'Saarn', 'Laul', 'Jes', 'Jer', 'Valit', 'Hes', 'Dan', 'Hoos', 'Joel', 'Aam', 'Ob', 'Joona', 'Miika', 'Nah', 'Hab', 'Sef', 'Hagg', 'Sak', 'Mal', 'Matt', 'Mark', 'Luuk', 'Joh', 'Ap.t', 'Room', '1Kor', '2Kor', 'Gal', 'Ef', 'Fil', 'Kol', '1Tess', '2Tess', '1Tim', '2Tim', 'Tit', 'Filem', 'Hepr', 'Jaak', '1Piet', '2Piet', '1Joh', '2Joh', '3Joh', 'Juud', 'Ilm']
predef_kirjat_nimet = ['1. Mooseksen kirja', '2. Mooseksen kirja', '3. Mooseksen kirja', '4. Mooseksen kirja', '5. Mooseksen kirja', 'Joosuan kirja', 'Tuomarien kirja', 'Ruutin kirja', '1. Samuelin kirja', '2. Samuelin kirja', '1. Kuninkaiden kirja', '2. Kuninkaiden kirja', '1. Aikakirja', '2. Aikakirja', 'Esran kirja', 'Nehamian kirja', 'Esterin kirja', 'Jobin kirja', 'Psalmien kirja', 'Sananlaskujen kirja', 'Saarnaajan kirja', 'Laulujen laulu', 'Jesajan kirja', 'Jeremian kirja', 'Valitusvirret', 'Hesekielin kirja', 'Danielin kirja', 'Hoosean kirja', 'Joelin kirja', 'Aamoksen kirja', 'Obadjan kirja', 'Joonan kirja', 'Miikan kirja', 'Nahumin kirja', 'Habakukin kirja', 'Sefanjan kirja', 'Haggain kirja', 'Sakarjan kirja', 'Malakian kirja', 'Evankeliumi Matteuksen mukaan', 'Evankeliumi Markuksen mukaan', 'Evankeliumi Luukkaan mukaan', 'Evankeliumi Johanneksen mukaan', 'Apostolien teot', 'Kirje roomalaisille', '1. Kirje korianttilaisille', '2. Kirje korianttilaisille', 'Kirje galatalaisille', 'Kirje efesolaisille', 'Kirje filiooiläsille', 'Kirje kolossalaisille', '1. Kirje tessalonikalaisille', '2. Kirje tessalonikalaisille', '1. kirje Timoteukselle', '2. kirje Timoteukselle', 'Kirje Titukselle', 'Kirje Filemonille', 'Kirje heprealaisille', 'Jaakobin kirje', '1. Pietarin kirje', '2. Pietarin kirje', '1. Johanneksen kirje', '2. Johanneksen kirje', '3. Johanneksen kirje', 'Juudaksen kirje', 'Johanneksen ilmestys']
for predef_kirja in predef_kirjat:
        filew.write('<a href="#'+predef_kirja+'">'+predef_kirjat_nimet[predef_kirjat.index(predef_kirja)]+' ('+predef_kirja+')'+'</a>&emsp;')

for line in filer:
    cline=line
    vkirja = kirja
    
    kirja = cline.split (".")[0]
    splitter = "."

    if (kirja == "Ap"):
        kirja = "Ap.t"
    if (len(kirja) > 10):
        kirja = cline.split (" ")[0]
        splitter = " "
    vluku = luku

    if (kirja == "Ap.t"):
        luku = cline[cline.find(splitter)+3:cline.find(":")]
    else:
        luku = cline[cline.find(splitter)+1:cline.find(":")]

    jae = cline[cline.find(":")+1:cline.find(" ")]
    
    if (vkirja != kirja):
        print(kirja)
        kirjat.append(kirja)
        filew.write('<a name="'+kirja+'">'+"<hr><h1>"+kirja+"</h1>")

    if (vluku != luku):
        print(luku)
        filew.write("<h2>"+luku+"</h2>")

    #print (jae)
    if (not splitlines):
        filew.write ("<b><big>"+jae+"  </big></b>")
    else:
        filew.write ("<h4>"+jae+"</h4>")

    teksti = cline.split (" ", 1)[1]
    

    filew.write (teksti)

print ("Seuraavat välilinkit on luotu: ")
print (kirjat)

filew.close()
filer.close()
