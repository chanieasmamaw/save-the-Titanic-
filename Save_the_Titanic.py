

############Saving the Titanic, Miracle behind the shipp                                                              ##########################
############ Since may 2024, SOFTWARE ENGINEER:BERLIN: chanieasmamaw@yahoo.com or yehunchanie@gmail.com
############ Completerd PhD in atmospheric phsycis in 2021 and MS.c in satellite geodesy 2013
############  Emoji+4915566400997, +4917626315666
########### Current address: Mülheim am Main, Germany
def auto_pilot_next_step(titanic_row,titanic_col,ocean_size):
    occean_size=10
    if titanic_col == 0:
        return "WEST"
    if get_cell(titanic_row, titanic_col -1)== "🧊" :
        if titanic_row == occean_size -1:
            return "NORTH"
        return "SOUTH"
    return "WEST"


##########################################################################################################
