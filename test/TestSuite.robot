*** Settings ***
Documentation   dtep tests
...             
...             You should allways call
...             set required before any other options
...
Library         dtepTestLib.py

*** Test Cases ***
Create default c++
  Set required  new   test_project  c++
  Run dtep
  Check file with extension   test_project/src/main   .cc
  Clean directory   test_project

Create default c
  Set required  new   test_project  c
  Run dtep
  Check file with extension   test_project/src/main   .c
  Clean directory   test_project

Create c++ with .cpp extension
  Set required  new   test_project  c++
  Add extension argument  .cpp
  Run dtep
  Check file with extension   test_project/src/main   .cpp
  Clean directory   test_project
