# -*- coding: utf-8 -*-
""" Namespace for all widgets (that are not layouts).
"""

# flake8: noqa

from __future__ import print_function, absolute_import, with_statement, unicode_literals, division

from .. import Widget

from ._button import BaseButton, Button, ToggleButton, RadioButton, CheckBox
from ._slider import Slider
from ._lineedit import LineEdit
from ._label import Label
from ._group import GroupWidget
from ._progressbar import ProgressBar
from ._plotwidget import PlotWidget
from ._iframe import IFrame
from ._bokeh import BokehWidget
from ._canvas import CanvasWidget
from ._color import ColorSelectWidget
from ._media import ImageWidget, VideoWidget, YoutubeWidget
