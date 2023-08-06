Intro
=====

A library of functions (just one at the moment) to streamline the saving
and exporting of matplotlib plots as images and whatnot.

I wrote it because I was spending a lot of time creating and saving
plots in another project of mine and wanted to automate it.

Usage
=====

::

    from matplotsave import pltsave

    xs = list(range(10))
    ys = [i**2 for i in xs]
    with pltsave("myplot.png") as (fig,ax):
        ax.plot(xs,ys)

This will export the plot to ``myplot.png`` painlessly after you are
given the chance to actually plot some data.

Because the ``pltsave`` context manager returns the fig and ax objects
the entire matplotlib api si still accessible.
