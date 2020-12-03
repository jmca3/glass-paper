[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4304619.svg)](https://doi.org/10.5281/zenodo.4304619)

# Installation

Using Anaconda and pipenv, create an environment with the required packages:

```shell
$ pipenv install
```

The last successfully used package versions are listed in
[requirements.txt](requirements.txt).

Enable the Sankey widget:

```shell
$ pipenv shell
$ jupyter nbextension enable --py --sys-prefix ipysankeywidget
```

Run the Jupyter notebook server:

```shell
$ pipenv run jupyter notebook
```