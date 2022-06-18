from ast import Break
from Module.Calcule import *
from Module.Syntaxe import *
from Module.Show import *
import os

################################## Globals Outils ####################################
global liste_command_de_base
global resultats
global liste_operation_get
global liste_operation_show
global historique
global names
global values
######################################################################################
resultats = []

historique = []

names = []

values = []

liste_command_de_base = [
    'Get-Calc',
    'Show',
    'Set',
    'ValueOf',
    'Exit',
    'Clear'
    ]

liste_operation_get = [
    'Somme',
    'Sustract',
    'Max',
    'Min',
    'Division',
    'Multiplication',
    'Power',
    'Dividers'
    ]

liste_operation_show = ['Historique','Resultats']
########################################################################################

def protocol_get(tab_args):
    if tab_args[1] in liste_operation_get:
        if tab_args[1] == 'Somme':
            if not is_tabel(tab_args[2]):
                try:
                    resultat = get_somme(tab_args[2:])
                except Exception as e:
                    resultat = get_somme(tab_args[3:])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
            if is_tabel(tab_args[2]):
                if tab_args[2].find(":")!=-1:
                    tab_args[2] = clean_tabel(tab_args[2])
                    resultat = get_somme_limited(tab_args[2])
                    resultats.append(resultat)
                    print(">> "+str(resultat))
                    return
                #####################################
                else:
                    tab_args[2] = clean_tabel(tab_args[2])
                    if is_tabel(tab_args[3]):
                        tab_args[3] = clean_tabel(tab_args[3])
                        tab_1 = tab_args[2].split(',')
                        tab_2 = tab_args[3].split(',')
                        resultat = get_somme_tab(tab_1,tab_2)
                        resultats.append(resultat)
                        print(">> "+str(resultat))
                        return
                    else:
                        tab_1 = tab_args[2].split(',')
                        resultat = get_somme_tab_to_int(tab_1, tab_args[3])
                        resultats.append(resultat)
                        print(">> "+str(resultat))
                        return
        if tab_args[1] == 'Sustract':
            if len(tab_args)==4:
                if is_tabel(tab_args[2]):
                    tab_args[2] = clean_tabel(tab_args[2])
                    tab_1 = tab_args[2].split(',')
                    if is_tabel(tab_args[3]):
                        #soustract 2 tab :
                        tab_args[3] = clean_tabel(tab_args[3])
                        tab_2 = tab_args[3].split(',')
                        resultat = get_soustract_tab(tab_1,tab_2)
                        print(">> "+str(resultat))
                        resultats.append(resultat)
                        return
                    if not is_tabel(tab_args[3]):
                        #soustract element from all tab items:
                        resultat = get_soustract_tab_to_int(tab_1,tab_args[3])
                        resultats.append(resultat)
                        print(">> "+str(resultat))
                        return
                else:
                    #soustract too items:
                    tab_args = tab_args[2:]
                    resultat = get_soustract(tab_args)
                    resultats.append(resultat)
                    print(">> "+str(resultat))
                    return
        if tab_args[1] == 'Max':
            if not is_tabel(tab_args[2]) and len(tab_args)>=3:
                resultat = get_max(tab_args[2:])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
        if tab_args[1] == 'Min':
            if not is_tabel(tab_args[2]) and len(tab_args)>=3:
                resultat = get_min(tab_args[2:])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
        if tab_args[1] == 'Division':
            if not is_tabel(tab_args[2]) and not is_tabel(tab_args[3]):
                #division 2 items:
                resultat = get_division_simple(tab_args[2],tab_args[3])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
            if is_tabel(tab_args[2]) and is_tabel(tab_args[3]):
                #division 2 tab :
                tab_args[2] = clean_tabel(tab_args[2])
                tab_args[3] = clean_tabel(tab_args[3])
                tab_1 = tab_args[2].split(',')
                tab_2 = tab_args[3].split(',')
                resultat = get_division_tab(tab_1,tab_2)
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
            if is_tabel(tab_args[2]) and not is_tabel(tab_args[3]):
                #division tab by element:
                tab_args[2] = clean_tabel(tab_args[2])
                tab_1 = tab_args[2].split(',')
                resultat = get_division_tab_to_element(tab_1,tab_args[3])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
        if tab_args[1] == 'Multiplication':
            if is_tabel(tab_args[2]) and is_tabel(tab_args[3]):
                #Multiplication 2 tab:
                tab_args[2] = clean_tabel(tab_args[2])
                tab_args[3] = clean_tabel(tab_args[3])
                tab_1 = tab_args[2].split(',')
                tab_2 = tab_args[3].split(',')
                resultat = get_multiplication_tab(tab_1,tab_2)
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
            if is_tabel(tab_args[2]) and not is_tabel(tab_args[3]):
                #Mulstiplication tab by item:
                tab_args[2] = clean_tabel(tab_args[2])
                tab_1 = tab_args[2].split(',')
                resultat = get_multiplication_tab_to_element(tab_1,tab_args[3])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
            if not is_tabel(tab_args[2]) and not is_tabel(tab_args[3]):
                #Multiplication 2 item :
                resultat = get_multiplication(tab_args[2],tab_args[3])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
        if tab_args[1]=='Power':
            if is_tabel(tab_args[2]) and is_tabel(tab_args[3]):
                # tab1[itr]^tab2[itr]:
                tab_args[2] = clean_tabel(tab_args[2])
                tab_args[3] = clean_tabel(tab_args[3])
                tab_1 = tab_args[2].split(',')
                tab_2 = tab_args[3].split(',')
                resultat = get_power_tab(tab_1,tab_2)
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
            if is_tabel(tab_args[2]) and not is_tabel(tab_args[3]):
                #tab[itr]^element for itr in range elements :
                tab_args[2] = clean_tabel(tab_args[2])
                tab_1 = tab_args[2].split(',')
                resultat = get_power_tab_item(tab_1,tab_args[3])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
            if not is_tabel(tab_args[2]) and not is_tabel(tab_args[3]):
                # element^element:
                resultat = get_power(tab_args[2],tab_args[3])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
        if tab_args[1] == 'Dividers':
            if not is_tabel(tab_args[2]):
                # get Dividers liste of one element :
                resultat = get_dividers(tab_args[2])
                resultats.append(resultat)
                print(">> "+str(resultat))
                return
            if is_tabel(tab_args[2]):
                if tab_args[2].find(":")!=-1:
                    # is atable limited :
                    tab_args[2] = clean_tabel(tab_args[2])
                    resultat = get_dividers_tab_limited(tab_args[2])
                    resultats.append(resultat)
                    print(">> "+str(resultat))
                    return
                else:
                    # get Dividers liste of liste element :
                    tab_args[2] = clean_tabel(tab_args[2])
                    tab = tab_args[2].split(',')
                    resultat = get_dividers_tab(tab)
                    resultats.append(resultat)
                    print(">> "+str(resultat))
                    return
    return

def protocol_show(tab_args):
    if tab_args[1] in liste_operation_show:
        if tab_args[1] == 'Historique':
            if len(tab_args)>=3:
                # show historique with option
                option = ['-All','-Last','-Ferst','-Index']
                if tab_args[2] in option[:-1]:
                    show_historique(historique,option.index(tab_args[2]))
                if tab_args[2] == '-Index':
                    show_historique_by_index(historique,int(tab_args[3]))
        if tab_args[1] == 'Resultats':
            if len(tab_args)>=3:
                # show resultat with option
                option = ['-All','-Ferst']
                if tab_args[2] in option:
                    show_resultats_by_index(resultats,option.index(tab_args[2]))
            else:
                #show last resultat :
                show_resultats_by_index(resultats,-1)
    return

def protocolo_set(tab_args):
    # tab args[1] is var name :
    name = tab_args[1]
    if not name in names:
        names.append(name)
        # cleaning the tab args :
        tab_args = tab_args[2:]
        # recall get_syntaxe :
        command = ' '.join(tab_args)
        if get_syntaxe(command)==1:
            values.append(resultats[-1])
        return
    if name in names:
        # cleaning the tab args :
        tab_args = tab_args[2:]
        # recall get_syntaxe :
        command = ' '.join(tab_args)
        if get_syntaxe(command)==1:
            values[names.index(name)] = resultats[-1]
        return

def ValueOf(var_name):
    if var_name in names:
        resultat = values[names.index(var_name)]
        resultats.append(resultat)
        print(">> "+str(resultat))
    return

def get_syntaxe(command):
    command = command.split(' ')
    if command[0] in liste_command_de_base:
        if command[0] == 'ValueOf':
            ValueOf(command[1])
            return 1
        if command[0] == 'Get-Calc':
            protocol_get(command)
            return 1
        if command[0] == 'Exit':
            return -1
        if command[0] == 'Show':
            protocol_show(command)
            return 1
        if command[0] == 'Set':
            protocolo_set(command)
            return 1
        if command[0] == 'Clear':
            os.system("clear")
            return 1
    #========== Var ============
    if not command[0] in liste_command_de_base:
        if len(command)==2:
            #declarin a variable :
            if not is_in_name(names, command[0]):
                #var name :
                names.append(command[0])
                #var value :
                values.append(command[1])
            else :
                update_var(names,values,command[0],command[1])
        if len(command)==1:
            #showing a variable :
            resultat = show_variables(names,values,command[0])
            resultats.append(resultat)
            print(">> "+str(resultat))
    if len(command)==0 :
        return -1


#########################################################################################


if __name__ == '__main__':
    condition = True
    while condition==True:
        current_command = input()
        historique.append(current_command)
        protocol = get_syntaxe(current_command)
        if protocol == -1:
            condition = False
