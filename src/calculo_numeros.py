from exceptions import ingrese_numero, NumeroDebeSerPositivo

def main():
    
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except ValueError as e:
            print(f"Error: {e}")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break

if __name__ == "__main__":
    main() 