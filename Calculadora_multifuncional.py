# --- CALCULADORA ELÉTRICA MULTIFUNCIONAL (POO) ---

import math
import sys

# --- FUNÇÃO GENÉRICA DE VALIDAÇÃO ---
def validar_numero_positivo(valor, nome_campo):
    """Valida se o valor digitado é um número positivo, aceitando vírgula."""
    try:
        num_str = valor.replace(',', '.').strip()
        num = float(num_str)
        if num <= 0:
            raise ValueError(f"O campo '{nome_campo}' deve ser maior que zero.")
        return num
    except (ValueError, TypeError):
        raise ValueError(f"Entrada inválida para o campo '{nome_campo}'.")

# --- CALCULADORA DE OHM E POTÊNCIA ---
class CalculadoraOhmPotencia:
    """Calcula V, I e P usando a Primeira Lei de Ohm e as Fórmulas de Potência."""
    
    def calcular_tensao(self):
        print("\n" + "="*40); print("CÁLCULO DE TENSÃO (V = I × R)"); print("="*40)
        try:
            I = validar_numero_positivo(input("Digite a Corrente (I) em A: "), "Corrente")
            R = validar_numero_positivo(input("Digite a Resistência (R) em Ω: "), "Resistência")
            V = I * R
            print("\n--- PASSO A PASSO ---")
            print(f"Resultado: V = {V:.2f} V")
            print("="*40)
        except ValueError as e: print(f"Erro: {e}")

    def calcular_corrente(self):
        print("\n" + "="*40); print("CÁLCULO DE CORRENTE (I = V / R)"); print("="*40)
        try:
            V = validar_numero_positivo(input("Digite a Tensão (V) em Volts: "), "Tensão")
            R = validar_numero_positivo(input("Digite a Resistência (R) em Ω: "), "Resistência")
            I = V / R
            print("\n--- PASSO A PASSO ---")
            print(f"Resultado: I = {I:.3f} A")
            print("="*40)
        except ValueError as e: print(f"Erro: {e}")

    def calcular_potencia(self):
        print("\n" + "="*40); print("CÁLCULO DE POTÊNCIA (P)"); print("="*40)
        print("Forneça exatamente dois valores (V, I, R).")
        try:
            v_input = input("  - Tensão (V): ").strip()
            i_input = input("  - Corrente (I): ").strip()
            r_input = input("  - Resistência (R): ").strip()

            if v_input and i_input and not r_input:
                V = validar_numero_positivo(v_input, "Tensão"); I = validar_numero_positivo(i_input, "Corrente")
                P = V * I; formula = "P = V × I"
            elif v_input and r_input and not i_input:
                V = validar_numero_positivo(v_input, "Tensão"); R = validar_numero_positivo(r_input, "Resistência")
                P = V**2 / R; formula = "P = V² / R"
            elif i_input and r_input and not v_input:
                I = validar_numero_positivo(i_input, "Corrente"); R = validar_numero_positivo(r_input, "Resistência")
                P = I**2 * R; formula = "P = I² × R"
            else:
                print("Erro: Forneça exatamente dois valores."); return

            print("\n--- PASSO A PASSO ---"); print(f"Fórmula: {formula}"); print(f"Resultado: P = {P:.2f} W")
            print("="*40)
        except ValueError as e: print(f"Erro: {e}")
    
    def executar(self):
        while True:
            print("\n" + "="*50); print("      CALCULADORA DE OHM E POTÊNCIA"); print("="*50)
            print("1 - Calcular Tensão (V)"); print("2 - Calcular Corrente (I)"); print("3 - Calcular Potência (P)"); print("0 - Voltar")
            opcao = input("Escolha: ").strip()
            if opcao == '1': self.calcular_tensao()
            elif opcao == '2': self.calcular_corrente()
            elif opcao == '3': self.calcular_potencia()
            elif opcao == '0': break
            else: print("Opção inválida!")

# --- CALCULADORA DE RESISTÊNCIA ---
class CalculadoraDeResistencia:
    """Calcula Resistência por Cores, Primeira Lei e Segunda Lei de Ohm."""
    def __init__(self):
        # Dicionários (Combinando as listas mais completas)
        self.cores_resistor = { # Dígitos 1 e 2
            'preto': 0, 'marrom': 1, 'vermelho': 2, 'laranja': 3,
            'amarelo': 4, 'verde': 5, 'azul': 6, 'violeta': 7,
            'cinza': 8, 'branco': 9
        }
        self.multiplicadores = { # Faixa 3
            'preto': 1, 'marrom': 10, 'vermelho': 100, 'laranja': 1000,
            'amarelo': 10000, 'verde': 100000, 'azul': 1000000,
            'dourado': 0.1, 'prateado': 0.01
        }
        self.tolerancias = { # Faixa 4
            'marrom': 1, 'vermelho': 2, 'verde': 0.5, 'azul': 0.25,
            'violeta': 0.1, 'cinza': 0.05, 'dourado': 5, 'prateado': 10,
            'sem_cor': 20
        }
        self.resistividades = { # Segunda Lei de Ohm
            'cobre': 1.68e-8, 'aluminio': 2.65e-8, 'ouro': 2.44e-8,
            'prata': 1.59e-8, 'ferro': 9.71e-8, 'niquel': 6.99e-8, 
            'tungsteno': 5.60e-8, 'platina': 1.06e-7, 'chumbo': 2.20e-7, 'grafite': 3.5e-5
        }

    def validar_cores(self, cores): 
        """Valida se todas as cores inseridas são válidas em algum dos dicionários."""
        cores_validas = set(list(self.cores_resistor.keys()) + list(self.multiplicadores.keys()) + list(self.tolerancias.keys()))
        for i, cor in enumerate(cores):
            if cor.lower() not in cores_validas:
                raise ValueError(f"Cor '{cor}' não é válida na posição {i+1}!")
        return [cor.lower() for cor in cores]

    def resistencia_codigo_cores(self):
        print("\n" + "="*40); print("RESISTÊNCIA POR CÓDIGO DE CORES"); print("="*40)
        entrada = input("Digite as 4 cores (ex: Marrom, Preto, Vermelho, Dourado): ").strip()
        try:
            cores = [c.strip() for c in entrada.split(',')]
            if len(cores) != 4: raise ValueError("Digite 4 cores separadas por vírgula.")
            
            cores = self.validar_cores(cores) # Validação robusta
            
            d1, d2 = self.cores_resistor[cores[0]], self.cores_resistor[cores[1]]
            mult, tol = self.multiplicadores[cores[2]], self.tolerancias[cores[3]]
            R = (d1*10 + d2)*mult
            
            print("\n--- PASSO A PASSO ---")
            print(f"Resultado: R = {R} Ω ±{tol}%")
            print(f"Faixa: {R*(1-tol/100):.2f} Ω a {R*(1+tol/100):.2f} Ω")
            print("="*40)
        except Exception as e: print(f"Erro: {e}")

    def resistencia_segunda_lei_ohm(self):
        print("\n" + "="*40); print("RESISTÊNCIA PELA SEGUNDA LEI DE OHM"); print("="*40)
        print("Materiais:", list(self.resistividades.keys()))
        try:
            material = input("Material: ").lower().strip()
            if material not in self.resistividades: raise ValueError("Material inválido.")
            L = validar_numero_positivo(input("Comprimento (m): "), "Comprimento")
            A = validar_numero_positivo(input("Área (m²): "), "Área")
            R = self.resistividades[material]*L/A
            print("\n--- PASSO A PASSO ---"); print(f"Fórmula: R = ρ * L / A")
            print(f"Resultado: R = {R:.3e} Ω")
            print("="*40)
        except Exception as e: print(f"Erro: {e}")

    def resistencia_primeira_lei_ohm(self):
        print("\n" + "="*40); print("RESISTÊNCIA PELA PRIMEIRA LEI DE OHM (R = V/I)"); print("="*40)
        try:
            V = validar_numero_positivo(input("Tensão (V): "), "Tensão")
            I = validar_numero_positivo(input("Corrente (A): "), "Corrente")
            R = V/I
            print("\n--- PASSO A PASSO ---"); print(f"Resultado: R = {R:.2f} Ω")
            print("="*40)
        except Exception as e: print(f"Erro: {e}")

    def executar(self):
        while True:
            print("\n" + "="*50); print("         CALCULADORA DE RESISTÊNCIA"); print("="*50)
            print("1 - Código de cores"); print("2 - Segunda Lei de Ohm"); print("3 - Primeira Lei de Ohm (R = V/I)"); print("0 - Voltar")
            opcao = input("Escolha: ").strip()
            if opcao == '1': self.resistencia_codigo_cores()
            elif opcao == '2': self.resistencia_segunda_lei_ohm()
            elif opcao == '3': self.resistencia_primeira_lei_ohm()
            elif opcao == '0': break
            else: print("Opção inválida!")

# --- CALCULADORA DE ENERGIA ELÉTRICA ---
class CalculadoraEnergia:
    """Calcula o consumo de energia elétrica em kWh."""
    def calcular_energia(self):
        print("\n" + "="*40); print("CÁLCULO DE ENERGIA ELÉTRICA (kWh)"); print("="*40)
        try:
            P = validar_numero_positivo(input("Potência (W): "), "Potência")
            t = validar_numero_positivo(input("Tempo de uso (h): "), "Tempo")
            E = P * t / 1000
            print("\n--- PASSO A PASSO ---"); print(f"Fórmula: E = P * t / 1000")
            print(f"Resultado: Energia = {E:.3f} kWh")
            print("="*40)
        except ValueError as e: print(f"Erro: {e}")

    def executar(self):
        while True:
            print("\n" + "="*50); print("      CALCULADORA DE ENERGIA ELÉTRICA"); print("="*50)
            print("1 - Calcular energia elétrica (kWh)"); print("0 - Voltar")
            opcao = input("Escolha: ").strip()
            if opcao == '1': self.calcular_energia()
            elif opcao == '0': break
            else: print("Opção inválida!")

# --- CALCULADORA ELÉTRICA MULTIFUNCIONAL ---
class CalculadoraMultifuncional:
    """Menu principal para acesso às calculadoras específicas."""
    def __init__(self):
        self.ohm_potencia = CalculadoraOhmPotencia()
        self.resistencia = CalculadoraDeResistencia()
        self.energia = CalculadoraEnergia()

    def executar(self):
        while True:
            print("\n" + "="*60); print("           CALCULADORA ELÉTRICA MULTIFUNCIONAL"); print("="*60)
            print("1 - Ohm e Potência"); print("2 - Resistência"); print("3 - Energia Elétrica (kWh)"); print("0 - Sair")
            opcao = input("Escolha: ").strip()
            if opcao == '1': self.ohm_potencia.executar()
            elif opcao == '2': self.resistencia.executar()
            elif opcao == '3': self.energia.executar()
            elif opcao == '0':
                print("\nObrigado por usar a Calculadora Multifuncional!")
                break
            else: print("Opção inválida!")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    CalculadoraMultifuncional().executar()