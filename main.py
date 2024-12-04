"""suite de syracuse"""


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = [n]
    while n > 1:
        if n%2 != 0:
            n = n*3+1
        else:
            n = n//2
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    return len(l)

    n = 0
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    n0 = l[0]
    count = 0
    for value in l:
        if value >= n0:
            count += 1
        else:
            break
    return count


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    return max(l)


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    n_values = [3, 4, 5, 6, 15]
    for n in n_values:
        lsyr = syracuse_l(n)
        print(f"Suite de Syracuse pour n = {n} : {lsyr}")
        print(f"Temps de vol pour n = {n} : {temps_de_vol(lsyr)}")
        print(f"Temps de vol en altitude pour n = {n} : {temps_de_vol_en_altitude(lsyr)}")
        print(f"Altitude maximale pour n = {n} : {altitude_maximale(lsyr)}")
        print("-" * 50)

if __name__ == "__main__":
    main()