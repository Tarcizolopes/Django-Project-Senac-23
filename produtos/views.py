from django.shortcuts import render

# Create your views here.
def listagem_produtos(request):
    produtos_dos_vendedores = [{
        'vendedor': {'nome': 'Joseph Climber'},
        'produtos': [
            {'nome': 'Uva', 'preco': 12}, 
            {'nome': 'Melância', 'preco': 10},
            {'nome': 'Banana', 'preco': 15},
        ]
    },
    {
       'vendedor': {'nome': 'John Pay Pay'},
       'produtos': [
            {'nome': 'Carro', 'preco': 45000}, 
            {'nome': 'Moto', 'preco': 1000},
            {'nome': 'Bike', 'preco': 1500},
        ]
    }
    ]
    context = {'produtos_dos_vendedores': produtos_dos_vendedores}
    return render(request, './templates/listagem_produtos.html', context)


