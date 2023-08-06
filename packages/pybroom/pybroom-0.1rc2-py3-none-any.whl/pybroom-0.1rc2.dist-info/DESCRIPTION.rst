
pybroom
=======

**Pybroom** is a small python 3 library for converting fitting results
(curve fitting or other optimizations)
to `Pandas <http://pandas.pydata.org/>`__
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe>`__
in tidy format
`(Wickham 2014) <http://dx.doi.org/10.18637/jss.v059.i10>`__.
The DataFrames in tidy format (or long-form) follow a simple rule:
one "observation" per row and one "variable" per column.
This simple structure makes it easy to process the data with clear and
well-understood idioms (for filtering, aggregation, etc.) and allows
plot libraries to automatically generate complex plots in which many
variables are compared. Plotting libraries supporting tidy DataFrames
include `seaborn <https://web.stanford.edu/~mwaskom/software/seaborn/>`__,
recent versions of `matplotlib <http://matplotlib.org/>`__,
`bokeh <http://bokeh.pydata.org/>`__ and
`altair <https://github.com/ellisonbg/altair>`__.
pybroom development was inspired by the R library
`broom <https://github.com/dgrtwo/broom>`__.
See `this video <https://www.youtube.com/watch?v=eM3Ha0kTAz4>`__
for details of the philosophy behind broom and pybroom.

See the `pybroom homepage<http://pybroom.readthedocs.io/>`__ for more info.


