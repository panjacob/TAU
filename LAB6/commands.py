class Commands:

    def __init__(self, mode):


        self.commands_linux = {
            'ls': {
                '': 'wyświetla pliki i katalogi',
                '-a': 'pokazuje ukryte pliki',
                '-l': 'pokazuje więcej informacji o pliku'
            },
            'rm': {
                '': 'usuwa pliki',
                '-f': 'usunięcie plików zabezpieczonych przed kopiowaniem',
                '-r': 'usunięcie plików również w podkatalogach',
                '-rf': 'usuwa cały system plików'
            },
            'cd': {
                '': '{argument} wejscie do katalogu',
                '..': 'wyjscie z katalogu',
            },
            'pwd': {
                '': 'wyświetla aktualną ścieżkę'
            },
            'mail': {
                '': '{argument} otwiera plik z pocztą'
            }
        }

        self.commands_windows = {
            'cls': {
                '': 'czyści ekran'
            },
            'cd': {
                '': '{argument} wejscie do katalogu / wyświetla aktualną ścieżkę',
                '..': 'wyjscie z katalogu',
            },
            'rd': {
                '': 'usuwa pliki',
                '-r': 'usuwa cały system plików'
            },
            'mkdir': {
                '': '{argument} tworzy ścieżkę',
            },
            'tasklist': {
                '': 'wyświetla wszystkie aktywne procesy',
            },
        }
        if mode == "Windows":
            self.commands = self.commands_windows
        elif mode == "Linux":
            self.commands = self.commands_linux
        else:
            raise Exception("Wrong mode name")

        self.mode = mode

    def clean_command(self, dirty_command):
        if not isinstance(dirty_command, str):
            return None
        all_arguments = dirty_command.lower().split(" ")
        if len(all_arguments) < 1:
            return None
        return all_arguments

    def help(self, dirty_command):
        all_arguments = self.clean_command(dirty_command)
        if all_arguments is None:
            return None

        if all_arguments[0] in self.commands:
            command = self.commands[all_arguments[0]]
            if len(all_arguments) > 1:
                if all_arguments[1] in command:
                    return command[all_arguments[1]]
                else:
                    return command['']
            else:
                return command['']
        else:
            return None


command = Commands("Linux")
result = command.help('lsa -ab')
print(result)