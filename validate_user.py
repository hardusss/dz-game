import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = 'User Data'
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    page.theme_mode = 'dark'
    user_name = ft.TextField(label='Name', border_color='green')
    user_year = ft.TextField(label='Year', width=150, border_color='green')
    user_month = ft.TextField(label='Month', width=150, border_color='green')
    result_text = ft.Text(value='', size=20, color='green')


    def result():
        if user_month.value !='' and user_year.value != '' and user_name.value !='':
            result_text.value = f'Name: {user_name.value}, Year: {user_year.value}, Month: {user_month.value}'
            with open('user.txt', 'a') as user:
                user.write(f'Name: {user_name.value}\nYear: {user_year.value}\nMonth: {user_month.value}\n')
        else:
            pass


    def validate_month():
        if int(user_month.value) <= 12 and int(user_month.value) >= 1:
            user_month.border_color = 'green'
            result()
        else:
            user_month.border_color = 'red'
            user_month.label = 'ERROR'
        page.update()

    def validate_year():
      if  len(user_year.value) >= 1 and int(user_year.value) >= 5 and int(user_year.value) <= 120:
          user_year.border_color = 'green'
          validate_month()
      else:
          user_year.border_color = 'red'
          user_year.label = 'ERROR'
          validate_month()
      page.update()


    def validate(e):
        if len(user_name.value) > 2:
            user_name.border_color = 'green'
            validate_year()
        else:
            user_name.border_color = 'red'
            user_name.label = 'ERROR'
            validate_year()

        page.update()


    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        result_text,
                        user_name
                    ]
                )

            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        ft.Row(
            [
                user_year,
                user_month
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(text='Done', on_click=validate, width=200, height=40)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
