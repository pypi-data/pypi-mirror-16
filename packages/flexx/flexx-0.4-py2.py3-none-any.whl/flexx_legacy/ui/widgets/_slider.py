# -*- coding: utf-8 -*-
"""

Simple example:

.. UIExample:: 50

    s = ui.Slider(min=10, max=20, value=12)


Interactive example:

.. UIExample:: 100

    from flexx import app, ui, event
    
    class Example(ui.Widget):
    
        def init(self):
            with ui.HBox():
                self.slider = ui.Slider(flex=0, min=1, max=20, step=1)
                self.label = ui.Label(flex=1)
        
        class JS:
            @event.connect('slider.value')
            def _change_label(self, *events):
                self.label.text = 'x' * events[-1].new_value
"""

from __future__ import print_function, absolute_import, with_statement, unicode_literals, division

from ...pyscript import window
from ... import event
from . import Widget


#todo: implement this in a way so it looks/behaves the same everywhere.

class Slider(Widget):
    """ An input widget to select a value in a certain range (aka HTML
    range input).
    """
    
    CSS = ".flx-Slider {min-height: 30px;}"
    
    class Both(object):
            
        @event.prop
        def step(self, v=0.01):
            """ The step size for the slider."""
            return float(v)
        
        @event.prop
        def min(self, v=0):
            """ The minimal slider value."""
            return float(v)
        
        @event.prop
        def max(self, v=1):
            """ The maximum slider value."""
            return float(v)
        
        @event.prop
        def value(self, v=0):
            """ The current slider value (settable)."""
            return float(min(self.max, max(self.min, v)))
    
    class JS(object):
        
        def _init_phosphor_and_node(self):
            self.phosphor = window.phosphor.createWidget('input')
            self.node = self.phosphor.node
            
            self.node.type = 'range'
            f = lambda ev: self._set_prop('user_value', self.node.value)
            self.node.addEventListener('input', f, False)
            #if IE10:
            #   this.node.addEventListener('change', f, False)
        
        @event.readonly
        def user_value(self, v=None):
            """ The slider value set by the user (updates on user interaction). """
            if v is not None:
                v = float(v)
                self.value = v
            return v
        
        @event.connect('value')
        def __value_changed(self, *events):
            self.node.value = events[-1].new_value
        
        @event.connect('step')
        def __step_changed(self, *events):
            self.node.step= events[-1].new_value
        
        @event.connect('min')
        def __min_changed(self, *events):
            self.node.min = events[-1].new_value
        
        @event.connect('max')
        def __max_changed(self, *events):
            self.node.max = events[-1].new_value
