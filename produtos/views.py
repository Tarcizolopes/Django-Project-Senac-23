from django.shortcuts import render

# Create your views here.
def listagem_produtos(request):
    context = {
        'produtos': [{'nome': 'Uva', 'preco': 12}, 
                     {'nome': 'Melância', 'preco': 10},
                     {'nome': 'Banana', 'preco': 15}
                    ]
    }
    return render(request, './templates/listagem_produtos.html', context)


