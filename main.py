import flet as ft

def criar_campos():
    atributos = {
        'width': 400,
        'border_radius': 10,
        'bgcolor': 'white',
        'color': 'black'
    }
    nome = ft.TextField(label="NOME", **atributos)
    sobrenome = ft.TextField(label="SOBRENOME", **atributos)
    email = ft.TextField(label="EMAIL", **atributos, keyboard_type=ft.KeyboardType.EMAIL)
    numero = ft.TextField(label="TELEFONE",**atributos, keyboard_type=ft.KeyboardType.NUMBER)
    cpf = ft.TextField(label='CPF', **atributos)
    return nome, sobrenome, email, numero, cpf

def cria_error():
    nome = ft.Text('', color='red')
    sobrenome = ft.Text('', color='red')
    email = ft.Text('', color='red')
    numero = ft.Text('', color='red')
    cpf = ft.Text('', color='red')
    return nome, sobrenome, email, numero, cpf

def validaCpf(cpf):
    def verifica_id(cpfsemid):
        contador_regressivo = len(cpfsemid) + 1
        resultado = 0
        for digito in cpfsemid:
            resultado += int(digito) * contador_regressivo
            contador_regressivo-=1
        
        resultado = (resultado * 10) % 11
        cpfid = resultado if resultado < 10 else 0
        cpfsemid += str(cpfid)
        return cpfsemid

    if len(cpf.value) != 11 or not cpf.value.isdigit():
        return False
    
    cpf_sem_id = cpf.value[:9]
    cpf_sem_id = verifica_id(cpf_sem_id)
    cpf_sem_id = verifica_id(cpf_sem_id)

    if cpf_sem_id == cpf.value:
        return True
    else:
        return False
    

def limpar_campos(campos):
    for campo in campos:
        campo.value = ''

def main(pagina):
    def on_submit(evento):
        formulario_valido = True
        if nome.value == '':
            nome_error.value = 'ESTE CAMPO É OBRIGATÓRIO'
            formulario_valido = False
        elif nome.value.isdigit():
            nome_error.value = 'NOME NÃO PODE CONTER NÚMEROS'
            formulario_valido = False
        else:
            nome_error.value = ''

        if sobrenome.value == '':
            sobrenome_error.value = 'ESTE CAMPO É OBRIGATÓRIO'
            formulario_valido = False
        elif sobrenome.value.isdigit():
            sobrenome_error.value = 'SOBRENOME NÃO PODE CONTER NÚMEROS'
        else:
            sobrenome_error.value = ''

        if 'outlook' in email.value.lower() or 'gmail' in email.value.lower():
            email_error.value = ''
        else:
            email_error.value = 'DIGITE UM EMAIL VÁLIDO'
            formulario_valido = False

        if numero.value.isdigit() == True and len(numero.value) >= 8:
            numero_error.value = ''
        else:
            numero_error.value = 'DIGITE UM TELEFONE VÁLIDO'
            formulario_valido = False
        
        if validaCpf(cpf):
            cpf_error.value = ''
        elif cpf.value == '':
            cpf_error.value = 'ESTE CAMPO É OBRIGATÓRIO'
            formulario_valido = False
        else:
            cpf_error.value = 'CPF INVÁLIDO'
            formulario_valido=False

        if formulario_valido:
            popup()
        
        pagina.update()
    
    def popup():
        janela.open = True
        pagina.update()

    def close_popup(e):
        janela.open = False
        limpar_campos([nome, sobrenome, email, numero, cpf])
        pagina.update()

    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    nome, sobrenome, email, numero, cpf = criar_campos()
    nome_error, sobrenome_error, email_error,  numero_error, cpf_error= cria_error()

    botao_enviar = ft.ElevatedButton(text='ENVIAR', on_click=on_submit)
    linha_botao = ft.Row(controls=[ft.Container(content=botao_enviar, padding=ft.padding.only(left=725))])  


    pagina.add(
        ft.Column(controls=[nome, nome_error]),
        ft.Column(controls=[sobrenome, sobrenome_error]),
        ft.Column(controls=[email, email_error]),
        ft.Column(controls=[numero, numero_error]),
        ft.Column(controls=[cpf, cpf_error]),
        linha_botao
    )

    botao_ok = ft.ElevatedButton(text='OK', on_click=close_popup)
    titulo = ft.Text('CADASTRO FOI REALIZADO COM SUCESSO')
    janela = ft.AlertDialog(title=titulo, actions=[botao_ok])
    pagina.add(janela)

ft.app(main)