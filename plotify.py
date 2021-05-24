"""
My standard plot adjustments to make things look nice.
Suited for simple plots, e.g., an online blog/article
rather than for scientific publication.
"""
def hide_spines(axlist = None,
                add_grid = True):
    """
    Hides the top and rightmost axis spines from view
    Args:
        axlist : List of axes objects to adjust
        add_grid : Boolean value to add horizontal grid lines
    """

    try:
        iter(axlist)
    except TypeError as e:
        axlist = list(axlist)

    for ax in axlist:
        # Disable spines.
        ax.spines['right'].set_color('none')
        ax.spines['left'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_color('xkcd:grey')
        # Disable ticks.
        ax.xaxis.set_ticks_position('bottom')
        if add_grid == True:
            ax.grid(b = True, 
                    axis = 'y',
                    color = 'xkcd:grey',
                    linestyle =  '-',
                    linewidth =  0.5,
                    alpha     =  0.4,
                    )
            ax.tick_params(axis = 'y',
                            length = 0.0)


def add_data_source(ax = None,
                    text = None,
                    x = 0.95,
                    y = 0.9,
                    ha = 'right'):

    text = 'Data source: ' + text

    ax.text(x, y,
            text,
            transform=ax.transAxes,
            fontsize = 7,
            alpha = 0.6,
            ha = ha,
            zorder = 1000)

def colours():
    plot_colours = [
                'lightsteelblue',
                'slategrey',
                'lightcoral',
                'black',
                'gold',
                'crimson',
                'dodgerblue',
                'darkorange',
                'tab:brown',
                'tab:olive',
                'tab:cyan'
                ]
    return plot_colours
