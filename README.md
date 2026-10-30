# Projeto 4 — Calculadora Simples

> Recebe dois números e um operador e mostra o resultado, como uma calculadora de bolso, só que colorida e com teclas no terminal.

| | |
|---|---|
| **Tema** | Algoritmos |
| **Nível** | Iniciante |
| **O que pratica** | Entrada e saída de dados, variáveis, tipos de dados, `if/elif/else` e tomada de decisões |

---

## 📸 Visual

```
            CALCULADORA
        calculadora de bolso

       +      -      *      /
      soma  menos  vezes   div

  1  Primeiro número: 10
  2  Segundo número: 3
  3  Operador (+ - * /): /

  [ faixa cinza ]
                          10 / 3
  [ faixa cinza ]

  ✔ RESULTADO  3.33
```

No terminal ele é colorido: barra de título azul, uma tecla de cada cor para cada operação, passos numerados em azul, visor em cinza e uma etiqueta verde (sucesso) ou vermelha (erro) no final.

## 🚀 Como rodar

Você só precisa do **Python 3.6 ou superior**. Não há nada para instalar.

```bash
python main.py
```

> 💡 Use o terminal do VS Code ou o Windows Terminal para ver as cores e os símbolos corretamente.

## 🎮 Como usar

O programa pergunta três coisas, uma de cada vez e **nesta ordem**:

| Ordem | Informação | Valores aceitos |
|:---:|---|---|
| 1 | Primeiro número | Qualquer número, inteiro ou decimal (decimais com **ponto**, como `2.5`) |
| 2 | Segundo número | Qualquer número, inteiro ou decimal |
| 3 | Operador | `+` soma, `-` subtração, `*` multiplicação ou `/` divisão |

### Exemplos

| Entradas (na ordem) | O programa exibe |
|---|---|
| `8`, `2`, `+` | `10` |
| `3`, `5`, `-` | `-2` |
| `1.5`, `2`, `*` | `3` |
| `7`, `2`, `/` | `3.5` |
| `10`, `3`, `/` | `3.33` |
| `10`, `0`, `/` | `Não é possível dividir por zero` |
| `5`, `3`, `%` | `Operador inválido` |

Os resultados inteiros aparecem **sem casa decimal** (`10` em vez de `10.0`) e os decimais com **no máximo 2 casas** (`3.33` em vez de `3.3333333333333335`).

## 🧠 Como o código funciona

Como pede o enunciado, o programa **não usa funções próprias**. Tudo é resolvido com o que já foi estudado, em blocos:

1. **Cores**: constantes com os códigos ANSI (as mesmas do `cores.py`, copiadas para o arquivo funcionar sozinho).
2. **Cabeçalho**: título e teclas, montados com `print()` e `.center()`.
3. **Entrada de dados**: três `input()`, na ordem do enunciado. Os números viram `float()`.
4. **Cálculo**: um `if/elif/else` escolhe a operação. Na divisão, um `if` interno confere se o segundo número é zero.
5. **Saída**: o resultado (ou a mensagem de erro) é a **última coisa exibida**, em uma única linha. Por isso a etiqueta colorida vem **antes** do valor, e nada é impresso depois dele.

## ✅ Testes

O arquivo `teste.py` (do professor) roda 14 testes automáticos: somas, subtrações, multiplicações, divisões, divisão por zero, operador inválido e a regra de não criar funções próprias.

```bash
pip install pytest
python -m pytest teste.py
```

> Rode o comando dentro da pasta do projeto, porque os testes abrem o `main.py` que está ao lado deles.

---
---

# Projeto 5 — Calculadora Aprimorada (Novo!)

> Evolução do projeto anterior: agora feita de funções que trabalham com vários números de uma vez, respeitando a ordem das operações (BODMAS) e com o mascote CalcCat no terminal!

| | |
|---|---|
| **Tema** | Algoritmos |
| **Nível** | Iniciante |
| **O que pratica** | Funções, fluxo de controle, listas, laços `while` e ordem das operações (BODMAS) |

---

## 📸 Visual (Projeto 5)

```
            CALCULADORA INFINITA (BODMAS)
          Construa sua conta passo a passo

     /\_/\ 
    ( o.o )  Olá! Eu sou o CalcCat!
     > ^ <   Vamos montar uma conta juntos?

  ➜ Digite o 1º número: 1
  -------------------------------------------------
  ➜ Operador (+, -, *, /) ou '=' para calcular: +
  ➜ Digite o próximo número: 3
  -------------------------------------------------
  ➜ Operador (+, -, *, /) ou '=' para calcular: *
  ➜ Digite o próximo número: 4
  -------------------------------------------------
  ➜ Operador (+, -, *, /) ou '=' para calcular: =

  [ visor cinza escuro ]
                                        1 + 3 * 4
  [ visor cinza escuro ]

  ✔ RESULTADO FINAL  13

  CalcCat analisou o seu resultado:
  • Não é um número Par.
  • É um número Inteiro.
```

O terminal ganhou uma paleta renovada: cabeçalho em roxo, mascote em amarelo, passos com setas em ciano e o resultado em destaque verde.

## 🚀 Como rodar (Projeto 5)

Para rodar a versão nova e aprimorada, use o arquivo `main2.py`:

```bash
python main2.py
```

## 🎮 Como usar (Projeto 5)

O programa permite montar a conta do tamanho que você quiser, interativamente:

| Ordem | Informação | Valores aceitos |
|:---:|---|---|
| 1 | Número | Qualquer número, inteiro ou decimal |
| 2 | Operador | `+`, `-`, `*`, `/` ou `=` para ver o resultado |
| 3 | Repetição | Continua pedindo número e operador até você digitar `=` |

### Exemplos

| Entradas (na ordem) | O programa exibe |
|---|---|
| `5`, `+`, `10`, `+`, `15`, `=` | `30` |
| `2`, `*`, `5`, `=` | `10` |
| `1`, `+`, `3`, `*`, `4`, `=` | `13` *(BODMAS: multiplica 3*4 primeiro)* |
| `10`, `/`, `0`, `=` | `Não é possível dividir por zero` |

## 🧠 Como o código funciona (Projeto 5)

Desta vez, o programa é modular, feito com **4 funções obrigatórias**:

1. `somarmultiplosnumeros(numeros)`: soma toda a lista.
2. `multiplicarmultiplosnumeros(numeros)`: multiplica toda a lista.
3. `ehinteiro(numero)`: devolve `True` se for inteiro, `False` se não for.
4. `ehpar(numero)`: devolve `True` se for par e inteiro.

O programa principal lê as entradas num laço de repetição (`while`) e salva tudo numa lista (ex: `[1, '+', 3, '*', 4]`). Depois, usa as funções para resolver primeiro as multiplicações/divisões e, em seguida, as somas/subtrações (Regra BODMAS).

---

## 🎨 Como personalizar

Tudo que é visual fica no topo dos arquivos `main.py` e `main2.py`:

- **Tamanho da barra e do visor**: mude `LARGURA = 36` (no main) ou `LARGURA = 50` (no main2).
- **Cores e Mascote**: troque as constantes ANSI de fundo/frente. No `main2.py`, você pode até mudar o desenho ASCII do gatinho.
- **Casas decimais**: no `main.py`, troque o `2` em `round(resultado, 2)`.

Se aparecer `?` no lugar dos símbolos (`✔ ✖ ➜`), é a fonte do terminal. Troque por `v`, `x` e `->`.

## 📁 Arquivos

```
04_calculadora_simples/
├── main.py     # a calculadora original (Projeto 4)
├── main2.py    # a calculadora aprimorada (Projeto 5)
├── README.md   # este arquivo com a documentação unida
└── teste.py    # testes automáticos (do professor)
```

## 👩‍💻 Autoria

Feito por **Beatris Antunes Silva** durante o Bootcamp de Análise de Dados da **Generation Brasil**.