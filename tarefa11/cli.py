import users_wrapper as u

op = True

while op:
    print("1 - List")
    print("2 - Read")
    print("3 - Creat")
    print("4 - Update")
    print("5 - Delete")
    print("0 - Exit")
    op = input("Select: ")
    if op == "1":
        print("List:")
        users = u.list()
        if users:
            for user in users:
                print(f"ID: {user['id']}, Nome: {user['name']}")
        else:
            print("Usuário não encontrado")

    if op == "2":
        user_id = input("Digite o ID: ")
        user = u.read(user_id)
        if user:
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
        else:
            print("Usuário não encontrado")

    if op == "3":
        user_id = input("Digite o ID: ")
        user = u.read(user_id)
        if user:
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
            user["name"] = input("Digite: ")
            user["email"] = input("Digite: ")
            user["phone"] = input("Digite: ")
            novo_usuario = u.update(user_id, user)
            if novo_usuario:
                print(f"Usuário {novo_usuario['name']} atualizado com sucesso")
            else:
                print("Erro")

    if op == "4":
        user_id = input("Digite o ID: ")
        user = u.read(user_id)
        if user:
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
            confirmacao = input("Deseja excluir usuário? (s/n): ")
            if confirmacao == "s":
                u.delete(user_id)
                print("Usuário excluído")
            else:
                print("Exclusão cancelada")

    if op == "5":
        print("Digite os dados do novo usuário:")
        user = {}
        user["name"] = input("Nome: ")
        user["email"] = input("Email: ")
        user["phone"] = input("Telefone: ")
        confirmacao = input("Deseja criar usuário? (s/n): ")
        if confirmacao == "s":
            novo_usuario = u.create(user)
            if novo_usuario:
                print(f"Usuário {novo_usuario['name']} criado com sucesso")
            else:
                print("Erro")

    if op == "6":
        print("Out")
        op = False