import math

# number_of_model - int
# fibre_content - float
# E_for_fiber - float
# nu_for_fiber - float
# E_for_matrix - float
# nu_for_matrix - float
def Elastic_modules_for_unidirectional_composite(number_of_model, fibre_content, E_for_fiber, nu_for_fiber, E_for_matrix, nu_for_matrix):
    ## Это модель возвращает 9 упругих характеристик в следующем порядке [E1, E2, E3, nu12, n13, nu23, G12, G13, G23]
    ## Для данной модели подразумевается, что направление 1 - вдоль волокна, а 2 и 3 - это поперечные направления
    G_for_fiber = E_for_fiber/(2*(1+nu_for_fiber))
    G_for_matrix= E_for_matrix/(2*(1+nu_for_matrix))
    match number_of_model:
    ## Правило смеси    
    ## По этой модели невозможо получить характеристики nu23 и G23
        case 1: 
            E1 = fibre_content*E_for_fiber + E_for_matrix*(1 - fibre_content)
            E2 = 1/(fibre_content/E_for_fiber + (1 - fibre_content)/E_for_matrix)
            E3 = 1/(fibre_content/E_for_fiber + (1 - fibre_content)/E_for_matrix)
            nu12 = nu_for_fiber*fibre_content + nu_for_matrix*(1 - fibre_content)
            nu13 = nu_for_fiber*fibre_content + nu_for_matrix*(1 - fibre_content)
            nu23 = -1
            G12 = fibre_content*G_for_fiber + G_for_matrix*(1 - fibre_content)
            G13 = fibre_content*G_for_fiber + G_for_matrix*(1 - fibre_content)
            G23 = -1
            return[ E1, E2, E3, nu12, nu13, nu23, G12, G13, G23]
    ## Модель Ванина. Описанно в "Микромеханика композиционных материалов"
    ## Для G12, G13, G23 приведены значения лишь в первом приближении. Для уточнения значений необходимо ввести более сложный вид формул. См. стр. 23
        case 2: 
            chi_for_fiber = 3-4*nu_for_fiber 
            chi_for_matrix = 3-4*nu_for_matrix
            ## Ванина. Описанно в "Микромеханика композиционных материалов", стр. 29
            E1 = fibre_content*E_for_fiber + (1 - fibre_content)*E_for_matrix + (8*G_for_matrix*(nu_for_fiber-nu_for_matrix)*(nu_for_fiber-nu_for_matrix)*fibre_content *(1-fibre_content ))/(2-fibre_content +fibre_content*chi_for_matrix+(1-fibre_content)*(chi_for_fiber-1)*(G_for_matrix)/(G_for_fiber))
            nu21 = nu_for_matrix - (chi_for_matrix + 1)*(nu_for_matrix - nu_for_fiber)*fibre_content/(2 - fibre_content + fibre_content*chi_for_matrix + (1-fibre_content)*(chi_for_fiber-1)*(G_for_matrix)/(G_for_fiber))
            nu31 = nu_for_matrix - (chi_for_matrix + 1)*(nu_for_matrix - nu_for_fiber)*fibre_content/(2 - fibre_content + fibre_content*chi_for_matrix + (1-fibre_content)*(chi_for_fiber-1)*(G_for_matrix)/(G_for_fiber))
            ## "Микромеханика композиционных материалов" стр. 33
            E2 = 1/(nu21/E1 + 1/(8*G_for_matrix)*((2*(1 - fibre_content)*(chi_for_matrix - 1) + (chi_for_fiber - 1)*(chi_for_matrix - 1 + 2*fibre_content)*(G_for_matrix)/(G_for_fiber))/(2 - fibre_content + chi_for_matrix*fibre_content + (1 - fibre_content)*(chi_for_fiber - 1)*(G_for_matrix)/(G_for_fiber)) + 2*(chi_for_matrix*(1 - fibre_content) + (1 + fibre_content*chi_for_matrix)*(G_for_matrix)/(G_for_fiber))/(chi_for_matrix + fibre_content+(1-fibre_content)*(G_for_matrix)/(G_for_fiber))))
            E3 = 1/(nu21/E1 + 1/(8*G_for_matrix)*((2*(1-fibre_content)*(chi_for_matrix-1)+(chi_for_fiber-1)*(chi_for_matrix-1+2*fibre_content)*(G_for_matrix)/(G_for_fiber))/(2-fibre_content+chi_for_matrix*fibre_content+(1-fibre_content)*(chi_for_fiber-1)*(G_for_matrix)/(G_for_fiber))+2*(chi_for_matrix*(1-fibre_content)+(1+fibre_content*chi_for_matrix)*(G_for_matrix)/(G_for_fiber))/(chi_for_matrix+fibre_content+(1-fibre_content)*(G_for_matrix)/(G_for_fiber))))
            nu23 = E2*(-nu21/E1 + 1/(8*G_for_matrix)*(-(2*(1-fibre_content)*(chi_for_matrix-1)+(chi_for_fiber-1)*(chi_for_matrix-1+2*fibre_content)*(G_for_matrix)/(G_for_fiber))/(2-fibre_content+chi_for_matrix*fibre_content+(1-fibre_content)*(chi_for_fiber-1)*(G_for_matrix)/(G_for_fiber))+2*(chi_for_matrix*(1-fibre_content)+(1+fibre_content*chi_for_matrix)*(G_for_matrix)/(G_for_fiber))/(chi_for_matrix+fibre_content+(1-fibre_content)*(G_for_matrix)/(G_for_fiber))))
            nu12 = nu21* E2/E1
            nu13 = nu31* E3/E1
            ## "Микромеханика композиционных материалов" стр. 22, 32
            G12 = 1/((1/G_for_matrix)*(1 - fibre_content + (1 + fibre_content)*G_for_matrix/G_for_fiber)/(1+fibre_content+(1-fibre_content)*G_for_matrix/G_for_fiber))
            G13 = 1/((1/G_for_matrix)*(1 - fibre_content + (1 + fibre_content)*G_for_matrix/G_for_fiber)/(1+fibre_content+(1-fibre_content)*G_for_matrix/G_for_fiber))
            G23 = 1/((1/G_for_matrix)*((1 - fibre_content)*chi_for_matrix + (1 + chi_for_matrix*fibre_content)*G_for_matrix/G_for_fiber)/(chi_for_matrix + fibre_content + (1-fibre_content)*G_for_matrix/G_for_fiber))
            return[E1, E2, E3, nu12, nu13, nu23, G12, G13, G23]

def Thermal_expansion_for_unidirectional_composite(number_of_model, fibre_content , E_for_fiber, nu_for_fiber, alpha_for_fiber, E_for_matrix, nu_for_matrix, alpha_for_matrix):
    G_for_fiber = E_for_fiber/(2*(1+nu_for_fiber))
    G_for_matrix= E_for_matrix/(2*(1+nu_for_matrix))
    chi_for_fiber = 3-4*nu_for_fiber 
    chi_for_matrix = 3-4*nu_for_matrix
    nu21 = Elastic_modules_for_unidirectional_composite(2,fibre_content,E_for_fiber, nu_for_fiber,E_for_matrix, nu_for_matrix)[3]*Elastic_modules_for_unidirectional_composite(2,fibre_content,E_for_fiber, nu_for_fiber,E_for_matrix, nu_for_matrix)[0]/Elastic_modules_for_unidirectional_composite(2,fibre_content,E_for_fiber, nu_for_fiber,E_for_matrix, nu_for_matrix)[1]
    nu31 = Elastic_modules_for_unidirectional_composite(2,fibre_content,E_for_fiber, nu_for_fiber,E_for_matrix, nu_for_matrix)[4]*Elastic_modules_for_unidirectional_composite(2,fibre_content,E_for_fiber, nu_for_fiber,E_for_matrix, nu_for_matrix)[0]/Elastic_modules_for_unidirectional_composite(2,fibre_content,E_for_fiber, nu_for_fiber,E_for_matrix, nu_for_matrix)[2]
    match number_of_model:
    ## Модель Ванина. Описанно в "Микромеханика композиционных материалов", стр. 184       
        case 1:
            alpha1 = alpha_for_matrix - (alpha_for_matrix - alpha_for_fiber)*fibre_content/Elastic_modules_for_unidirectional_composite(2,fibre_content,E_for_fiber, nu_for_fiber,E_for_matrix, nu_for_matrix)[0]*(E_for_fiber + (8*G_for_matrix*(nu_for_fiber - nu_for_matrix)*(1 - fibre_content)*(1 + nu_for_fiber))/(2 - fibre_content + fibre_content*chi_for_matrix + (1 - fibre_content)*(chi_for_fiber + 1)*(G_for_matrix)/(G_for_fiber)))
            alpha2 = alpha_for_matrix + (alpha_for_matrix - alpha1)*nu21 - (alpha_for_matrix-alpha_for_fiber)*(1 + nu_for_fiber)*(nu_for_matrix-nu21)/(nu_for_matrix-nu_for_fiber)
            alpha3 = alpha_for_matrix + (alpha_for_matrix - alpha1)*nu31 - (alpha_for_matrix-alpha_for_fiber)*(1 + nu_for_fiber)*(nu_for_matrix-nu31)/(nu_for_matrix-nu_for_fiber)
            return [alpha1, alpha2, alpha3]
            
def Thermal_conductivity_for_unidirectional_composite(number_of_model, fibre_content , K_for_fiber, K_for_matrix): 
    match number_of_model:
        ## Правило смеси + дипломная работа Thermal conductivity characterization of composite materials
        case 1: 
            K1 = fibre_content*K_for_fiber + (1 - fibre_content)*K_for_matrix
            K2 = 1/(fibre_content/K_for_fiber + (1 - fibre_content)/K_for_matrix)
            K3 = 1/(fibre_content/K_for_fiber + (1 - fibre_content)/K_for_matrix)
            return [K1, K2, K3]
        ## Модель Ванина для тетрагональной укладки. Описанно в "Микромеханика композиционных материалов", стр. 192
        case 2: 
            K1 = fibre_content*K_for_fiber + (1 - fibre_content)*K_for_matrix
            K_2_zero = K_for_matrix * ((1 + fibre_content+(1 - fibre_content)*K_for_fiber/K_for_matrix)/(1 - fibre_content+(1 - fibre_content)*K_for_fiber/K_for_matrix))
            n = 6
            K2 = K_2_zero * (1 + n*n*(n - 1)*K_2_zero/K_for_matrix*((1 - K_for_fiber/K_for_matrix)/(1 - fibre_content + (1 + fibre_content)*K_for_fiber/K_for_matrix))*((1 - K_for_fiber/K_for_matrix)/(1 - fibre_content + (1 + fibre_content)*K_for_fiber/K_for_matrix))*((math.sin(math.pi/2)*math.sin(math.pi/2))/(math.pow(math.pi/2,n)))*(fibre_content*fibre_content - math.pow(fibre_content,2*n)*((1 - K_for_fiber/K_for_matrix)/(1 + K_for_fiber/K_for_matrix))*((1 - K_for_fiber/K_for_matrix)/(1 + K_for_fiber/K_for_matrix))))
            K3 = K_2_zero * (1 + n*n*(n - 1)*K_2_zero/K_for_matrix*((1 - K_for_fiber/K_for_matrix)/(1 - fibre_content + (1 + fibre_content)*K_for_fiber/K_for_matrix))*((1 - K_for_fiber/K_for_matrix)/(1 - fibre_content + (1 + fibre_content)*K_for_fiber/K_for_matrix))*((math.sin(math.pi/2)*math.sin(math.pi/2))/(math.pow(math.pi/2,n)))*(fibre_content*fibre_content - math.pow(fibre_content,2*n)*((1 - K_for_fiber/K_for_matrix)/(1 + K_for_fiber/K_for_matrix))*((1 - K_for_fiber/K_for_matrix)/(1 + K_for_fiber/K_for_matrix))))
            return [K1, K2, K3]


def Elastic_modules_for_honeycomb(number_of_model, l_cell_side_size, h_cell_side_size, wall_thickness, angle, E_for_honeycomb, nu_for_honeycomb):
    ## angle between the horizontal and the inclined cell wall
    ## angle in radians!
    ## статья Effective Elastic Properties of Periodic Hexagonal Honeycombs
    ## Для данной модели подразумевается, что направление 3 - перпендикулярно плоскости ячеек, а 1 и 2 - В плоскости ячеек. 1 и размер ячейки l - перпендикулярно направлению жёсткости, 2 и размер ячейки h - по направлению жёсткости
    G_for_honeycomb= E_for_honeycomb/(2*(1+nu_for_honeycomb))
    match number_of_model:
        case 1:
            lb = l_cell_side_size - wall_thickness/(2*math.cos(angle))
            hb = h_cell_side_size - (wall_thickness*(1 - math.sin(angle))/math.cos(angle))
            E1 = E_for_honeycomb*(wall_thickness/lb)*(wall_thickness/lb)*(wall_thickness/lb)*(math.cos(angle)/((h_cell_side_size/l_cell_side_size + math.sin(angle))*math.sin(angle)*math.sin(angle)))*(1/(1 + (2.4 + 1.5*nu_for_honeycomb + 1/(math.tan(angle)*math.tan(angle)))*(wall_thickness*wall_thickness)/(lb*lb)))
            E2 = E_for_honeycomb * (wall_thickness/lb)*(wall_thickness/lb)*(wall_thickness/lb)*((h_cell_side_size/l_cell_side_size+math.sin(angle))/(math.cos(angle)*math.cos(angle)*math.cos(angle)))*(1/(1 + (2.4 + 1.5*nu_for_honeycomb + math.tan(angle)*math.tan(angle)+ (2*hb/lb)/(math.cos(angle)*math.cos(angle)))*(wall_thickness*wall_thickness)/(lb*lb)))
            E3 = E_for_honeycomb*(1 - (lb*(hb + lb*math.sin(angle)))/(l_cell_side_size*(h_cell_side_size + l_cell_side_size*math.sin(angle))))
            nu12 = ((math.cos(angle)*math.cos(angle))/((h_cell_side_size/l_cell_side_size + math.sin(angle))*math.sin(angle)))*((1 + (1.4 + 1.5*nu_for_honeycomb)*(wall_thickness*wall_thickness)/(lb*lb))/(1 + (2.4 + 1.5*nu_for_honeycomb + 1/(math.tan(angle)*math.tan(angle)))*(wall_thickness*wall_thickness)/(lb*lb)))
            nu13 = E1/E3*nu_for_honeycomb
            nu23 = E2/E3*nu_for_honeycomb
            C = (1 + 2*(hb/lb) + (wall_thickness*wall_thickness)/(lb*lb)*((2.4 + 1.5*nu_for_honeycomb)/(hb/lb)*(2 + h_cell_side_size/l_cell_side_size + math.sin(angle)) + (h_cell_side_size/l_cell_side_size + math.sin(angle))/((wall_thickness*wall_thickness)/(lb*lb))*((h_cell_side_size/l_cell_side_size + math.sin(angle))*math.tan(angle)*math.tan(angle) + math.sin(angle))))
            G12 = E_for_honeycomb * (wall_thickness/lb)*(wall_thickness/lb)*(wall_thickness/lb) * (h_cell_side_size/l_cell_side_size + math.sin(angle))/((hb*hb)/(lb*lb)*math.cos(angle)) * 1/C
            G13 = G_for_honeycomb * (((wall_thickness)/(l_cell_side_size))/(((h_cell_side_size)/(l_cell_side_size) + math.sin(angle))*math.cos(angle))) * (math.cos(angle)*math.cos(angle)*lb/l_cell_side_size + 0.75*wall_thickness/l_cell_side_size*2*math.tan(angle) - math.cos(angle) / 2 *wall_thickness/l_cell_side_size*(2*math.sin(angle) - 1))
            G23 = G_for_honeycomb * (((wall_thickness)/(l_cell_side_size))/(((h_cell_side_size)/(l_cell_side_size) + math.sin(angle))*math.cos(angle))) * (math.sin(angle)*math.sin(angle)*lb/l_cell_side_size + hb/(2*l_cell_side_size) + 0.75*wall_thickness/l_cell_side_size*2*math.tan(angle) - (math.sin(angle)*math.sin(angle)) / (2*math.cos(angle)) *wall_thickness/l_cell_side_size*(2*math.sin(angle) - 1))
            return [E1, E2, E3, nu12, nu13, nu23, G12, G13, G23]

def Thermal_expansion_for_honeycomb(number_of_model, l_cell_side_size, h_cell_side_size, wall_thickness, angle, alpha_for_honeycomb):
    match number_of_model:
        case 1:
            alpha1 = alpha_for_honeycomb
            alpha2 = ((h_cell_side_size)/(l_cell_side_size)*alpha_for_honeycomb - math.cos(angle)*alpha_for_honeycomb)/((h_cell_side_size)/(l_cell_side_size) - math.cos(angle))
            alpha3 = alpha_for_honeycomb
            return [alpha1, alpha2, alpha3]

# assert Elastic_modules_for_unidirectional_composite(2.0, 0.2, 100.0, 0.3, 5.0, 0.2) == [
#     24.011723329425557,
#     6.5683701067350135,
#     6.5683701067350135,
#     0.06240625050144681,
#     0.06240625050144681,
#     0.18585515203940609,
#     2.9945407835581253,
#     2.9945407835581253,
#     2.769465602708258
# ]
# assert Thermal_expansion_for_unidirectional_composite(1, 0.2, 100.0, 0.3, 1e-6, 5.0, 0.2, 20e-5) == [
#     0.00003303092919697953,
#     0.0001653038466333737,
#     0.0001653038466333737
# ]
# assert Thermal_conductivity_for_unidirectional_composite(2, 0.2, 100, 1) == [
#     20.8,
#     1.3300670235932428,
#     1.3300670235932428
# ]
# assert Elastic_modules_for_honeycomb(1,9.24 ,8.4619, 0.4, math.pi/6 , 7.07, 0.2) == [
#     0.0014972693834675922,
#     0.0013344741623586129,
#     0.3592394105863781,
#     1.0512175946777975,
#     0.0008335774635770805,
#     0.0007429441887683659,
#     0.00028697519513263696,
#     0.07995563727728495,
#     0.0755763830773748
# ]
# assert Thermal_expansion_for_honeycomb(1, 9.24 ,8.4619, 0.4, math.pi/6 , 20e-5) == [
#     0.0002,
#     0.00019999999999999966,
#     0.0002
# ]
