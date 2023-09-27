import math 
# Coordenadas dos pontos 

x1 = 1.0 
y1 = 2.0 
x2 = 4.0 
y2 = 6.0 

# Cálculo da distância usando o Teorema de Pitágoras 

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 

print("A distância entre os pontos ({}, {}) e ({}, {}) é {}".format(x1,y1,x2,y2,distancia)) 

# Coordenadas polares 

DistPolar = 5.0 

AnguloPolar = 45.0  # ângulo em graus 


# Conversão de coordenadas polares para cartesianas 

x = DistPolar * math.cos(math.radians(AnguloPolar)) 

y = DistPolar * math.sin(math.radians(AnguloPolar)) 


print("As coordenadas cartesianas correspondentes são ({:.2f}, {:.2f})".format(x,y)) 

 

 

# Inicialização de variáveis 

origem_x = 0 

origem_y = 0 

propriedade_x1 = 0 

propriedade_y1 = 0 

propriedade_x2 = 0 

propriedade_y2 = 0 

TotMeteoritos = 0 

MeteoritosNaPropriedade = 0 

MeteoritosNaSede = 0 

QuadranteAtingido = [0, 0, 0, 0]  # [NE, NW, SW, SE] 


while True: 

    # Apresentar menu de opções 

    print("Menu de Opções:") 

    print("1. Definir localização da propriedade e sede") 

    print("2. Configurar sobreposição de origem dos referenciais") 

    print("3. Ler localização de meteoritos (terminar com distância negativa)") 

    print("4. Apresentar estatísticas") 

    print("5. Sair") 

 

    escolha = input("Escolha uma opção: ") 

 

    if escolha == "1": 

        # Definir localização da propriedade e sede 

        propriedade_x1 = float(input("Digite a coordenada x do canto inferior esquerdo da propriedade: ")) 

        propriedade_y1 = float(input("Digite a coordenada y do canto inferior esquerdo da propriedade: ")) 

        propriedade_x2 = float(input("Digite a coordenada x do canto superior direito da propriedade: ")) 

        propriedade_y2 = float(input("Digite a coordenada y do canto superior direito da propriedade: ")) 

        origem_x += propriedade_x1 

        origem_y += propriedade_y1 

    elif escolha == "2": 

        # Configurar sobreposição de origem dos referenciais 

        origem_x = float(input("Digite a coordenada x da nova origem: ")) 

        origem_y = float(input("Digite a coordenada y da nova origem: ")) 

 

    elif escolha == "3": 

        # Ler localização de meteoritos 

        while True: 

            distancia = float(input("Digite a distância do meteorito (-1 para encerrar): ")) 

            if distancia < 0: 

                break 

            angulo = float(input("Digite o ângulo do meteorito em relação ao eixo leste magnético: ")) 

            x, y = converter_para_cartesianas(distancia, angulo) 

            if propriedade_x1 <= x <= propriedade_x2 and propriedade_y1 <= y <= propriedade_y2: 

                MeteoritosNaPropriedade += 1 

            if calcular_distancia(x, y, origem_x, origem_y) <= 10: 

                MeteoritosNaSede += 1 

            if x >= origem_x and y >= origem_y: 

                QuadranteAtingido[0] += 1  # NE 

            elif x < origem_x and y >= origem_y: 

                QuadranteAtingido[1] += 1  # NW 

            elif x < origem_x and y < origem_y: 

                QuadranteAtingido[2] += 1  # SW 

            else: 

                QuadranteAtingido[3] += 1  # SE 

            TotMeteoritos += 1 

 

    elif escolha == "4": 

        # Apresentar estatísticas 

        print("Estatísticas:") 

        print(f"Total de meteoritos: {TotMeteoritos}") 

        print(f"Meteoritos dentro da propriedade: {MeteoritosNaPropriedade}") 

        print(f"Meteoritos que atingiram a sede: {MeteoritosNaSede}") 

        print(f"Quadrante mais atingido: NE: {QuadranteAtingido[0]}, NW: {QuadranteAtingido[1]}, SW: {QuadranteAtingido[2]}, SE: {QuadranteAtingido[3]}") 

 

    elif escolha == "5": 

        # Sair do programa 

        break 

 

    else: 

        print("Opção inválida. Por favor, escolha uma opção válida.") 