# 14 — Order bumps e upsell

Objetivo: aumentar o ticket médio com **3 order bumps** no checkout e **1 upsell** numa página própria depois da compra. Em tráfego pago de low ticket, é isso que faz a conta fechar: com o produto principal sozinho, o CPA de empate é quase o preço do produto.

## Quando fazer

- No pré-voo (`00-inicializacao.md`) perguntar: **"Quer que eu já crie os order bumps e o upsell?"**. Registrar em `estado.json` → `extras.fazer`.
- Se **sim**: executar esta fase logo depois da fase 08 (checkout principal criado), antes do QA da fase 09.
- Se **não**: deixar só as propostas no briefing (nome, preço, status "proposta").
- Também pode ser pedido depois, para um produto que já está rodando. Nesse caso, ler o `estado.json` do lançamento e seguir daqui.

## 1. Pesquisar e escolher (sem pedir aprovação)

Para cada bump e para o upsell, a pergunta é: **o que o comprador vai precisar logo depois de usar o produto principal, que o principal não entrega?**

- Ler o briefing e o manifesto do principal para não repetir conteúdo.
- Pesquisar na Biblioteca de Anúncios e na web o que concorrentes do nicho oferecem como bump e upsell (complementos, kits, "pacote completo").
- Critérios: complemento natural, produção viável com qualidade, entrega em **um arquivo** quando possível (facilita o tipo E-book na Wiapy), e promessa honesta.

**Faixas de preço padrão** (ajustar ao preço do principal):

| Item | Preço | Exemplo (calculadora de precificação, R$ 19,90) |
|---|---|---|
| Bump 1 (o mais forte) | R$ 9,90 | Planilha Controle de Encomendas e Caixa |
| Bump 2 | R$ 7,90 | Etiquetas Prontas para Doces e Bolos (PDF preenchível) |
| Bump 3 | R$ 7,90 | Tabela de medidas e rendimentos (PDF) |
| Upsell | R$ 24,90 a R$ 27 | Guia Encomendas o Ano Todo (calendário + 60 legendas + plano 30 dias) |

Regras: o bump não pode ser condição para receber o que foi anunciado; o upsell é sempre opcional e a recusa tem que ser clara e fácil.

## 2. Produzir os entregáveis

Seguir `03-entregaveis.md` (qualidade, revisão, manifesto), com pasta própria para cada extra:

```text
lancamentos/AAAA-MM-DD-slug/extras/
  bump1-<slug>/   bump2-<slug>/   bump3-<slug>/   upsell-<slug>/
  src/            (HTML/CSS/scripts que geram os arquivos)
  manifesto-extras.md
```

Técnicas que funcionaram:
- **Planilha** (openpyxl): mesma identidade visual do principal, células amarelas para preencher, fórmulas clássicas (SUMIFS, COUNTIFS, EOMONTH), listas suspensas, formatação condicional. Recalcular no LibreOffice e conferir 0 erros e os exemplos à mão.
- **PDF de leitura** (HTML + CSS do principal → `google-chrome --headless --print-to-pdf`): capa, seções curtas, tabelas. Conferir o número de páginas e se nada transbordou para uma folha vazia.
- **PDF preenchível** (reportlab + pypdf): campos AcroForm. Para "digite uma vez e a folha toda preenche", campos com o mesmo nome precisam virar **um campo pai com várias kids** (pós-processar com pypdf) e o AcroForm precisa de `/NeedAppearances true` e `/DR` com a fonte Helvetica. Testar preenchendo por script e renderizando.
- Dados técnicos (medidas, datas, legislação): pesquisar e conferir. Datas do calendário de vendas conferidas com código (ex.: Páscoa, Dia das Mães = 2º domingo de maio).

## 3. Imagens no ChatGPT

Para cada extra: **thumb quadrada** (1:1, ≤ 1 MB, para a Wiapy e para a caixinha do bump) e, para o upsell, **mockup** do produto e prévias em mockup para o carrossel. Mandar ao ChatGPT as páginas reais renderizadas como referência (regra geral: nada de print cru na página).

## 4. Wiapy: conteúdos entregáveis dos extras

Para cada bump e para o upsell: **Produtos → Conteúdos entregáveis → CRIAR CONTEÚDO** (`08-wiapy.md`, seção 1).
- Um arquivo → tipo **E-book** (PDF/XLSX). Vários → Drive + **Link enviado por E-mail**.
- Campos: Nome (= nome do produto), Descrição curta, Categoria, **Capa 1080x1920** (≤2 MB: imagem quadrada do GPT centralizada num fundo vertical, script `vert.py`), explicação com **mínimo 100 caracteres** → SALVAR.
- Depois de salvo aparecem as abas Configurações / **Arquivos** / Visualizar. Em Arquivos → **Novo Arquivo** → nome + arquivo (via repositório privado + postMessage) → SALVAR.
- Cuidado ao injetar arquivo por JS: a página tem também o input de anexo do **chat de suporte** (`name="attach_file"`, sem `accept`). Escolher sempre o input cujo `accept` contém `pdf`/`jpg`.

**Order bump NÃO precisa de checkout próprio**: ele aponta direto para o conteúdo entregável. Só o upsell vira produto com checkout.

## 5. Wiapy: Order Bumps (recomendado 3)

1. **Produtos → aba Orderbumps → CRIAR ORDERBUMP** (`/producer/checkout/orderbump`). Campos:
   - **Título\* (máx. 40 caracteres)** = **o nome do produto** (ex.: "Controle de Encomendas e Caixa"). Não usar "Sim! Quero… por R$ X": o usuário quer o nome do produto, e frases longas são cortadas no limite de 40.
   - Descrição: 1 linha do benefício.
   - **Conteúdo entregável do Orderbump**: digitar o nome e clicar na linha do conteúdo (não na primeira linha verde "Adicionar novo produto").
   - **Valor\*** e **Valor promocional fictício\*** (aparece riscado como "De"): colocar o **mesmo valor** nos dois, para não inventar desconto.
   - Thumbnail 1:1, ≤1 MB (a imagem do GPT em 1080 jpg) → SALVAR.
2. Vincular: abrir o **produto principal** (Produtos → Produtos → ícone configurar) → menu **Orderbumps** → selecionar os 3 na ordem (mais forte primeiro).
3. **CTA para Orderbumps**: o padrão da Wiapy é "APROVEITE E LEVE JUNTO COM 90% DE DESCONTO" — trocar por um texto sem desconto falso (ex.: "APROVEITE E LEVE JUNTO COM SEU PRODUTO"). Deixar desligado "selecionar todos de uma vez" → SALVAR.
4. A caixinha já vem desmarcada ("Adicionar oferta"). Conferir no link do checkout que os 3 aparecem com nome, imagem e preço certos.
5. Nunca editar os orderbumps de outros produtos do usuário (filtrar a lista pelo título dos seus).

## 6. Upsell: página própria + Wiapy

### 6.1 Site do upsell
- Criar um **site novo** na pasta raiz do projeto (ex.: `lancamentos/.../upsell/` ou uma pasta `upsell/` no repositório do lançamento), com `index.html` (oferta) e `obrigado.html` (para quem recusa).
- Modelo pronto: `assets/modelo-upsell.html` (exemplo preenchido). Estrutura, nesta ordem:
  1. Faixa no topo ("Oferta para quem acabou de comprar…")
  2. Selo "Compra confirmada!" + headline curta (2–3 linhas) + sub
  3. Mockup do produto (GPT)
  4. Card da oferta: tag, nome, preço grande, "pagamento único", lista de 5–6 itens com check, **CTA verde** e **link de recusa** logo abaixo
  5. Garantia de 7 dias
  6. "Veja por dentro": abas + carrossel com 4 prévias (mockups GPT das páginas reais)
  7. Bloco "Por que agora?", CTA final + recusa, FAQ curto, rodapé com suporte
- Scripts de tracking do **mesmo dashboard** do produto principal (UTMizey: `utmizey.js` + `pixel.js`).
- O script da página repassa a query string (UTMs) para o link do checkout do upsell e para o `obrigado.html`.
- **Cronômetro opcional:** só se o usuário pedir. Se pedir, deixar claro no texto o que ele mede (ex.: "esta oferta fica nesta página por 10 minutos").
- Depoimentos só de clientes reais e autorizados. Sem eles, a seção de prova mostra as prévias do material.
- `noindex` no `<head>`; sem barra flutuante, salvo pedido do usuário.

### 6.2 Publicar
- Projeto Vercel próprio, domínio curto sem hífen (ex.: `meuprodutoplus.vercel.app`).
- Se não for possível criar um repositório novo, colocar o site numa pasta `upsell/` do repositório privado do lançamento e criar o projeto Vercel com **Root Directory = `upsell`** .

### 6.3 Ligar na Wiapy
1. Criar o upsell como **produto normal**: Produtos → aba Produtos → **CRIAR PRODUTO**: Título (≤40), Descrição, conteúdo entregável, Pagamento único, Pix + cartão, Valor, parcelas 1x, **URL da Página de Vendas = URL da página do upsell**, e-mail de suporte, **Nome de Exibição** (copiar do produto principal), tema, thumb 1:1 → SALVAR.
2. Ao salvar, a Wiapy pode abrir **"Confirmar e-mail de suporte"** com código de 6 dígitos enviado para o e-mail. **Não pedir o código ao usuário**: fechar o modal e avisar que ele precisa confirmar o e-mail no produto (sem isso o checkout não recebe vendas).
3. No produto do upsell → menu **Links** → copiar a **Oferta Principal** e colocar em `UPSELL_CHECKOUT` na página do upsell. Publicar de novo.
4. No **produto principal** → menu **Upsells** → ligar **"Página de obrigado ou upsell externo? Habilitar"** (é o "Upsell por URL") → **URL da página** = `https://<dominio>.vercel.app/` → SALVAR.
5. Conferir que o produto principal continua ativo e com o checkout de sempre.

## 7. QA dos extras

- Checkout principal em aba anônima: 3 bumps visíveis, preços somam certo no total.
- Página do upsell: abre no celular, CTA vai para o checkout do upsell levando as UTMs, recusa vai para o `obrigado.html`.
- Se houver compra de teste autorizada: confirmar redirecionamento pós-compra para o upsell e e-mails de entrega de cada extra. Sem autorização, registrar como "não testado com compra real".
- No UTMizey, vendas dos extras entram no mesmo dashboard (o webhook da Wiapy precisa incluir os produtos dos extras: criar uma integração **nova** só com eles, nunca editar a existente; ver REGRA CRÍTICA).

## 8. Registro

`estado.json` → `extras`: para cada bump/upsell, nome, preço, arquivo, ID/link do produto e checkout na Wiapy, status (criado / vinculado / testado). URL do site do upsell, projeto Vercel, e se o "Upsell por URL" está ligado.
