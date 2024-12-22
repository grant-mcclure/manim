from manim import *
import numpy as np

from manim import *
import numpy as np

class SineWaveInDegrees(Scene):
    def construct(self):
        # Axes in degrees
        axes = Axes(
            x_range=[0, 2*PI, 2*PI/2],  # X-axis in degrees with 90-degree steps
            y_range=[-1, 1, 0.5],  # Y-axis range with step size of 0.5
            x_length=10,  # Length of x-axis
            y_length=4,  # Length of y-axis
            axis_config={"color": WHITE},  # Axis color
            #x_axis_config={"numbers_to_include": [0, 180, 360, 540, 720], "include_ticks": True},  # X-axis labels
            tips=True,  # Disable arrow tips
        )
        
        # Adding axis labels
        axes_labels = axes.get_axis_labels(x_label="x (degrees)", y_label="f(x)")

        # Sine wave using degrees
        sine_wave = axes.plot(
            lambda x: np.sin((x)),  # Convert degrees to radians for sine function
            x_range=[0, 2*PI],  # Range in degrees
            color=BLUE,
        )
        
        # Add axes, labels, and sine wave to the scene
        self.add(axes, axes_labels, sine_wave)

        # Animate sine wave
        self.play(Create(sine_wave))
        self.wait(5)

        ###get wave to move 
        wave_tracker = ValueTracker(0)

        dynamic_sine_wave = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin((x) + wave_tracker.get_value()),  # Traveling wave
                x_range=[0, 2*PI],  # Range in degrees
                color=BLUE,
            )
        )

        # Add dynamic sine wave
        self.add(dynamic_sine_wave)
        self.play(FadeOut(sine_wave))

        # Animate the traveling wave
        self.play(wave_tracker.animate.increment_value(4 * PI), run_time=10, rate_func=linear)
        self.wait(2)