# 08 — Checkout Wiapy: arquivos, produto, visual, link e webhook de vendas

## Pré-requisitos

- Produto principal **já produzido e revisado** (fase 03).
- Imagem de capa/thumbnail **real**, quadrada e, para checkout quando requerido, <= 1 MB.
- URL **real** da página de vendas na Vercel (fase 06).
- Base de tracking configurada na fase 07 (Pixel, integração Meta e dashboard).
- E-mail de suporte indicado no pré-voo.
- Acesso Wiapy legitimamente autenticado; **não comprar/contratar serviço** sem autorização.

## 1. Criar conteúdo entregável

No painel Wiapy, procurar **Produtos → Conteúdos Entregáveis** (ou o nome efetivamente existente na interface). Criar um conteúdo/produto digital com:

- Nome exato do produto.
- Descrição breve e conteúdo real.
- Capa feita pelo ChatGPT e comprimida para o limite que o formulário efetivamente indicar.
- Upload dos arquivos do `produto/entregaveis/` ou `produto/entrega-final.zip` quando suportado, com relação clara do que o comprador obtém.
- Conferir o upload abrindo/previsualizando; testar que o arquivo não ficou privado/indisponível ao cliente por configuração errada.

### Tipo de entregável (perguntar ao usuário no pré-voo)
- O tipo do conteúdo **não pode ser alterado** depois de criado, e o tipo **E-book** aceita só **um** arquivo.
- **Drive (padrão para mais de um arquivo):** criar a pasta do produto no Google Drive **da conta Google informada no pré-voo** (`conta_google_drive`; conferir o avatar antes), subir todos os arquivos (método do repositório GitHub privado + postMessage descrito no SKILL.md), compartilhar como **"Qualquer pessoa com o link – Leitor"** e testar em aba anônima. Na Wiapy, criar o conteúdo do tipo **"Link enviado por E-mail"** com o link da pasta (`…/folders/<id>?usp=sharing`), nome do produto, descrição e capa.
- **Arquivo único:** tipo E-book com o PDF/XLSX anexado.
- Se você criou um conteúdo do tipo errado, desativar só esse conteúdo (que você criou) para não aparecer duplicado no seletor do checkout; nunca mexer em conteúdos de outros produtos.

Se o painel não tiver esse caminho, localizar **Como cadastrar um produto** na ajuda Wiapy e seguir a nomenclatura atual. Não simular entrega.

## 2. Criar checkout

No painel procurar **Checkout → Criar checkout**, ou **Produtos → Produtos** se a sessão apresentar o fluxo descrito pelo usuário; seguir a interface real, sem adivinhar. A documentação da Wiapy registra checkout vinculado a um produto **já cadastrado**.

Preencher:

- Título: nome descritivo, observando limite do formulário (a ajuda pública cita **40 caracteres** para o título).
- Descrição objetiva.
- **Produtos do checkout:** selecionar o produto entregável correto.
- **Tipo de pagamento:** pagamento único, a menos que oferta aprovada preveja assinatura real.
- **Valor:** preço exato do briefing (R$ 10–29).
- Meios de pagamento (Pix/cartão) apenas os efetivamente disponíveis; parcelas coerentes.
- **URL da Página de Vendas:** colar o `.vercel.app` verificado na fase 06.
- **E-mail de suporte:** usar somente o e-mail autorizado; não inserir e-mail privado não designado para suporte.
- Tema light/dark e miniatura quadrada válida. Salvar e verificar mensagem de sucesso.

## 3. Edição visual

Abrir checkout recém-criado → **Editar visual**. Preferir layout limpo, mobile, capa e banner autorais.

- Adicionar **banner no topo** produzido pelo ChatGPT em resolução compatível com o editor; revisar texto e corte no mobile.
- **Cronômetro no topo:** só se o usuário pedir, configurado de forma coerente com o prazo informado.
- Ajustar cores e descrições para refletirem a página; mostrar preço e o que será entregue sem poluição.
- Não colocar avaliações, selos de segurança, descontos ou contadores falsos.
- Salvar; acessar visualização real em desktop e celular.

## 4. Order bumps e upsell (fase 08b, se o usuário quiser)

Seguir `references/14-orderbumps.md`. Resumo: bump = conteúdo entregável + orderbump; upsell = conteúdo + produto com checkout. **Order Bumps** (Produtos → aba Orderbumps): criar 3 com título = nome do produto, apontando direto para o conteúdo entregável (sem checkout próprio), e vincular no produto principal → menu Orderbumps, trocando o CTA padrão de "90% de desconto". **Upsell:** checkout como produto normal → link Oferta Principal nos botões da página do upsell → no produto principal, aba **Upsell**, colar a URL da página e **ligar "Upsell por URL"**.

## 5. Obter o link correto

Na Wiapy abrir **Checkout → Meu checkout → Links** e copiar URL da **Oferta Principal** — essa é a URL de pagamento. Não confundir com o link **Página de Vendas**, que pode redirecionar de volta à landing.

Registrar `checkout/configuracao.md` com nome, preço, URL do site, URL do checkout, produtos selecionados, status de teste e observações. **Não salvar credenciais nem dados de compradores.**

## 6. Webhook de vendas para o tracking

**Crítico:** um script no site **não basta** para atribuir uma venda paga se o checkout não informa pedidos ao tracking. Com o checkout criado, conectar a Wiapy à ferramenta escolhida na fase 07:

- Para **UTMizey + Wiapy** com MCP conectado: `criar_webhook(dashboard_id, plataforma="Wiapy")` e colar a URL devolvida na Wiapy. Sem MCP: buscar `Integrações → Webhooks`, escolher Wiapy e gerar URL do webhook. Na Wiapy, cadastrar essa URL na área de Webhook, criar segredo/token compartilhado quando solicitado e ativar eventos apropriados (pago, pendente, reembolso, chargeback etc.). A integração oficial inclui instruções para o script UTMs e parâmetros do anúncio.
- Evitar eventos Purchase duplicados quando checkout, tracking e Meta CAPI enviarem o mesmo pedido. Escolher uma fonte principal de Purchase ou configurar deduplicação por `event_id` quando suportada.
- Exigir consistência de moeda BRL, `value`, identificação do pedido, status e relação com anúncio.

Registrar em `tracking/verificacao.md` quais eventos foram habilitados. Os testes do webhook e a contagem de Purchase são feitos na fase 09.

## Observações práticas

- O checkout só salva com o conteúdo entregável completo. E-book: 1 arquivo PDF/XLS/XLSX/DOC. Vários arquivos: Drive público + tipo "Link enviado por E-mail".
- UTMizey: depois de trocar o dashboard, recarregar a página e conferir o cabeçalho antes de copiar a URL do webhook (a lista não atualiza sozinha).
- Thumb (1:1, ≤1 MB) e banner do checkout: sempre imagens geradas no ChatGPT.

## 7. Validação

- O checkout abre em aba anônima, sem autenticação do produtor.
- Preço, nome, capa, e-mail e produto corretos.
- O link da Oferta Principal abre direto o checkout certo (o caminho página → checkout é testado na fase 09, depois da troca do CTA).
- O fluxo de entrega é confirmado por ferramenta de preview/teste autorizado quando disponível.
- Webhook salvo na Wiapy e na ferramenta de tracking, com eventos registrados.
- Nunca realizar pagamento real sem autorização específica para despesa de teste.

Fontes úteis: `https://help.wiapy.com/pt-br/article/como-criar-um-checkout-e-pegar-o-link-de-venda-1omdaab/` e `https://help.wiapy.com/pt-br/category/produtores-19df9l4/`.

### REGRA CRÍTICA — integrações em contas que já têm outros produtos (UTMizey, Wiapy, pixel)
Incidente real (lançamento anterior): o agente gerou/copiou o webhook Wiapy do UTMizey com OUTRO dashboard ativo e substituiu o webhook Wiapy que já existia nesse dashboard de outro produto do usuário. Para nunca repetir:
1. Antes de qualquer ação em Integrações/Webhooks/Pixel do UTMizey, ler o seletor de dashboard no topo e confirmar que é EXATAMENTE o dashboard do lançamento atual (nome e ID anotados em estado.json). Se não for, trocar de dashboard primeiro. Depois de trocar, **recarregar a página** e conferir de novo o cabeçalho "Dashboard · <nome>": a lista de webhooks/pixels não atualiza sozinha e continua mostrando o dashboard anterior. Se não der para ter certeza, parar e perguntar.
2. Nunca clicar em "Adicionar webhook", "Gerar novo", "Regenerar", "Excluir" ou "Substituir" em um dashboard que já tenha webhook da mesma plataforma; isso pode sobrescrever a integração de outro produto. Se o dashboard do lançamento já tiver um, reutilizar a URL dele.
3. Na Wiapy, criar sempre uma integração NOVA, marcando somente o produto do lançamento ("Todos os produtos" desmarcado). Nunca editar, desativar ou excluir integrações existentes.
4. Antes de salvar, registrar em estado.json: dashboard UTMizey (nome+ID), URL do webhook (só o ID final abreviado), produto Wiapy marcado. Depois de salvar, conferir nos dois painéis que as integrações antigas continuam ativas e intactas.
5. Mesma lógica para pixels/conjuntos de dados e contas de anúncio: nunca reaproveitar, renomear ou alterar ativos de outros produtos.

## Banner no checkout (visual editor) — validado 09/11
- Banner: gerar no GPT em 3:1 (salvar 2172x724 JPG), mesmo estilo do criativo.
- Produtos → checkout do produto → "Editar visual checkout".
- Clicar no CABEÇALHO → no painel esquerdo clicar em "Imagem" (arrastar NÃO funciona) → bloco vazio aparece.
- Selecionar o bloco → Propriedades (direita) → "Fazer upload" (o Wiapy hospeda no CDN dele; NÃO precisa URL pública). Via automação: setar o File no input[type=file][accept="image/*"] (não o do chat) + dispatch input/change.
- Texto alternativo = nome do produto; Largura 100; Borda 0; Espaçamento 0.
- O cronômetro do cabeçalho troca de cor sozinho pra combinar com o banner — ok.
- "Salvar" (topo direito) → toast "Checkout salvo com sucesso" → conferir o link pay.wiapy.com do produto.
