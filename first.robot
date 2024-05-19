*** Settings ***
Library            third.py

*** Test Cases ***
TC01 Search for an entity
    ${list}            Fetch Text From Wiki
    
