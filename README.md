# 📊 Simulador de Receita de Campanha

## Objetivo do Projeto

O Simulador de Receita de Campanha é uma aplicação desenvolvida em Python com o objetivo de estimar a receita acumulada de uma campanha publicitária ao longo do tempo por meio da aplicação de conceitos de Cálculo Integral.

O sistema utiliza um modelo matemático baseado em uma função exponencial para representar a receita instantânea de uma campanha, considerando um comportamento de decaimento ao longo das horas. A partir dessa função, é realizada uma integração numérica para calcular a receita total estimada durante todo o período da campanha.

Além do processamento matemático, o projeto armazena automaticamente os resultados em um banco de dados SQLite, permitindo o registro e a consulta das simulações realizadas.

---

## Funcionalidades

* Simulação da receita instantânea utilizando uma função exponencial.
* Cálculo da receita acumulada por meio de integração numérica.
* Armazenamento automático das simulações em banco de dados SQLite.
* Registro das seguintes informações:

  * Nome da campanha;
  * Duração da campanha;
  * Receita total estimada.

---

## Tecnologias Utilizadas

* Python 3
* SQLite3
* NumPy
* SciPy (`scipy.integrate.quad`)

---

## Modelo Matemático

A receita instantânea da campanha é definida pela função:

```text
r(t) = A · e^(-kt)
```

Onde:

* **A** → Receita inicial (R$/hora);
* **k** → Taxa de decaimento;
* **t** → Tempo em horas.

A receita total acumulada é obtida pela integral definida:

```text
          T
R(T) = ∫  A · e^(-kt) dt
         0
```

---

## Estrutura do Projeto

```text
simulador-receita-campanha/
│
├── simulador.py
├── campanhas.db
└── README.md
```

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Entre na pasta do projeto:

```bash
cd seu-repositorio
```

3. Instale as dependências necessárias:

```bash
pip install numpy scipy
```

4. Execute o programa:

```bash
python simulador.py
```

---

## Exemplo de Execução

```text
=== Simulador de Receita de Campanha ===

Digite o nome da campanha:
Black Friday

Digite a duração da campanha (em horas):
24

Receita total estimada para "Black Friday" após 24 horas:

R$ 909,28

Resultado salvo com sucesso no banco de dados.
```

---

## Finalidade Acadêmica

Este projeto foi desenvolvido para aplicar conceitos de Cálculo Integral, Programação em Python e Banco de Dados SQLite, demonstrando como técnicas matemáticas e computacionais podem ser utilizadas para modelar e estimar receitas em campanhas publicitárias.

---

## Autora

**Letícia Monteiro**

Projeto desenvolvido para fins acadêmicos e de estudo.
