def show_historique(tab,option):
    if option==0:
        for elment in tab:
            print("<->"+str(elment))
        return
    if option==1:
        print("<->"+str(tab[-2]))
        return
    if option==2:
        print("<->"+str(tab[0]))
        return

def show_historique_by_index(tab,index):
    try:
        print("<->"+str(tab[index]))
    except Exception as e:
        print("<->"+str(e))
    return

def show_resultats_by_index(tab, index):
    if index == -1:
        print("<->"+str(tab[-1]))
    if index == 0:
        for element in tab:
            print("<->"+str(element))
    if index == 1:
        print("<->"+str(tab[0]))
    return

def show_variables(name,value,element):
    for row in name:
        if element==row:
            return value[name.index(element)]

def is_in_name(name,element):
    return element in name

def update_var(name,value,el_name,ele_val):
    for item in name:
        if item == el_name:
            value[name.index(item)]=ele_val
    return