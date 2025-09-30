import pytest
from src.decorators import log, my_function
import os


def test_log_errors(capsys):

    @log()
    def foo(x, y):
        return x + y

    with pytest.raises(TypeError):
        foo(1, "2")
    message = capsys.readouterr()
    assert "".join(message.out.split("-->")[-2:]) == " TypeError:  (1, '2'), {}\n"


def test_log_file_errors():
    @log(filename="log.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("log.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        message = all_lines[-1]
    assert "".join(message.split("-->")[-2:]) == " my_function  OK\n"


def test_log_invalid_file() -> None:
    filename = "log.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, filename)

    # Сохраняем текущую директорию
    original_cwd = os.getcwd()

    try:
        # Меняем рабочую директорию на data_dir
        os.chdir(data_dir)

        @log(filename)
        def func_error1(x: int, y: int) -> int:
            raise TypeError

        with pytest.raises(TypeError):
            func_error1(10, 20)
    finally:
        # Возвращаем обратно
        os.chdir(original_cwd)

    with open(file_path, mode="r") as file:
        data = file.read()

        # Проверяем фактический формат
    assert "TypeError: --> (10, 20), {}" in data
    # Или проверяем частично
    assert "TypeError" in data
    assert "(10, 20)" in data
    assert "{}" in data

def test_my_function() -> None:
    assert my_function(2, 5) == 7
