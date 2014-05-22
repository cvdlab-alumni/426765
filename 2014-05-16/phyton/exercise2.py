from pyplasm import *
from scipy import *
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *
from architectural import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#           MAIN MASTER:
master = assemblyDiagramInit([1,3,2])([[10.4],[3.6,1.6,4.4],[0.3,3]])
V_master,CV_master = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV_master)),CYAN,2)
#VIEW(hpc)

#           MASTER 1:   (1)
master_uno = assemblyDiagramInit([3,1,1])([[2,2.4,5.2],[3.6],[3]])
V_uno,CV_uno = master_uno
hpc_uno = SKEL_1(STRUCT(MKPOLS(master_uno)))
hpc_uno = cellNumbering (master_uno,hpc_uno)(range(len(CV_uno)),CYAN,2)
#VIEW(hpc_uno)

#           MASTER 2:   (3)
master_due = assemblyDiagramInit([2,1,1])([[6,3.6],[1.6],[3]])
V_due,CV_due = master_due
hpc_due = SKEL_1(STRUCT(MKPOLS(master_due)))
hpc_due = cellNumbering (master_due,hpc_due)(range(len(CV_due)),CYAN,2)
#VIEW(hpc_due)

#           MASTER 3:   (5)
master_tre = assemblyDiagramInit([2,1,1])([[4.4,5.2],[4.4],[3]])
V_tre,CV_tre = master_tre
hpc_tre = SKEL_1(STRUCT(MKPOLS(master_tre)))
hpc_tre = cellNumbering (master_tre,hpc_tre)(range(len(CV_tre)),CYAN,2)
#VIEW(hpc_tre)

#           INSERISCO MASTER DENTRO IL MAIN MASTER

toMerge_primo = 1
toMerge_secondo = 2
toMerge_terzo = 3

master = diagram2cell(master_uno,master,toMerge_primo)
master = diagram2cell(master_due,master,toMerge_secondo)
master = diagram2cell(master_tre,master,toMerge_terzo)
#
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)


#           STANZINO:
diagramStanzino = assemblyDiagramInit([3,3,2])([[0.3,2,0.1],[0.3,3.6,0.1],[0.3,3]])
hpcStanzino = SKEL_1(STRUCT(MKPOLS(diagramStanzino)))
VStanzino,CVStanzino = diagramStanzino
hpcStanzino = cellNumbering (diagramStanzino,hpcStanzino)(range(len(CVStanzino)),CYAN,2)
#VIEW(hpcStanzino)

toMerge = 11

doorStanzino = assemblyDiagramInit([3,1,2])([[0.8,0.8,0.4],[0.1],[2.2,0.5]])
masterStanzino = diagram2cell(doorStanzino,diagramStanzino,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterStanzino)))
hpc = cellNumbering (masterStanzino,hpc)(range(len(masterStanzino[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,9]
masterStanzino = masterStanzino[0], [cell for k,cell in enumerate(masterStanzino[1]) if not (k in toRemove)]
#DRAW(masterStanzino)

toMerge = 7

windowStanzino = assemblyDiagramInit([3,1,3])([[0.6,0.8,0.6],[0.1],[2.2,3,3.5]])
masterStanzino = diagram2cell(windowStanzino,masterStanzino,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterStanzino)))
hpc = cellNumbering (masterStanzino,hpc)(range(len(masterStanzino[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterStanzino = masterStanzino[0], [cell for k,cell in enumerate(masterStanzino[1]) if not (k in toRemove)]
#DRAW(masterStanzino)

#           CUCINA:
diagramCucina = assemblyDiagramInit([3,3,2])([[0.1,2.4,0.1],[0.3,3.6,0.1],[0.3,3]])
hpcCucina = SKEL_1(STRUCT(MKPOLS(diagramCucina)))
VCucina,CVCucina = diagramCucina
hpcCucina = cellNumbering (diagramCucina,hpcCucina)(range(len(CVCucina)),CYAN,2)
#VIEW(hpcCucina)

toMerge = 11

doorCucina = assemblyDiagramInit([3,1,2])([[0.4,0.8,1.2],[0.1],[2.2,0.5]])
masterCucina = diagram2cell(doorCucina,diagramCucina,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCucina)))
hpc = cellNumbering (masterCucina,hpc)(range(len(masterCucina[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,9]
masterCucina = masterCucina[0], [cell for k,cell in enumerate(masterCucina[1]) if not (k in toRemove)]
#DRAW(masterCucina)

toMerge = 7

windowCucina = assemblyDiagramInit([3,1,2])([[0.6,1,0.6],[0.1],[2.2,0.5]])
masterCucina = diagram2cell(windowCucina,masterCucina,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCucina)))
hpc = cellNumbering (masterCucina,hpc)(range(len(masterCucina[1])),CYAN,2)
#VIEW(hpc)

toRemove = [22]
masterCucina = masterCucina[0], [cell for k,cell in enumerate(masterCucina[1]) if not (k in toRemove)]
#DRAW(masterCucina)

#           STANZA_3:
diagramStanza_3 = assemblyDiagramInit([3,3,2])([[0.1,5.2,0.3],[0.3,3.6,0.1],[0.3,3]])
hpcStanza_3 = SKEL_1(STRUCT(MKPOLS(diagramStanza_3)))
VStanza_3,CVStanza_3 = diagramStanza_3
hpcDiagramStanza_3 = cellNumbering (diagramStanza_3,hpcStanza_3)(range(len(CVStanza_3)),CYAN,2)
#VIEW(hpcDiagramStanza_3)

toMerge = 11

doorStanza_3 = assemblyDiagramInit([3,1,2])([[0.4,0.5,2],[0.1],[2.2,0.5]])
masterStanza_3 = diagram2cell(doorStanza_3,diagramStanza_3,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterStanza_3)))
hpc = cellNumbering (masterStanza_3,hpc)(range(len(masterStanza_3[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,9]
masterStanza_3 = masterStanza_3[0], [cell for k,cell in enumerate(masterStanza_3[1]) if not (k in toRemove)]
#DRAW(masterStanza_3)

toMerge = 13

windowStanza_3 = assemblyDiagramInit([1,3,3])([[0.3],[1.2,1.6,0.8],[2,3.5,2]])
masterStanza_3 = diagram2cell(windowStanza_3,masterStanza_3,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterStanza_3)))
hpc = cellNumbering (masterStanza_3,hpc)(range(len(masterStanza_3[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterStanza_3 = masterStanza_3[0], [cell for k,cell in enumerate(masterStanza_3[1]) if not (k in toRemove)]
#DRAW(masterStanza_3)

#           CORRIDOIO:
diagramCorridoio = assemblyDiagramInit([3,3,2])([[0.3,6,0.1],[0.1,1.6,0.1],[0.3,3]])
hpcCorridoio = SKEL_1(STRUCT(MKPOLS(diagramCorridoio)))
VCorridoio,CVCorridoio = diagramCorridoio
hpcDiagramCorridoio = cellNumbering (diagramCorridoio,hpcCorridoio)(range(len(CVCorridoio)),CYAN,2)
#VIEW(hpcDiagramCorridoio)

toMerge = 3

doorCorridoio = assemblyDiagramInit([1,3,2])([[0.3],[0.4,0.8,0.4],[2.2,0.5]])
masterCorridoio = diagram2cell(doorCorridoio,diagramCorridoio,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCorridoio)))
hpc = cellNumbering (masterCorridoio,hpc)(range(len(masterCorridoio[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterCorridoio = masterCorridoio[0], [cell for k,cell in enumerate(masterCorridoio[1]) if not (k in toRemove)]
#DRAW(masterCorridoio)

#           BAGNO
diagramBagno = assemblyDiagramInit([3,3,2])([[0.1,3.6,0.3],[0.1,1.6,0.1],[0.3,3]])
hpcBagno = SKEL_1(STRUCT(MKPOLS(diagramBagno)))
VBagno,CVBagno = diagramBagno
hpcDiagramBagno = cellNumbering (diagramBagno,hpcBagno)(range(len(CVBagno)),CYAN,2)
#VIEW(hpcDiagramBagno)

toMerge = 3

doorBagno = assemblyDiagramInit([1,3,2])([[0.3],[0.4,0.8,0.4],[2.2,0.5]])
masterBagno = diagram2cell(doorBagno,diagramBagno,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterBagno)))
hpc = cellNumbering (masterBagno,hpc)(range(len(masterBagno[1])),CYAN,2)
#VIEW(hpc)

toMerge = 14

windowBagno = assemblyDiagramInit([1,3,3])([[0.3],[0.4,0.8,0.4],[2,3.5,2]])
masterBagno = diagram2cell(windowBagno,masterBagno,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterBagno)))
hpc = cellNumbering (masterBagno,hpc)(range(len(masterBagno[1])),CYAN,2)
#VIEW(hpc)

toRemove = [26,8,18]
masterBagno = masterBagno[0], [cell for k,cell in enumerate(masterBagno[1]) if not (k in toRemove)]
#DRAW(masterBagno)

#           STANZA_1
diagramStanza_1 = assemblyDiagramInit([3,3,2])([[0.3,4.4,0.1],[0.1,4.4,0.3],[0.3,3]])
hpcStanza_1 = SKEL_1(STRUCT(MKPOLS(diagramStanza_1)))
VStanza_1,CVStanza_1 = diagramStanza_1
hpcDiagramStanza_1 = cellNumbering (diagramStanza_1,hpcStanza_1)(range(len(CVStanza_1)),CYAN,2)
#VIEW(hpcDiagramStanza_1)

toMerge = 7

doorStanza_1 = assemblyDiagramInit([3,1,2])([[3.2,0.8,0.4],[0.3],[2.2,0.5]])
masterStanza_1 = diagram2cell(doorStanza_1,diagramStanza_1,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterStanza_1)))
hpc = cellNumbering (masterStanza_1,hpc)(range(len(masterStanza_1[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterStanza_1 = masterStanza_1[0], [cell for k,cell in enumerate(masterStanza_1[1]) if not (k in toRemove)]
#DRAW(masterStanza_1)

toMerge = 9

#windowStanza_1 = assemblyDiagramInit([3,1,3])([[2,1.6,0.8],[0.3],[0.8,1.6,2]])
windowStanza_1 = assemblyDiagramInit([3,1,3])([[1.2,1.6,0.8],[0.3],[2,3.5,2]])
masterStanza_1 = diagram2cell(windowStanza_1,masterStanza_1,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterStanza_1)))
hpc = cellNumbering (masterStanza_1,hpc)(range(len(masterStanza_1[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterStanza_1 = masterStanza_1[0], [cell for k,cell in enumerate(masterStanza_1[1]) if not (k in toRemove)]
#DRAW(masterStanza_1)



#           STANZA_2:
diagramStanza_2 = assemblyDiagramInit([3,3,2])([[0.1,5.3,0.3],[0.1,4.4,0.3],[0.3,3]]) #5.2 -> 5.3
hpcStanza_2 = SKEL_1(STRUCT(MKPOLS(diagramStanza_2)))
VStanza_2,CVStanza_2 = diagramStanza_2
hpcDiagramStanza_2 = cellNumbering (diagramStanza_2,hpcStanza_2)(range(len(CVStanza_2)),CYAN,2)
#VIEW(hpcDiagramStanza_2)

toMerge = 7

doorStanza_2 = assemblyDiagramInit([3,1,2])([[0.4,0.8,4],[0.3],[2.2,0.5]])
masterStanza_2 = diagram2cell(doorStanza_2,diagramStanza_2,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterStanza_2)))
hpc = cellNumbering (masterStanza_2,hpc)(range(len(masterStanza_2[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterStanza_2 = masterStanza_2[0], [cell for k,cell in enumerate(masterStanza_2[1]) if not (k in toRemove)]
#DRAW(masterStanza_2)

toMerge = 13

windowStanza_2 = assemblyDiagramInit([1,3,3])([[0.3],[0.8,1.6,2],[2,3.5,2]])
masterStanza_2 = diagram2cell(windowStanza_2,masterStanza_2,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterStanza_2)))
hpc = cellNumbering (masterStanza_2,hpc)(range(len(masterStanza_2[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterStanza_2 = masterStanza_2[0], [cell for k,cell in enumerate(masterStanza_2[1]) if not (k in toRemove)]
#DRAW(masterStanza_2)


#       INSERISCO STANZINO:

toMerge_stanzino = 3
master = diagram2cell(masterStanzino,master,toMerge_stanzino)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)

#       INSERISCO CUCINA:

toMerge_cucina = 3
master = diagram2cell(masterCucina,master,toMerge_cucina)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)

#       INSERISCO STANZA_3:

toMerge_stanza_3 = 3
master = diagram2cell(masterStanza_3,master,toMerge_stanza_3)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)

#       INSERISCO CORRIDOIO:

toMerge_corridoio = 3
master = diagram2cell(masterCorridoio,master,toMerge_corridoio)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)

#       INSERISCO BAGNO:

toMerge_bagno = 3
master = diagram2cell(masterBagno,master,toMerge_bagno)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)

#       INSERISCO STANZA_1:

toMerge_stanza_1 = 3
master = diagram2cell(masterStanza_1,master,toMerge_stanza_1)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)

#       INSERISCO STANZA_2:

toMerge_stanza_2 = 3
master = diagram2cell(masterStanza_2,master,toMerge_stanza_2)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)


toRemove = [93,90,97,114,111,15,43,145]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

CREA_MODELLO = COMP([STRUCT,MKPOLS])
modelloPiano = CREA_MODELLO(master)
#VIEW(modelloPiano)



#       PORTA DI INGRESSO

porta = COLOR([0.58823529411,0.29411764705,0])(CUBOID([1,0.15,1.5]))

linea0 = T([1,2])([0,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
linea1 = T([1,2])([0.1,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
linea2 = T([1,2])([0.2,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
linea3 = T([1,2])([0.3,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
linea4 = T([1,2])([0.4,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
linea5 = T([1,2])([0.5,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
linea6 = T([1,2])([0.6,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
linea7 = T([1,2])([0.7,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
linea8 = T([1,2])([0.8,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
linea9 = T([1,2])([0.9,-0.01])(COLOR(BLACK)(CUBOID([0.05,0.03,1.5])))
primoPezzoManiglia = T([1,2,3])([0.9,-0.1,0.95])(CUBOID([0.03,0.1,0.03]))

secondoPezzoManiglia = T([1,2,3])([0.75,-0.1,0.95])(CUBOID([0.2,0.03,0.03]))
maniglia = STRUCT([primoPezzoManiglia,secondoPezzoManiglia])
maniglia = COLOR([0.8,0.4,0])(maniglia)

portaIngresso = STRUCT([porta,linea0,linea1,linea2,linea3,linea4,linea5,linea6,linea7,linea8,linea9,maniglia])
portaIngresso = T([1,2,3])([0.1,4.9,0.57])(S(3)(1.5)(R([1,2])(-PI/2)(portaIngresso)))

#VIEW(STRUCT([modelloPiano,portaIngresso]))


#       PORTA INTERNA

porta = COLOR([0.58823529411,0.29411764705,0])(CUBOID([1,0.06,2.5]))

primoPezzoManiglia = T([1,2,3])([0.9,-0.1,0.95])(CUBOID([0.03,0.1,0.03]))

secondoPezzoManiglia = T([1,2,3])([0.75,-0.1,0.95])(CUBOID([0.2,0.03,0.03]))
maniglia = STRUCT([primoPezzoManiglia,secondoPezzoManiglia])
maniglia = COLOR([0.8,0.4,0])(maniglia)
maniglia2 = maniglia
maniglia2 = R([2,2])(PI)(maniglia2)
maniglia2 = T(2)(0.05)(maniglia2)
portaInterna = STRUCT([porta,maniglia, maniglia2])
portaInternaStanza_1 = portaInterna

portaInterna = STRUCT([porta,maniglia,maniglia2])
portaInternaStanza_1 = T([1,2,3])([3.3,5.22,0.57])(portaInterna)
portaInternaStanza_2 = T([1,2,3])([5.1,5.22,0.57])(portaInterna)
portaInternaBagno = T([1,2,3])([6.59,3.755,0.57])(R([1,2])(PI/2)(portaInterna))
portaInternaStanza_3 = T([1,2,3])([5.5,3.53,0.57])(portaInterna)
portaInternaCucina = T([1,2,3])([2.5,3.53,0.57])(portaInterna)
portaInternaStanzino = T([1,2,3])([0.75,3.53,0.57])(portaInterna)
casaConPorte = STRUCT([modelloPiano,portaIngresso,portaInternaStanza_1,portaInternaStanza_2,portaInternaBagno,portaInternaStanza_3,portaInternaCucina,portaInternaStanzino])
#VIEW(casaConPorte)

#       FINESTRE

finestraX = COLOR(CYAN)(CUBOID([9.18,0.2,2.8]))
finestraY = COLOR(CYAN)(CUBOID([0.2,7,2]))
finestraX = T([1,2,3])([0.5,0.02,0.3])(finestraX)
finestraY = T([1,2,3])([10.18,1.4,1])(finestraY)
finestraXsup = T([1,2,3])([0.5,9.35,0.18])(finestraX)




#               BALCONE

sottoBalcone = CUBOID([1.66,0.86,0.2])

pezzoRinghiera1 = T([1,2])([0.03,0.03])(CYLINDER([0.018,1])(30))
pezzoRinghiera2 = T([1,2])([0.23,0.03])(CYLINDER([0.018,1])(30))
pezzoRinghiera3 = T([1,2])([0.43,0.03])(CYLINDER([0.018,1])(30))
pezzoRinghiera4 = T([1,2])([0.63,0.03])(CYLINDER([0.018,1])(30))
pezzoRinghiera5 = T([1,2])([0.83,0.03])(CYLINDER([0.018,1])(30))
pezzoRinghiera6 = T([1,2])([1.03,0.03])(CYLINDER([0.018,1])(30))
pezzoRinghiera7 = T([1,2])([1.23,0.03])(CYLINDER([0.018,1])(30))
pezzoRinghiera8 = T([1,2])([1.43,0.03])(CYLINDER([0.018,1])(30))
pezzoRinghiera9 = T([1,2])([1.63,0.03])(CYLINDER([0.018,1])(30))

pezzoRinghiera11 = T([1,2])([0.03,0.23])(CYLINDER([0.018,1])(30))
pezzoRinghiera12 = T([1,2])([0.03,0.43])(CYLINDER([0.018,1])(30))
pezzoRinghiera13 = T([1,2])([0.03,0.63])(CYLINDER([0.018,1])(30))
pezzoRinghiera14 = T([1,2])([0.03,0.83])(CYLINDER([0.018,1])(30))

pezzoRinghiera15 = T([1,2])([1.63,0.23])(CYLINDER([0.018,1])(30))
pezzoRinghiera16 = T([1,2])([1.63,0.43])(CYLINDER([0.018,1])(30))
pezzoRinghiera17 = T([1,2])([1.63,0.63])(CYLINDER([0.018,1])(30))
pezzoRinghiera18 = T([1,2])([1.63,0.83])(CYLINDER([0.018,1])(30))

ringhiera = STRUCT([pezzoRinghiera1,pezzoRinghiera2,pezzoRinghiera3,pezzoRinghiera4,pezzoRinghiera5,pezzoRinghiera6,pezzoRinghiera7,pezzoRinghiera8,pezzoRinghiera9,pezzoRinghiera11,
                    pezzoRinghiera12,pezzoRinghiera13,pezzoRinghiera14,pezzoRinghiera15,pezzoRinghiera16,pezzoRinghiera17,pezzoRinghiera18])

tienitiBene = T([1,2,3])([0.01,0.008,0.95])(CUBOID([1.63,0.08,0.08]))
tienitiBeneDX = T([1,2,3])([1.6,0.008,0.95])(CUBOID([0.08,0.88,0.08]))
tienitiBeneSX = T([1,2,3])([0.01,0.008,0.95])(CUBOID([0.08,0.88,0.08]))

balcone = T([1,2,3])([2.6,-1,0.4])(STRUCT([COLOR(BLACK)(ringhiera),sottoBalcone,COLOR(BROWN)(tienitiBene),COLOR(BROWN)(tienitiBeneSX),COLOR(BROWN)(tienitiBeneDX)]))



pianoTerra = STRUCT([casaConPorte,finestraX,finestraY,finestraXsup])
pianiVari = STRUCT([casaConPorte,finestraX,finestraY,finestraXsup,balcone])
pianiVari = T(3)(3)(STRUCT([pianiVari,T(3)(3)]*5))
tetto = T(3)(18)(CUBOID([10.4,9.6,0.3]))
palazzo = STRUCT([pianoTerra,pianiVari,tetto])

palazzo = T(1)(3)(palazzo)
piattaforma = T([1,2])([-3,3.5])(CUBOID([6,2,0.35]))
piattaforme = STRUCT([piattaforma,T(3)(3)]*7)
palazzi = STRUCT([palazzo,S(1)(-1)(palazzo),piattaforme])

#       SCALA A CHIOCCIOLA
def spiralStair(thickness=0.2,R=1.,r=0.5,riser=0.1,pitch=2.,nturns=2.,steps=18):
    V,CV = larSolidHelicoid(thickness,R,r,pitch,nturns,steps)()
    W = CAT([[V[k],V[k+1],V[k+2],V[k+3]]+[SUM([V[k+1],[0,0,-riser]]),SUM([V[k+3],[0,0,-riser]])]
        for k,v in enumerate(V[:-4]) if k%4==0])
    for k,w in enumerate(W[:-12]):
        if k%6==0: W[k+1][2]=W[k+10][2]; W[k+3][2]=W[k+11][2]
    nsteps = len(W)/12
    CW =[SUM([[0,1,2,3,6,8,10,11],[6*k]*8])
            for k in range(nsteps)]
    return W,CW

stair = STRUCT(MKPOLS(spiralStair(0.2,1,0.5,0.1,2,15,18)))
stair = R([1,2])(PI/2)(stair)
stair = T(2)(2.5)(stair)

attraversamentoUltimoPiano = T([2,3])([1.5,15])(CUBOID([0.5,2,0.2]))


VIEW(STRUCT([palazzi,stair,attraversamentoUltimoPiano]))