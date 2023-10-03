# Calculadora de Índice de Massa Corporal (IMC)

Este programa calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos. Além disso, fornece um diagnóstico com base no IMC calculado.

## Como Executar

Certifique-se de que você tem Python instalado em seu ambiente.

1. Clone o repositório ou faça o download do código fonte.
2. Navegue até o diretório onde o código está localizado.
3. Execute o programa a partir da linha de comando:

```bash
python main.py
```

## Estrutura do Código

O código foi organizado em módulos para manter uma estrutura limpa e modular.

### Módulos

- `calcular_imc.py`: Contém a função `calcular_imc` que realiza o cálculo do IMC.
- `diagnosticar_imc.py`: Contém a função `diagnosticar_imc` que fornece um diagnóstico com base no IMC calculado.
- `main.py`: O script principal que interage com o usuário e utiliza as funções dos módulos para calcular e diagnosticar o IMC.

### Execução do Programa

O programa começa solicitando ao usuário que insira seu peso em quilogramas e sua altura em metros. Em seguida, ele calcula o IMC e fornece um diagnóstico baseado nesse valor.

O cálculo do IMC é feito pela função `calcular_imc` e o diagnóstico é determinado pela função `diagnosticar_imc`.   

```python
from funcoes.calcular_imc import calcular_imc
from funcoes.diagnosticar_imc import diagnosticar_imc

peso = input("Informe seu peso em Kg: ").replace(',', '.')
peso = float(peso)

altura = input("Informe sua altura em Mts: ").replace(',', '.')
altura = float(altura)

resultado = calcular_imc(peso, altura)
mensagem = diagnosticar_imc(resultado)

```

## Como Usar

1. Execute o programa.
2. Forneça seu peso em quilogramas e sua altura em metros quando solicitado.
3. O programa calculará o IMC e fornecerá uma mensagem de diagnóstico com base no IMC calculado.

Exemplo de uso:

```shell
Informe seu peso em Kg: 75.5 
Informe sua altura em Mts: 1,73

Seu IMC é: 25.23
Info: Acima do peso
```

Certifique-se de fornecer números válidos para peso e altura para obter um cálculo preciso do IMC e uma mensagem de diagnóstico relevante.

---