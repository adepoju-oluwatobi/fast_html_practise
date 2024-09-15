from fasthtml.common import *

def header():
    return Nav(
        Ul(
            Li(A('Home', href='#home', _class='px-4')),
            Li(A('Skills', href='#skills', _class='px-4')),
            Li(A('Projects', href='#projects', _class='px-4')),
            Li(A('Contact', href='#contact', _class='px-4')),
            _class='flex space-x-4'
        ), 
        _class='flex justify-center py-4 fixed top-0 left-0 w-full z-10'
    )
