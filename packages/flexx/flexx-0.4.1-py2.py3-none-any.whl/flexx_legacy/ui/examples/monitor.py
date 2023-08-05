# -*- coding: utf-8 -*-
"""
Simple web app to monitor the CPU and memory usage of the server process.
Requires psutil.

This app might be running at the demo server: http://flexx1.zoof.io
"""

from __future__ import print_function, absolute_import, with_statement, unicode_literals, division

import time
import psutil

from flexx import app, ui, event

nsamples = 16


class Relay(event.HasEvents):
    
    def __init__(self):
        super(Relay, self).__init__()
        app.manager.connect(self._set_n_connections, 'connections_changed')
        self._set_n_connections()
        self.refresh()
    
    def _set_n_connections(self, *events):
        n = 0
        for name in app.manager.get_app_names():
            proxies = app.manager.get_connections(name)
            n += len(proxies)
        self._n_connections = n
        self.system_info()
    
    @event.emitter
    def system_info(self):
        return dict(cpu=psutil.cpu_percent(),
                    mem=psutil.virtual_memory().percent,
                    sessions=self._n_connections,
                    total_sessions=app.manager.total_sessions,
                    )
        
    def refresh(self):
        self.system_info()
        app.call_later(1, self.refresh)


class Monitor(ui.Widget):
    
    def init(self):
        with ui.HBox():
            with ui.VBox():
                ui.Label(text='<h3>Server monitor</h3>')
                self.info = ui.Label(text='...')
                
                if app.current_server().serving[0] == 'localhost':
                    # Don't do this for a public server
                    self.button = ui.Button(text='Do some work')
                    self.button.connect('mouse_down', self._do_work)
                
                self.cpu_plot = ui.PlotWidget(style='width: 640px; height: 320px;',
                                              xdata=[], yrange=(0, 100), 
                                              ylabel='CPU usage (%)',
                                              sync_props=False)
                self.mem_plot = ui.PlotWidget(style='width: 640px; height: 320px;',
                                              xdata=[], yrange=(0, 100), 
                                              ylabel='Mem usage (%)',
                                              sync_props=False)
                ui.Widget(flex=1)
        
        # Relay global info into this app
        relay.connect(self._push_info, 'system_info:' + self.id)
    
    def _push_info(self, *events):
        if not self.session.status:
            return relay.disconnect('system_info:' + self.id)
        self.emit('system_info', events[-1])
    
    
    def _do_work(self, *events):
        etime = time.time() + len(events)
        while time.time() < etime:
            pass
    
    class JS(object):
        cpu_count = psutil.cpu_count()
        nsamples = nsamples
        
        def init(self):
            super(JS, self).init()
            import time
            self.start_time = time.time()
        
        @event.connect('system_info')
        def _update_info(self, *events):
            ev = events[-1]
            
            # Set connections
            n = ev.sessions, ev.total_sessions
            self.info.text = ('There are %i connected clients.<br />' % n[0] +
                              'And in total we served %i connections.<br />' % n[1])
            
            # Prepare plots
            import time
            times = self.cpu_plot.xdata.copy()
            times.append(time.time() - self.start_time)
            times = times[-self.nsamples:]
            self.cpu_plot.xdata = times
            self.mem_plot.xdata = times
            
            # cpu data
            usage = self.cpu_plot.ydata
            usage.append(ev.cpu)
            usage = usage[-self.nsamples:]
            self.cpu_plot.ydata = usage
            
            # mem data
            usage = self.mem_plot.ydata
            usage.append(ev.mem)
            usage = usage[-self.nsamples:]
            self.mem_plot.ydata = usage


# Create global relay
relay = Relay()


if __name__ == '__main__':
    app.serve(Monitor)
    # m = app.launch(Monitor)  # for use during development
    app.start()
