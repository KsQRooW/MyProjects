import plotly.express as px
import plotly.figure_factory as ff
from abc import ABC, abstractmethod


class Graf(ABC):
    def __init__(self):
        self._plots = None

    def __call__(self, df, columns: list):
        self._plots = None
        self.df = df
        self.columns = columns
        return self

    @property
    def plots(self):
        if not self._plots:
            self._plots = self._gen_plots(self.columns)
        return self._plots

    @abstractmethod
    def _gen_plots(self, columns):
        pass


class Hist(Graf):
    def _gen_plots(self, columns: list):
        return [px.histogram(self.df, x=column, histfunc='count') for column in columns]


class Dist(Graf):
    def _gen_plots(self, columns: list):
        return [ff.create_distplot([self.df[column]], [column], show_rug=False) for column in columns]
