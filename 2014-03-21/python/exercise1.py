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
polygon_trapezius = COLOR([0.68,0.57,0.4])(STRUCT(polylines_trapezius))

#OTTAGONO INTERNO (da utilizzare dopo nel metodo della differenza - serve per creare il "buco" sul solaio del primo piano

internal_octagon = [[53,81],[41,69],[41,53],[53,40],[71,40],[82,53],[82,69],[71,81],[53,81]]
polyline_internal_octagon = (AA(POLYLINE)([internal_octagon]))
polygon_internal_octagon = STRUCT(polyline_internal_octagon)
polygon_internal_octagon_SOLIDIFY = SOLIDIFY(polygon_internal_octagon)

complete_base_structure_2D = STRUCT([polygon_sides, polygon_octagons, polygon_trapezius])
complete_base_structure_SOLIDIFY = SOLIDIFY(complete_base_structure_2D)


#intera struttura
internal_structure = (AA(POLYLINE)([side_1,octagon_1, side_2,octagon_2, side_3, octagon_3, side_4,octagon_4, side_5,octagon_5, side_6,octagon_6, side_7,octagon_7, side_8, octagon_8]))
polygon_internal_structure = SOLIDIFY(STRUCT(internal_structure))
polygon_internal_structure_empty = DIFFERENCE([polygon_internal_structure,polygon_internal_octagon_SOLIDIFY])first_floor_thick = PROD([((polygon_internal_structure_empty)),Q(3)])first_floor_color = COLOR([0.74,0.7,0.66])(first_floor_thick)relived_first_floor = T(3)(25)(first_floor_color)top = COLOR([0.74,0.7,0.66])(T(3)(52)(polygon_internal_structure))bottom = COLOR([0.74,0.7,0.66])(polygon_internal_structure)
structure_2D = COLOR([0.74,0.7,0.66])(DIFFERENCE([complete_base_structure_SOLIDIFY,   polygon_internal_octagon_SOLIDIFY]))
piano_terra = STRUCT([structure_2D,bottom])

#alzo le torri

octagon_1 = [[36,20],[30,14],[30,6],[36,0],[44,0],[50,6],[50,14],[44,20],[36,20]]
octagon_2 = [[72,14],[72,6],[78,0],[86,0],[92,6],[92,14],[86,20],[78,20],[72,14]]
octagon_3 = [[102,36],[108,30],[116,30],[122,36],[122,44],[116,50],[108,50],[102,44],[102,36]]
octagon_4 = [[108,72],[116,72],[122,78],[122,86],[116,92],[108,92],[102,86],[102,78],[108,72]]
octagon_5 = [[72,108],[72,116],[78,122],[86,122],[92,116],[92,108],[86,102],[78,102],[72,108]]
octagon_6 = [[36,102],[30,108],[30,116],[36,122],[44,122],[50,116],[50,108],[44,102],[36,102]]
octagon_7 = [[14,72],[6,72],[0,78],[0,86],[6,92],[14,92],[20,86],[20,78],[14,72]]
octagon_8 = [[20,36],[14,30],[6,30],[0,36],[0,44],[6,50],[14,50],[20,44],[20,36]]
octagon_1 = (AA(POLYLINE)([octagon_1]))octagon_2 = (AA(POLYLINE)([octagon_2]))octagon_3 = (AA(POLYLINE)([octagon_3]))octagon_4 = (AA(POLYLINE)([octagon_4]))octagon_5 = (AA(POLYLINE)([octagon_5]))octagon_6 = (AA(POLYLINE)([octagon_6]))octagon_7 = (AA(POLYLINE)([octagon_7]))octagon_8 = (AA(POLYLINE)([octagon_8]))o1 = (STRUCT(octagon_1))o2 = (STRUCT(octagon_2))o3 = (STRUCT(octagon_3))o4 = (STRUCT(octagon_4))o5 = (STRUCT(octagon_5))o6 = (STRUCT(octagon_6))o7 = (STRUCT(octagon_7))o8 = (STRUCT(octagon_8))only_top = STRUCT([o1,o2,o3,o4,o5,o6,o7,o8])only_top_SOLIDIFY = SOLIDIFY(only_top)torri = STRUCT([only_top_SOLIDIFY])torri_alzate = COLOR([0.68,0.57,0.4])(T(3)(52)(torri))
floor1 = COLOR([0.68,0.57,0.4])(T(3)(28)(polygon_internal_structure_empty))

_25D = STRUCT([piano_terra,floor1,torri_alzate])


structure_2D = COLOR([0.74,0.7,0.66])(DIFFERENCE([complete_base_structure_SOLIDIFY,   polygon_internal_octagon_SOLIDIFY]))
structure_2D_alta = T(3)(28)(structure_2D)
floor0 = STRUCT([bottom,structure_2D])
floor1 = COLOR([0.74,0.7,0.66])(T(3)(28)(polygon_internal_structure_empty))

# make floor 3:

octagon_1 = [[36,20],[30,14],[30,6],[36,0],[44,0],[50,6],[50,14],[44,20],[36,20]]
octagon_2 = [[72,14],[72,6],[78,0],[86,0],[92,6],[92,14],[86,20],[78,20],[72,14]]
octagon_3 = [[102,36],[108,30],[116,30],[122,36],[122,44],[116,50],[108,50],[102,44],[102,36]]
octagon_4 = [[108,72],[116,72],[122,78],[122,86],[116,92],[108,92],[102,86],[102,78],[108,72]]
octagon_5 = [[72,108],[72,116],[78,122],[86,122],[92,116],[92,108],[86,102],[78,102],[72,108]]
octagon_6 = [[36,102],[30,108],[30,116],[36,122],[44,122],[50,116],[50,108],[44,102],[36,102]]
octagon_7 = [[14,72],[6,72],[0,78],[0,86],[6,92],[14,92],[20,86],[20,78],[14,72]]
octagon_8 = [[20,36],[14,30],[6,30],[0,36],[0,44],[6,50],[14,50],[20,44],[20,36]]only_top = STRUCT([o1,o2,o3,o4,o5,o6,o7,o8])floor2 = COLOR([0.74,0.7,0.66])(SOLIDIFY(only_top))

VIEW(floor0)    # visualizza il piano terra
VIEW(floor1)    # visualizza il primo piano
VIEW(floor2)    # visualizza la copertura delle torri
VIEW(_25D)      # visualizza lo shema in 2.5D