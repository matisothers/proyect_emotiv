"""
=================
Animated subplots
=================

This example uses subclassing, but there is no reason that the proper function
couldn't be set up and then use FuncAnimation. The code is long, but not
really complex. The length is due solely to the fact that there are a total of
9 lines that need to be changed for the animation as well as 3 subplots that
need initial set up.

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation


class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        fig, (ax1,ax2) = plt.subplots(2)

        self.data1 = []
        self.data2 = []
        self.t = [0,1,2,3,4,5,6]


        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        self.line1 = Line2D([], [], color='black')
        self.line2 = Line2D([], [], color='red')
        self.line3 = Line2D([], [], color='blue')
        self.line4 = Line2D([], [], color='green')
        self.line5 = Line2D([], [], color='purple')

        ax1.add_line(self.line1)
        ax1.add_line(self.line2)
        ax1.add_line(self.line3)
        ax1.add_line(self.line4)
        ax1.add_line(self.line5)
        

        ax2.set_xlabel('x')
        ax2.set_ylabel('y')
        self.line1b = Line2D([], [], color='black')
        self.line2b = Line2D([], [], color='red')
        self.line3b = Line2D([], [], color='blue')
        self.line4b = Line2D([], [], color='green')
        self.line5b = Line2D([], [], color='purple')

        ax2.add_line(self.line1b)
        ax2.add_line(self.line2b)
        ax2.add_line(self.line3b)
        ax2.add_line(self.line4b)
        ax2.add_line(self.line5b)
        

       
        animation.TimedAnimation.__init__(self, fig, interval=50, blit=True)

    def _draw_frame(self, framedata):
        i = framedata
        head = i - 1
        head_slice = (self.t > self.t[i] - 1.0) & (self.t < self.t[i])

        self.line1.set_data(self.x[:i], self.y[:i])
        self.line1a.set_data(self.x[head_slice], self.y[head_slice])
        self.line1e.set_data(self.x[head], self.y[head])

        self.line2.set_data(self.y[:i], self.z[:i])
        self.line2a.set_data(self.y[head_slice], self.z[head_slice])
        self.line2e.set_data(self.y[head], self.z[head])

        
        self._drawn_artists = [self.line1, self.line1a, self.line1e,
                               self.line2, self.line2a, self.line2e]

    def new_frame_seq(self):
        return iter(range(self.t.size))

    def _init_draw(self):
        lines = [self.line1, self.line1a, self.line1e,
                 self.line2, self.line2a, self.line2e,]
        for l in lines:
            l.set_data([], [])

ani = SubplotAnimation()
# ani.save('test_sub.mp4')
plt.show()
