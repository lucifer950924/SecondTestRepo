from pywinauto.application import Application


def start_an_app(app):
    Appl = Application().start(app)


start_an_app('calc.exe')  
start_an_app('explorer.exe')