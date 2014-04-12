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

#LISTA DEI TRAPEZI INTERNI (quelli presenti sul secondo piano)

trapezius_1 = [[22,42],[43,22],[50,36],[38,50],[22,42]]
trapezius_2 = [[47,20],[76,20],[70,34],[53,34],[47,20]]
trapezius_3 = [[73,36],[80,22],[100,42],[86,50],[73,36]]
trapezius_4 = [[88,54],[102,46],[102,76],[88,70],[88,54]]
trapezius_5 = [[86,73],[100,80],[80,100],[73,86],[86,73]]
trapezius_6 = [[70,87],[76,102],[47,102],[53,87],[70,87]]
trapezius_7 = [[38,73],[50,86],[43,100],[22,80],[38,73]]
trapezius_8 = [[20,46],[36,54],[36,70],[20,76],[20,46]]

polylines_trapezius = (AA(POLYLINE)([trapezius_1,trapezius_8,trapezius_2,trapezius_3,trapezius_4,trapezius_5,trapezius_6,trapezius_7]))
polygon_trapezius = COLOR([0.86,0.81,0.79])(STRUCT(polylines_trapezius))

#OTTAGONO INTERNO (da utilizzare dopo nel metodo della differenza - serve per creare il "buco" sul solaio del primo piano

internal_octagon = [[53,81],[41,69],[41,53],[53,40],[71,40],[82,53],[82,69],[71,81],[53,81]]
polyline_internal_octagon = (AA(POLYLINE)([internal_octagon]))
polygon_internal_octagon = STRUCT(polyline_internal_octagon)
polygon_internal_octagon_SOLIDIFY = SOLIDIFY(polygon_internal_octagon)

complete_base_structure_2D = STRUCT([polygon_sides, polygon_octagons, polygon_trapezius])
complete_base_structure_SOLIDIFY = SOLIDIFY(complete_base_structure_2D)

structure_2D = COLOR([0.69,0.66,0.61])(DIFFERENCE([complete_base_structure_SOLIDIFY,   polygon_internal_octagon_SOLIDIFY]))
structure_2D_alta = T(3)(28)(structure_2D)

#creo il solido vero e proprio

solid = PROD ([(structure_2D) , Q(52)])

#creo tutti i buchi (passaggi tra porte, e finestre)

hole_1 = CUBOID([10,5,7])hole_1_R =  T([1,2,3])([45,40,28])(R([1,2])(PI/4)(hole_1))

hole_1_sub = CUBOID([10,5,7])hole_1_R_sub =  T([1,2])([45,40])(R([1,2])(PI/4)(hole_1_sub))hole_3_sub = CUBOID([12,5,7])hole_3_R_sub = T([1,2])([72,50])(R([1,2])(-PI/4)(hole_3_sub))hole_3 = CUBOID([12,5,7])hole_3_R = T([1,2,3])([72,50,28])(R([1,2])(-PI/4)(hole_3))hole_5_sub = CUBOID([12,5,7])hole_5_R_sub =  T([1,2])([75,71])(R([1,2])(PI/4)(hole_5_sub))hole_5 = CUBOID([12,5,7])hole_5_R =  T([1,2,3])([75,71,28])(R([1,2])(PI/4)(hole_5))hole_7_sub = CUBOID([12,5,7])hole_7_R_sub =  COLOR([0.74,0.7,0.66])(T([1,2])([38,78])(R([1,2])(-PI/4)(hole_7_sub)))hole_7 = CUBOID([12,5,7])hole_7_R =  COLOR([0.74,0.7,0.66])(T([1,2,3])([38,78,28])(R([1,2])(-PI/4)(hole_7)))

hole_2 = CUBOID([5,10,7])hole_2_T = (T([1,2,3])([60,34,28])(hole_2))

hole_2_sub = CUBOID([5,10,7])hole_2_T_sub = (T([1,2])([60,34])(hole_2_sub))

hole_8 = CUBOID([10,5,7])hole_8_T = (T([1,2,3])([36,60,28])(hole_8))hole_8_sub = CUBOID([10,5,7])hole_8_T_sub = (T([1,2])([36,60])(hole_8_sub))

hole_4 = CUBOID([15,5,7])hole_4_T = (T([1,2,3])([76,60,28])(hole_4))hole_4_sub = CUBOID([15,5,7])hole_4_T_sub = (T([1,2])([76,60])(hole_4_sub))hole_6 = CUBOID([5,15,7])hole_6_T = (T([1,2,3])([60,78,28])(hole_6))hole_6_sub = CUBOID([5,10,7])hole_6_T_sub = (T([1,2])([60,78])(hole_6_sub))hole_stanza_7_1_sub = CUBOID([8,36,7])hole_stanza_7_1_T_sub = (T([1,2])([24,44])(hole_stanza_7_1_sub))hole_stanza_7_1 = CUBOID([8,36,7])hole_stanza_7_1_T = (T([1,2,3])([24,44,28])(hole_stanza_7_1))hole_stanza_5_3_sub = CUBOID([8,36,7])hole_stanza_5_3_T_sub = (T([1,2])([90,44])(hole_stanza_5_3_sub))hole_stanza_5_3 = CUBOID([8,36,7])hole_stanza_5_3_T = (T([1,2,3])([90,44,28])(hole_stanza_5_3))hole_stanza_7_5_sub = CUBOID([36,8,7])hole_stanza_7_5_T_sub = (T([1,2])([44,90])(hole_stanza_7_5_sub))hole_stanza_7_5 = CUBOID([36,8,7])hole_stanza_7_5_T = (T([1,2,3])([44,90,28])(hole_stanza_7_5))hole_stanza_1_3_sub = CUBOID([36,8,7])hole_stanza_1_3_T_sub = (T([1,2])([44,26])(hole_stanza_1_3_sub))hole_stanza_1_3 = CUBOID([36,8,7])hole_stanza_1_3_T = (T([1,2,3])([44,26,28])(hole_stanza_1_3))solid = DIFFERENCE([solid,hole_8_T,hole_4_T,hole_2_T,hole_8_T_sub,hole_4_T_sub,hole_2_T_sub,hole_6_T,hole_6_T_sub,hole_1_R_sub, hole_3_R_sub,hole_5_R_sub,hole_7_R_sub,hole_1_R,hole_3_R,hole_5_R,hole_7_R,hole_stanza_7_1_T,hole_stanza_7_1_T_sub,hole_stanza_5_3_T,hole_stanza_5_3_T_sub,hole_stanza_7_5_T,hole_stanza_7_5_T_sub,hole_stanza_1_3_T,hole_stanza_1_3_T_sub])

s = COLOR([0.74,0.7,0.66])(solid)

#definisco porte e finestre

big_door = CUBOID([10,2,22])big_door = T([1,2])([56,12])(big_door)smaller_door = T(3)(3)(CUBOID([6,2,10]))smaller_door = T([1,2])([58,11.99])(smaller_door)triangolo_sopra_porta = CUBOID([7,2,7])triangolo_sopra_porta = R([1,3])(PI/4)(triangolo_sopra_porta)triangolo_sopra_porta = T([1,2,3])([61,12,17])(triangolo_sopra_porta)structure_with_door = STRUCT([COLOR([0.74,0.7,0.66])(solid),COLOR([0.59,0.52,0.47])(big_door),COLOR([0.28,0.2,0.14])(smaller_door),COLOR([0.59,0.52,0.47])(triangolo_sopra_porta)])

internal_structure = (AA(POLYLINE)([side_1,octagon_1, side_2,octagon_2, side_3, octagon_3, side_4,octagon_4, side_5,octagon_5, side_6,octagon_6, side_7,octagon_7, side_8, octagon_8]))
polygon_internal_structure = SOLIDIFY(STRUCT(internal_structure))
polygon_internal_structure_empty = DIFFERENCE([polygon_internal_structure,polygon_internal_octagon_SOLIDIFY])#first_floor_thick = PROD([((polygon_internal_structure_empty)),Q(3)])#first_floor_color = COLOR([0.74,0.7,0.66])(first_floor_thick)#relived_first_floor = T(3)(25)(first_floor_color)internal_octagon = [[53,81],[41,69],[41,53],[53,40],[71,40],[82,53],[82,69],[71,81],[53,81]]
polyline_internal_octagon = (AA(POLYLINE)([internal_octagon]))
polygon_internal_octagon = STRUCT(polyline_internal_octagon)
polygon_internal_octagon_SOLIDIFY = SOLIDIFY(polygon_internal_octagon)

complete_base_structure_2D = STRUCT([polygon_sides, polygon_octagons])
complete_base_structure_SOLIDIFY = SOLIDIFY(complete_base_structure_2D)

structure_2D = COLOR([0.69,0.66,0.61])(DIFFERENCE([PROD([complete_base_structure_SOLIDIFY, Q(2)]),   PROD([polygon_internal_octagon_SOLIDIFY,Q(2)])]))
structure_2D_alta_spessa = T(3)(28)(structure_2D)
top = COLOR([0.74,0.7,0.66])(T(3)(52)(polygon_internal_structure))bottom = COLOR([0.85,0.81,0.76])(polygon_internal_structure)# alzo le torrioctagon_1 = [[36,20],[30,14],[30,6],[36,0],[44,0],[50,6],[50,14],[44,20],[36,20]]
octagon_2 = [[72,14],[72,6],[78,0],[86,0],[92,6],[92,14],[86,20],[78,20],[72,14]]
octagon_3 = [[102,36],[108,30],[116,30],[122,36],[122,44],[116,50],[108,50],[102,44],[102,36]]
octagon_4 = [[108,72],[116,72],[122,78],[122,86],[116,92],[108,92],[102,86],[102,78],[108,72]]
octagon_5 = [[72,108],[72,116],[78,122],[86,122],[92,116],[92,108],[86,102],[78,102],[72,108]]
octagon_6 = [[36,102],[30,108],[30,116],[36,122],[44,122],[50,116],[50,108],[44,102],[36,102]]
octagon_7 = [[14,72],[6,72],[0,78],[0,86],[6,92],[14,92],[20,86],[20,78],[14,72]]
octagon_8 = [[20,36],[14,30],[6,30],[0,36],[0,44],[6,50],[14,50],[20,44],[20,36]]
octagon_1 = (AA(POLYLINE)([octagon_1]))octagon_2 = (AA(POLYLINE)([octagon_2]))octagon_3 = (AA(POLYLINE)([octagon_3]))octagon_4 = (AA(POLYLINE)([octagon_4]))octagon_5 = (AA(POLYLINE)([octagon_5]))octagon_6 = (AA(POLYLINE)([octagon_6]))octagon_7 = (AA(POLYLINE)([octagon_7]))octagon_8 = (AA(POLYLINE)([octagon_8]))o1 = (STRUCT(octagon_1))o2 = (STRUCT(octagon_2))o3 = (STRUCT(octagon_3))o4 = (STRUCT(octagon_4))o5 = (STRUCT(octagon_5))o6 = (STRUCT(octagon_6))o7 = (STRUCT(octagon_7))o8 = (STRUCT(octagon_8))octagon_1b = PROD([o1,Q(8)])octagon_2b = PROD([o2,Q(8)])octagon_3b = PROD([o3,Q(8)])octagon_4b = PROD([o4,Q(8)])octagon_5b = PROD([o5,Q(8)])octagon_6b = PROD([o6,Q(8)])octagon_7b = PROD([o7,Q(8)])octagon_8b = PROD([o8,Q(8)])only_top = STRUCT([octagon_1b,octagon_2b,octagon_3b,octagon_4b,octagon_5b,octagon_6b,octagon_7b,octagon_8b])only_top_SOLIDIFY = SOLIDIFY(only_top)torri = STRUCT([only_top_SOLIDIFY])torri_alzate = COLOR([0.74,0.7,0.66])(T(3)(52)(torri))#finestre:window_8 = CUBOID([6,3.1,5])window_8_T = COLOR([0.63,1,1])(T([1,2,3])([13.999,58,28])(window_8))window_4 = CUBOID([6,3.1,5])window_4_T = COLOR([0.63,1,1])(T([1,2,3])([102,59.009,28])(window_4))window_6 = CUBOID([3,6,5.1])window_6_T = COLOR([0.63,1,1])(T([1,2,3])([59.5,102.009,28])(window_6))window_over_door = COLOR([0.63,1,1])(CUBOID([3,6,5.1]))window_over_door = T([1,2,3])([59.5,13.999,28])(window_over_door)# piano di sottowindow_8 = CUBOID([6,3,5])window_8_T_sub = COLOR([0.63,1,1])(T([1,2,3])([13.999,58,12])(window_8))window_4 = CUBOID([6,3,5])window_4_T_sub = COLOR([0.63,1,1])(T([1,2,3])([102,59,12])(window_4))window_6 = CUBOID([3,6,5])window_6_T_sub = COLOR([0.63,1,1])(T([1,2,3])([59.5,102.009,12])(window_6))#scalini di ingressoprimo_scalino = CUBOID([15,5,1])secondo_scalino = T([2,3])([1,1])(CUBOID([15,4,1]))terzo_scalino = T([2,3])([2,2])(CUBOID([15,3,1]))scalini = T([1,2])([53.5,9])(COLOR([0.46,0.35,0.25])(STRUCT([primo_scalino,secondo_scalino,terzo_scalino])))structure_complete = STRUCT([structure_2D_alta_spessa,structure_with_door,window_over_door,torri_alzate,window_8_T,window_4_T, window_6_T,bottom,scalini,top,window_6_T_sub,window_4_T_sub,window_8_T_sub])
################# BASAMENTO:rettangolo_base = [[-350,-330],[-300,450],[500,450],[500,-330],[-350,-330]]polylines_rettangolo_base = (AA(POLYLINE)([rettangolo_base]))
polygon_rettangolo_base = SOLIDIFY(STRUCT(polylines_rettangolo_base))polygon_rettangolo_base = COLOR([0.09803921568,0.54509803921,0.0862745098])(polygon_rettangolo_base)struttura_con_campo = STRUCT([polygon_rettangolo_base,structure_complete])def lampione():
    tronco = COLOR([0,0,0])(CYLINDER([1,15])(30))
    lampada = COLOR([1,0.94117647058,0])(T(3)(15)(SPHERE(2.7)([20,20])))
    return STRUCT([tronco,lampada])bordo_laterale = CIRCLE(130)([50,3])bordo_laterale_piccolo = CIRCLE(100)([50,3])bordo_completo = COLOR([0.90588235294,0.84705882352,0.34509803921])(DIFFERENCE([bordo_laterale,bordo_laterale_piccolo]))sentiero_1 = T([1,2])([125,-20])(COLOR([0.90588235294,0.84705882352,0.34509803921])(STRUCT([CUBOID([250,40,0.1]),lampione()])))sentiero_2 = R([1,2])(PI/4)(sentiero_1)sentiero_3 = R([1,2])(PI/4)(sentiero_2)sentiero_4 = R([1,2])(PI/4)(sentiero_3)sentiero_5 = R([1,2])(PI/4)(sentiero_4)sentiero_6 = R([1,2])(PI/4)(sentiero_5)sentiero_7 = R([1,2])(PI/4)(sentiero_6)sentiero_8 = R([1,2])(PI/4)(sentiero_7)sentieri = STRUCT([sentiero_1,sentiero_2,sentiero_3,sentiero_4,sentiero_5,sentiero_6,sentiero_7,sentiero_8])struttura_cerchio_sentieri = T([1,2,3])([60,60,1])(STRUCT([bordo_completo,sentieri]))def aiuola(raggio):    return T(3)(2/3*raggio)(SPHERE(raggio)([20,20]))aiuola_1 = T([1,2])([-80,0])(COLOR([0.05490196078,0.78431372549,0])(aiuola(8)))aiuola_2 = T([1,2])([190,10])(COLOR([0.05490196078,0.78431372549,0])(aiuola(12)))aiuola_3 = T([1,2])([30,130])(COLOR([0.05490196078,0.78431372549,0])(aiuola(4)))aiuola_4 = T([1,2])([-70,140])(COLOR([0.05490196078,0.78431372549,0])(aiuola(18)))aiuola_5 = T([1,2])([-30,-100])(COLOR([0.05490196078,0.78431372549,0])(aiuola(20)))def albero(scala):    tronco = COLOR([0.5882,0.2941,0])(CYLINDER([0.2,2])(30))
    foglieP = SPHERE(0.5)([30,30])
    foglie = COLOR([0.502,0.502,0])(STRUCT([T([1,3])([-0.2,2])(foglieP), T([1,3])([0.2,2])(foglieP), T(3)([2.2])(foglieP)]))
    return S([1,2,3])([scala,scala,scala])(STRUCT([foglie,tronco]))

albero_1 = albero(10)albero_2 = T([1,2])([-50,-15])(albero(12))albero_3 = T([1,2])([100,-100])(albero(15))albero_4 = T([1,2])([100,200])(albero(15))albero_5 = T([1,2])([-10,300])(albero(15))VIEW(STRUCT([struttura_cerchio_sentieri,struttura_con_campo,aiuola_1,aiuola_2,aiuola_3,aiuola_4,aiuola_5,albero_1,albero_2,albero_3,albero_4,albero_5]))