try:
    altura = float(input("Digite sua altura em metros: "))
    peso = float(input("Digite seu peso em kg: "))
    
    if altura <= 0 or peso <= 0:
        print("Altura e peso devem ser valores positivos.")
    else:
        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}")
        
except ValueError:
    print("Por favor, insira valores numéricos válidos para altura e peso.")
