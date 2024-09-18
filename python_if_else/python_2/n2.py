idade = 5

# Verificar idades
if idade < 12:
    print(f"Recomendamos que assista o filme INFANTIL por conta da idade de {idade} anos")
elif idade >= 12 and idade < 18:
    print(f"Como você tem {idade} anos, recomendamos o filme pra ADOLESCENTES")
else:
    print(f"Por ser maior de idade, recomendamos o filme pra ADULTOS")

#Verifica se tem ingressos 
quantidade_de_ingressos = 0

if quantidade_de_ingressos == 0:
    print(f"Porém, há um problema, INFELIZMENTE OS INGRESSOS SE ESGOTARAM")
else:
    print(f"Fique à vontade pra comprar seus ingressos")