from scipy import *
from splines import *
from sysml import *
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
# numerazione
def numbering(master):
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
    VIEW(hpc)
# merge
def diagram2cellGroup(diagram,master,group):
    group.sort();
    group.reverse();
    for i in group:
        master = diagram2cell(diagram,master,i)
    numbering(master)
    return master

# delete
def cellsOff(master,group):
    V,CV = master
    master =  V,[cell for i,cell in enumerate(CV) if not (i in group)]
    numbering(master)
    return master



#   INSERISCE AUTOMATICAMENTE CELLE
def automaticInsert(master,group,diagram):
    numbering(master)
    master = diagram2cellGroup(diagram,master,group)
    return master


#   RIMUOVE AUTOMATICAMENTE CELLE
def automaticRemove(master, group):
	master = cellsOff(master,group)
	return master