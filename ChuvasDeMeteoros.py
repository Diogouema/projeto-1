import math 

# Inicialização de variáveis 
#UPMCC
BaseMonit_x = 0 
BaseMonit_y = 0 

#Área Da Propriedade
propriedade_x_sul = 0 
propriedade_y_sul = 0 

propriedade_x_norte = 0 
propriedade_y_norte = 0 

#Área Da fazenda
sede_x_sul = 0
sede_x_norte = 0

sede_y_sul = 0
sede_y_norte = 0

#Variaveis dos Meteoros
TotMeteoritos = 0 
MeteoritosNaPropriedade = 0 
MeteoritosNaSede = 0 

Quadrante1 = 0  # NE
Quadrante2 = 0  # NO 
Quadrante3 = 0  # SO
Quadrante4 = 0  # SE

#Limitador de passagem para as opções 3 e 4
trava = 0


while True: 

    # Apresentar menu de opções 
    print("*"*100)
    print("-:: Menu de Opções ::-") 
    print("1. Definir localização da propriedade e sede") 
    print("2. Configurar sobreposição de origem dos referenciais") 
    print("3. processar registros de chuva de meteoros") 
    print("4. Apresentar estatísticas") 
    print("5. Sair") 
    print("*"*100)
 
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1: 

        # Definir localização da propriedade e sede 
        print("-"*100)
        print("-"*100)
        
        propriedade_x_sul = float(input("Digite a coordenada x do canto inferior esquerdo da propriedade: ")) 
        propriedade_y_sul = float(input("Digite a coordenada y do canto inferior esquerdo da propriedade: ")) 

        propriedade_x_norte = float(input("Digite a coordenada x do canto superior direito da propriedade: ")) 
        propriedade_y_norte = float(input("Digite a coordenada y do canto superior direito da propriedade: ")) 

        print("\nentre as coordenadas da Sede:\n")
        sede_x_sul = float(input("Digite a coordenada x do canto inferior esquerdo da sede: ")) 
        sede_y_sul = float(input("Digite a coordenada y do canto inferior esquerdo da sede: ")) 

        sede_x_norte = float(input("Digite a coordenada x do canto superior direito da sede: ")) 
        sede_y_norte = float(input("Digite a coordenada y do canto superior direito da sede: "))  

        print("-"*100)
        print("-"*100)
        
    elif escolha == 2: 

        print("defina as cordenadas da Base de Monitoramento")
        
        BaseMonit_x = float(input("defina as cordenadas de X da base: "))
        BaseMonit_y = float(input("defina as cordenadas de Y da base: "))
        
        trava =+ 1

 
    elif escolha == 3: 
        if trava == 1:

            # Ler localização de meteoritos 
            print("PARA SAIR DO REGISTRO DIGITE -1 NA DISTÂNCIA")
            while True: 
                print ("registro # ", TotMeteoritos +1)
                distancia = float(input(" -> Distância: ")) 

                if distancia < 0: 
                    break 

                angulo = float(input(" -> Ângulo: ")) 
                print("*"*100)
                
                Cordenada_Cartesiano_x = (math.cos(angulo * ((2 * math.pi) / 360 )) * distancia) + BaseMonit_x
                Cordenada_Cartesiano_y = (math.sin(angulo * ((2 * math.pi) / 360 )) * distancia) + BaseMonit_y

                #verificando se caiu na propriedade
                if propriedade_x_norte <= Cordenada_Cartesiano_x <= propriedade_x_sul and propriedade_y_sul <= Cordenada_Cartesiano_y <= propriedade_y_norte: 
                    MeteoritosNaPropriedade += 1 
                    
                    #definindo em qual quadrante o meteoro caiu
                    if Cordenada_Cartesiano_x >= 0 and Cordenada_Cartesiano_y >= 0: 
                        Quadrante1 += 1  # NE 
                    elif Cordenada_Cartesiano_x <= 0 and Cordenada_Cartesiano_y >= 0: 
                        Quadrante2 += 1  # NO 
                    elif Cordenada_Cartesiano_x >= 0 and Cordenada_Cartesiano_y <= 0: 
                        Quadrante3 += 1  # SE 
                    else: 
                        Quadrante4 += 1  # SO 

                TotMeteoritos += 1 
                
                #verificando se caiu na Sede
                if sede_x_norte <= Cordenada_Cartesiano_x <= sede_x_sul and sede_y_sul <= Cordenada_Cartesiano_y <= sede_y_norte:
                    MeteoritosNaSede += 1 
        else:
            print("Impossível processar qualquer registro de queda no momento: localização da propriedade ainda não informada.")
    

    elif escolha == 4: 
        if trava == 1:
        # Apresentar estatísticas 

            print("-:: Estatísticas: ::-") 

            print("Total de Quedas Registradas: {} ({:.2%})".format(TotMeteoritos,(TotMeteoritos / TotMeteoritos)))

            print("Meteoritos dentro da propriedade: {} ({:.2%})".format(MeteoritosNaPropriedade, (MeteoritosNaPropriedade / TotMeteoritos))) 

            print("->NE: {} ({:.2%})".format(Quadrante1,(Quadrante1 / MeteoritosNaPropriedade)))  
            print("->NO: {} ({:.2%})".format(Quadrante2,(Quadrante2 / MeteoritosNaPropriedade))) 
            print("->SE: {} ({:.2%})".format(Quadrante3,(Quadrante3 / MeteoritosNaPropriedade))) 
            print("->SO: {} ({:.2%})".format(Quadrante4,(Quadrante4 / MeteoritosNaPropriedade)))
            print(MeteoritosNaSede) 

            if MeteoritosNaSede > 0 :
                print("A Sede foi atingida? SIM")
                print("Meteoritos que atingiram a sede: {} ({:.2%})".format(MeteoritosNaSede, (MeteoritosNaSede / TotMeteoritos)))
           
            else:
                print("A Sede foi atingida? NÃO")
               
        else:
            print("Impossível processar qualquer registro de queda no momento: não foi feita a unificação dos sistemas referenciais usados nos cálculos.")
 

    elif escolha == 5: 
        # Sair do programa 
        break 

    else: 
        print("Opção inválida. Por favor, escolha uma opção válida.") 