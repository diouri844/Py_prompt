import math

def get_somme(tab):
    somme = 0
    try:
        for itr in tab:
            somme += float(itr)
        return somme
    except Exception as e:
        return e

def get_somme_limited(tab):
    tab = tab.split(':')
    if int(tab[1])>int(tab[0]):
        item = float(tab[0])
        somme = 0
        limite = float(tab[1])
        while item <= limite:
            somme += item
            item += 1
        return somme
    return -1

def get_soustract(tab):
    for i in range(len(tab)):
        tab[i] = float(tab[i])
    return max(tab)-min(tab)

def get_somme_tab(tab_1,tab_2):
    if len(tab_1)==len(tab_2):
        resultat = []
        try:
            for i in range(len(tab_1)):
                resultat.append(float(tab_1[i])+float(tab_2[i]))
            return resultat
        except Exception as e:
            return e

def get_soustract_tab(tab_1,tab_2):
    if len(tab_1)==len(tab_2):
        resultat = []
        try:
            for i in range(len(tab_1)):
                resultat.append(
                    max(float(tab_1[i]),float(tab_2[i]))-min(float(tab_1[i]),float(tab_2[i]))
                )
            return resultat
        except Exception as e:
            return e

def get_soustract_tab_to_int(tab,element):
    try:
        element = float(element)
        for itr in range(len(tab)):
            tab[itr] = max(float(tab[itr]),element)-min(float(tab[itr]),element)
        return tab
    except Exception as e:
        return e

def get_somme_tab_to_int(tab,element):
    try:
        element = float(element)
        for itr in range(len(tab)):
            tab[itr] = float(tab[itr])+element
        return tab
    except Exception as e:
        return e

def get_division_simple(ele1,ele2):
    try:
        ele1 = float(ele1)
        ele2 = float(ele2)
        return ele1/ele2
    except Exception as e:
        return e

def get_division_tab(tab_1,tab_2):
    if len(tab_1)==len(tab_2):
        resultat = []
        try:
            for itr in range(len(tab_1)):
                resultat.append(
                   float(tab_1[itr])/float(tab_2[itr]) 
                )
            return resultat
        except Exception as e:
            return e

def get_division_tab_to_element(tab,element):
    try:
        element = float(element)
        for itr in range(len(tab)):
            tab[itr] = float(tab[itr])/element
        return tab
    except Exception as e:
        return e

def get_multiplication_tab(tab1,tab2):
    if len(tab1)==len(tab2):
        resultat = []
        try:
            for itr in range(len(tab1)):
                resultat.append(
                    float(tab1[itr])*float(tab2[itr])
                )
            return resultat
        except Exception as e:
            return e

def get_multiplication_tab_to_element(tab,element):
    try:
        element = float(element)
        for itr in range(len(tab)):
            tab[itr] = float(tab[itr])*element
        return tab
    except Exception as e:
        return e

def get_multiplication(e1,e2):
    try:
        return float(e1)*float(e2)
    except Exception as e:
        return e

def get_power_tab(tab1,tab2):
    if len(tab1)==len(tab2):
        resultat = []
        try:
            for itr in range(len(tab1)):
                resultat.append(
                    math.pow(float(tab1[itr]),float(tab2[itr]))
                )
            return resultat
        except Exception as e:
            return e

def get_power_tab_item(tab,element):
    try:
        element = float(element)
        for itr in range(len(tab)):
            tab[itr] = math.pow(float(tab[itr]), element)
        return tab
    except Exception as e:
        return e

def get_power(e1,e2):
    try:
        return math.pow(float(e1), float(e2))
    except Exception as e:
        return e

def get_dividers(element):
    try:
        resultat = []
        limit = int(element)
        element = int(element)
        for contour in range(1,limit+1):
            if element%contour==0:
                resultat.append(contour)
        return resultat
    except Exception as e:
        return e

def get_dividers_tab(tab):
    try:
        resultat = []
        for itr in range(len(tab)):
            r = get_dividers(tab[itr])
            resultat.append(r)
        return resultat
    except Exception as e:
        return e

def get_dividers_tab_limited(tab):
    try:
        contour = int(tab[0])
        limite = int(tab[2])
        resultat = []
        for itr in range(contour,limite+1):
            r = get_dividers(itr)
            resultat.append(r)
        return resultat
    except Exception as e:
        return e

def get_max(tab):
    for i in range(len(tab)):
        tab[i]= int(tab[i])
    return max(tab)

def get_min(tab):
    for i in range(len(tab)):
        tab[i]= int(tab[i])
    return min(tab)