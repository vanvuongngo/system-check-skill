from mycroft import MycroftSkill, intent_file_handler
from smbus2 import SMBus

address = 0x4

class SystemCheck(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('check.system.intent')
    def handle_check_system(self, message):
        self.speak_dialog('check.system')
        
        bus = SMBus(1)
        pixels = []
        for i in range(6):
            pixels.append(255)
            pixels.append(0)
            pixels.append(0)
        bus.write_i2c_block_data(address, 0, pixels)
        bus.write_i2c_block_data(address, 6, pixels)
        self.speak_dialog("system.check", data={"color": "red"})
        bus.close()


def create_skill():
    return SystemCheck()

