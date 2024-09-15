from fasthtml.common import *
from components.profile import portfolio
from components.change import change

app, rt = fast_app(live=True)

@rt('/')
def get_home():
    return portfolio()

@rt('/change')
def get_change():
    return change()
