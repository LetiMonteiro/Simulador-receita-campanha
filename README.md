# 📊 Simulador de Receita de Campanha

Projeto desenvolvido em **Python** para simular a receita acumulada de uma campanha publicitária ao longo do tempo utilizando **Integrais Definidas** e armazenando os resultados em um banco de dados **SQLite**.

##  Sobre o projeto

O objetivo deste projeto é demonstrar a aplicação prática do cálculo integral em um cenário de marketing, onde a receita por hora de uma campanha sofre um decaimento exponencial.

A receita instantânea é representada pela função:

\[
r(t)=Ae^{-kt}
\]

e a receita total é obtida pela integral definida da função no intervalo de tempo da campanha.

Além do cálculo matemático, os resultados são persistidos em um banco de dados SQLite para futuras consultas.

---

##  Funcionalidades

- Calcular a receita por hora utilizando uma função exponencial.
- Calcular a receita total acumulada por meio de integração numérica.
- Salvar automaticamente os resultados em um banco SQLite.
- Registrar:
  - Nome da campanha
  - Duração
  - Receita total estimada

---

## 🛠 Tecnologias utilizadas

- Python 3
- SQLite3
- NumPy
- SciPy (`scipy.integrate.quad`)

---

##  Modelo Matemático

Receita por hora:

```
r(t) = A · e^(-kt)
```

Onde:

- **A** → Receita inicial (R$/hora)
- **k** → Taxa de decaimento
- **t** → Tempo (horas)

Receita total acumulada:

```
          T
R(T) = ∫  A·e^(-kt) dt
         0
```

---

##  Estrutura do projeto

```
📦 simulador-receita-campanha
│
├── simulador.py
├── campanhas.db
└── README.md
```

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Entre na pasta

```bash
cd seu-repositorio
```

### 3. Instale as dependências

```bash
pip install numpy scipy
```

### 4. Execute o programa

```bash
python simulador.py
```

---

##  Exemplo de execução

```
=== Simulador de Receita de Campanha ===

Digite o nome da campanha: Black Friday

Digite a duração da campanha (em horas): 24

Receita total estimada para 'Black Friday' após 24 horas:
R$ 909.28

✅ Resultado salvo no banco de dados (campanhas.db).
```

---

##  Objetivo acadêmico

Este projeto foi desenvolvido para aplicar conceitos de **Cálculo Integral**, **Programação em Python** e **Banco de Dados SQLite**, demonstrando como a matemática pode ser utilizada para modelar e resolver problemas reais de estimativa de receita em campanhas publicitárias.

---

## 📄 Licença

Este projeto é destinado para fins educacionais e de estudo.