# Copyright (C) 2021 Van Vuong Ngo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from mycroft import MycroftSkill, intent_file_handler
from smbus2 import SMBus
import time

address = 0x4

class SystemCheck(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('check.system.intent')
    def handle_check_system(self, message):
        self.speak_dialog('check.system')
        time.sleep(3) # wait because mycroft is using pixels
        
        bus = SMBus(1)
        pixels = []
        for i in range(6):
            pixels.append(255)
            pixels.append(0)
            pixels.append(0)
        bus.write_i2c_block_data(address, 0, pixels)
        bus.write_i2c_block_data(address, 6, pixels)

        time.sleep(2)
        response = self.ask_yesno('check_colors', data={"color": "red"})
        if response == 'yes':
            self.speak_dialog('color_checked', data={"color": "red"})
        else:
            self.speak_dialog('color_invalid', data={"color": "red"})
        time.sleep(4)

        # green
        pixels = []
        for i in range(6):
            pixels.append(0)
            pixels.append(255)
            pixels.append(0)
        bus.write_i2c_block_data(address, 0, pixels)
        bus.write_i2c_block_data(address, 6, pixels)
        time.sleep(4)

        response = self.ask_yesno('check_colors', data={"color": "green"})
        if response == 'yes':
            self.speak_dialog('color_checked', data={"color": "green"})
        else:
            self.speak_dialog('color_invalid', data={"color": "green"})
        time.sleep(4)

        # blue
        pixels = []
        for i in range(6):
            pixels.append(0)
            pixels.append(0)
            pixels.append(255)
        bus.write_i2c_block_data(address, 0, pixels)
        bus.write_i2c_block_data(address, 6, pixels)
        time.sleep(8)

        response = self.ask_yesno('check_colors', data={"color": "blue"})
        if response == 'yes':
            self.speak_dialog('color_checked', data={"color": "blue"})
        else:
            self.speak_dialog('color_invalid', data={"color": "blue"})

        bus.close()


def create_skill():
    return SystemCheck()

