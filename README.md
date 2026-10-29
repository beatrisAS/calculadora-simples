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

## 🎨 Como personalizar

Tudo que é visual fica no topo do `main.py`:

- **Tamanho da barra e do visor**: mude `LARGURA = 36`.
- **Cor das teclas**: troque a constante de fundo (por exemplo, `FUNDO_VERDE_CLARO` por `FUNDO_AZUL_CLARO`). Para ver todas as cores disponíveis, rode o `cores.py` das aulas.
- **Casas decimais**: troque o `2` em `round(resultado, 2)`.

Se aparecer `?` no lugar dos símbolos (`✔ ✖`), é a fonte do terminal. Troque por `v` e `x`.

## 📁 Arquivos

```
04_calculadora_simples/
├── main.py     # a calculadora
├── README.md   # este arquivo
└── teste.py    # testes automáticos (do professor)
```

## 👩‍💻 Autoria

Feito por **Beatris Antunes Silva** durante o Bootcamp de Análise de Dados da **Generation Brasil**.
