from fasthtml.common import *

def introduction():
    return Div(
        Div(
            Img(src='/static/images/profile_pics.jpg', alt='Adepoju Oluwatobi', style='border-radius: 10%; width: 80px; height: 120px; margin: auto;', _class='mx-auto mb-4'),  # Image centered horizontally
            Div(
                P('Adepoju Oluwatobi', _class='font-bold text-lg text-black text-center'),  # Center text
                P('Fullstack Developer', _class='text-black font-bold text-2xl text-center'),  # Center text
            ),
            P('I specialize in building modern web applications...', _class='text-gray-600 text-center mb-8'),  # Center text
            _class='text-center'
        ),
        _class="bg-gray-100 p-6 rounded-lg shadow-md mb-8 flex flex-col justify-center items-center",  # Flexbox centering
        id="home"
    )
