*** Settings ***
Library        Excel_reader.py
Library        SeleniumLibrary

*** Test Cases ***
TC01_Read Excel From file
    ${xcl_lst}        Read Excel    F:/test_repo/output.xlsx
    Log To console     ${xcl_lst}