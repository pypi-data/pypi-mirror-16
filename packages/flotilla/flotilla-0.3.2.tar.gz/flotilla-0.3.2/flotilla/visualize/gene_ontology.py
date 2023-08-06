"""

"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


MACHINE_EPSILON = np.finfo(float).eps


def plot_go_enrichment(x_col='bonferonni_corrected_negative_log_p_value',
                       data=None, ax=None, max_categories=10,
                       yticklabels='go_name',
                       **kwargs):
    data = data.sort_values(x_col, ascending=False)
    if data.shape[0] > max_categories:
        data = data.iloc[:max_categories, :]
    if ax is None:
        ax = plt.gca()

    bottom = np.arange(data.shape[0])
    width = data[x_col]
    # width = -np.log10(data[x_col])
    ax.barh(bottom, width, **kwargs)
    ax.set(yticks=bottom + 0.4, yticklabels=data[yticklabels],
           xlabel='$-\log_{10}(q)$', ylim=(0, bottom.max() + 1))
    sns.despine()
    return ax
