import subprocess
from os.path import exists
from os import chdir, mkdir
from shutil import rmtree


class dtepTestLib(object):

    def __init__(self) -> None:
        self.python: str = "./venv/bin/python"
        self.dtep: str = "../dtep"
        self.mode: str
        self.project_name: str
        self.language: str
        self.arguments = []
        self.command = []

    def set_python_and_dtep(self, dtep: str, python: str) -> None:
        self.python = python
        self.dtep = dtep

    def go_back_one_directory(self) -> None:
        chdir("..")

    def create_and_change_directory(self, name: str) -> None:
        mkdir(name)
        chdir(name)

    def add_argument(self, argument: str) -> None:
        self.arguments += [argument]

    def add_argument_with_option(self, argument: str, option: str) -> None:
        self.arguments += [argument] + [option]

    def run_dtep(self) -> None:
        self.command = [self.python] + [self.dtep] + self.arguments
        subprocess.run(self.command)

    def _set_mode(self, mode: str) -> None:
        self.mode = mode

    def _set_project_name(self, name: str) -> None:
        self.project_name = name

    def _set_language(self, lang: str) -> None:
        self.language = lang

    def set_required(self, mode: str, name: str, lang: str) -> None:
        self._set_mode(mode)
        self._set_project_name(name)
        self._set_language(lang)
        self.arguments = [self.mode, self.project_name, self.language]

    def check_std(self, path: str, std: str) -> None:
        assert self._check_file_contains_substring(path, "-std="+std), str(
            "std in makefile does not match given: "+std)

    def check_variable_from_makefile(self,
                                     makefile: str,
                                     dir_variable: str,
                                     name: str
                                     ) -> None:
        assert self._check_file_contains_substring(
            makefile, dir_variable+" = "+name), str(
            dir_variable+" = "+name+" not found in makefile")

    def check_file_exists(self, path: str) -> None:
        assert exists(path), "file "+path+" does not exist"

    def check_gitignore_contents(
            self, path: str, obj: str, out: str) -> None:
        assert self._check_file_contains_substring(
            path, obj), obj+" not found in gitignore"
        assert self._check_file_contains_substring(
            path, out), out+" not found in gitignore"

    def go_back_and_clean(self, dir_name: str) -> None:
        self.go_back_one_directory()
        self.clean_directory(dir_name)

    def clean_directory(self, name: str) -> None:
        rmtree(name)

    def _check_file_contains_substring(
            self, file_path: str, substring: str) -> bool:
        if exists(file_path):
            with open(file_path, 'r') as file:
                file_content = file.read()
                if substring in file_content:
                    return True
                else:
                    return False
        else:
            raise KeyError(
                "file given to substring check does not exist: "+file_path)
