from fasthtml.common import *

def home():
    return Titled(
        'Greeting',
        Div(P('Hello world')),
        P(A('Change', href='/change'))
    )
