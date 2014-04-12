from pyplasm import *
from larcc import *
from lar2psm import *
side_1 = [[20,36],[36,20]]
side_2 = [[50,14],[72,14]]
side_3 = [[86,20],[102,36]]
side_4 = [[108,50],[108,72]]
side_5 = [[102,86],[86,102]]
side_6 = [[72,108],[50,108]]
side_7 = [[36,102],[20,86]]
side_8 = [[14,72],[14,50]]

polylines_sides = (AA(POLYLINE)([side_1,side_2,side_3,side_4,side_5,side_6,side_7,side_8]))
polygon_sides = COLOR([0.74,0.7,0.66])(STRUCT(polylines_sides))

octagon_1 = [[36,20],[30,14],[30,6],[36,0],[44,0],[50,6],[50,14]]
octagon_2 = [[72,14],[72,6],[78,0],[86,0],[92,6],[92,14],[86,20]]
octagon_3 = [[102,36],[108,30],[116,30],[122,36],[122,44],[116,50],[108,50]]
octagon_4 = [[108,72],[116,72],[122,78],[122,86],[116,92],[108,92],[102,86]]
octagon_5 = [[72,108],[72,116],[78,122],[86,122],[92,116],[92,108],[86,102]]
octagon_6 = [[36,102],[30,108],[30,116],[36,122],[44,122],[50,116],[50,108]]
octagon_7 = [[14,72],[6,72],[0,78],[0,86],[6,92],[14,92],[20,86]]
octagon_8 = [[20,36],[14,30],[6,30],[0,36],[0,44],[6,50],[14,50]]

polylines_octagons = (AA(POLYLINE)([octagon_1,octagon_2,octagon_3,octagon_4,octagon_5,octagon_6,octagon_7,octagon_8]))
polygon_octagons = COLOR([0.74,0.7,0.66])(STRUCT(polylines_octagons))


octagon_1 = [[36,20],[30,14],[30,6],[36,0],[44,0],[50,6],[50,14]]
octagon_2 = [[72,14],[72,6],[78,0],[86,0],[92,6],[92,14],[86,20]]
octagon_3 = [[102,36],[108,30],[116,30],[122,36],[122,44],[116,50],[108,50]]
octagon_4 = [[108,72],[116,72],[122,78],[122,86],[116,92],[108,92],[102,86]]
octagon_5 = [[72,108],[72,116],[78,122],[86,122],[92,116],[92,108],[86,102]]
octagon_6 = [[36,102],[30,108],[30,116],[36,122],[44,122],[50,116],[50,108]]
octagon_7 = [[14,72],[6,72],[0,78],[0,86],[6,92],[14,92],[20,86]]
octagon_8 = [[20,36],[14,30],[6,30],[0,36],[0,44],[6,50],[14,50]]octagon_1 = (AA(POLYLINE)([octagon_1]))octagon_2 = (AA(POLYLINE)([octagon_2]))octagon_3 = (AA(POLYLINE)([octagon_3]))octagon_4 = (AA(POLYLINE)([octagon_4]))octagon_5 = (AA(POLYLINE)([octagon_5]))octagon_6 = (AA(POLYLINE)([octagon_6]))octagon_7 = (AA(POLYLINE)([octagon_7]))octagon_8 = (AA(POLYLINE)([octagon_8]))o1 = (STRUCT(octagon_1))o2 = (STRUCT(octagon_2))o3 = (STRUCT(octagon_3))o4 = (STRUCT(octagon_4))o5 = (STRUCT(octagon_5))o6 = (STRUCT(octagon_6))o7 = (STRUCT(octagon_7))o8 = (STRUCT(octagon_8))octagon_1b = PROD([o1,Q(8)])octagon_2b = PROD([o2,Q(8)])octagon_3b = PROD([o3,Q(8)])octagon_4b = PROD([o4,Q(8)])octagon_5b = PROD([o5,Q(8)])octagon_6b = PROD([o6,Q(8)])octagon_7b = PROD([o7,Q(8)])octagon_8b = PROD([o8,Q(8)])only_top = STRUCT([octagon_1b,octagon_2b,octagon_3b,octagon_4b,octagon_5b,octagon_6b,octagon_7b,octagon_8b])only_top_SOLIDIFY = (only_top)torri = STRUCT([only_top_SOLIDIFY])torri_alzate = COLOR([0.74,0.7,0.66])(T(3)(52)(torri))

struttura_base_complete = PROD([(STRUCT([polygon_octagons,polygon_sides])),Q(56)])
compl = STRUCT([COLOR([0.74,0.7,0.66])(struttura_base_complete),torri_alzate])




# finestre:window_8 = CUBOID([0,3.1,5])window_8_T = COLOR([0.63,1,1])(T([1,2,3])([14,58,28])(window_8))window_4 = CUBOID([0,3.1,5])window_4_T = COLOR([0.63,1,1])(T([1,2,3])([108,59,28])(window_4))window_6 = CUBOID([3,0,5.1])window_6_T = COLOR([0.63,1,1])(T([1,2,3])([59.5,108,28])(window_6))window_over_door = COLOR([0.63,1,1])(CUBOID([3,0,5.1]))window_over_door = T([1,2,3])([59.5,14,28])(window_over_door)

# finestre del piano di sottowindow_8 = CUBOID([0,3,5])window_8_T_sub = COLOR([0.63,1,1])(T([1,2,3])([14,58,12])(window_8))window_4 = CUBOID([0,3,5])window_4_T_sub = COLOR([0.63,1,1])(T([1,2,3])([108,59,12])(window_4))window_6 = CUBOID([3,0,5])window_6_T_sub = COLOR([0.63,1,1])(T([1,2,3])([59.5,108,12])(window_6))

big_door = CUBOID([10,2,22])big_door = T([1,2])([56,12])(big_door)smaller_door = T(3)(3)(CUBOID([6,2,10]))smaller_door = T([1,2])([58,11.99])(smaller_door)triangolo_sopra_porta = CUBOID([7,2,7])triangolo_sopra_porta = R([1,3])(PI/4)(triangolo_sopra_porta)triangolo_sopra_porta = T([1,2,3])([61,12,17])(triangolo_sopra_porta)structure_with_door = STRUCT([COLOR([0.59,0.52,0.47])(big_door),COLOR([0.28,0.2,0.14])(smaller_door),COLOR([0.59,0.52,0.47])(triangolo_sopra_porta)])

primo_scalino = CUBOID([15,5,1])secondo_scalino = T([2,3])([1,1])(CUBOID([15,4,1]))terzo_scalino = T([2,3])([2,2])(CUBOID([15,3,1]))scalini = T([1,2])([53.5,9])(COLOR([0.46,0.35,0.25])(STRUCT([primo_scalino,secondo_scalino,terzo_scalino])))

compl_2 = STRUCT([compl,window_8_T,window_4_T,window_6_T,window_over_door,window_8_T_sub,window_4_T_sub,window_6_T_sub,structure_with_door,scalini])
VIEW(compl_2)