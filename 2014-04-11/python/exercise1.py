from pyplasm import *

#LISTA DEI LATI

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

#LISTA DEGLI OTTAGONI (non completi, ma si adeguano punto per punto ai vari muri adiacenti

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

octagon_1_complete = [[36,20],[30,14],[30,6],[36,0],[44,0],[50,6],[50,14],[44,20],[36,20]]
octagon_2_complete = [[72,14],[72,6],[78,0],[86,0],[92,6],[92,14],[86,20],[78,20],[72,14]]
octagon_3_complete = [[102,36],[108,30],[116,30],[122,36],[122,44],[116,50],[108,50],[102,44],[102,36]]
octagon_4_complete = [[108,72],[116,72],[122,78],[122,86],[116,92],[108,92],[102,86],[102,78],[108,72]]
octagon_5_complete = [[72,108],[72,116],[78,122],[86,122],[92,116],[92,108],[86,102],[78,102],[72,108]]
octagon_6_complete = [[36,102],[30,108],[30,116],[36,122],[44,122],[50,116],[50,108],[44,102],[36,102]]
octagon_7_complete = [[14,72],[6,72],[0,78],[0,86],[6,92],[14,92],[20,86],[20,78],[14,72]]
octagon_8_complete = [[20,36],[14,30],[6,30],[0,36],[0,44],[6,50],[14,50],[20,44],[20,36]]
octagon_1_complete = (AA(POLYLINE)([octagon_1_complete]))octagon_2_complete = (AA(POLYLINE)([octagon_2_complete]))octagon_3_complete = (AA(POLYLINE)([octagon_3_complete]))octagon_4_complete = (AA(POLYLINE)([octagon_4_complete]))octagon_5_complete = (AA(POLYLINE)([octagon_5_complete]))octagon_6_complete = (AA(POLYLINE)([octagon_6_complete]))octagon_7_complete = (AA(POLYLINE)([octagon_7_complete]))octagon_8_complete = (AA(POLYLINE)([octagon_8_complete]))o1 = (STRUCT(octagon_1_complete))o2 = (STRUCT(octagon_2_complete))o3 = (STRUCT(octagon_3_complete))o4 = (STRUCT(octagon_4_complete))o5 = (STRUCT(octagon_5_complete))o6 = (STRUCT(octagon_6_complete))o7 = (STRUCT(octagon_7_complete))o8 = (STRUCT(octagon_8_complete))top_ottagoni_torri = STRUCT([o1,o2,o3,o4,o5,o6,o7,o8])
top_ottagoni_torri_SOLIDIFY = SOLIDIFY(top_ottagoni_torri)
top_ottagoni_torri_SOLIDIFY_spesse = PROD([top_ottagoni_torri_SOLIDIFY,Q(2)])
top_ottagoni_torri_SOLIDIFY_spesse_rialzate = T(3)(70)(top_ottagoni_torri_SOLIDIFY_spesse)
#VIEW(top_ottagoni_torri_SOLIDIFY_spesse_rialzate)
#######################

strutturaDiBase = STRUCT([polygon_octagons,polygon_sides])
strutturaDiBaseSpessa = SOLIDIFY(PROD([strutturaDiBase, Q(2)]))

primo_piano = T(3)(28)(strutturaDiBaseSpessa)

tetto = DIFFERENCE([SOLIDIFY(strutturaDiBase), SOLIDIFY(STRUCT([top_ottagoni_torri]))])
tetto_spesso = PROD([tetto, Q(2)])
tetto_spesso_alzato = T(3)(56)(tetto_spesso)

internal_octagon = [[53,81],[41,69],[41,53],[53,40],[71,40],[82,53],[82,69],[71,81],[53,81]]
polyline_internal_octagon = (AA(POLYLINE)([internal_octagon]))
polygon_internal_octagon = STRUCT(polyline_internal_octagon)
polygon_internal_octagon_SOLIDIFY = SOLIDIFY(polygon_internal_octagon)

complete_base_structure_2D = STRUCT([polygon_sides, polygon_octagons])
complete_base_structure_SOLIDIFY = SOLIDIFY(complete_base_structure_2D)

structure_2D = COLOR([0.69,0.66,0.61])(DIFFERENCE([PROD([complete_base_structure_SOLIDIFY, Q(2)]),   PROD([polygon_internal_octagon_SOLIDIFY,Q(2)])]))
structure_2D_alta_spessa = T(3)(28)(structure_2D)

strutturaDiBase = STRUCT([polygon_octagons,polygon_sides])
strutturaDiBaseSpessa = SOLIDIFY(PROD([strutturaDiBase, Q(2)]))

#LISTA DEI TRAPEZI INTERNI (quelli presenti sul secondo piano)

trapezius_1 = [[22,42],[43,22],[50,36],[38,50],[22,42]]
trapezius_2 = [[47,20],[76,20],[70,34],[53,34],[47,20]]
trapezius_3 = [[73,36],[80,22],[100,42],[86,50],[73,36]]
trapezius_4 = [[88,54],[102,46],[102,76],[88,70],[88,54]]
trapezius_5 = [[86,73],[100,80],[80,100],[73,86],[86,73]]
trapezius_6 = [[70,87],[76,102],[47,102],[53,87],[70,87]]
trapezius_7 = [[38,73],[50,86],[43,100],[22,80],[38,73]]
trapezius_8 = [[20,46],[36,54],[36,70],[20,76],[20,46]]

wall_1 = [[47,20],[53,34],[50,36],[43,22],[47,20]]
wall_2 = [[76,20],[80,22],[73,36],[70,34],[76,20]]
wall_3 = [[100,42],[102,46],[88,54],[86,50],[100,42]]
wall_4 = [[88,70],[102,76],[100,80],[86,73],[88,70]]
wall_5 = [[80,100],[76,102],[70,87],[73,86],[80,100]]
wall_6 = [[47,102],[43,100],[50,86],[53,87],[47,102]]
wall_7 = [[38,73],[22,80],[20,76],[36,70],[38,73]]
wall_8 = [[36,54],[20,46],[22,42],[38,50],[36,54]]

polylines_walls = (AA(POLYLINE)([wall_1,wall_2,wall_3,wall_4,wall_5,wall_6,wall_7,wall_8]))
polygon_walls = COLOR([0.74,0.7,0.66])(STRUCT(polylines_walls))
poligoni_solidify = SOLIDIFY(polygon_walls)
muri_alti = PROD([poligoni_solidify, Q(56)])

polylines_trapezius = (AA(POLYLINE)([trapezius_1,trapezius_8,trapezius_2,trapezius_3,trapezius_4,trapezius_5,trapezius_6,trapezius_7]))
polygon_trapezius = COLOR([0.86,0.81,0.79])(STRUCT(polylines_trapezius))

muro_interno_1 = CUBOID([20,3,28])
porta = T(1)(7)(CUBOID([7,3,15]))
muro_interno_1 = DIFFERENCE([muro_interno_1,porta])
muro_interno_1 = T([1,2])([51,34])(muro_interno_1)

muro_interno_2 = CUBOID([21,3,28])
muro_interno_2 = DIFFERENCE([muro_interno_2,porta])
muro_interno_2 = R([1,2])(PI/4)(muro_interno_2)
muro_interno_2 = T([1,2])([72,35])(muro_interno_2)

muro_interno_3 = CUBOID([20,3,28])
muro_interno_3 = DIFFERENCE([muro_interno_3,porta])
muro_interno_3 = R([1,2])(PI/2)(muro_interno_3)
muro_interno_3 = T([1,2])([88,51])(muro_interno_3)

muro_interno_4 = CUBOID([20,3,28])
muro_interno_4 = DIFFERENCE([muro_interno_4,porta])
muro_interno_4 = R([1,2])(-PI/4)(muro_interno_4)
muro_interno_4 = T([1,2])([71,85])(muro_interno_4)

muro_interno_5 = CUBOID([21,3,28])
muro_interno_5 = DIFFERENCE([muro_interno_5,porta])
muro_interno_5 = R([1,2])(PI)(muro_interno_5)
muro_interno_5 = T([1,2])([72,88])(muro_interno_5)

muro_interno_6 = CUBOID([21,3,28])
muro_interno_6 = DIFFERENCE([muro_interno_6,porta])
muro_interno_6 = R([1,2])(PI/4)(muro_interno_6)
muro_interno_6 = T([1,2])([38,71])(muro_interno_6)

muro_interno_7 = CUBOID([20,3,28])
muro_interno_7 = DIFFERENCE([muro_interno_7,porta])
muro_interno_7 = R([1,2])(PI/2)(muro_interno_7)
muro_interno_7 = T([1,2])([39,51])(muro_interno_7)

muro_interno_8 = CUBOID([21,3,28])
muro_interno_8 = DIFFERENCE([muro_interno_8,porta])
muro_interno_8 = R([1,2])(-PI/4)(muro_interno_8)
muro_interno_8 = T([1,2])([36,49])(muro_interno_8)

############################################    PRIMO PIANO:

muro_interno_1_primopiano = CUBOID([20,3,28])
porta_primopiano = T(1)(7)(CUBOID([7,3,15]))
muro_interno_1_primopiano = DIFFERENCE([muro_interno_1_primopiano,porta_primopiano])
muro_interno_1_primopiano = T([1,2,3])([51,34,30])(muro_interno_1_primopiano)

muro_interno_2_primopiano = CUBOID([21,3,28])
muro_interno_2_primopiano = DIFFERENCE([muro_interno_2_primopiano,porta_primopiano])
muro_interno_2_primopiano = R([1,2])(PI/4)(muro_interno_2_primopiano)
muro_interno_2_primopiano = T([1,2,3])([72,35,30])(muro_interno_2_primopiano)

muro_interno_3_primopiano = CUBOID([20,3,28])
muro_interno_3_primopiano = DIFFERENCE([muro_interno_3_primopiano,porta_primopiano])
muro_interno_3_primopiano = R([1,2])(PI/2)(muro_interno_3_primopiano)
muro_interno_3_primopiano = T([1,2,3])([88,51,30])(muro_interno_3_primopiano)

muro_interno_4_primopiano = CUBOID([20,3,28])
muro_interno_4_primopiano = DIFFERENCE([muro_interno_4_primopiano,porta_primopiano])
muro_interno_4_primopiano = R([1,2])(-PI/4)(muro_interno_4_primopiano)
muro_interno_4_primopiano = T([1,2,3])([71,85,30])(muro_interno_4_primopiano)

muro_interno_5_primopiano = CUBOID([21,3,28])
muro_interno_5_primopiano = DIFFERENCE([muro_interno_5_primopiano,porta_primopiano])
muro_interno_5_primopiano = R([1,2])(PI)(muro_interno_5_primopiano)
muro_interno_5_primopiano = T([1,2,3])([72,88,30])(muro_interno_5_primopiano)

muro_interno_6_primopiano = CUBOID([21,3,28])
muro_interno_6_primopiano = DIFFERENCE([muro_interno_6_primopiano,porta_primopiano])
muro_interno_6_primopiano = R([1,2])(PI/4)(muro_interno_6_primopiano)
muro_interno_6_primopiano = T([1,2,3])([38,71,30])(muro_interno_6_primopiano)

muro_interno_7_primopiano = CUBOID([20,3,28])
muro_interno_7_primopiano = DIFFERENCE([muro_interno_7_primopiano,porta_primopiano])
muro_interno_7_primopiano = R([1,2])(PI/2)(muro_interno_7_primopiano)
muro_interno_7_primopiano = T([1,2,3])([39,51,30])(muro_interno_7_primopiano)

muro_interno_8_primopiano = CUBOID([21,3,28])
muro_interno_8_primopiano = DIFFERENCE([muro_interno_8_primopiano,porta_primopiano])
muro_interno_8_primopiano = R([1,2])(-PI/4)(muro_interno_8_primopiano)
muro_interno_8_primopiano = T([1,2,3])([36,49,30])(muro_interno_8_primopiano)

struttura_primo_piano = STRUCT([muro_interno_1_primopiano,muro_interno_2_primopiano,muro_interno_3_primopiano,muro_interno_4_primopiano,muro_interno_5_primopiano,muro_interno_6_primopiano,muro_interno_7_primopiano,muro_interno_8_primopiano])

hole_stanza_7_1_sub = CUBOID([8,36,15])hole_stanza_7_1_T_sub = (T([1,2,3])([24,44,2])(hole_stanza_7_1_sub))
hole_stanza_7_1 = CUBOID([8,36,15])hole_stanza_7_1_T = (T([1,2,3])([24,44,30])(hole_stanza_7_1))
hole_stanza_5_3_sub = CUBOID([8,36,15])hole_stanza_5_3_T_sub = (T([1,2,3])([90,44,2])(hole_stanza_5_3_sub))hole_stanza_5_3 = CUBOID([8,36,15])hole_stanza_5_3_T = (T([1,2,3])([90,44,30])(hole_stanza_5_3))hole_stanza_7_5_sub = CUBOID([36,8,15])hole_stanza_7_5_T_sub = (T([1,2,3])([44,90,2])(hole_stanza_7_5_sub))hole_stanza_7_5 = CUBOID([36,8,15])hole_stanza_7_5_T = (T([1,2,3])([44,90,30])(hole_stanza_7_5))hole_stanza_1_3_sub = CUBOID([36,8,15])hole_stanza_1_3_T_sub = (T([1,2,3])([44,23,2])(hole_stanza_1_3_sub))hole_stanza_1_3 = CUBOID([36,8,15])hole_stanza_1_3_T = (T([1,2,3])([44,23,30])(hole_stanza_1_3))
a = STRUCT([strutturaDiBaseSpessa,top_ottagoni_torri_SOLIDIFY_spesse_rialzate,muro_interno_1,muro_interno_2,muro_interno_3,muro_interno_4,muro_interno_5,muro_interno_6,muro_interno_7,muro_interno_8,muri_alti,struttura_primo_piano,structure_2D_alta_spessa,tetto_spesso_alzato])
b = DIFFERENCE([a,hole_stanza_7_1_T_sub,hole_stanza_7_1_T,hole_stanza_5_3_T_sub,hole_stanza_5_3_T,hole_stanza_7_5_T_sub,hole_stanza_7_5_T,hole_stanza_1_3_T,hole_stanza_1_3_T_sub])
b = COLOR([0.74,0.7,0.66])(b)

VIEW(b)