from faker import Faker

faker = Faker('pt-br')

produtos = ['Adaptador', 'Cabo', 'Escritório', 'Gabinete', 'Headset Gamer', 'Mesa', 'Digitalizadora',
            'Mochila', 'Mouse', 'Gamer', 'Pen', 'Drive', 'Suporte', 'Teclado', 'Mouse', 'Teclado', 'WebCam']

# Gera um dicinario com
dicio = []
for item in produtos:
    dicio.append(dict(id_produto=faker.random.randint(1000, 9000), produto=item, preco=faker.random.randint(100, 1000)))

# Gera tres arquivos com dados randomicos de lojas
for item in [1, 2, 3]:
    with open(f'loja_{item}', 'w', encoding='utf=8') as arquivo:
        # head
        arquivo.write('id_cliente,nome,idade,uf,id_produto,quatidade,preco\n')
        # gera os dados
        for num in range(61):
            prod_dicio = faker.random.choice(dicio)
            arquivo.write(
                f'{faker.random.randint(1000, 9000)},'
                f'{faker.name()},'
                f'{faker.random.randint(18, 40)},'
                f'{faker.random.choice(["SP", "RJ", "MG"])},'
                f'{prod_dicio["id_produto"]},'
                f'{prod_dicio["produto"]},'
                f'{prod_dicio["preco"]}'
                f'\n'
            )
