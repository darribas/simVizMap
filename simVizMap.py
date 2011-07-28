import pylab as pl
import numpy as np
import scipy

class SimVizMap:
    '''
    Spatial visualization of simulation results as presented in Arribas-Bel,
    Koschinsky & Amaral (2011) [1]_
    ...

    Parameters
    ----------

    Attributes
    ----------

    Methods
    -------

    References
    ----------

    .. [1] Arribas-Bel, D., Koschinsky, J., Amaral, P. V. (2011) "Improving the
        Multi-Dimensional Comparison of Simulation Results: A Spatial
        Visualization Approach"
    '''
    def __init__(self, csv_link, cmap='Blues', cb_orientation='horizontal'):
        x, rows, cols = self._csv2m(csv_link)
        n, k = x.shape

        y = self._align_array(x)
        p = pl.subplot(111)
        fill = pl.pcolor(y, cmap=cmap)
        if cb_orientation:
            sep = (np.max(y) - np.min(y))/4.
            ran = np.arange(np.min(y), np.max(y) + sep, sep)
            c = pl.colorbar(fill, ticks=ran, format='%0.3f', \
                     orientation=cb_orientation)
        self._addlines(n, k, rows, cols)

        pl.xticks([], [])
        pl.yticks([], [])
        p.set_xlim(xmax=x.shape[1])
        p.set_ylim(ymax=x.shape[0])

        self.x = x
        self.p = p

    def _csv2m(self, csv_link):
        '''
        Import the csv as an array, clipping out strings for bars
        ...

        Arguments
        ---------
        csv_link        : str
                          Path to csv file to be converted into a map

        Returns
        -------
        m               : array
                          Array of floats to be plotted as map
        rows            : list
                          List of tuples (row, color) to locate horizontal bars
        cols            : list
                          List of tuples (col, color) to locate vertical bars    
        '''
        csv = [line.strip('\n').strip('\r').split(',') for line in open(csv_link).readlines()]
        a = np.array(csv)
        rows, cols = [], []
        for i, row in enumerate(a):
            color =  [row[0], row[-1]]
            if 'w' in color or 'b' in color:
                rows.append((i, color[0]))
        for i, col in enumerate(a.T):
            color =  [col[0], col[-1]]
            if 'w' in color or 'b' in color:
                cols.append((i, color[0]))
        m = scipy.delete(a, [i[0] for i in rows], 0)
        m = scipy.delete(m, [i[0] for i in cols], 1)
        return np.array(m, dtype=float), rows, cols

    def _align_array(self, x):
        '''
        Modify the array to display properly in Matplotlib's 'pcolor'
        ...
        
        Arguments
        ---------
        x       : array
                 Input array
        Attributes
        ----------
        y       : array
                  Modified array in which columns have been reversed
        '''
        y = np.zeros(x.shape)
        for i in np.arange(y.shape[1]):
            y[:, i] = x[:, i][:: -1]
        return y

    def _addlines(self, n, k, rows, cols):
        '''
        Adds thin and thick lines to the plot
        '''
        #Thin v. lines
        for i in range(1, k):
            pl.axvline(i, linewidth=0.25, ls='-', color='k')
        #Thin h. lines
        for i in range(1, n):
            pl.axhline(i, linewidth=0.25, ls='-', color='k')
        #Thick h. lines
        for o, i in enumerate(cols):
            if i[1] == 'b':
                lw = 2
                color = 'k'
            elif i[1] == 'w':
                lw = 4
                color = 'w'
            else:
                print "\n\n\tMake sure the color cells in your csv have either 'b' or 'w'\n\n"
            pl.axvline(i[0]-o, linewidth=lw, ls='-', color=color)
        #Thick v. line
        for o, i in enumerate(rows):
            if i[1] == 'b':
                lw = 2
                color = 'k'
            elif i[1] == 'w':
                lw = 4
                color = 'w'
            else:
                print "\n\n\tMake sure the color cells in your csv have either 'b' or 'w'\n\n"
            pl.axhline(i[0]-o, linewidth=lw, ls='-', color=color)
        return 'Lines added'

    def show(self):
        pl.show()

    def save(self, png_link):
        pl.savefig(png_link)

def set_h_tags(y, tags, subplot, fontsize=15, rotation=0, weight=None,
        verticalalignment='center', horizontalalignment='center'):
    '''
    Set horizontal tags
    ...

    Arguments
    ---------
    y           : float
                  Horizontal axis along which tags will be plotted
    tags        : list
                  List of strings to be plotted
    subplot     : subplot
                  Pylab subplot object
    ...         : other text parameters
    '''
    n = len(tags)
    sep = 1. / (2*n)
    for i, tag in zip(range(n), tags):
        x = float(i)/n + sep
        pl.text(x, y, tag, transform=subplot.transAxes,
                fontsize=fontsize, weight=weight, rotation=rotation,
                verticalalignment=verticalalignment,
                horizontalalignment=horizontalalignment)
    return 'ph'

def set_v_tags(x, tags, subplot, fontsize=15, rotation=0, weight=None,
        verticalalignment='center', horizontalalignment='center'):
    '''
    Set vertical tags
    ...

    Arguments
    ---------
    y           : float
                  Vertical axis along which tags will be plotted
    tags        : list
                  List of strings to be plotted
    subplot     : subplot
                  Pylab subplot object
    ...         : other text parameters
    '''
    n = len(tags)
    sep = 1. / (2*n)
    for i, tag in zip(range(n), tags):
        y = float(i)/n + sep
        pl.text(x, y, tag, transform=subplot.transAxes,
                fontsize=fontsize, weight=weight, rotation=rotation,
                verticalalignment=verticalalignment,
                horizontalalignment=horizontalalignment)
    return 'ph'

if __name__ == '__main__':
    link = 'rejRate_anselinRey.csv'
    p = SimVizMap(link, cb_orientation=None)
    #p.save('/Users/dani/Desktop/test.png')
    p.show()

