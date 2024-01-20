# import flet
# from flet import Page, AppBar, TextField, FilledButton, Text, colors, Column, Container


# def first_page(page: Page):
#     page.window_width = 720
#     page.window_height = 1280
    
#     page.appbar = AppBar(title = Text("what's up nigga"))

# flet.app(target=first_page)


import flet
from flet import Page, AppBar, TextField, Image, FilledButton, Text, colors, Column, Container, ImageFit, Control, ElevatedButton

list_contact = []

def test(page: Page):
    page.window_width = 800
    page.window_height=800
    def btn_clicked(e):
        page.clean()
    
    

            
    page.appbar=AppBar(title=Text("Coucou Rayane "), bgcolor=colors.CYAN_700, center_title=True)
    img =Image(
        src =f"/Users/mbm/Desktop/Xperiences_Flet/FigmaTry.png")
    #     # src =f"C:\Users\moham\OneDrive\Bureau\Chingu B-Days\spmn.png",

    #     fit= "contain"
    # )
    page.padding = 0
    page.add(

        # Container(
        #     image_src='XPERIENCES_FLET/FigmaTry.png',
        #     image_fit=ImageFit.COVER,
        #     expand=True,
        #     # content=Control()
        # )
    )
    global login
    global password
    login = TextField(label="Email", hint_text="Email Adresse", height=100, width=400)
    f1 = Container(
        content=ElevatedButton(text="Elevated Button in Container",width=400, height=100, on_click= btn_clicked),
        bgcolor=colors.GREY,
        # padding=5,
    )
    # btn = FilledButton(text="Login", width=400, height=100, on_click=btn_clicked)
    password=TextField(label="Passeword", password=True,can_reveal_password=True, hint_text="your password")

    page.add(
        Container(
            content=Column([
        
        img,
        login,
        password,
        #   btn
        f1,
    ], spacing=20)

        )
        )
    

flet.app(target=test)




