*** Settings ***
Documentation   dtep tests
...             
...             This test suite tests all dtep options
...             (not including "-h"). Some possible
...             cases that might be missed are ones
...             where a option influences something
...             that is not being tested in the same
...             test case (that will hopefully not 
...             happen). I still think these test
...             are valuable.
...
Library         dtepTestLib.py

*** Test Cases ***
Create default c++
  Set required  new   test_project  c++
  Run dtep
  Check file exists  test_project/src/main.cc
  [Teardown]  Clean directory   test_project

Create default c
  Set required  new   test_project  c
  Run dtep
  Check file exists  test_project/src/main.c
  [Teardown]  Clean directory   test_project

Create a project with cpp instead of c++
  Set required  new  test_project  cpp
  Run dtep
  Check file exists  test_project/src/main.cc
  [Teardown]   Clean directory   test_project

Create c++ with .cpp extension
  Set required  new   test_project  c++
  Add argument with option  -e  .cpp
  Run dtep
  Check file exists   test_project/src/main.cpp
  [Teardown]  Clean directory   test_project

Create c with std c89
  Set required  new   test_project  c
  Add argument with option  --std  c89
  Run dtep
  Check std  test_project/makefile  c89
  [Teardown]   Clean directory   test_project

Create a c project with git ignore and custom obj and out directory
  Set required  new  test_project  c 
  Add argument  -g
  Add argument with option  --object-dir  objects
  Add argument with option  --output-dir  output
  Run dtep
  Check file exists  test_project/.gitignore
  Check gitignore contents  test_project/.gitignore  objects  output
  Check variable from makefile  test_project/makefile  OBJ_DIR  objects
  Check variable from makefile  test_project/makefile  OUT_DIR  output
  [Teardown]   Clean directory   test_project

Create a c++ project with custom source directory
  Set required  new  test_project  c++
  Add argument with option  -s  source
  Run dtep
  Check file exists  test_project/source/main.cc 
  Check variable from makefile  test_project/makefile  SRC_DIR  source
  [Teardown]   Clean directory   test_project

Use init to create a c project instead of new
  Create and change directory  test_project
  Set python and dtep  ../../dtep  ../venv/bin/python
  Set required  init  test_project  c
  Run dtep
  Check file exists  src/main.c
  [Teardown]   Go back and clean  test_project
