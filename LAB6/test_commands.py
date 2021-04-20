import pytest

from commands import Commands


class TestCommands:
    def test_has_commands_before_initialization(self):
        hasattr(Commands, 'commands')

    def test_has_commands_after_initialization(self):
        mode = "Linux"
        commands = Commands(mode)
        hasattr(commands, 'commands')

    def test_mode_linux(self):
        mode = "Linux"
        commands = Commands(mode)
        assert commands.mode == mode

    def test_mode_windows(self):
        mode = "Windows"
        commands = Commands(mode)
        assert commands.mode == mode

    def test_mode_wrong(self):
        mode = "Wrong"
        with pytest.raises(Exception):
            Commands(mode)

    def test_mode_none(self):
        mode = None
        with pytest.raises(Exception):
            Commands(mode)

    def test_mode_integer(self):
        mode = 2
        with pytest.raises(Exception):
            Commands(mode)

    def test_mode_float(self):
        mode = 3.14
        with pytest.raises(Exception):
            Commands(mode)

    def test_mode_array(self):
        mode = [1, 2, 3]
        with pytest.raises(Exception):
            Commands(mode)


class TestCommandsLinux:

    def test_linux_ls(self):
        command = Commands("Linux")
        result = command.help('ls')
        assert result == 'wyświetla pliki i katalogi'

    def test_linux_xd(self):
        command = Commands("Linux")
        result = command.help('xd')
        assert result is None

    def test_linux_xd_wrong_arguments(self):
        command = Commands("Linux")
        result = command.help('xd -hehe')
        assert result is None

    def test_linux_xd_wrong_arguments2(self):
        command = Commands("Linux")
        result = command.help('xd -hehe 123')
        assert result is None

    def test_linux_integer(self):
        command = Commands("Linux")
        result = command.help(123)
        assert result is None

    def test_linux_float_parameter(self):
        command = Commands("Linux")
        result = command.help(3.14)
        assert result is None

    def test_linux_empty(self):
        command = Commands("Linux")
        result = command.help("")
        assert result is None


class TestCommandsWindows:
    def test_windows_wrong_command(self):
        command = Commands("Windows")
        result = command.help('xd')
        assert result is None

    def test_windows_wrong_command_wrong_arguments(self):
        command = Commands("Windows")
        result = command.help('xd -hehe')
        assert result is None

    def test_windows_wrong_command_wrong_arguments2(self):
        command = Commands("Windows")
        result = command.help('xd -hehe 123')
        assert result is None

    def test_windows_cls(self):
        command = Commands("Windows")
        result = command.help('cls')
        assert result == 'czyści ekran'

    def test_windows_two_valid_third_wrong(self):
        command = Commands("Windows")
        result = command.help('cd .. wrong')
        assert result == 'wyjscie z katalogu'

    def test_windows_new_line(self):
        command = Commands("Windows")
        result = command.help('cd /n')
        assert result == '{argument} wejscie do katalogu / wyświetla aktualną ścieżkę'

    def test_windows_none(self):
        command = Commands("Windows")
        result = command.help(None)
        assert result is None
