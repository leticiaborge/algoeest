usuario = input("Insira um nome de usuário.")
usuario = str.lower(usuario)
senha = input("Insira uma senha com pelo menos 8 caractere.")
if len(senha) >=8: 
    print("Usuário e senha criados.")
else:
    print("Senha fraca")
    senha = input("Insira uma senha com pelo menos 8 caractere.")
    if len(senha) >=8: 
         print("Usuário e senha criados.")
    else:
         print("Senha fraca, você não tem salvação e eu não tenho while. Reinicie o sistema.")    
verificaUsuario = input("Insira seu usuário.")
verificaSenha = input("Insira sua senha.")
if usuario == verificaUsuario and senha == verificaSenha:
    print(f"Bem vindo, {usuario}!")
else:
    print("Acesso negado!")
