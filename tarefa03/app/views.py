from django.shortcuts import render

def usuarios(request):
    lista_usuarios = [
        {"nome": "Zezin", "matricula": 111, "idade": 20, "cidade": "Good Jesus"},
        {"nome": "Joaquim", "matricula": 222, "idade": 23, "cidade": "Natal"},
        {"nome": "Mateus", "matricula": 222, "idade": 21, "cidade": "Santa Maria"},
        {"nome": "Cirilo", "matricula": 222, "idade": 36, "cidade": "Elói de Souza"},
        {"nome": "Thierry", "matricula": 222, "idade": 18, "cidade": "Parnamirim"}
    ]

    context = {
        "usuarios": lista_usuarios,
    }
    return render(request, "usuarios.html", context)