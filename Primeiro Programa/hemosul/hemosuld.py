nao_pode_doar = {"Hepatite apos 11 anos de idade?": "tem Hepatite",
                 "Chagas": "tem chagas",
                 "Cancer": "tem Cancer",
                 "Sifilis": "tem sifilis",
                 "HIV": "tem HIV",
                 "Uso de drogas injetaveis, ilicitas": "teve uso de drogas"
                 }
deve_aguardar={"Transfusao de sangue":365,
"Tatuagem":365,
"Piercing":365,
"Parto normal":365,
"Amamentação":365,
"Dengue Classica":30,
"Dengue Grave":180,
"Gripe":14,
"Uso de PrEP/PEP oral":120,
"Uso de PrEP Injetavel":720,
"Procedimentos Endoscopios":180, 
}
vacina={"Antirrabica":365,
        "Antitetanica":2,
        "Rubéola":30,
        "Sarampo":30,
        "Varicela":30,
        "Febre Amarela":30,
        "Dengue":30,
        "Gripe":2,
        "Covid":2}
def Triagem_Inicial():
     
    while True:
        documento=input(" Possui documento oficial com foto?(sim/nao): ").lower()
        if documento != "sim" and documento != "nao":
            print("Erro, Escreva com sim ou nao")
            
        elif documento == "nao":
            print("Você não pode doar, precisa apresentar documento oficial com foto")    
            return
        else:
            break
    while True:
        try:
            peso=float(input("Qual seu peso?: "))
            if peso < 51:
                print("O peso minimo para doação é de 51kg")
                return
            break
        except:
            print("Erro, escreva apenas com numero")




    while True:
        try:

            idade = int(input("Digite a sua idade (anos): "))
            if idade < 16 or idade > 69:
                print("não pode doar: A idade deve estar entre 16 e 69 anos.")
                return
                
            elif idade >=16 and idade <=17: 
                
                    acompanhado=input("Você está acompanhado de um responsavel?(sim/nao):").lower()
                    if acompanhado != 'sim' and acompanhado != "nao":
                        print("Escreva com sim ou não")
                    elif acompanhado == "nao":
                            print("Você não pode doar deve estar acompanhado com um responsavel")
                            return
                    else:
                        break
            else:
                break
        except:
            print("Erro, escreva apenas com numero")



    while True:
        saude=input("Está gripado ou com infecção?(sim/nao)").lower()
        if saude != "sim" and saude != "nao":
            print("Erro, Escreva com sim ou nao")
        elif saude == "sim":
            print("Voce nao pode doar precisa estar saudavel")
            return
        else:
            break
    while True:
        descanso=input("Está descansado e alimentado?(sim/nao)").lower()
        if descanso != "sim" and descanso != "nao":
            print("Erro, Escreva com sim ou nao")
        elif descanso =="nao":
            print("Você precisa estar descansado e alimentado para doar sangue")
            return
        else: 
            break
        
    print("Você pode doar sangue.")
    

def Triagem_Completa():
    for x in nao_pode_doar:
        while True:
            resposta=input(f"Teve:{x}?(sim/nao): ").lower()
            if resposta!="sim"and resposta!="nao":
                print("Erro, Escreva sim ou nao")
            elif resposta =="sim":
                print("Voce nao pode doar")
                print(f"Voce {nao_pode_doar[x]}")
                return
            else:
                break

    for i in deve_aguardar:
        while True:
            res=input(f"Teve:{i}?(sim/nao): ").lower()
            if res!="sim"and res!="nao":
                print("Erro, Escreva sim ou nao")
            elif res == "sim":
                print(f"Voce deve aguardar:{deve_aguardar[i]} dias")
                return
            else:
                break

    for a in vacina:
        while True:
            resp=input(f"Tomou a vacina:{a}?(sim/nao): ").lower()
            if resp!="sim"and resp!="nao":
                print("Erro, Escreva sim ou nao")
            elif resp == "sim":
                print(f"Voce deve aguardar {vacina[a]}")
                return
            else:
                break
    print("voce pode doar sangue")
    print("="*30)

def menu():
    while True:
        print("\nBem Vindo ao Sistema de Triagem Hemosul ")
        print("="*40)
        print("1 - Triagem Inicial")
        print("2 - Triagem Completa")
        print("3 - Intervalo")
        print("4 - Recomendações")
        print("5 - Sair")
        try:
            op = int(input("Escolha uma opção: "))
        except:
            print("Erro, Escreva com numeros")
            continue
        print("="*30)
            
        if op > 5 or op < 1:
            print("Escreva entre 5 e 1")
        
        elif op == 1:
            Triagem_Inicial()
        elif op == 2: 
            Triagem_Completa()
        elif op == 3:
            intervalo()
        elif op == 4:
            recomendacoes()
        elif op == 5:
            print("Encerrando..")
            break
        else:
            print("Opção incorreta")

def recomendacoes():
    print("----Recomendações!----")
    print("- Não ingerir bebidas por 12 hrs ate o horario da doação")
    print("- não fumar por 2 hrs ")
    print("- esteja bem alimentado\n (evite alimentos gordurosos no dia anterior à doação!)")
    print("- ingerir bastante água!\n (3 copos de água antes da doação)")
    print("- caso obtenha crianças (menores 12 anos),estejam acompanhados de um outro responsavel.")
    print("="*30)
    
def intervalo():
   
    while True:
         genero=input("Digite seu genero(feminino/masculino): ").lower()
         if genero != "feminino" and genero != "masculino":
             print("Erro, Escreva feminino ou masculino")
         elif genero == "feminino":
             intervalo=int(input("Faz quantos dias desde a ultima doação?: "))
             if intervalo < 90:
                 print(f"Você não pode doar, deve aguardar{90-intervalo} dias")
                 return
             else:
                 intervalo_ano=int(input("Quantas vezes você fez doação no periodo de um ano?: "))
                 if intervalo_ano > 3:
                     print("Você atingiu o limite de doações no ano")
                     return
                 else:
                     print("Você pode doar sangue.")
                     break
                 
         elif genero == "masculino":
             intervalo=int(input("Faz quantos dias desde a ultima doação?: "))
             if intervalo < 60:
                 print(f"Você não pode doar, deve aguardar {60-intervalo} dias")
                 return
             else:
                 intervalo_ano=int(input("Quantas vezes você fez doação no periodo de um ano?: "))
                 if intervalo_ano > 4:
                     print("Você atingiu o limite de doações no ano")
                     return
                 else:
                     print("Você pode doar sangue.")
                     break
           
menu()