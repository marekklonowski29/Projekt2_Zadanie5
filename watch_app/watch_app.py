from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.clock import Clock
from datetime import datetime
from math import cos, sin, radians
from kivy.uix.image import Image

class AnalogClock(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width = 300
        self.height = 300
        self.clock_center_x = self.center_x
        self.clock_center_y = self.center_y
        self.hour_hand_length = 100
        self.minute_hand_length = 120
        self.second_hand_length = 140
        self.clock_face = Image(source='tarcza.png', size=self.size)
        self.clock_day_face = Image(source='day.png', size=self.size)
        self.clock_night_face = Image(source='night.png', size=self.size)
        Clock.schedule_interval(self.update, 1)  # Update every second

    def update(self, dt):
        now = datetime.now()
        self.canvas.before.clear()
        with self.canvas.before:
            # Draw time of day
            if now.hour > 6 and now.hour < 21:
                Rectangle(source=self.clock_day_face.source, pos=self.pos, size=self.size)
            else:
                Rectangle(source=self.clock_night_face.source, pos=self.pos, size=self.size)
                Color(0, 0, 0)

            # Draw clock face image
            Rectangle(source=self.clock_face.source, pos=self.pos, size=self.size)
            
            
        self.canvas.after.clear()
        with self.canvas.after:
            
            # Draw hour hand
            if now.hour > 6 and now.hour < 21:
                Color(0, 1, 0)
            else:
                Color(0, 0, 1)
            
            hour_angle = 30 * now.hour + 0.5 * now.minute
            hour_hand_x = self.clock_center_x + self.hour_hand_length * \
                          1 * sin(radians(hour_angle))
            hour_hand_y = self.clock_center_y + self.hour_hand_length * \
                          cos(radians(hour_angle))
            Line(points=[self.clock_center_x, self.clock_center_y, hour_hand_x, hour_hand_y], width=5)

            # Draw minute hand
            minute_angle = 6 * now.minute + 0.1 * now.second
            minute_hand_x = self.clock_center_x + self.minute_hand_length * \
                            1 * sin(radians(minute_angle))
            minute_hand_y = self.clock_center_y + self.minute_hand_length * \
                            cos(radians(minute_angle))
            Line(points=[self.clock_center_x, self.clock_center_y, minute_hand_x, minute_hand_y], width=3)

            # Draw second hand
            Color(1, 0, 0)
            second_angle = 6 * now.second
            second_hand_x = self.clock_center_x + self.second_hand_length * \
                            1 * sin(radians(second_angle))
            second_hand_y = self.clock_center_y + self.second_hand_length * \
                            cos(radians(second_angle))
            Line(points=[self.clock_center_x, self.clock_center_y, second_hand_x, second_hand_y], width=1)

            
class AnalogClockApp(App):
    def build(self):
        
        return AnalogClock()


if __name__ == '__main__':
    AnalogClockApp().run()
