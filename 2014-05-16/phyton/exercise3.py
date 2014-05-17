from pyplasm import *
from scipy import *
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)

def merge(diagram,master,toMerge):
    for i in toMerge:
        master = diagram2cell(diagram,master,i)
        hpc = SKEL_1(STRUCT(MKPOLS(master)))
        hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
        VIEW(hpc)

diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
merge(diagram,master,[33,13])
