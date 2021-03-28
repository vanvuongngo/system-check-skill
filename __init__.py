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
        response = self.ask_yesno('see_colors', data={"color": "red"})
        if response == 'yes':
            self.speak_dialog('color_checked', data={"color": "red"})
            return
        if response == 'no':
            self.speak_dialog('color_invalid', data={"color": "red"})
            return

        bus.close()


def create_skill():
    return SystemCheck()

