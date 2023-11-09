'''
This is a test library for a tool named dtep

things that need testing (test cases):
    * dtep with no extra arguments
    * -e <.extension> changed the file extension for source files
      found in src/main.extension
      Makefile line: EXTENSION = .extension
    * --std <standard> to change the standard (c99 c++20)
      found in Makefile
    * -g to create a .gitignore file
      the .gitignore file has the obj and out directory
    * all the directory commands (-s --object-dir --output-dir)
'''

import subprocess
from os.path import exists
from shutil import rmtree

class dtepTestLib(object):

    def __init__(self):
        self.python: str = "./venv/bin/python"
        self.dtep: str = "../dtep"
        self.mode: str
        self.project_name: str
        self.language: str
        self.arguments = []
        self.command = []

    def add_extension_argument(self, extension: str):
        self.arguments += ["-e"] + [extension]

    def run_dtep(self):
        self.command = [self.python] + [self.dtep] + self.arguments
        subprocess.run(self.command)

    def set_mode(self, mode: str):
        self.mode = mode

    def set_project_name(self, name:str):
        self.project_name = name

    def set_language(self, lang: str):
        self.language = lang

    def set_required(self, mode: str, name: str, lang: str):
        self.set_mode(mode)
        self.set_project_name(name)
        self.set_language(lang)
        self.arguments = [self.mode, self.project_name, self.language]

    def check_file(self, path: str):
        assert exists(path), "file "+path+" does not exist"

    def check_file_with_extension(self, path: str, extension: str):
        assert exists(path+extension), "file "+path+extension+" does not exist"

    def clean_directory(self, name: str):
        rmtree(name)
