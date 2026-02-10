# Simulador SIR com Autômatos Celulares

Projeto de simulação de propagação de doenças infecciosas usando autômato celular no modelo SIR (Suscetível, Infectado, Recuperado).

## Sobre o projeto

O simulador representa uma população em uma grade 60x60 onde cada célula da grade representa um indivíduo que pode estar em um dos estados:

- 0 – Suscetível  
- 1 – Infectado  
- 2 – Recuperado  

A cada passo da simulação:
- indivíduos podem ser infectados pelos vizinhos,
- infectados podem se recuperar,
- o sistema gera curvas epidemiológicas e um mapa espacial final.

O objetivo é mostrar como uma epidemia pode surgir e se espalhar a partir de interações locais entre indivíduos.

## Saída

O programa exibe:

- Mapa final da distribuição espacial (S, I, R)  
- Curvas epidemiológicas ao longo do tempo

## Tecnologias utilizadas

- Python  
- NumPy  
- Matplotlib

## Requisitos

Instale as bibliotecas necessárias com:

```bash
pip install -r requirements.txt
```

## Como executar

Após instalar as dependências, rode o programa com:

```bash
python simulador.py
```
