from fasthtml.common import *

def change():
    return Titled(
        'Change',
        Div(P('Change is good')),
        P(A('Home', href='/'))
    )
