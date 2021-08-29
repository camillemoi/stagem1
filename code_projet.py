#Initialisation et appel des extensions
from qgis.PyQt import QtGui
from qgis.core import *
from qgis.core import QgsProject
import processing
import os
import sys

#Etablir les chemins d'accès aux dossiers
#Génération d'une boite de dialogue
#input_source = QInputDialog.getText(None, "Dossier des couches" ,"Chemin du dossier des couches existantes (adresse complète avec / à la fin) :")
##Affecter la valeur entrée par l'utilisateur à une variable
#if input_source[1]:
#   dossier_source = input_source[0]
#   print(dossier_source)
#input_icones = QInputDialog.getText(None, "Dossier des icones" ,"Chemin du dossier des icones (adresse complète avec / à la fin) :")
#if input_icones[1]:
#    dossier_icones = input_icones[0]
#    print(dossier_icones)
#input_new = QInputDialog.getText(None, "Dossier des nouvelles couches", "Chemin du dossier des couches créées par le code (adresse complète avec / à la fin) :")
#if input_new[1]:
#    dossier_new = input_new[0]
#    print(dossier_new)
#input_photos = QInputDialog.getText(None, "Dossier des photos", "Chemin du dossier des photos (adresse complète avec / à la fin) :")
#if input_photos[1]:
#    dossier_photos = input_photos[0]
#    print(dossier_photos)
#input_fiches = QInputDialog.getText(None, "Dossier des fiches", "Chemin du dossier pour stocker les fiches (adresse complète avec / à la fin) :")
#if input_fiches[1]:
#    dossier_fiches = input_fiches[0]
#    print(dossier_fiches)
    
#Appel de la fonctionnalité permettant de gérer les couches dans le projet
root = QgsProject.instance().layerTreeRoot()

#Définition de la projection du projet
projectObj = QgsProject.instance()
projectCrs = QgsCoordinateReferenceSystem.fromEpsgId(2154)
projectObj.setCrs(projectCrs)

#Module d'installation et de formatage du projet QGIS
def installation_projet():
    #Insérer les couches
    #Couches des plans
    #Insertion de la couche avec adresse et type (ogr pour toutes les couches spatiales)
    espace_vert = iface.addVectorLayer(""+ dossier_source +'espaces_verts_tout.shp', '','ogr',)
    #Modification du nom dans la couche dans le projet
    espace_vert.setName('espace_vert')
    eau = iface.addVectorLayer(""+ dossier_source +'eau_all.shp', '', 'ogr',)
    eau.setName('eau')
    train_plan = iface.addVectorLayer(""+ dossier_source +'ligne_train_L93.shp', '', 'ogr',)
    train_plan.setName('train_plan')
    parking_plan = iface.addVectorLayer(""+ dossier_source +'parking_tout.shp', '', 'ogr',)
    parking_plan.setName('parking_plan')
    quais = iface.addVectorLayer(""+ dossier_source +'quais.shp', '', 'ogr',)
    bati_autre = iface.addVectorLayer(""+ dossier_source +'tout_bati_accessibilite.shp', '', 'ogr',)
    bati_autre.setName('bati_autre')
    bati_gare_complem = iface.addVectorLayer(""+ dossier_source +'bati_gare_complem.shp', '', 'ogr',)
    bati_gare = iface.addVectorLayer(""+ dossier_source +'bati_gare_mix2.shp', '', 'ogr',)
    bati_gare.setName('bati_gare')
    cimetieres = iface.addVectorLayer(""+ dossier_source +'cimetiere_all.shp', '', 'ogr',)
    cimetieres.setName('cimetieres')
    arbres = iface.addVectorLayer(""+ dossier_source +'arbres_tout.shp', '', 'ogr',)
    arbres.setName('arbres')
    cyclable = iface.addVectorLayer(""+ dossier_source +'cyclable_tout.shp', '', 'ogr',)
    cyclable.setName('cyclable')
    pieton = iface.addVectorLayer(""+ dossier_source +'pieton_tout.shp', '', 'ogr',)
    pieton.setName('pieton')
    infrastructures = iface.addVectorLayer(""+ dossier_source +'infrastructure_tout.shp', '', 'ogr',)
    infrastructures.setName('infrastructures')
    transportco_plan = iface.addVectorLayer(""+ dossier_source +'transportco_final.shp', '', 'ogr',)
    transportco_plan.setName('transportco_plan')
    plan_fonctionnel = iface.addVectorLayer(""+ dossier_source +'plan_fonctionnel_with_rot.shp', '', 'ogr',)
    
    #Couches de la carte générale
    train_gen = iface.addVectorLayer(""+ dossier_source +'ligne_train_L93.shp', '', 'ogr',)
    train_gen.setName('train_gen')
    zone_urba = iface.addVectorLayer(""+ dossier_source +'zone_urba.shp', '', 'ogr',)
    parking_gen = iface.addVectorLayer(""+ dossier_source +'parking_l93.shp', '', 'ogr',)
    parking_gen.setName('parking_gen')
    residentiel = iface.addVectorLayer(""+ dossier_source +'residentiel_l93.shp', '', 'ogr',)
    logistics = iface.addVectorLayer(""+ dossier_source +'logistics_l93.shp', '', 'ogr',)
    commercial = iface.addVectorLayer(""+ dossier_source +'commercial_l93.shp', '', 'ogr',)
    entreprises = iface.addVectorLayer(""+ dossier_source +'entreprises_l93.shp', '', 'ogr',)
    loisirs = iface.addVectorLayer(""+ dossier_source +'loisirs_l93.shp', '', 'ogr',)
    scolaire = iface.addVectorLayer(""+ dossier_source +'scolaire_l93.shp', '', 'ogr',)
    
    #Couches de la carte d'accessibilité
    train_acc = iface.addVectorLayer(""+ dossier_source +'ligne_train_L93.shp', '', 'ogr',)
    train_acc.setName('train_acc')
    velo_lines = iface.addVectorLayer(""+ dossier_source +'velolinesall_formap.shp', '', 'ogr',)
    velo_lines.setName('velo_lines')
    pieton_lines = iface.addVectorLayer(""+ dossier_source +'pietonlinesall_formap.shp', '', 'ogr',)
    pieton_lines.setName('pieton_lines')
    voiture_lines = iface.addVectorLayer(""+ dossier_source +'voiturelinesall_formap.shp', '', 'ogr',)
    voiture_lines.setName('voiture_lines')
    bus_acces = iface.addVectorLayer(""+ dossier_source +'reseau_bus_region_tisseo.shp', '', 'ogr',)
    bus_acces.setName('bus_acces')
    lineos = iface.addVectorLayer(""+ dossier_source +'tc_ligne_lineo.TAB', '', 'ogr',)
    lineos.setName('lineos')
    reseaux_rapides_acces = iface.addVectorLayer(""+ dossier_source +'ligneTC_toulouseL93.shp', '', 'ogr',)
    reseaux_rapides_acces.setName('reseaux_rapides_acces')
    autopartage = iface.addVectorLayer(""+ dossier_source +'stations-d-auto-partage.geojson', '', 'ogr',)
    transportco_acces = iface.addVectorLayer(""+ dossier_source +'transportco_final.shp', '', 'ogr',)
    transportco_acces.setName('transportco_acces')
    
    #Couches de la carte de localisation
    commune = iface.addVectorLayer(""+ dossier_source +'COMMUNE.shp', '', 'ogr',)
    metropole = iface.addVectorLayer(""+ dossier_source +'com_metropole.shp', '', 'ogr',)
    metropole.setName('metropole')
    reseaux_rapides_loc = iface.addVectorLayer(""+ dossier_source +'ligneTC_toulouseL93.shp', '', 'ogr',)
    reseaux_rapides_loc.setName('reseaux_rapides_loc')
    stations_loc = iface.addVectorLayer(""+ dossier_source +'stations_detail_rr.shp', '', 'ogr',)
    stations_loc.setName('stations_loc')
    portions_train = iface.addVectorLayer(""+ dossier_source +'portions_train.shp', '', 'ogr',)
    
    #Couches dans plusieurs cartes
    gares_provi = iface.addVectorLayer(""+ dossier_source +'gares_individus.shp', '', 'ogr',)
    gares_provi.setName('gares_provi')
    
    #Tableaux CSV
    #Définition du chemin d'accès - l'ajout de "?delimiter=," indique que le séparateur de champ est la virgule dans ce cas
    bloc1url = "file:///"+ dossier_source +"bloc1.csv?delimiter=,"
    #Définition des paramètres de la couche : chemin, nom, type
    bloc1 = QgsVectorLayer(bloc1url, 'bloc1', 'delimitedtext')
    #ajout du tableau CSV
    QgsProject.instance().addMapLayer(bloc1)
    bloc2url = "file:///"+ dossier_source +"bloc2.csv?delimiter=,"
    bloc2 = QgsVectorLayer(bloc2url, 'bloc2', 'delimitedtext')
    QgsProject.instance().addMapLayer(bloc2)
    bloc3url = "file:///"+ dossier_source +"bloc3.csv?delimiter=,"
    bloc3 = QgsVectorLayer(bloc3url, 'bloc3', 'delimitedtext')
    QgsProject.instance().addMapLayer(bloc3)
    
    #Jointure du bloc1 sur les couches des gares : créé un nouveau fichier avec la jointure faite
    processing.run("native:joinattributestable", {'INPUT':""+ dossier_source +"gares_individus.shp",'FIELD':'Name','INPUT_2': bloc1,'FIELD_2':'gares','FIELDS_TO_COPY':['vrai_nom','vocation','niveau_sce','situation'],'METHOD':1,'DISCARD_NONMATCHING':False,'PREFIX':'','OUTPUT':""+ dossier_new +"gares_jointure.shp" })
    #Ajout de la nouvelle couche au projet en 2x pour le statut et la vocation
    gares_voc = iface.addVectorLayer(""+ dossier_new +'gares_jointure.shp', '', 'ogr',)
    gares_statut = iface.addVectorLayer(""+ dossier_new +'gares_jointure.shp', '', 'ogr',)
    gares_voc.setName('gares_voc')
    gares_statut.setName('gares_statut')
    
    #FORMATAGE DE LA SYMBOLOGIE
    #Couches sans groupe
    #Statut des gares : symbologie catégorisée
    #Dictionnaire des valeurs de la catégorie
    values_statut = {"Gare existante", "Gare potentielle"}
    categories_statut = []
    #Affecter un symbole pour chaque valeur du dictionnaire
    for value in values_statut:    
        svgStylestat = {}
        #Couleur du symbole SVG
        svgStylestat['fill'] = '#000000'
        if value == "Gare existante" :
            #Chemin d'accès du symbole SVG
            svgStylestat['name'] = ""+ dossier_icones + "train_bleu.svg"
        elif value == "Gare potentielle" :
            svgStylestat['name'] = ""+ dossier_icones + "train_rose.svg"
        #Couleur du contour, épaisseur et taille du logo
        svgStylestat['outline'] = '#000000'
        svgStylestat['outline-width'] = '0.3'
        svgStylestat['size'] = '4.6'
        #Création de la symbologie
        situation = QgsSvgMarkerSymbolLayer.create(svgStylestat)
    
        #Ajout du symbole
        symbol_statut = QgsSymbol.defaultSymbol(gares_statut.geometryType())
        symbol_statut.appendSymbolLayer(situation)
        symbol_statut.deleteSymbolLayer(0)
        
        #Regroupement des symboles
        category = QgsRendererCategory(value, symbol_statut, str(value))
        categories_statut.append(category)
    #Création de la symbologie catégorisée et indication de la colonne à utiliser
    renderer_statut = QgsCategorizedSymbolRenderer('situation', categories_statut)
    if renderer_statut is not None:
       gares_statut.setRenderer(renderer_statut)
    gares_statut.triggerRepaint()
    
    #Vocation des gares : chargement d'un fichier style
    gares_voc.loadNamedStyle(""+ dossier_source +"vocation_fiche.qml")
    
    #Couches de localisation
    #Portions de train : remplissage
    symboportions = QgsSimpleLineSymbolLayer()
    colorportion = QtGui.QColor(0, 0, 0, 255)
    symboportions.setColor(colorportion)
    symboportions.setWidth(0.26)
    portions_train.renderer().symbol().changeSymbolLayer(0, symboportions)
    portions_train.triggerRepaint()
    
    #Portions de train : étiquettes
    labels_portions = QgsPalLayerSettings()
    text_portions = QgsTextFormat()
    #Police et taille
    text_portions.setFont(QFont("MS Shell Dlg 2", 7))
    text_portions.setSize(7)
    #Placement et options de placement de ligne
    labels_portions.placement = QgsPalLayerSettings.Curved
    labels_portions.placementFlags = QgsPalLayerSettings.OnLine
                    
    labels_portions.enabled = True
    #Options du buffer de fond
    buffer_portions = QgsTextBufferSettings()
    buffer_portions.setColor(QColor('white'))
    buffer_portions.setSize(1)
    buffer_portions.setEnabled(True)
    text_portions.setBuffer(buffer_portions)
    labels_portions.setFormat(text_portions)
    labels_portions.fieldName = "len_str"
    
    labeling_port = QgsVectorLayerSimpleLabeling(labels_portions)
    portions_train.setLabelsEnabled(True)
    portions_train.setLabeling(labeling_port)
    portions_train.triggerRepaint()
    
    #Stations : symbologie catégorisée à deux éléments
    values_stationsloc = {"ligne A", "ligne B", "ligne C", "ligne T1", "Téléo"}
    categories_stationsloc = []
    for value in values_stationsloc:    
        pointStylestationloc1 = {}
        pointStylestationloc2 = {}
        if value == "ligne A" :
            pointStylestationloc1['name'] = "diamond"
            pointStylestationloc1['color'] = '#d83e38'
            pointStylestationloc2['name'] = "diamond"
            pointStylestationloc2['color'] = '#ffffff'
            pointStylestationloc2['color_border'] = '#d83e38'
        elif value == "ligne B" :
            pointStylestationloc1['name'] = "diamond"
            pointStylestationloc1['color'] = '#eeea63'
            pointStylestationloc2['name'] = "diamond"
            pointStylestationloc2['color'] = '#ffffff'
            pointStylestationloc2['color_border'] = '#eeea63'
        elif value == 'ligne C' :
            pointStylestationloc1['name'] = "diamond"
            pointStylestationloc1['color'] = '#d8962c'
            pointStylestationloc2['name'] = "diamond"
            pointStylestationloc2['color'] = '#ffffff'
            pointStylestationloc2['color_border'] = '#d8962c'
        elif value == 'ligne T1' :
            pointStylestationloc1['name'] = "diamond"
            pointStylestationloc1['color'] = '#3ab7d9'
            pointStylestationloc2['name'] = "diamond"
            pointStylestationloc2['color'] = '#ffffff'
            pointStylestationloc2['color_border'] = '#3ab7d9'
        elif value == 'Téléo' :
            pointStylestationloc1['name'] = "diamond"
            pointStylestationloc1['color'] = '#29cf6e'
            pointStylestationloc2['name'] = "diamond"
            pointStylestationloc2['color'] = '#ffffff'
            pointStylestationloc2['color_border'] = '#29cf6e'
            
        pointStylestationloc1['color_border'] = '#232323'
        pointStylestationloc1['outline_width'] = '0'
        pointStylestationloc2['outline_width'] = '0.05'
        pointStylestationloc1['size'] = '1.84'
        pointStylestationloc2['size'] = '3'
        stationloc1 = QgsSimpleMarkerSymbolLayer.create(pointStylestationloc1)
        stationloc2 = QgsSimpleMarkerSymbolLayer.create(pointStylestationloc2)
    
        symbol_stationloc = QgsSymbol.defaultSymbol(stations_loc.geometryType())
        symbol_stationloc.appendSymbolLayer(stationloc2)
        symbol_stationloc.appendSymbolLayer(stationloc1)
        symbol_stationloc.deleteSymbolLayer(0)
        
        category = QgsRendererCategory(value, symbol_stationloc, str(value))
        categories_stationsloc.append(category)
    
    renderer_stationloc = QgsCategorizedSymbolRenderer('ligne', categories_stationsloc)
    if renderer_stationloc is not None:
       stations_loc.setRenderer(renderer_stationloc)
    stations_loc.triggerRepaint()
    
    #Stations - étiquettes
    labels_stationsloc = QgsPalLayerSettings()
    text_stationsloc = QgsTextFormat()
        
    text_stationsloc.setFont(QFont("Arial", 9))
    text_stationsloc.setSize(9)
    text_stationsloc.setColor(QColor(73, 94, 123, 255))
    
    #Options de placement pour les points : Cartographic = 6; Around point = 0; Offset from point = 1 
    #                                       Quadrant position: QuadrantAboveLeft = 0; QuadrantAbove = 1,...
    labels_stationsloc.placement = 1
    labels_stationsloc.quadOffset = 8
    labels_stationsloc.xOffset = 0
    labels_stationsloc.yOffset = 1.6
    
    labels_stationsloc.priority = 30
                    
    labels_stationsloc.enabled = True
    
    buffer_stationsloc = QgsTextBufferSettings()
    buffer_stationsloc.setColor(QColor('white'))
    buffer_stationsloc.setSize(0.6)
    buffer_stationsloc.setEnabled(True)
    text_stationsloc.setBuffer(buffer_stationsloc)
    labels_stationsloc.setFormat(text_stationsloc)
    labels_stationsloc.fieldName = "name"
    
    labeling_stationsloc = QgsVectorLayerSimpleLabeling(labels_stationsloc)
    stations_loc.setLabelsEnabled(True)
    stations_loc.setLabeling(labeling_stationsloc)
    stations_loc.triggerRepaint()
    
    #rReseaux rapides : symbologie catégorisée pour les lignes
    values_rrloc = {"Ligne A", "Ligne B", "Ligne M3", "Ligne T1", "Téléo", "Téléoex", "Ligne Bex", "Ligne C"}
    categories_rrloc = []
    for value in values_rrloc:    
        lineStylerrloc = {}
        if value == "Ligne A" :
            lineStylerrloc['color'] = '#ff131e'
        elif value == "Ligne B" :
            lineStylerrloc['color'] = '#e0e936'
        elif value == 'Ligne T1' :
            lineStylerrloc['color'] = '#1fb6e4'
        elif value == 'Ligne C' :
            lineStylerrloc['color'] = '#b26512'
        elif value == 'Ligne M3' or 'Téléo' or 'Téléoex' or 'Ligne Bex' :
            lineStylerrloc['color'] = '#6dd83c'
            lineStylerrloc['penstyle'] = 'dash'
        lineStylerrloc['outline_width'] = '0.86'
        lineStylerrloc['joinstyle'] = 'round'
        lineStylerrloc['capstyle'] = 'round'
        rrloc = QgsSimpleLineSymbolLayer.create(lineStylerrloc)
    
        symbol_rrloc = QgsSymbol.defaultSymbol(reseaux_rapides_loc.geometryType())
        symbol_rrloc.appendSymbolLayer(rrloc)
        symbol_rrloc.deleteSymbolLayer(0)
        
        category = QgsRendererCategory(value, symbol_rrloc, str(value))
        categories_rrloc.append(category)
    
    renderer_rrloc = QgsCategorizedSymbolRenderer('name', categories_rrloc)
    if renderer_rrloc is not None:
       reseaux_rapides_loc.setRenderer(renderer_rrloc)
    reseaux_rapides_loc.triggerRepaint()
    
    #Reseaux rapides - étiquettes
    labels_rrloc = QgsPalLayerSettings()
    text_rrloc = QgsTextFormat()
        
    text_rrloc.setFont(QFont("MS Shell Dlg 2", 10))
    text_rrloc.setSize(10)
    
    labels_rrloc.placement = QgsPalLayerSettings.Curved
    labels_rrloc.placementFlags = QgsPalLayerSettings.OnLine
    
    labels_rrloc.RepeatDistance = 1500
    labels_rrloc.RepeatDistanceUnit = 'Meters'
    labels_rrloc.isObstacle = True
    labels_rrloc.priority = 4
                    
    labels_rrloc.enabled = True
    
    buffer_rrloc = QgsTextBufferSettings()
    buffer_rrloc.setColor(QColor('white'))
    buffer_rrloc.setSize(1)
    buffer_rrloc.setEnabled(True)
    text_rrloc.setBuffer(buffer_rrloc)
    labels_rrloc.setFormat(text_rrloc)
    labels_rrloc.fieldName = "vrai_nom"
    
    labeling_rrloc = QgsVectorLayerSimpleLabeling(labels_rrloc)
    reseaux_rapides_loc.setLabelsEnabled(True)
    reseaux_rapides_loc.setLabeling(labeling_rrloc)
    reseaux_rapides_loc.triggerRepaint()
    
    #Metropole : remplissage
    colormetfill = QColor(114, 155, 111, 0)
    colormetout = QtGui.QColor(252, 143, 126, 255)
    symbo_met = QgsSimpleFillSymbolLayer(color = colormetfill, strokeColor = colormetout, strokeWidth = 2.46)
    metropole.renderer().symbol().changeSymbolLayer(0, symbo_met)
    metropole.triggerRepaint()
    
    #Commune : remplissage
    colorcomfill = QColor(0, 0, 0, 0)
    colorcomout = QtGui.QColor('#495e7b')
    symbo_com = QgsSimpleFillSymbolLayer(color = colorcomfill, strokeColor = colorcomout, strokeWidth = 0.4)
    commune.renderer().symbol().changeSymbolLayer(0, symbo_com)
    commune.triggerRepaint()
    
    #Commune : étiquettes par chargement de style
    commune.loadNamedStyle(""+ dossier_source +"commune_style.qml")
    
    #Groupe accessibilité
    #Arrêts de transportco : symbologie catégorisée
    values_tco = {"arrêt de bus", "arrêt tram", "station métro", "station téléo"}
    categories_tco = []
    for value in values_tco:    
        svgStyletco = {}
        svgStyletco['fill'] = '#232323'
        rondStyletco = {}
        if value == "arrêt de bus" :
            rondStyletco['name'] = "circle"
            rondStyletco['color'] = '#ffffff'
            rondStyletco['color_border'] = '#322e85'
            rondStyletco['outline_width'] = '0.4'
            rondStyletco['size'] = '1.6'
            svgStyletco['size'] = '0'
        elif value == "arrêt tram" :
            svgStyletco['name'] = "C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr/svg/transport/transport_tram_stop.svg"
            svgStyletco['size'] = '3.448270'
            rondStyletco['name'] = 'circle'
            rondStyletco['color'] = '#ffffff'
            rondStyletco['color_border'] = '#232323'
            rondStyletco['size'] = '4'
        elif value == "station métro":
            svgStyletco['name'] = "C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr/svg/transport/transport_train_station.svg"
            svgStyletco['size'] = '4.31'
            rondStyletco['name'] = 'circle'
            rondStyletco['color'] = '#ffffff'
            rondStyletco['color_border'] = '#232323'
            rondStyletco['size'] = '5'
        elif value == "station téléo":
            svgStyletco['name'] = ""+ dossier_icones +"cable-car-cabin.svg"
            svgStyletco['size'] = '3.44'
            rondStyletco['name'] = 'circle'
            rondStyletco['color'] = '#ffffff'
            rondStyletco['color_border'] = '#232323'
            rondStyletco['size'] = '4.4'
        tco = QgsSvgMarkerSymbolLayer.create(svgStyletco)
        tco_rond = QgsSimpleMarkerSymbolLayer.create(rondStyletco)
    
        symbol_tco = QgsSymbol.defaultSymbol(transportco_acces.geometryType())
        symbol_tco.appendSymbolLayer(tco_rond)
        symbol_tco.appendSymbolLayer(tco)
        symbol_tco.deleteSymbolLayer(0)
        
        category = QgsRendererCategory(value, symbol_tco, str(value))
        categories_tco.append(category)
    
    renderer_tco = QgsCategorizedSymbolRenderer('type', categories_tco)
    if renderer_tco is not None:
       transportco_acces.setRenderer(renderer_tco)
    transportco_acces.triggerRepaint()
        
    #Autopartage : superposition de deux logos
    #Premier logo simple
    autofond = QgsSimpleMarkerSymbolLayer(size = 5, color = QColor(255, 255, 255, 255), strokeColor = QColor(35, 35, 35, 255))
    autopartage.renderer().symbol().changeSymbolLayer(0, autofond)
    #2e logo (svg)
    symbolauto = QgsSvgMarkerSymbolLayer('C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr/svg/transport/transport_car_share.svg')
    symbolauto.setSize(4.14)
    symbolauto.setFillColor(QColor('#13b937'))
    symbolauto.setStrokeColor(QColor(35, 35, 35, 0))
    symbolauto.setStrokeWidth(0.2)
    #Ajout du 2e symbole à la symbologie d'origine
    autopartage.renderer().symbol().appendSymbolLayer(symbolauto)
    autopartage.triggerRepaint()
    
    #Réseaux rapides : symbologie catégorisée
    values_rracc = {"Ligne A", "Ligne B", "Ligne M3", "Ligne T1", "Téléo", "Téléoex", "Ligne Bex", "Ligne C"}
    categories_rracc = []
    for value in values_rracc:    
        lineStylerracc = {}
        if value == "Ligne A" :
            lineStylerracc['color'] = '#ff131e'
        elif value == "Ligne B" :
            lineStylerracc['color'] = '#e0e936'
        elif value == 'Ligne T1' :
            lineStylerracc['color'] = '#1fb6e4'
        elif value == 'Ligne C' :
            lineStylerracc['color'] = '#b26512'
        elif value == 'Ligne M3' or 'Téléo' or 'Téléoex' or 'Ligne Bex' :
            lineStylerracc['color'] = '#6dd83c'
            lineStylerracc['penstyle'] = 'dash'
        lineStylerracc['outline_width'] = '0.86'
        lineStylerracc['joinstyle'] = 'Round'
        lineStylerracc['capstyle'] = 'Round'
        rracc = QgsSimpleLineSymbolLayer.create(lineStylerracc)
    
        symbol_rracc = QgsSymbol.defaultSymbol(reseaux_rapides_acces.geometryType())
        symbol_rracc.appendSymbolLayer(rracc)
        symbol_rracc.deleteSymbolLayer(0)
        
        category = QgsRendererCategory(value, symbol_rracc, str(value))
        categories_rracc.append(category)
    
    renderer_rracc = QgsCategorizedSymbolRenderer('name', categories_rracc)
    if renderer_rracc is not None:
       reseaux_rapides_acces.setRenderer(renderer_rracc)
    reseaux_rapides_acces.triggerRepaint()
    
    #Réseaux rapides : étiquettes
    labels_rracc = QgsPalLayerSettings()
    text_rracc = QgsTextFormat()
        
    text_rracc.setFont(QFont("MS Shell Dlg 2", 10))
    text_rracc.setSize(10)
    
    labels_rracc.placement = QgsPalLayerSettings.Curved
    labels_rracc.placementFlags = QgsPalLayerSettings.OnLine
    
    labels_rracc.RepeatDistance = 1500
    labels_rracc.RepeatDistanceUnit = 'Meters'
    labels_rracc.isObstacle = True
    labels_rracc.priority = 4
                    
    labels_rracc.enabled = True
    
    buffer_rracc = QgsTextBufferSettings()
    buffer_rracc.setColor(QColor('white'))
    buffer_rracc.setSize(1)
    buffer_rracc.setEnabled(True)
    text_rracc.setBuffer(buffer_rrloc)
    labels_rracc.setFormat(text_rrloc)
    labels_rracc.fieldName = "vrai_nom"
    
    labeling_rracc = QgsVectorLayerSimpleLabeling(labels_rracc)
    reseaux_rapides_acces.setLabelsEnabled(True)
    reseaux_rapides_acces.setLabeling(labeling_rracc)
    reseaux_rapides_acces.triggerRepaint()
    
    #Linéos : remplissage
    colorlineo = QColor('#303bb6')
    symbo_lineo = QgsSimpleLineSymbolLayer()
    symbo_lineo.setColor(colorlineo)
    symbo_lineo.setWidth(0.4)
    lineos.renderer().symbol().changeSymbolLayer(0, symbo_lineo)
    lineos.triggerRepaint()
    
    #Linéos : étiquettes
    labels_lineos = QgsPalLayerSettings()
    text_lineos = QgsTextFormat()
        
    text_lineos.setFont(QFont("MS Shell Dlg 2", 10))
    text_lineos.setSize(10)
    
    labels_lineos.placement = QgsPalLayerSettings.Curved
    labels_lineos.placementFlags = QgsPalLayerSettings.OnLine
    
    labels_lineos.RepeatDistance = 800
    labels_lineos.RepeatDistanceUnit = 'Meters'
    labels_lineos.isObstacle = True
    labels_lineos.priority = 40
                    
    labels_lineos.enabled = True
    
    buffer_lineos = QgsTextBufferSettings()
    buffer_lineos.setColor(QColor('white'))
    buffer_lineos.setSize(1)
    buffer_lineos.setEnabled(True)
    text_lineos.setBuffer(buffer_lineos)
    labels_lineos.setFormat(text_lineos)
    labels_lineos.fieldName = "LIGNE"
    
    labeling_lineos = QgsVectorLayerSimpleLabeling(labels_lineos)
    lineos.setLabelsEnabled(True)
    lineos.setLabeling(labeling_lineos)
    lineos.triggerRepaint()
    
    #Réseau de bus : remplissage
    colorbus = QColor('#303bb6')
    symbo_bus = QgsSimpleLineSymbolLayer()
    symbo_bus.setColor(colorbus)
    symbo_bus.setWidth(0.2)
    bus_acces.renderer().symbol().changeSymbolLayer(0, symbo_bus)
    bus_acces.triggerRepaint()
        
    #Lignes de voitures : remplissage
    colorvoit = QColor('#525252')
    symbo_voit = QgsSimpleLineSymbolLayer()
    symbo_voit.setColor(colorvoit)
    symbo_voit.setWidth(0.35)
    voiture_lines.renderer().symbol().changeSymbolLayer(0, symbo_voit)
    voiture_lines.triggerRepaint()
    
    #Lignes de vélo : remplissage
    colorvelo = QColor('#a869a8')
    symbo_velo = QgsSimpleLineSymbolLayer()
    symbo_velo.setColor(colorvelo)
    symbo_velo.setWidth(0.35)
    velo_lines.renderer().symbol().changeSymbolLayer(0, symbo_velo)
    velo_lines.triggerRepaint()
    
    #Lignes de piétons : remplissage
    colorpieton = QColor('#00d8ca')
    symbo_pieton = QgsSimpleLineSymbolLayer()
    symbo_pieton.setColor(colorpieton)
    symbo_pieton.setWidth(0.35)
    pieton_lines.renderer().symbol().changeSymbolLayer(0, symbo_pieton)
    pieton_lines.triggerRepaint()
    
    #Ligne de train ; remplissage
    colortrainacc = QColor('#5e5e5e')
    symbo_trainacc = QgsSimpleLineSymbolLayer()
    symbo_trainacc.setColor(colortrainacc)
    symbo_trainacc.setWidth(0.16)
    train_acc.renderer().symbol().changeSymbolLayer(0, symbo_trainacc)
    train_acc.triggerRepaint()
    
    #Groupe de la carte générale
    #scolaire : remplissage
    colorscol1 = QColor('#d8780a')
    symbo_scolaire = QgsSimpleFillSymbolLayer(color = colorscol1, strokeColor = colorscol1, strokeWidth = 0)
    scolaire.renderer().symbol().changeSymbolLayer(0, symbo_scolaire)
    scolaire.triggerRepaint()
    
    #loisirs : remplissage
    colorlois1 = QColor('#f17dc7')
    symbo_loisirs = QgsSimpleFillSymbolLayer(color = colorlois1, strokeColor = colorlois1, strokeWidth = 0)
    loisirs.renderer().symbol().changeSymbolLayer(0, symbo_loisirs)
    loisirs.triggerRepaint()
    
    #entreprises : remplissage
    colorent1 = QColor('#10e4ba')
    symbo_entreprises = QgsSimpleFillSymbolLayer(color = colorent1, strokeColor = colorent1, strokeWidth = 0)
    entreprises.renderer().symbol().changeSymbolLayer(0, symbo_entreprises)
    entreprises.triggerRepaint()
    
    #commercial : remplissage
    colorcom1 = QColor('#ab1ba9')
    symbo_commercial = QgsSimpleFillSymbolLayer(color = colorcom1, strokeColor = colorcom1, strokeWidth = 0)
    commercial.renderer().symbol().changeSymbolLayer(0, symbo_commercial)
    commercial.triggerRepaint()
    
    #logistics : remplissage
    colorlog1 = QColor('#fe003f')
    symbo_log = QgsSimpleFillSymbolLayer(color = colorlog1, strokeColor = colorlog1, strokeWidth = 0)
    logistics.renderer().symbol().changeSymbolLayer(0, symbo_log)
    logistics.triggerRepaint()
    
    #residentiel : remplissage
    colorres1 = QColor('#aba3a3')
    symbo_res = QgsSimpleFillSymbolLayer(color = colorres1, strokeColor = colorres1, strokeWidth = 0)
    residentiel.renderer().symbol().changeSymbolLayer(0, symbo_res)
    residentiel.triggerRepaint()
    
    #parking: remplissage et logo centroïde
    #remplissage
    colorpark = QtGui.QColor(88, 88, 88, 255)
    symbo_park = QgsSimpleFillSymbolLayer(color = colorpark, strokeColor = colorpark, strokeWidth = 0)
    parking_gen.renderer().symbol().changeSymbolLayer(0, symbo_park)
    parking_gen.triggerRepaint()
    
    #symbole centroïde
    symbol_parkcent = QgsCentroidFillSymbolLayer.create()
    symbol_parkcent.setColor(QColor("transparent"))
    colorP = QtGui.QColor(255, 255, 255, 255)       
    #transformation du centroïde en marqueur lettre         
    symbolparkP = QgsFontMarkerSymbolLayer(fontFamily = 'Arial Black', chr = 'P', pointSize = 2, color = colorP)
    
    #Ajout du centroïde en temps que sous-symbole
    marker_P = QgsMarkerSymbol()
    marker_P.changeSymbolLayer(0, symbolparkP)
    symbol_parkcent.setSubSymbol(marker_P)
    
    parking_gen.renderer().symbol().appendSymbolLayer(symbol_parkcent)
    parking_gen.triggerRepaint()
        
    #zones à urbaniser : remplissage
    colorzu = QtGui.QColor('#000000')
    symbo_zu = QgsSimpleFillSymbolLayer(color = colorzu, strokeColor = colorzu, strokeWidth = 0.46, style = Qt.BDiagPattern)
    zone_urba.renderer().symbol().changeSymbolLayer(0, symbo_zu)
    zone_urba.triggerRepaint()
    
    #ligne train : remplissage
    colortraingen = QColor('#000000')
    symbo_traingen = QgsSimpleLineSymbolLayer()
    symbo_traingen.setColor(colortraingen)
    symbo_traingen.setWidth(0.16)
    train_gen.renderer().symbol().changeSymbolLayer(0, symbo_traingen)
    train_gen.triggerRepaint()
    
    #Groupe plans
    #tArrêts de transports : symbologie catégorisée de points
    values_tco2 = {"arrêt de bus", "arrêt tram", "station métro", "station téléo"}
    categories_tco2 = []
    for value in values_tco2:    
        svgStyletco2 = {}
        svgStyletco2['fill'] = '#232323'
        rondStyletco2 = {}
        if value == "arrêt de bus" :
            rondStyletco2['name'] = 'circle'
            rondStyletco2['color'] = '#ffffff'
            rondStyletco2['color_border'] = '#232323'
            rondStyletco2['size'] = '5.4'
            svgStyletco2['size'] = '4.72'
            svgStyletco2['name'] = "C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr/svg/transport/highway=bus_stop.svg"
        elif value == "arrêt tram" :
            svgStyletco2['name'] = "C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr/svg/transport/transport_tram_stop.svg"
            svgStyletco2['size'] = '5'
            rondStyletco2['name'] = 'circle'
            rondStyletco2['color'] = '#ffffff'
            rondStyletco2['color_border'] = '#232323'
            rondStyletco2['size'] = '5.8'
        elif value == "station métro":
            svgStyletco2['name'] = "C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr/svg/transport/transport_train_station.svg"
            svgStyletco2['size'] = '4.65'
            rondStyletco2['name'] = 'circle'
            rondStyletco2['color'] = '#ffffff'
            rondStyletco2['color_border'] = '#232323'
            rondStyletco2['size'] = '5.4'
        elif value == "station téléo":
            svgStyletco2['name'] = ""+ dossier_icones +"cable-car-cabin.svg"
            svgStyletco2['size'] = '4.54'
            svgStyletco2['xOffset'] = '-2.3'
            rondStyletco2['name'] = 'circle'
            rondStyletco2['color'] = '#ffffff'
            rondStyletco2['color_border'] = '#232323'
            rondStyletco2['size'] = '5.8'
        tco2 = QgsSvgMarkerSymbolLayer.create(svgStyletco2)
        tco_rond2 = QgsSimpleMarkerSymbolLayer.create(rondStyletco2)
    
        symbol_tco2 = QgsSymbol.defaultSymbol(transportco_plan.geometryType())
        symbol_tco2.appendSymbolLayer(tco_rond2)
        symbol_tco2.appendSymbolLayer(tco2)
        symbol_tco2.deleteSymbolLayer(0)
        
        category = QgsRendererCategory(value, symbol_tco2, str(value))
        categories_tco2.append(category)
    
    renderer_tco2 = QgsCategorizedSymbolRenderer('type', categories_tco2)
    if renderer_tco2 is not None:
       transportco_plan.setRenderer(renderer_tco2)
    transportco_plan.triggerRepaint()
    
    #infrastructures : symbologie catégorisée de points
    values_infra = {"abri", "banc", "tickets", "velo", "info", "colis", "guichet", "toilettes", "attente", "vending", "ascenseur", "PMR", "shop", "food"}
    categories_infra = []
    for value in values_infra:    
        svgStyleinfra = {}
        svgStyleinfra['fill'] = '#232323'
        rondStyleinfra = {}
        if value == "abri" :
            rondStyleinfra['name'] = 'square'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '3.6'
            svgStyleinfra['size'] = '3.6'
            svgStyleinfra['name'] = ""+ dossier_icones +"1200px-Pictograms-nps-shelter.svg.svg"
        elif value == "banc" :
            svgStyleinfra['name'] = ""+ dossier_icones +"bench-furniture.svg"
            svgStyleinfra['size'] = '3'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.8'
        elif value == "tickets":
            svgStyleinfra['name'] = ""+ dossier_icones +"movie-tickets-svgrepo-com.svg"
            svgStyleinfra['size'] = '3.58'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.2'
        elif value == "velo":
            svgStyleinfra['name'] = ""+ dossier_icones +"bike-parking-signal.svg"
            svgStyleinfra['size'] = '4.2'
            rondStyleinfra['name'] = 'square'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '2.92'
        elif value == "info":
            svgStyleinfra['name'] = "C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr/svg/amenity/amenity_information.svg"
            svgStyleinfra['size'] = '5.2'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.24'
        elif value == "colis":
            svgStyleinfra['name'] = ""+ dossier_icones +"2ef81056a03a25554a2fa1f01e018d55.svg"
            svgStyleinfra['size'] = '3.73'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.8'
        elif value == "guichet":
            svgStyleinfra['name'] = ""+ dossier_icones +"0d83a39a1d960c250dce5a3b837c5bfd.svg"
            svgStyleinfra['size'] = '3.57'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.6'
        elif value == "toilettes":
            svgStyleinfra['name'] = "C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr/svg/amenity/amenity_toilets.svg"
            svgStyleinfra['size'] = '3.68'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.6'
        elif value == "attente":
            svgStyleinfra['name'] = ""+ dossier_icones +"aiga_waiting_room.svg"
            svgStyleinfra['size'] = '3'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.8'
        elif value == "vending":
            svgStyleinfra['name'] = ""+ dossier_icones +"vending-machine-icon-24.svg"
            svgStyleinfra['size'] = '3.57'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.6'
        elif value == "ascenseur":
            svgStyleinfra['name'] = ""+ dossier_icones +"578px-Aiga_elevator.svg.svg"
            svgStyleinfra['size'] = '4.8'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.8'
        elif value == "PMR":
            svgStyleinfra['name'] = ""+ dossier_icones +"c546e05e1733e6c8fb6ef976bf896d59.svg"
            svgStyleinfra['size'] = '3.56'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.2'
        elif value == "shop":
            svgStyleinfra['name'] = ""+ dossier_icones +"3311f92aceff0ab41f1718b1f8606113.svg"
            svgStyleinfra['size'] = '3.28'
            rondStyleinfra['name'] = 'circle'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.6'
        elif value == "food":
            svgStyleinfra['name'] = ""+ dossier_icones +"simplefastfoodicon.svg"
            svgStyleinfra['size'] = '3.68'
            rondStyleinfra['name'] = 'square'
            rondStyleinfra['color'] = '#ffffff'
            rondStyleinfra['color_border'] = '#232323'
            rondStyleinfra['size'] = '4.6'
        infra = QgsSvgMarkerSymbolLayer.create(svgStyleinfra)
        infra_rond = QgsSimpleMarkerSymbolLayer.create(rondStyleinfra)
    
        symbol_infra = QgsSymbol.defaultSymbol(infrastructures.geometryType())
        symbol_infra.appendSymbolLayer(infra_rond)
        symbol_infra.appendSymbolLayer(infra)
        symbol_infra.deleteSymbolLayer(0)
        
        category = QgsRendererCategory(value, symbol_infra, str(value))
        categories_infra.append(category)
    
    renderer_infra = QgsCategorizedSymbolRenderer('type', categories_infra)
    if renderer_infra is not None:
       infrastructures.setRenderer(renderer_infra)
    infrastructures.triggerRepaint()
    
    #Accès piéton : ligne et logo SVG - chargement d'un style
    pieton.loadNamedStyle(""+ dossier_source +"pieton_style.qml")
    
    #Accès cycle : ligne de logo SVG - chargement d'un style
    cyclable.loadNamedStyle(""+ dossier_source +"cycle_style.qml")
    
    #Arbres : remplissage et forme de points
    arbres_list = {}
    arbres_list['name'] = 'hexagon'
    arbres_list['size'] = '2'
    arbres_list['color'] = '175, 223, 172, 187'
    arbres_list['color_border'] = '#8b8b8b'
    arbres_list['outline_width'] = '0.1'
    arbresstyle = QgsSimpleMarkerSymbolLayer.create(arbres_list)
    arbres.renderer().symbol().changeSymbolLayer(0, arbresstyle)
    arbres.triggerRepaint()
    
    #cimetieres : remplissage à motifs
    colorcim = QtGui.QColor('#000000')
    symbo_cim = QgsSimpleFillSymbolLayer(color = colorzu, strokeColor = colorzu, strokeWidth = 0.46, style = Qt.Dense6Pattern)
    cimetieres.renderer().symbol().changeSymbolLayer(0, symbo_cim)
    cimetieres.triggerRepaint()
    
    #parking : remplissage et centroïde
    colorparkplan = QtGui.QColor('#bebebe')
    symbo_parkplan = QgsSimpleFillSymbolLayer(color = colorparkplan, strokeColor = colorparkplan, strokeWidth = 0)
    parking_plan.renderer().symbol().changeSymbolLayer(0, symbo_parkplan)
    parking_plan.triggerRepaint()
    
    symbol_parkplancent = QgsCentroidFillSymbolLayer.create()
    symbol_parkplancent.setColor(QColor("transparent"))
    colorPplan = QtGui.QColor(255, 255, 255, 255)                       
    symbolparkPplan = QgsFontMarkerSymbolLayer(fontFamily = 'Arial Black', chr = 'P', pointSize = 8, color = colorPplan)
    
    marker_Pplan = QgsMarkerSymbol()
    marker_Pplan.changeSymbolLayer(0, symbolparkPplan)
    symbol_parkplancent.setSubSymbol(marker_Pplan)
    
    parking_plan.renderer().symbol().appendSymbolLayer(symbol_parkplancent)
    parking_plan.triggerRepaint()
    
    #Bati gare : chargement d'un style (multiples symboles catégorisés)
    bati_gare.loadNamedStyle(""+ dossier_source +"bati_mix_style.qml")
    
    #Bati gare complémentaire : remplissage
    colorcomplem1 = QColor('#952a23')
    colorcomplem2 = QtGui.QColor('#232323')
    symbo_complem = QgsSimpleFillSymbolLayer(color = colorcomplem1, strokeColor = colorcomplem2, strokeWidth = 0.26)
    bati_gare_complem.renderer().symbol().changeSymbolLayer(0, symbo_complem)
    bati_gare_complem.triggerRepaint()
    
    #bati autre : remplissage
    colorautre1 = QColor('#f2f2f2')
    colorautre2 = QtGui.QColor('#a2bcd1')
    symbo_autre = QgsSimpleFillSymbolLayer(color = colorautre1, strokeColor = colorautre2, strokeWidth = 0.26)
    bati_autre.renderer().symbol().changeSymbolLayer(0, symbo_autre)
    bati_autre.triggerRepaint()
        
    #quais : remplissage catégorisé
    values_quais = {"existant", "potentiel"}
    categories_quais = []
    for value in values_quais:    
        fillStylequais = {}
        if value == "existant" :
            fillStylequais['color'] = '222, 192, 103, 167'
        elif value == "potentiel" :
            fillStylequais['color'] = '255, 204, 1, 255'
            fillStylequais['style'] = 'dense6'
            fillStylequais['color_border'] = '#232323'
            fillStylequais['outline_width'] = '0.26'
        quaissymb = QgsSimpleFillSymbolLayer.create(fillStylequais)
        symbol_quais = QgsSymbol.defaultSymbol(quais.geometryType())
        symbol_quais.appendSymbolLayer(quaissymb)
        symbol_quais.deleteSymbolLayer(0)
        category = QgsRendererCategory(value, symbol_quais, str(value))
        categories_quais.append(category)
    
    renderer_quais = QgsCategorizedSymbolRenderer('type', categories_quais)
    if renderer_quais is not None:
       quais.setRenderer(renderer_quais)
    quais.triggerRepaint()
    
    #train plan : remplissage
    colortrainplan = QColor('#000000')
    symbo_trainplan = QgsSimpleLineSymbolLayer()
    symbo_trainplan.setColor(colortrainplan)
    symbo_trainplan.setWidth(0.16)
    train_plan.renderer().symbol().changeSymbolLayer(0, symbo_trainplan)
    train_plan.triggerRepaint()
    
    #eau : remplissage
    coloreau = QColor('#d3edf3')
    symbo_eau = QgsSimpleFillSymbolLayer(color = coloreau, strokeColor = coloreau, strokeWidth = 0)
    eau.renderer().symbol().changeSymbolLayer(0, symbo_eau)
    eau.triggerRepaint()
    
    #espaces verts : remplissage
    colorvert = QColor('#b8c6a2')
    symbo_vert = QgsSimpleFillSymbolLayer(color = colorvert, strokeColor = colorvert, strokeWidth = 0)
    espace_vert.renderer().symbol().changeSymbolLayer(0, symbo_vert)
    espace_vert.triggerRepaint()
    
    #Insérer les couches Raster
    #URL
    url_osm_mono = 'type=xyz&url=http://tiles.wmflabs.org/bw-mapnik/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0'
    #Indiquer les paramètres
    osm_mono = QgsRasterLayer(url_osm_mono, 'OpenStreetMap Monochrome', 'wms')
    #Insérer la couche
    QgsProject.instance().addMapLayer(osm_mono)
    esri_url = 'type=xyz&url=http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D&zmax=16&zmin=0'
    esri_gray = QgsRasterLayer(esri_url, 'Esri Gray (light)', 'wms')
    QgsProject.instance().addMapLayer(esri_gray)
    url_osm_hot = 'type=xyz&url=http://a.tile.openstreetmap.fr/hot/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0'
    osm_hot = QgsRasterLayer(url_osm_hot, 'OpenStreetMap H.O.T.', 'wms') 
    QgsProject.instance().addMapLayer(osm_hot)
    url_cartodb = 'type=xyz&url=http://basemaps.cartocdn.com/light_all/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=20&zmin=0'
    cartodb = QgsRasterLayer(url_cartodb, 'CartoDb Positron', 'wms')
    QgsProject.instance().addMapLayer(cartodb)
    
    #Répartir les couches dans les groupes
    #Groupe plan
    root = QgsProject.instance().layerTreeRoot()
    plans_group = root.addGroup("plans")
    plans_group.addLayer(plan_fonctionnel)
    plans_group.addLayer(transportco_plan)
    plans_group.addLayer(infrastructures)
    plans_group.addLayer(pieton)
    plans_group.addLayer(cyclable)
    plans_group.addLayer(arbres)
    plans_group.addLayer(cimetieres)
    plans_group.addLayer(bati_gare)
    plans_group.addLayer(bati_gare_complem)
    plans_group.addLayer(bati_autre)
    plans_group.addLayer(quais)
    plans_group.addLayer(parking_plan)
    plans_group.addLayer(train_plan)
    plans_group.addLayer(eau)
    plans_group.addLayer(espace_vert)
    
    #Groupe général
    generale_group = root.addGroup("carte_generale")
    generale_group.addLayer(scolaire)
    generale_group.addLayer(loisirs)
    generale_group.addLayer(entreprises)
    generale_group.addLayer(commercial)
    generale_group.addLayer(logistics)
    generale_group.addLayer(residentiel)
    generale_group.addLayer(parking_gen)
    generale_group.addLayer(zone_urba)
    generale_group.addLayer(train_gen)
    
    #Groupe accès
    acces_group = root.addGroup("carte_accessibilite")
    acces_group.addLayer(transportco_acces)
    acces_group.addLayer(autopartage)
    acces_group.addLayer(reseaux_rapides_acces)
    acces_group.addLayer(lineos)
    acces_group.addLayer(bus_acces)
    acces_group.addLayer(voiture_lines)
    acces_group.addLayer(pieton_lines)
    acces_group.addLayer(velo_lines)
    acces_group.addLayer(train_acc)
    
    #Groupe localisation
    loc_group = root.addGroup("carte_localisation")
    loc_group.addLayer(portions_train)
    loc_group.addLayer(stations_loc)
    loc_group.addLayer(reseaux_rapides_loc)
    loc_group.addLayer(metropole)
    loc_group.addLayer(commune)
    
#Fonction de génération des fiches
def generation_ficheV2():
    #Appel des mises en page
    layoutp1 = QgsProject.instance().layoutManager().layoutByName("page1")
    layoutp2 = QgsProject.instance().layoutManager().layoutByName("page2")
    #PAGE 1
    #BLOC 1 INFOS
    #Appel du bloc1, découpage en fonction de la gare en entrée et insertion de la nouvelle couche
    bloc1 = QgsProject.instance().mapLayersByName('bloc1')[0]
    processing.run("native:extractbyattribute", {'INPUT': bloc1,'FIELD':'gares','OPERATOR':0,'VALUE':''+ gare +'','OUTPUT':""+ dossier_new +"data1"+ gare +".csv"})
    data1 = iface.addVectorLayer(""+ dossier_new +"data1"+ gare +".csv", '','ogr',)
    #Assigner les objets de la mise en page à des variables
    ordre = layoutp1.itemById('ordre')
    nom_gare = layoutp1.itemById('nom_gare')
    nom_commune = layoutp1.itemById('nom_commune')
    typologie_gare = layoutp1.itemById('typologie_gare')
    voca_gare = layoutp1.itemById('voc_gare')
    centrale = layoutp1.itemById('centrale')
    interco = layoutp1.itemById('pem')
    densegrand = layoutp1.itemById('densegrand')
    denselocal = layoutp1.itemById('denselocal')
    perigrand = layoutp1.itemById('perigrand')
    perilocal = layoutp1.itemById('perilocal')
    trame_voc = layoutp1.itemById('trame_voc')
    #Assigner les valeurs du bloc1 aux variables créées précédemment
    for row in data1.getFeatures():
        ordretxt = row[6]
        ordre.setText(''+ ordretxt +'')
        nom_gare_txt = row[1]
        nom_gare.setText(''+ nom_gare_txt.upper() +'')
        nom_commune_txt = row[2]
        nom_commune.setText(''+ nom_commune_txt +'')
        type_gare = row[5]
        typologie_gare.setText(''+ type_gare +'')
        vocation_gare = row[3]
        voca_gare.setText(''+ vocation_gare +'')
    #Assigner un logo et la couleur de la trame de la mise en page en fonction du type de gare 
    if type_gare == "Gare existante":
        symbolstat = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"train_bleu.svg")
        trame_voc.setPicturePath(""+ dossier_icones +"bloc1_typologieB.svg")
    elif type_gare == "Gare potentielle":
        symbolstat = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"train_rose.svg")
        trame_voc.setPicturePath(""+ dossier_icones +"bloc1_typologieR.svg")
    #Assigner un logo et la couleur de la trame de la mise en page en fonction de la vocation de la gare 
    if vocation_gare == "Gare centrale":
        if type_gare == "Gare existante":
            centrale.setPicturePath(""+ dossier_icones +"curseurs/curseurB_centrale.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/centraleblue.svg")
        else:
            centrale.setPicturePath(""+ dossier_icones +"curseurs/curseurR_centrale.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/centralered.svg")
        #Modifier la taille des symboles en fonction du symbole SVG concerné, certains étant plus gros
        symbolvoc.setSize(20)
        symbolstat.setSize(8)
        #Renseigner un champ vide pour les autres objets de la mise en page
        interco.setPicturePath("")
        denselocal.setPicturePath("")
        densegrand.setPicturePath("")
        perilocal.setPicturePath("")
        perigrand.setPicturePath("")
    elif vocation_gare == "Gare d'échanges majeurs":
        centrale.setPicturePath("")
        if type_gare == "Gare existante":
            interco.setPicturePath(""+ dossier_icones +"curseurs/curseurB_pem.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/intercoblue.svg")
        else:
            interco.setPicturePath(""+ dossier_icones +"curseurs/curseurR_pem.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/intercored.svg")
        symbolvoc.setSize(20)
        symbolstat.setSize(8)
        denselocal.setPicturePath("")
        densegrand.setPicturePath("")
        perilocal.setPicturePath("")
        perigrand.setPicturePath("")
    elif vocation_gare == "Gare urbaine à rayonnement large":
        centrale.setPicturePath("")
        interco.setPicturePath("")
        denselocal.setPicturePath("")
        if type_gare == "Gare existante":
            densegrand.setPicturePath(""+ dossier_icones +"curseurs/curseurB_grand.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/densegrandblue.svg")
        else:
            densegrand.setPicturePath(""+ dossier_icones +"curseurs/curseurR_grand.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/densegrandred.svg")
        symbolvoc.setSize(20)
        symbolstat.setSize(8)
        perilocal.setPicturePath("")
        perigrand.setPicturePath("")
    elif vocation_gare == "Gare urbaine à rayonnement local":
        centrale.setPicturePath("")
        interco.setPicturePath("")
        if type_gare == "Gare existante":
            denselocal.setPicturePath(""+ dossier_icones +"curseurs/curseurB_petit.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/denselocalblue.svg")
        else:
            denselocal.setPicturePath(""+ dossier_icones +"curseurs/curseurR_petit.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/denselocalred.svg")
        symbolvoc.setSize(30)
        symbolstat.setSize(10)
        densegrand.setPicturePath("")
        perilocal.setPicturePath("")
        perigrand.setPicturePath("")
    elif vocation_gare == "Gare périurbaine à rayonnement local":
        centrale.setPicturePath("")
        interco.setPicturePath("")
        denselocal.setPicturePath("")
        densegrand.setPicturePath("")
        if type_gare == "Gare existante":
            perilocal.setPicturePath(""+ dossier_icones +"curseurs/curseurB_petit.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/perilocalblue.svg")
        else:
            perilocal.setPicturePath(""+ dossier_icones +"curseurs/curseurR_petit.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/perilocalred.svg")
        symbolvoc.setSize(30)
        symbolstat.setSize(10)
        perigrand.setPicturePath("")
    elif vocation_gare == "Gare périurbaine à rayonnement large":
        centrale.setPicturePath("")
        interco.setPicturePath("")
        denselocal.setPicturePath("")
        densegrand.setPicturePath("")
        perilocal.setPicturePath("")
        if type_gare == "Gare existante":
            perigrand.setPicturePath(""+ dossier_icones +"curseurs/curseurB_grand.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/perigrandblue.svg")
        else:
            perigrand.setPicturePath(""+ dossier_icones +"curseurs/curseurR_grand.svg")
            symbolvoc = QgsSvgMarkerSymbolLayer(""+ dossier_icones +"logos_voc_fond/perigrandred.svg")
        symbolvoc.setSize(20)
        symbolstat.setSize(8)
    #Insérer la photo dans la mise en page
    photo = layoutp1.itemById('photo')
    photo.setPicturePath(""+ dossier_photos +""+ gare +'.png')
    
    #CARTE LOCALISATION
    #Découper les données spatiales
    processing.run("native:extractbyattribute", {'INPUT':""+ dossier_source +'gares_individus.shp','FIELD':'Name','OPERATOR':0,'VALUE':''+ gare +'','OUTPUT':""+ dossier_new +'data_geo'+ gare +'.shp'})
    data_geo = iface.addVectorLayer(""+ dossier_new +'data_geo'+ gare +'.shp', '','ogr',)
    #Création du buffer autour de la gare
    processing.run("native:buffer", {'INPUT':QgsProcessingFeatureSourceDefinition(""+ dossier_new +'data_geo'+ gare +'.shp', selectedFeaturesOnly=False, featureLimit=-1, geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),'DISTANCE':2000,'SEGMENTS':10,'END_CAP_STYLE':0,'JOIN_STYLE':0,'MITER_LIMIT':2,'DISSOLVE':False,'OUTPUT':""+ dossier_new +'buffer_loc'+ gare +'.shp'})
    buffer_loc = iface.addVectorLayer(""+ dossier_new +'buffer_loc'+ gare +'.shp', '', 'ogr',)
    #sélectionner le buffer
    buffer_loc.startEditing()
    buffer_loc.selectAll()
    #Utilisateur du plugin "mask"
    from mask import aeag_mask
    aeag_mask.do()
    #symbologie du buffer pour la localisation
    color1 = QtGui.QColor(255, 0, 0, 0)
    color2 = QtGui.QColor('#ffffff')
    symbo = QgsSimpleFillSymbolLayer(color = color1, strokeColor = color2, strokeWidth = 1.26)
    buffer_loc.renderer().symbol().changeSymbolLayer(0, symbo)
    buffer_loc.triggerRepaint()
    buffer_loc.removeSelection()
    
    #symbologie de la vocation
    symbolvoc.setStrokeWidth(0)
    data_geo.renderer().symbol().changeSymbolLayer(0, symbolvoc)
    data_geo.triggerRepaint()
    
    #symbologie du statut
    gare_statut = iface.addVectorLayer(""+ dossier_new +'data_geo'+ gare +'.shp', '','ogr',)
    gare_statut.setName('data_geo_statut')
    symbolstat.setStrokeWidth(0)
    gare_statut.renderer().symbol().changeSymbolLayer(0, symbolstat)
    gare_statut.triggerRepaint()
    
    #Etiquettes des gares: basées sur des règles
    #Configuration des paramètres des étiquettes de la gare principale
    layer_settings1 = QgsPalLayerSettings()
    text_format1 = QgsTextFormat()
    
    text_format1.setFont(QFont("Arial Narrow", 10))
    text_format1.setSize(10)
    
    layer_settings1.placement = 1
    layer_settings1.quadOffset = 2
    layer_settings1.xOffset = 5
    layer_settings1.yOffset = -5
    layer_settings1.enabled = True
    
    background_color1 = QgsTextBackgroundSettings()
    background_color1.setFillColor(QColor('white'))
    background_color1.setStrokeColor(QColor('darkBlue'))
    background_color1.setStrokeWidth(0.2)
    background_color1.setEnabled(True)
    text_format1.setBackground(background_color1)
    layer_settings1.setFormat(text_format1)
    layer_settings1.fieldName = "vrai_nom"
    #Configuration des paramètres des étiquettes des autres gares
    layer_settings2 = QgsPalLayerSettings()
    text_format2 = QgsTextFormat()
    
    text_format2.setFont(QFont("Arial", 7))
    text_format2.setSize(7)
    
    layer_settings2.placement = 0
    layer_settings2.dist = 5
    layer_settings2.enabled = True
    
    background_color2 = QgsTextBackgroundSettings()
    background_color2.setFillColor(QColor('white'))
    background_color2.setEnabled(True)
    text_format2.setBackground(background_color2)
    layer_settings2.setFormat(text_format2)
    layer_settings2.fieldName = "vrai_nom"
    #Création des règles
    root = QgsRuleBasedLabeling.Rule(QgsPalLayerSettings())
    rule1 = QgsRuleBasedLabeling.Rule(layer_settings1)
    rule2 = QgsRuleBasedLabeling.Rule(layer_settings2)
    #Paramètres des règles
    rule1.setFilterExpression("\"Name\" = '{}'".format(gare))
    rule2.setFilterExpression("\"Name\" != '{}'".format(gare))
    root.appendChild(rule1)
    root.appendChild(rule2)
    #Appliquer la configuration des paramètres
    rules = QgsRuleBasedLabeling(root)
    gares_toutes.setLabeling(rules)
    gares_toutes.setLabelsEnabled(True)
    gares_toutes.triggerRepaint()
    #Zoomer sur le buffer
    map_loc = layoutp1.itemById("map_loc")
    map_loc.zoomToExtent(buffer_loc.extent())
    #Assigner les couches à des variables
    gares_toutes_statut = QgsProject.instance().mapLayersByName('gares_statut')[0]
    stations_loc = QgsProject.instance().mapLayersByName('stations_loc')[0]
    reseaux_rapides_loc = QgsProject.instance().mapLayersByName('reseaux_rapides_loc')[0]
    ligne_train = QgsProject.instance().mapLayersByName('portions_train')[0]
    metropole = QgsProject.instance().mapLayersByName('metropole')[0]
    communes = QgsProject.instance().mapLayersByName('COMMUNE')[0]
    bati_autre = QgsProject.instance().mapLayersByName('bati_autre')[0]
    eau = QgsProject.instance().mapLayersByName('eau')[0]
    espace_vert = QgsProject.instance().mapLayersByName('espace_vert')[0]
    esri_gray = QgsProject.instance().mapLayersByName('Esri Gray (light)')[0]
    mask = QgsProject.instance().mapLayersByName('Mask')[0]
    #Choix des couches à afficher dans la carte
    map_loc.setLayers([gare_statut, data_geo, buffer_loc, mask, gares_toutes_statut, gares_toutes, stations_loc, reseaux_rapides_loc, ligne_train, metropole, communes, bati_autre, eau, espace_vert, esri_gray])
    map_loc.storeCurrentLayerStyles()
    iface.mapCanvas().refresh()
    
    #PLANS
    #Extraction du rectangle de la gare
    processing.run("native:extractbyattribute", {'INPUT':""+ dossier_source +'plan_fonctionnel_with_rot.shp','FIELD':'name','OPERATOR':0,'VALUE':''+ gare +'','OUTPUT':""+ dossier_new +'plan_unique'+ gare +'.shp'})
    plan_unique = iface.addVectorLayer(""+ dossier_new +'plan_unique'+ gare +'.shp', '','ogr',)
    #Rendre le rectangle invisible
    plan_unique.setOpacity(0)
    plan_unique.triggerRepaint()
    #zoom sur le plan
    plan = layoutp1.itemById("plan")
    planextent = plan_unique.extent()
    plan.setExtent(planextent)
    #rotation du plan
    for rot in plan_unique.getFeatures():
        rotation = rot[1]
        plan.setMapRotation(rotation)
    #Changer la taille de la carte
    plan.attemptResize(QgsLayoutSize(197, 80, QgsUnitTypes.LayoutMillimeters))
    plan.refresh()
        
    #Assigner les couches à des variables et choisir celles de la carte
    infrastructures = QgsProject.instance().mapLayersByName('infrastructures')[0]
    transportco_plan = QgsProject.instance().mapLayersByName('transportco_plan')[0]
    pieton = QgsProject.instance().mapLayersByName('pieton')[0]
    cyclable = QgsProject.instance().mapLayersByName('cyclable')[0]
    arbres = QgsProject.instance().mapLayersByName('arbres')[0]
    cimetieres = QgsProject.instance().mapLayersByName('cimetieres')[0]
    quais = QgsProject.instance().mapLayersByName('quais')[0]
    parking_plan = QgsProject.instance().mapLayersByName('parking_plan')[0]
    bati_gare_complem = QgsProject.instance().mapLayersByName('bati_gare_complem')[0]
    bati_gare = QgsProject.instance().mapLayersByName('bati_gare')[0]
    train_plan = QgsProject.instance().mapLayersByName('train_plan')[0]
    cartodb = QgsProject.instance().mapLayersByName('CartoDb Positron')[0]
    plan.setLayers([infrastructures, transportco_plan, pieton, cyclable, arbres, cimetieres, quais, parking_plan, bati_gare, bati_gare_complem, bati_autre, train_plan, eau, espace_vert, cartodb])
    plan.storeCurrentLayerStyles()
    iface.mapCanvas().refresh()
    
    #INFOS BLOC 2
    #Extraction de la gare du bloc2
    bloc2 = QgsProject.instance().mapLayersByName('bloc2')[0]
    processing.run("native:extractbyattribute", {'INPUT': bloc2,'FIELD':'gares','OPERATOR':0,'VALUE':''+ gare +'','OUTPUT':""+ dossier_new +'data2'+ gare +'.csv'})
    data2 = iface.addVectorLayer(""+ dossier_new +'data2'+ gare +'.csv', '','ogr',)
    #Assigner les objets de mise en page à des variables et leur assigner les données du bloc2
    freq_jour = layoutp1.itemById('freq_jour')
    freq_annee = layoutp1.itemById('freq_annee')
    freq_semaine_we = layoutp1.itemById('freq_semaine_we')
    quai_nb = layoutp1.itemById('quai_nb')
    quai_len = layoutp1.itemById('quai_len')
    quai_acces = layoutp1.itemById('quai_acces')
    voies = layoutp1.itemById('voies')
    metro_proche = layoutp1.itemById('metro_proche')
    bus_proche = layoutp1.itemById('bus_proche')
    trans_sem_we = layoutp1.itemById('trans_sem_we')
    velo_park = layoutp1.itemById('velo_park')
    car_park = layoutp1.itemById('car_park')
    for row2 in data2.getFeatures():
        freq_j_txt = row2[17]
        freq_a_txt = row2[1]
        freq_jour.setText(""+ freq_j_txt +" voyageurs par jour")
        freq_annee.setText(""+ freq_a_txt +" voyageurs par an (estim.)")
        freq_semtxt = row2[2]
        freq_wetxt = row2[3]
        freq_semaine_we.setText(""+ freq_semtxt +" en semaine et "+ freq_wetxt +" le dimanche")
        quainb_txt = row2[4]
        quai_nb.setText ("" + quainb_txt +"")
        quailen_txt = row2[5]
        quai_len.setText(""+ quailen_txt +"m (2019)")
        quaiaccess_txt = row2[6]
        quai_acces.setText(""+ quaiaccess_txt +" accès")
        voies_txt1 = row2[18]
        voies_txt2 = row2[19]
        voies.setText("" + voies_txt1 +" voies dont "+ voies_txt2 +" à quai")
        metro_txt = row2[14]
        metro_proche.setText("" + metro_txt + "")
        busdist_txt = row2[8]
        busline_txt = row2[15]
        busstop_txt = row2[9]
        bus_proche.setText(""+ busdist_txt +"m - bus "+ busline_txt +" ("+ busstop_txt +")")
        trans_sem_we.setText(""+ row2[10] +" en semaine et "+ row2[11] +" le dimanche")
        velo_txt = row2[12]
        velo_park.setText(""+ velo_txt +" places")
        car_txt = row2[13]
        car_park.setText(""+ car_txt +" places")
    #Exporter la mise en page de la page1
    exporterp1 = QgsLayoutExporter(layoutp1)
    filenamep1 = ""+ dossier_fiches +""+ gare +'_page1.pdf'
    exporterp1.exportToPdf(filenamep1, QgsLayoutExporter.PdfExportSettings())
    
    #PAGE 2
    #Bande du haut
    ordrep2 = layoutp2.itemById('ordrep2')
    nom_garep2 = layoutp2.itemById('nom_garep2')
    for row in data1.getFeatures():
        ordrep2_txt = row[6]
        ordrep2.setText("" + ordrep2_txt + "")
        nom_txtp2 = row[1]
        nom_garep2.setText("" + nom_txtp2.upper() + "")
    #CARTE OCCUPATION
    #symbologie du buffer créé précédemment
    color1 = QtGui.QColor(255, 0, 0, 0)
    color2 = QtGui.QColor(255, 255, 255, 255)
    symbo = QgsSimpleFillSymbolLayer(color = color1, strokeColor = color2, strokeWidth = 1.26)
    buffer_loc.renderer().symbol().changeSymbolLayer(0, symbo)
    buffer_loc.setOpacity(1)
    buffer_loc.triggerRepaint()
    #symbologie du point de la gare principale
    #symbologie du rond au fond
    data_geo_p2 = iface.addVectorLayer(""+ dossier_new +'data_geo'+ gare +'.shp', '','ogr',)
    data_geo_p2.setName('data_geo_svg')
    data_geo_p2.renderer().symbol().setSize(9)
    data_geo_p2.renderer().symbol().setColor(QColor("white"))
    data_geo_p2.triggerRepaint()
    #symbologie du logo SVG devant
    data_geo_svg = iface.addVectorLayer(""+ dossier_new +'data_geo'+ gare +'.shp', '','ogr',)
    data_geo_svg.setName('data_geo_svg2')
    symbolsvg = QgsSvgMarkerSymbolLayer('C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr/svg/transport/transport_train_station2.svg')
    symbolsvg.setSize(7.714280)
    symbolsvg.setFillColor(QColor('#000000'))
    symbolsvg.setStrokeColor(QColor('#ffffff'))
    symbolsvg.setStrokeWidth(0)
    data_geo_svg.renderer().symbol().changeSymbolLayer(0, symbolsvg)
    #zoom sur le buffer
    map_occupation = layoutp2.itemById("map_occupation")
    map_occupation.zoomToExtent(buffer_loc.extent())
    #Assigner les couches à des variables et choisir les couches à afficher
    osm_hot = QgsProject.instance().mapLayersByName('OpenStreetMap H.O.T.')[0]
    train_gen = QgsProject.instance().mapLayersByName('train_gen')[0]
    zone_urba = QgsProject.instance().mapLayersByName('zone_urba')[0]
    parking_gen = QgsProject.instance().mapLayersByName('parking_gen')[0]
    residentiel = QgsProject.instance().mapLayersByName('residentiel_l93')[0]
    commercial = QgsProject.instance().mapLayersByName('commercial_l93')[0]
    logistique = QgsProject.instance().mapLayersByName('logistics_l93')[0]
    loisirs = QgsProject.instance().mapLayersByName('loisirs_l93')[0]
    entreprises = QgsProject.instance().mapLayersByName('entreprises_l93')[0]
    scolaire = QgsProject.instance().mapLayersByName('scolaire_l93')[0]
    map_occupation.setLayers([data_geo_svg, data_geo_p2, buffer_loc, scolaire, residentiel, entreprises, loisirs, logistique, commercial, parking_gen, zone_urba, train_gen, osm_hot])
    map_occupation.storeCurrentLayerStyles()
    iface.mapCanvas().refresh()
    
    #BLOC 3
    #Extraction des données, assignation à des variables et assignation des données du bloc3
    bloc3 = QgsProject.instance().mapLayersByName('bloc3')[0]
    processing.run("native:extractbyattribute", {'INPUT': bloc3,'FIELD':'gares','OPERATOR':0,'VALUE':''+ gare +'','OUTPUT':""+ dossier_new +'data3'+ gare +'.csv'})
    data3 = iface.addVectorLayer(""+ dossier_new +'data3'+ gare +'.csv', '','ogr',)
    hab2 = layoutp2.itemById('hab2')
    hab5 = layoutp2.itemById('hab5')
    emploi2 = layoutp2.itemById('emploi2')
    emploi5 = layoutp2.itemById('emploi5')
    zu2 = layoutp2.itemById('zu2')
    zu5 = layoutp2.itemById('zu5')
    for row3 in data3.getFeatures():
        hab2_txt = row3[1]
        hab5_txt = row3[2]
        hab2.setText("" + hab2_txt + "")
        hab5.setText("" + hab5_txt + "")
        emploi2_txt = row3[3]
        emploi2.setText("" + emploi2_txt + "")
        emploi5_txt = row3[4]
        emploi5.setText("" + emploi5_txt + "")
        zu2_txt = row3[7]
        zu2.setText(""+ zu2_txt +" ha")
        zu5_txt = row3[8]
        zu5.setText(""+ zu5_txt +" ha")
    #MAP ACCES
    #Definition des couches en commun
    train_acces = QgsProject.instance().mapLayersByName('train_acc')[0]
    bus_entier = QgsProject.instance().mapLayersByName('bus_acces')[0]
    reseaux_rapides_acces = QgsProject.instance().mapLayersByName('reseaux_rapides_acces')[0]
    transportco_acc = QgsProject.instance().mapLayersByName('transportco_acces')[0]
    autopartage = QgsProject.instance().mapLayersByName('stations-d-auto-partage')[0]
    lineos = QgsProject.instance().mapLayersByName('lineos')[0]
    #CARTE MODES ACTIFS
    #Extraction du graphe vélo de la gare
    velo = QgsProject.instance().mapLayersByName('velo_lines')[0]
    processing.run("native:extractbyattribute", {'INPUT': velo,'FIELD':'Name','OPERATOR':0,'VALUE':''+ gare +'','OUTPUT':""+ dossier_new +'velo_solo'+ gare +'.shp'})
    velo_solo = iface.addVectorLayer(""+ dossier_new +'velo_solo'+ gare +'.shp', '','ogr',)
    #Remplissage simple
    color3 = QColor(168, 105, 168, 255)
    symbo_velo = QgsSimpleLineSymbolLayer()
    symbo_velo.setColor(color3)
    symbo_velo.setWidth(0.35)
    velo_solo.renderer().symbol().changeSymbolLayer(0, symbo_velo)
    velo_solo.triggerRepaint()
    #Extraction du graphe piéton de la gare
    pieton = QgsProject.instance().mapLayersByName('pieton_lines')[0]
    processing.run("native:extractbyattribute", {'INPUT': pieton,'FIELD':'Name','OPERATOR':0,'VALUE':''+ gare +'','OUTPUT':""+ dossier_new +'pieton_solo'+ gare +'.shp'})
    pieton_solo = iface.addVectorLayer(""+ dossier_new +'pieton_solo'+ gare +'.shp', '','ogr',)
    color4 = QColor(0, 216, 202, 255)
    symbo_pieton = QgsSimpleLineSymbolLayer()
    symbo_pieton.setColor(color4)
    symbo_pieton.setWidth(0.35)
    pieton_solo.renderer().symbol().changeSymbolLayer(0, symbo_pieton)
    pieton_solo.triggerRepaint()
    #Zoom sur le graphe vélo (le plus large)
    map_acces2 = layoutp2.itemById("map_acces2")
    map_acces2.zoomToExtent(velo_solo.extent())
    #Choix des couches à afficher
    map_acces2.setLayers([data_geo_svg, data_geo_p2, reseaux_rapides_acces, train_acces, pieton_solo, velo_solo, osm_hot])
    map_acces2.storeCurrentLayerStyles()
    iface.mapCanvas().refresh()
    #MAP TRANSPORTCO
    #Extraction du graphe voiture de la gare
    voiture = QgsProject.instance().mapLayersByName('voiture_lines')[0]
    processing.run("native:extractbyattribute", {'INPUT': voiture,'FIELD':'Name','OPERATOR':0,'VALUE':''+ gare +'','OUTPUT':""+ dossier_new +'voiture_solo'+ gare +'.shp'})
    voiture_solo = iface.addVectorLayer(""+ dossier_new +'voiture_solo'+ gare +'.shp', '','ogr',)
    color5 = QColor(82, 82, 82, 255)
    symbo_voit = QgsSimpleLineSymbolLayer()
    symbo_voit.setColor(color5)
    symbo_voit.setWidth(0.35)
    voiture_solo.renderer().symbol().changeSymbolLayer(0, symbo_voit)
    voiture_solo.triggerRepaint()
    #Zoom sur le graphe voiture
    map_acces5 = layoutp2.itemById("map_acces5")
    map_acces5.zoomToExtent(voiture_solo.extent())
    #Choix des couches à afficher
    map_acces5.setLayers([data_geo_svg, data_geo_p2, autopartage, transportco_acc, lineos, reseaux_rapides_acces, bus_entier, train_acces, voiture_solo, osm_hot])
    map_acces5.storeCurrentLayerStyles()
    iface.mapCanvas().refresh()
    #Exporter la page 2
    exporterp2 = QgsLayoutExporter(layoutp2)
    filenamep2 = ""+ dossier_fiches +""+ gare +'_page2.pdf'
    exporterp2.exportToPdf(filenamep2, QgsLayoutExporter.PdfExportSettings())

#Génération des boites de dialogues
mb = QMessageBox()
mb.setText('Le projet est-il installé ?')
#Définition des réponses
mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
return_value = mb.exec()
#Conséquence des réponses
if return_value == QMessageBox.Yes:
    print('Etape suivante')
    mb.setText('Avez-vous chargé les mises en page ?')
    mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    return_valuemep = mb.exec()
    if return_valuemep == QMessageBox.Yes:
        print('Etape suivante')
        mb.setText('Voulez vous générer toutes les fiches ?')
        mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return_value2 = mb.exec()
        gares_toutes = QgsProject.instance().mapLayersByName('gares_voc')[0]
        if return_value2 == QMessageBox.No:
            input_unique = QInputDialog.getText(None, "Nom de la gare" ,"Indiquez le nom de la gare souhaitée :")
            if input_unique[1]:
                gare = input_unique[0]
                generation_ficheV2()
                print(''+ gare +' prête !')
            else:
                print('échec')
        elif return_value2 == QMessageBox.Yes:
            for row0 in gares_toutes.getFeatures():
                gare = row0[0]
                generation_ficheV2()
                print(''+ gare +' prête !')
            print('Toutes les fiches ont été générées')
    else:
        print('Veuillez charger les mises en page dans QGIS.')
elif return_value == QMessageBox.No:
    print('Installation du projet en cours...')
    installation_projet()
    print('Installation terminée ! Supprimez les doublons, ajoutez les mises en page, et relancez le programme.')
