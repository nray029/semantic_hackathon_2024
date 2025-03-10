import numpy as np
import matplotlib
import matplotlib as mpl	
import matplotlib.pyplot as plt



vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

def heatmap(data, row_labels, col_labels, ax=None, cbar_kw=None, cbarlabel="", **kwargs):
	"""
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data=A 2D numpy array of shape (M, N).
    row_labels=A list or array of length M with the labels for the rows.
    col_labels=A list or array of length N with the labels for the columns.
    ax=A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If not provided, use current axes or create a new one.  Optional.
    cbar_kw=A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel=The label for the colorbar.  Optional.
    **kwargs=All other arguments are forwarded to `imshow`.
	"""

	if ax is None:
		ax = plt.gca()

	if cbar_kw is None:
		cbar_kw = {}

    # Plot the heatmap
	im = ax.imshow(data, **kwargs)

    # Create colorbar
	cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
	cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom", )
	cbar.remove()
	#cbar.remove()
    # Show all ticks and label them with the respective list entries.
	ax.set_xticks(np.arange(data.shape[1]))
	ax.set_yticks(np.arange(data.shape[0]))
	ax.set_xticklabels(col_labels, size=10)
	ax.set_yticklabels(row_labels, size=10)
	
    # Let the horizontal axes labeling appear on top.
	ax.tick_params(top=True, bottom=False,
                   labeltop=False, labelbottom=True)

    # Rotate the tick labels and set their alignment.
	plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Turn spines off and create white grid.
	

	ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
	ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
	#ax.grid(which="minor", color="w", linestyle='-', linewidth=2)
	ax.tick_params(which="minor", bottom=False, left=False)

	return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",textcolors=("black", "white"), threshold=None, **textkw):
	"""
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
	"""

	if not isinstance(data, (list, np.ndarray)):
		data = im.get_array()

    # Normalize the threshold to the images color range.
	if threshold is not None:
		threshold = im.norm(threshold)
	else:
		threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
	kw = dict(horizontalalignment="center", verticalalignment="center")
	kw.update(textkw)

    # Get the formatter in case a string is supplied
	if isinstance(valfmt, str):
		valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
	texts = []
	for i in range(data.shape[0]):
		for j in range(data.shape[1]):
			kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
			text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
			texts.append(text)

	return texts


def plot_heatmap(a,b,c,y,z,x):
	fig, ax = plt.subplots()
	#mask =1- np.tri(a.shape[0], k=0)
		#a = np.array(a)
	print(a)
	#a=np.transpose(a)
	im, cbar = heatmap(a, b, c, ax=ax, cmap=y)
	texts = annotate_heatmap(im,valfmt="{x:.0f}", size=6)
	ax.set_title(x)
	ax.set_aspect(aspect=0.8)
	fig.tight_layout()
	plt.show()
	
#plot_heatmap(harvest, vegetables, farmers, "Wistia", "Harvest whole year")
