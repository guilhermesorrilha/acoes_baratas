# O Site das Ações Baratas

*Um guia explicando tudo do zero — sem enrolação e sem palavra difícil sem explicação.*

---

## 1. O que a gente quer construir

Um site que olha todas as empresas da bolsa brasileira e responde uma pergunta:

> **Quais dessas empresas estão sendo vendidas por menos do que realmente valem?**

É a mesma coisa que achar um videogame de R$ 3.000 sendo vendido por R$ 1.200 num bazar. O videogame não ficou pior — só que quem está vendendo não sabe (ou não liga) para o quanto ele vale.

Na bolsa isso acontece o tempo todo. O site vai ser um detector desses casos.

---

## 2. A pegadinha mais importante do documento inteiro

**Preço baixo NÃO é a mesma coisa que barato.**

Leia de novo, porque quase todo mundo erra isso.

| | Banca do João | Banca da Maria |
|---|---|---|
| Preço do pedacinho | **R$ 5** | **R$ 500** |
| Lucro da banca por ano | R$ 500 | R$ 1.000.000 |
| Quantos pedacinhos existem | 1.000 | 1.000 |
| Lucro que cabe a cada pedacinho | R$ 0,50 | R$ 1.000 |

O pedacinho do João custa R$ 5 e te dá R$ 0,50 por ano. Você leva **10 anos** pra recuperar seu dinheiro.

O pedacinho da Maria custa R$ 500 e te dá R$ 1.000 por ano. Você recupera seu dinheiro em **6 meses**.

A ação de R$ 500 é MUITO mais barata que a de R$ 5.

> **Barato não é o preço. Barato é o preço comparado com o que a empresa entrega.**

É exatamente isso que o site vai calcular.

---

## 3. As perguntas que o site vai fazer para cada empresa

A gente não vai usar uma métrica só, porque cada uma tem um ponto cego. Vamos usar 11, organizadas em 4 grupos.

Pensa nisso como uma ficha de avaliação, tipo boletim escolar — só que da empresa.

### 🏷️ Grupo 1 — "Está barato?" (45% da nota)

| Métrica | A pergunta que ela faz, em português |
|---|---|
| **EBIT / EV** | *"Se eu comprasse a empresa INTEIRA hoje — pagando as dívidas dela junto — quanto de lucro ela me devolveria por ano?"* Essa é a melhor de todas. |
| **FCF / EV** | Mesma coisa, mas com **dinheiro de verdade** em vez de lucro no papel. (Explico a diferença no item 4.) |
| **Lucro / Preço** | O clássico: quanto de lucro vem por real investido. |
| **P/VP** | *"Estou pagando mais ou menos do que valem as coisas que a empresa tem?"* (prédios, máquinas, estoque, dinheiro no banco) |

### ⭐ Grupo 2 — "É uma empresa boa?" (30% da nota)

Barato não basta. Uma bicicleta de R$ 50 é barata, mas se a roda está torta e o freio não funciona, você não quer.

| Métrica | A pergunta |
|---|---|
| **ROIC** | *"A cada R$ 100 que essa empresa investe no próprio negócio, quanto volta por ano?"* Se voltam R$ 25, é uma máquina de fazer dinheiro. Se voltam R$ 3, é um negócio ruim. |
| **Margem EBIT** | *"De cada R$ 100 que ela vende, quanto sobra de lucro?"* Mede se ela consegue cobrar caro sem perder cliente. |
| **Consistência** | *"Em quantos dos últimos 5 anos ela deu lucro?"* Cinco de cinco é ótimo. Dois de cinco é bandeira vermelha. |

### 🛡️ Grupo 3 — "Ela está endividada demais?" (20% da nota)

| Métrica | A pergunta |
|---|---|
| **Dívida líquida / EBITDA** | *"Quantos anos de lucro ela precisaria para quitar tudo que deve?"* Até 2 anos é tranquilo. Acima de 4, é sinal de perigo. |
| **Cobertura de juros** | *"O lucro dela dá pra pagar os juros da dívida?"* Se o lucro é R$ 100 e os juros são R$ 90, ela está no sufoco. |
| **Liquidez corrente** | *"Ela tem dinheiro suficiente pra pagar as contas dos próximos meses?"* |

### 🌊 Grupo 4 — "O mercado está fugindo dela?" (5% da nota)

| Métrica | A pergunta |
|---|---|
| **Retorno de 12 meses** | *"A ação está despencando faz um ano?"* |

Esse último parece contraditório num site de ações baratas — afinal, se despencou, ficou mais barata, não é?

É, mas tem um ditado no mercado: *não tente pegar uma faca caindo*. Quando uma ação cai sem parar por um ano inteiro, às vezes é porque muita gente descobriu um problema que ainda não apareceu nos números. Por isso essa métrica entra com peso pequeno — só como um alerta discreto.

---

## 4. Dois detalhes técnicos que valem entender

### Lucro ≠ dinheiro no bolso

A empresa vendeu R$ 1 milhão **fiado**, pra receber daqui a 6 meses. No papel, ela lucrou. No caixa, não entrou um centavo.

Por isso a gente olha o **fluxo de caixa livre** (FCF) além do lucro. Lucro é opinião do contador; caixa é fato. E lucro é bem mais fácil de maquiar.

### Por que a gente vira as contas de cabeça pra baixo

Você já deve ter ouvido falar em "P/L" (preço dividido por lucro). A gente vai usar o **inverso**: lucro dividido por preço.

Motivo: se a empresa tem **prejuízo**, o P/L fica negativo. Um P/L de −5 apareceria no ranking como se fosse mais barato que um P/L de +8, o que é uma bobagem. Já com a conta invertida, o prejuízo vira um número negativo que vai direto pro fim da fila, que é o lugar certo dele.

Detalhe pequeno, mas se você esquecer disso o ranking inteiro fica errado.

---

## 5. O problema de somar coisas diferentes (e como resolver)

Aqui está o coração do projeto.

A ideia original era: *"lucro tem peso 1, dívida tem peso 2, soma tudo"*. A intenção está certíssima, mas tem um problema:

- Lucro da Petrobras: **R$ 80.000.000.000**
- Dívida/EBITDA da Petrobras: **1,2**

Somar isso é somar 80 bilhões com 1,2. O lucro esmaga tudo — a dívida vira poeira na conta, mesmo com peso 2. É como somar a altura de alguém em centímetros com a idade em anos: o resultado não significa nada.

### A solução: nota vira colocação

Pensa na escola. Você tirou 6,5 na prova. Isso é bom ou ruim?

Depende. Se a prova era fácil e a média da turma foi 9, você foi mal. Se era dificílima e a média foi 3, você foi muito bem.

O que realmente informa é a **colocação**: *"você ficou em 5º lugar entre 40 alunos"*.

É isso que a gente vai fazer com cada métrica. Em vez de usar o valor bruto, a gente pergunta:

> "Entre as ~174 empresas que passaram na peneira, em que posição essa aqui está NESSA métrica?"

E converte pra uma nota de 0 a 100, chamada **percentil**:

- Percentil **95** = melhor que 95% das empresas. Excelente.
- Percentil **50** = bem no meio. Mediana.
- Percentil **10** = pior que 90% das empresas. Ruim.

Agora todas as 11 métricas falam a mesma língua — todas viraram notas de 0 a 100. **Aí sim** dá pra somar com pesos.

> Bônus: isso também protege contra malucos. Se uma empresa tem P/L de 900 por causa de um lucro de um centavo, ela simplesmente fica em último lugar. Não estraga a média de ninguém, porque a gente nunca usou o 900 — usou só a posição dela na fila.

---

## 6. A conta final

```
Nota final = (peso₁ × percentil₁ + peso₂ × percentil₂ + ... ) ÷ 100
```

### Exemplo com 3 métricas, pra ficar fácil de acompanhar

Empresa: **Pastelaria do João S.A.**

| Métrica | Colocação dela (percentil) | Peso |
|---|---|---|
| Está barata? (EBIT/EV) | 90 | 50 |
| É boa? (ROIC) | 80 | 30 |
| Está endividada? | 40 | 20 |

```
Nota = (90 × 50) + (80 × 30) + (40 × 20)
     = 4.500 + 2.400 + 800
     = 7.700 ÷ 100
     = 77
```

**Nota 77 de 100.** Barata e boa, mas com uma dívida meio alta puxando pra baixo.

Faz isso com as ~174 empresas, ordena da maior nota pra menor, e pronto: você tem o ranking.

### A tabela de pesos completa

| Métrica | Peso |
|---|---|
| **PREÇO — está barato?** | **45** |
| EBIT/EV | 18 |
| FCF/EV | 12 |
| P/VP | 8 |
| Lucro/Preço | 7 |
| **QUALIDADE — é uma empresa boa?** | **30** |
| ROIC | 15 |
| Margem EBIT | 8 |
| Consistência de lucro | 7 |
| **SAÚDE — está endividada?** | **20** |
| Dívida líquida/EBITDA | 10 |
| Cobertura de juros | 6 |
| Liquidez corrente | 4 |
| **MOMENTUM — está despencando?** | **5** |
| Retorno 12 meses | 5 |
| **TOTAL** | **100** |

Repare: **"estar barato" é só 45% da nota.** Menos da metade!

Isso é de propósito, e é o item 7 que explica por quê.

---

## 7. A armadilha do barato (leia com atenção)

Se você montar o site olhando **só** o preço, o topo do seu ranking vai ser um cemitério.

Casos reais da bolsa brasileira:

- **Americanas** — parecia baratíssima. Tinha um rombo de R$ 20 bilhões escondido na contabilidade. Quebrou.
- **IRB** — parecia baratíssima e ainda inventou que Warren Buffett era sócio. Não era. Despencou 90%.
- **Oi** — parecia barata por anos seguidos. Foi ficando cada vez "mais barata" enquanto afundava.

Todas essas estavam no topo de qualquer ranking de "ação barata". Todas destruíram o dinheiro de quem comprou.

O nome disso é **cilada de valor** (*value trap*): a ação não está barata por um erro do mercado — ela está barata porque a empresa está morrendo, e o mercado sabe disso antes de você.

**Como o site se defende disso:** os outros 55% da nota. Uma empresa em colapso pode até estar baratíssima (percentil 99 no grupo Preço), mas ela vai levar nota baixíssima em ROIC, em consistência de lucro e em dívida. A nota final derruba ela pro meio da tabela.

Barato **e** bom. Nunca só barato.

---

## 8. Freios de emergência

Peso é uma média — e média pode ser "vencida no voto". Uma empresa com dívida catastrófica ainda passaria se fosse barata o suficiente nas outras métricas.

Para riscos graves, em vez de tirar pontos, a gente **corta a nota pela metade**:

| Situação | O que acontece com a nota |
|---|---|
| Dívida acima de 4 anos de lucro | × 0,70 (perde 30%) |
| Lucro mal cobre os juros da dívida | × 0,60 (perde 40%) |
| Deu prejuízo no último ano | × 0,50 (perde metade) |

Uma empresa que caia nos três casos fica com **21%** da nota original. Ela some do ranking, que é exatamente o objetivo.

É aqui que mora aquela ideia inicial de *"dívida tem peso maior"* — só que de um jeito que funciona de verdade.


### ⚠️ Um cuidado com o freio do meio

O freio dos juros tem uma pegadinha que só apareceu quando fomos olhar de onde vem o dado.

Quando uma empresa brasileira pega dinheiro emprestado em dólar, a conta de "despesa financeira" dela não tem só juros dentro. Tem também o efeito do dólar subir ou descer.

Imagina o seguinte. A empresa deve US$ 100. O dólar sobe de R$ 5 para R$ 6. Do nada, a dívida dela em reais aumentou R$ 100 — e isso entra na contabilidade como despesa, mesmo que ela não tenha pago **um centavo a mais de juros**. No ano seguinte o dólar cai, e a mesma conta vira lucro.

Na Petrobras isso é gigante: dos R$ 92,9 bilhões de "despesa financeira" de um ano recente, R$ 60,8 bilhões eram só efeito do dólar. Só uns R$ 32 bilhões eram juros de verdade.

Ou seja: se a gente não separar as duas coisas, uma exportadora saudável leva ×0,60 de castigo num ano de dólar alto — **sem ter piorado em nada**. O freio dispararia pelo motivo errado, e ia derrubar do ranking justamente as empresas que ganham com o dólar alto.

**Como resolver:** quando o dado detalhado existir, usar só a linha de juros de verdade e ignorar a parte do câmbio. O item 12 mostra onde ela fica.

---

## 9. Antes de tudo: a peneira

Nem toda empresa da bolsa entra na conta. Algumas a gente elimina **antes** de calcular qualquer coisa.

| Corta quem... | Por quê | Onde a gente vê isso |
|---|---|---|
| ❌ Quase ninguém negocia (menos de R$ 1 milhão por dia) | Você compra e depois não consegue vender | Coluna `Liq.2meses` do Fundamentus |
| ❌ Deve mais do que tem (patrimônio negativo) | Já está no vermelho por definição | Coluna `Patrim. Líq` |
| ❌ Está em recuperação judicial | Já está oficialmente quebrando | Cadastro da CVM, campo `SIT_EMISSOR` |
| ❌ Listada há menos de 2 anos | Não tem histórico pra avaliar | Formulário FCA da CVM, campo `Data_Inicio_Listagem` |
| ❌ Ação repetida (PETR3 e PETR4) | Senão a Petrobras ocupa duas vagas no ranking | Nome da empresa que aparece na própria tabela |

### ⚠️ A coluna de liquidez tem um nome que engana

A coluna `Liq.2meses` parece dizer "o volume somado de dois meses inteiros".

**Não é isso.** É a **média por dia**, calculada ao longo de dois meses. Já vem dividida.

Dá pra conferir: a PETR4 aparece com 1.455.190.000 nessa coluna. Na página de detalhes da mesma ação, o campo se chama "Vol $ méd (2m)" e mostra 1.455.190.000. Mesmo número, e o nome ali diz "méd" de média.

Por que isso importa: se você achar que precisa dividir por 42 (o número de pregões em dois meses) pra transformar em "por dia", o filtro de R$ 1 milhão passa a deixar entrar só **75 ações** em vez de 196. Você teria jogado fora dois terços da bolsa sem perceber, e o ranking sairia mutilado sem dar nenhuma mensagem de erro.

Esse é o tipo de bug que não trava nada. Só entrega um resultado errado com cara de certo.

### O funil de verdade

Rodei a peneira nos dados reais pra ver quanto sobra. Ela é bem mais agressiva do que "corta uns 60%":

```
993 ações na tabela do Fundamentus
      ↓  volume de pelo menos R$ 1 milhão por dia
196 ações
      ↓  patrimônio líquido positivo
190 ações
      ↓  junta PETR3 com PETR4, BBDC3 com BBDC4, SANB3+SANB4+SANB11...
174 empresas
```

**São ~174 empresas. Não 400.**

Esse número não é curiosidade — ele é o **tamanho da turma** na hora de dar as notas, e o item 5 inteiro depende dele.

Com 174 empresas na fila, cada casinha que uma empresa sobe ou desce vale mais ou menos **0,6 ponto de percentil**. Consequência prática: duas empresas separadas por 2 ou 3 pontos de percentil estão **empatadas**. A diferença entre elas é do tamanho de uma casinha ou duas na fila — não é sinal de nada.

Se o site mostrar uma empresa com nota 71,4 acima de outra com 70,9, ele está fingindo uma precisão que os dados não têm. Vale arredondar a nota final e evitar dar a impressão de que a 12ª colocada é pior que a 11ª.

> Curiosidade útil: dá pra fazer a deduplicação de PETR3/PETR4 sem nenhuma consulta extra. A própria tabela do Fundamentus carrega o nome da empresa escondido em cada linha (aparece como balãozinho quando você passa o mouse). Duas linhas com o mesmo nome = mesma empresa. Fica só a mais negociada.

Esses filtros parecem detalhe burocrático, mas **eles importam mais que os pesos**. É a peneira que impede o ranking de virar lixo.

---

## 10. Banco é um bicho diferente

Todo esse modelo quebra quando você aponta pra um banco.

Por quê? Porque para uma empresa normal, **dívida é problema**. Para um banco, **dívida é o produto**. O dinheiro que você deixa na sua conta é, tecnicamente, uma dívida do banco com você. Um banco sem dívida seria um banco sem clientes.

Se você rodar o modelo principal na bolsa inteira, todo banco vai aparecer no topo por acidente matemático — e não porque está barato.

**Solução:** ranking separado para bancos e seguradoras, com métricas próprias.

| Métrica | Peso |
|---|---|
| P/VP | 30 |
| ROE (quanto rende o dinheiro dos sócios) | 30 |
| Lucro/Preço | 20 |
| Índice de Basileia (colchão de segurança) | 10 |
| Provisão para calote (quanto o banco já separou pra perdas) | 10 |

Mesma lógica de percentil, universo separado.

### Por que "provisão" e não "inadimplência"

A ideia original era medir **inadimplência**: de cada R$ 100 que o banco emprestou, quanto não voltou.

Esse número existe. O Banco Central publica os empréstimos separados por nível de risco, de A (o cliente vai pagar) até H (já era). Bastaria somar os piores níveis.

Só que o endereço que entrega esse dado pra um robô está **vazio**. Testei em todas as combinações de data e tipo de banco, e volta sempre sem nada — enquanto todos os outros relatórios do mesmo lugar respondem normalmente. É um dado que existe na tela do site do Banco Central, mas não sai pela porta automática.

O que sai é uma coisa parecida, e em certo sentido até melhor: a **provisão para perdas**.

Provisão é o dinheiro que o próprio banco separou de lado porque acha que não vai receber. É o banco falando em voz alta:

> *"Desses R$ 100 que emprestei, R$ 4 eu já dou como perdidos."*

Não é a mesma coisa que inadimplência. Inadimplência é o calote que **já aconteceu**; provisão é o palpite do banco sobre o calote que **está vindo**.

E é justamente por ser um palpite — feito por quem olha os clientes de perto todo dia — que ele costuma aparecer **antes**. Um banco que dobra a provisão de repente está avisando que enxergou algo feio no horizonte, meses antes de o calote aparecer nas estatísticas.

Para o nosso propósito, serve bem. A conta é:

```
Provisão para perdas ÷ Total emprestado
```

Os dois números vêm do relatório de Ativo do Banco Central.

> Ficando registrado, pra ninguém se confundir daqui a seis meses: essa métrica é um **substituto** da inadimplência, não o dado original. Se um dia a porta do Banco Central abrir, vale trocar.

**Ideia parecida, mais geral:** comparar cada empresa **dentro do próprio setor**. Empresa de energia elétrica é naturalmente endividada — ela toma empréstimo pra construir usina, é o normal do negócio. Comparar a dívida dela com a de uma empresa de software é injusto. Compare elétrica com elétrica.

---

## 11. O site precisa de servidor?

**Não.** E é melhor que não tenha.

### Por quê

Todo o "banco de dados" do site cabe num arquivo de menos de **100 KB** — menor que uma foto do celular. São ~174 empresas × 20 informações cada. Você manda o arquivo inteiro pro navegador de uma vez, e ele faz ordenação, filtro e busca sozinho, instantaneamente.

Além disso, os dados **não mudam a toda hora**. Os números da empresa saem a cada 3 meses. O preço muda durante o dia, mas atualizar uma vez por dia já é mais que suficiente pra um site desses.

Não existe nada aqui que exija um computador ligado 24 horas respondendo perguntas.

### Como funciona então

```
Uma vez por dia, de madrugada:

   robô acorda
      → busca os dados das ~174 empresas
      → calcula os percentis
      → calcula as notas
      → salva tudo num arquivo: acoes.json
      → publica o site novo

   ...e volta a dormir.
```

O robô é o **GitHub Actions** (de graça). O site fica na **Vercel** (de graça).

Pensa assim: um jornal impresso não precisa de um atendente. Ele é escrito uma vez, impresso, e milhões de pessoas leem o mesmo papel. O site vai ser um jornal, não um atendente.

**Custo total: R$ 0/mês.** E não tem servidor pra cair às 3 da manhã.

### A melhor parte

No arquivo, a gente salva o **percentil de cada métrica** separadamente — não só a nota final:

```json
{
  "ticker": "PETR4",
  "nome": "Petrobras",
  "setor": "Petróleo e Gás",
  "nota": 87.3,
  "percentis": {
    "ebit_ev": 94,
    "roic": 78,
    "fcf_ev": 91,
    "div_ebitda": 62
  },
  "valores_reais": {
    "pl": 4.2,
    "roic": 0.22,
    "div_ebitda": 1.1
  }
}
```

Com isso, o **usuário pode mexer nos pesos**.

Botou uns controles deslizantes na tela: *"quero que dívida importe mais"*, arrasta pra cima, e o ranking se reorganiza **na hora**. Sem recarregar, sem esperar, sem servidor.

Funciona porque recalcular é só multiplicar e somar — 174 empresas × 11 métricas = menos de 2.000 continhas. Seu celular faz isso em menos de 1 milésimo de segundo.

Essa é provavelmente a coisa mais legal do site inteiro: **"monte seu próprio conceito de barato"**. E ela é 100% grátis de rodar.

### Quando aí sim vai precisar de servidor

| Quero fazer... | Precisa de servidor? |
|---|---|
| Ranking, filtro, ordenar tabela | Não |
| Usuário mexer nos pesos | Não |
| Salvar os pesos favoritos do usuário | Não (fica salvo no navegador) |
| Gráfico da nota da empresa ao longo do tempo | **Sim** — precisa guardar histórico |
| Login, carteira pessoal, alerta por email | **Sim** |
| Cobrar assinatura / esconder os dados | **Sim** |

Nada disso é pro começo.

---

## 12. De onde vêm os dados

Aqui teve uma surpresa, e vale contar direito porque ela muda o plano.

### O que a gente achava

O plano era: pega tudo do **Fundamentus** (`fundamentus.com.br/resultado.php`), que entrega uma tabela pronta com a bolsa inteira, e em um dia de trabalho o ranking está no ar.

### O que apareceu quando foi conferir

O Fundamentus entrega **993 ações numa única visita à página**, com 22 colunas. É excelente, é de graça, e continua sendo a base do projeto.

Mas ele cobre **70 dos 100 pontos** da nota. Faltam 30.

**As 7 métricas que ele resolve direto:**

| Métrica | Peso | Coluna |
|---|---|---|
| EBIT/EV | 18 | `EV/EBIT`, virado de cabeça pra baixo |
| ROIC | 15 | `ROIC` |
| P/VP | 8 | `P/VP` |
| Margem EBIT | 8 | `Mrg Ebit` |
| Lucro/Preço | 7 | `P/L`, virado de cabeça pra baixo |
| Liquidez corrente | 4 | `Liq. Corr.` |
| ROE (ranking dos bancos) | — | `ROE` |

**A que dá pra montar juntando peças (peso 10):**

A **Dívida Líquida / EBITDA** não tem coluna própria. Mas todas as peças estão na mesa — é só remontar:

```
Valor de mercado  = P/VP × Patrimônio Líquido
Dívida líquida    = (Dív.Líq/Patrim) × Patrimônio Líquido
Valor da firma    = Valor de mercado + Dívida líquida
EBITDA            = Valor da firma ÷ (EV/EBITDA)

E aí:  Dívida líquida ÷ EBITDA
```

Testei na Petrobras e comparei com o que o próprio site mostra na página dela:

| | Nossa conta | O que o site diz |
|---|---|---|
| Valor de mercado | R$ 572,3 bi | R$ 571,2 bi |
| Dívida líquida | R$ 312,6 bi | R$ 312,8 bi |
| Valor da firma | R$ 884,9 bi | R$ 884,0 bi |

Erra só na terceira casa, porque o `P/VP` vem arredondado com duas casas decimais. Como a gente só usa esse número pra colocar a empresa em ordem na fila (item 5), esse errinho não muda nada.

**O que ele NÃO tem — 30 pontos de peso:**

| Faltando | Peso |
|---|---|
| FCF/EV | 12 |
| Consistência de lucro em 5 anos | 7 |
| Cobertura de juros | 6 |
| Retorno de 12 meses | 5 |

Mais o **setor** da empresa, e dois dos filtros do item 9: **recuperação judicial** e **idade de listagem**.

> ⚠️ Cuidado com uma armadilha aqui. O Fundamentus tem uma coluna chamada `Cresc. Rec. 5a`, e é muito tentador achar que ela resolve a "consistência de lucro". **Não resolve.** Ela mede **receita** — quanto a empresa vendeu. A gente precisa de **lucro** — quanto sobrou. São coisas bem diferentes: dá pra vender cada vez mais e perder dinheiro em cada venda. Foi assim que várias empresas quebraram parecendo saudáveis.

### A porta trancada

O Fundamentus até tem os balanços históricos completos. Tem um botão "Balanços em Excel" na página de cada empresa.

Fui lá conferir. A página é protegida por **CAPTCHA** — aquela figura com letras tortas que você tem que digitar pra provar que é gente. A mensagem é literalmente *"Digite os caracteres que você vê na figura abaixo"*.

CAPTCHA existe exatamente pra impedir robô. E o nosso robô roda de madrugada, sozinho, sem ninguém pra digitar nada.

**Então o histórico do Fundamentus está fora do jogo.** E isso explica por que aqueles 30 pontos faltam: fluxo de caixa, consistência de lucro e cobertura de juros dependem os três de balanço histórico. Não é que o Fundamentus não tenha — é que ele não deixa pegar automaticamente.

### Existe um site que tenha tudo de graça?

Resposta curta: **não.** Procurei e testei os dois candidatos óbvios.

- **brapi.dev** — o plano grátis dá 15 mil consultas por mês, o que seria de sobra pra 174 empresas. O problema é outro: balanço, resultado e fluxo de caixa **só vêm no plano pago**. Ou seja, justamente o que falta é o que não é de graça.
- **StatusInvest** — tem uma porta aberta que devolve **617 ações com 38 informações de uma vez só**, e em alguns pontos ganha do Fundamentus: já vem com o setor da empresa, com a liquidez diária pronta pra usar e com a dívida já dividida. Mas continua sem fluxo de caixa, sem cobertura de juros, sem consistência de lucro e sem o retorno de 12 meses.

Nenhum dos dois fecha a conta sozinho. Então a gente monta a fonte com peças.

### As 6 peças — todas gratuitas, nenhuma pede cadastro

**1. Fundamentus** — a base: as 8 métricas do quadro acima, numa visita só.
*(O StatusInvest pode entrar no lugar dele, ou ficar de reserva pra quando o Fundamentus estiver fora do ar. Cobre o mesmo e traz o setor de brinde.)*

**2. CVM — Dados Abertos** — resolve os três buracos grandes: 25 dos 30 pontos que faltavam.

A CVM é o órgão do governo que fiscaliza a bolsa. Por lei, toda empresa listada é obrigada a entregar os balanços pra ela. E a CVM publica tudo, de graça, em arquivos que qualquer um baixa direto:

```
dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2025.zip
```

São 13 MB com os balanços de **424 empresas** — e existe um arquivo desses para cada ano desde 2010.

| O que sai de lá | Como |
|---|---|
| **Fluxo de caixa livre** | Dinheiro que entrou da operação (conta `6.01`) menos o que ela gastou comprando máquina e construindo fábrica (contas `6.02.xx`) |
| **Cobertura de juros** | Lucro operacional (conta `3.05`) dividido pela despesa financeira (conta `3.06.02`) |
| **Consistência de lucro** | Lucro líquido (conta `3.11`), ano a ano, desde 2010 |

Essa é a fonte mais confiável de todas. É o número oficial, entregue pela própria empresa, com auditor assinando embaixo. Nenhum site intermediário no meio pra errar a digitação.

**3. CVM — Formulário FCA** — a lista de ações de cada empresa. É ele que diz, oficialmente, que PETR3 e PETR4 pertencem ao mesmo CNPJ. E traz a data em que cada ação começou a ser negociada, que resolve o filtro dos 2 anos do item 9.

**4. CVM — Cadastro das companhias** — tem um campo chamado `SIT_EMISSOR` que diz, com todas as letras, `EM RECUPERAÇÃO JUDICIAL OU EQUIVALENTE`. Hoje são 40 empresas nessa situação — e a Americanas, do item 7, é uma delas.

Repare como isso é bom: aquele filtro que parecia o mais difícil de todos ("como é que eu vou saber quem está em recuperação judicial?") acabou sendo um campo pronto, oficial, atualizado pelo próprio governo.

**5. Yahoo Finance** — o preço da ação ao longo do tempo, pro retorno de 12 meses:

```
query1.finance.yahoo.com/v8/finance/chart/PETR4.SA?range=1y&interval=1mo
```

Grátis, sem cadastro, responde na hora.

**6. Banco Central — IF.data** — as métricas dos bancos do item 10. O Índice de Basileia vem pronto, e a provisão para perdas também.

### Duas armadilhas nos dados da CVM

Vale conhecer as duas antes de começar, porque **nenhuma delas dá erro**. O número sai bonitinho — só sai errado.

**Armadilha 1: cada empresa dá o nome que quer pra conta de investimento.**

As contas principais da CVM são padronizadas. `3.05` é lucro operacional em todas as empresas, `6.01` é caixa da operação em todas. O próprio arquivo confirma isso com uma marquinha (`S` de "conta fixa"). Nessas você pode confiar de olhos fechados.

Só que a conta de **CAPEX** — o dinheiro gasto comprando máquina e construindo fábrica, que a gente precisa pra calcular o fluxo de caixa livre — vem marcada com `N`. Quer dizer: **cada empresa escreve o nome que quiser**. Uma escreve "Aquisições de ativos imobilizados e intangíveis". Outra escreve "Investimentos em imobilizado". Outra inventa um terceiro nome.

Então esse pedaço não dá pra pegar pelo número da conta. Vai ter que ser lendo o texto e caçando as palavras "imobilizado" e "intangível".

Funciona — mas é **o ponto mais frágil de toda a coleta**, e é o único lugar do projeto onde um erro passa completamente despercebido. Se o robô não achar a linha de CAPEX de uma empresa, ele vai calcular o fluxo de caixa livre como se ela não tivesse gastado nada com máquinas. A empresa aparece rica, sobe no ranking, e ninguém desconfia.

Vale conferir na mão as 20 maiores antes de confiar no resto.

**Armadilha 2: "despesa financeira" não é só juros.**

Já expliquei no item 8, mas repito aqui porque é neste ponto que o dado é lido: a linha `3.06.02` mistura os juros da dívida com o efeito do dólar subindo e descendo. Quando existir a linha detalhada `3.06.02.01`, use ela — é a que separa as duas coisas.

---

## 13. Uma coisa pra não esquecer

**Guarde o arquivo de todo dia**, desde o primeiro:

```
data/2026-08-18.json
data/2026-08-19.json
data/2026-08-20.json
...
```

Custa quase nada de espaço. E daqui a alguns meses você vai ter uma coisa valiosa: o histórico.

Com histórico, dá pra fazer a pergunta que muda tudo:

> *"As empresas que tiraram nota alta há 12 meses realmente subiram mais que as outras?"*

Se sim, o modelo funciona. Se não, dá pra descobrir **quais métricas** estavam acertando e quais estavam só atrapalhando — e ajustar os pesos com base em evidência, não em achismo.

Hoje os pesos da tabela do item 6 são um **chute bem informado**. Isso é normal e honesto pra uma versão 1. Mas com histórico eles deixam de ser chute.

⚠️ **Se você não começar a guardar agora, esse dado não volta.** Não existe jeito de recuperar depois qual era a nota de uma empresa em agosto de 2026 se você não salvou em agosto de 2026.


### E tem um segundo motivo, que só apareceu agora

A CVM **republica** balanço.

Quando uma empresa refaz as contas — porque achou um erro, porque o auditor mandou, ou porque alguém estava escondendo alguma coisa — ela reapresenta o balanço. O arquivo da CVM passa a ter a versão nova, e a versão velha some do site.

Pensa no que isso significa pro seu arquivo diário.

Se você guardar o arquivo de todo dia, você não está guardando só "qual era a nota da empresa em agosto". Você está guardando **quais eram os números antes de a empresa mudar a história**.

E esse é exatamente o rastro que a Americanas e o IRB deixaram — os casos do item 7. O número estava lá, publicado, assinado pelo auditor. Depois mudou.

Quem tinha o arquivo antigo conseguiu comparar e ver o tamanho da mudança. Quem não tinha, ficou só com a versão nova, que é a versão que a empresa quis contar.

---

## 14. Resumo em 10 linhas

1. Ação é um pedacinho de empresa.
2. Preço baixo ≠ barato. Barato é preço baixo **em relação ao que a empresa entrega**.
3. A gente mede 11 coisas: se está barata, se é boa, se está endividada, se está despencando.
4. Não dá pra somar bilhões com 1,2 — então cada métrica vira uma **colocação de 0 a 100**.
5. Aí sim aplica os pesos e soma. Sai uma nota de 0 a 100.
6. "Barato" vale só 45% da nota — os outros 55% existem pra fugir das ciladas.
7. Riscos graves não tiram pontos: **cortam a nota pela metade**.
8. Antes de tudo, peneira: fora quem não é negociado, quem está quebrando, quem está repetido.
9. Banco tem ranking próprio, porque pra banco dívida é o produto.
10. Site estático, robô roda 1x por dia, custo zero, e o usuário pode mexer nos pesos ao vivo.

---

## Próximo passo

Construir o robô: buscar os dados, calcular os percentis, gerar o `acoes.json`.

Depois, a tela.
