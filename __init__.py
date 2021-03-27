from mycroft import MycroftSkill, intent_file_handler


class SystemCheck(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('check.system.intent')
    def handle_check_system(self, message):
        self.speak_dialog('check.system')


def create_skill():
    return SystemCheck()

