from fasthtml.common import *

def contact():
    return Div(
        Titled('Contact Me',
            Div(
                H2('Let\'s Get in Touch', _class='text-2xl font-semibold text-blue-700 mb-4'),
                P('Email: johndoe@example.com', _class='text-lg mb-2'),
                P(A('LinkedIn', href='https://linkedin.com/in/johndoe', _class='text-blue-500 underline')),
                P(A('GitHub', href='https://github.com/johndoe', _class='text-blue-500 underline'))
            )
        ),
        id="contact",
        _class="p-6 bg-white rounded-lg shadow-md mb-8"
    )
