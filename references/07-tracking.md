# 07 — Meta Pixel + CAPI + UTMizey + script UTM no site

## Escopo desta fase

Montar a **base de rastreamento** antes de o checkout existir: Pixel/dataset, token CAPI quando necessário, dashboard, integração com a Meta, script UTM no site e template de parâmetros dos anúncios.

- O **webhook de vendas da Wiapy** é configurado na fase 08, porque depende do checkout criado.
- Os **testes de ponta a ponta** (UTMs chegando ao checkout, eventos, webhook, Purchase) acontecem na fase 09, porque dependem do CTA apontando para a Oferta Principal real.

Não tentar testar o caminho página → checkout nesta fase: o CTA ainda é `CHECKOUT_URL_PENDING`.

## Seleção

A ferramenta de tracking é a **UTMizey** (`utmizey.com.br`). Os caminhos exatos de menus podem mudar; identificar os rótulos **da sessão real** e seguir ajuda oficial quando necessário.

## Passo A — Meta Business / Events Manager

1. Usar BM e **conta de anúncios informada**. Conferir nome e ID visualmente antes de conectar ou criar recursos.
2. Abrir Configurações de Negócio / Gerenciador de Eventos, procurar fontes de dados / Pixel (também chamado dataset).
3. Verificar se já há Pixel do **mesmo projeto**; reutilizar se correto, senão criar Pixel novo com nome distintivo. **Não duplicar na retomada.**
4. Copiar ID do Pixel/dataset em **Gerenciador de Eventos → Configurações → "Identificação do conjunto de dados"** (não use o `selected_asset_id` da URL do Business Suite). Gerar token de CAPI somente se a integração escolhida realmente exigir token manual **e** o usuário tiver confirmado ciência no pré-voo (`capi_token_ciente: true`). Sem essa confirmação, perguntar antes de gerar.
5. Com a ciência confirmada, o agente pode gerar, copiar e colar o token no campo seguro da plataforma de tracking. Nunca colocá-lo em código cliente, URL, chat, logs, repo, `estado.json` ou relatório. Se a ferramenta usada pelo agente bloquear a inserção de tokens, indicar o campo exato e pedir que o usuário cole.
6. Associar ativo à conta de anúncios correta quando necessário e permitido.

## Passo B0 — UTMizey pelo MCP (caminho padrão quando conectado)

Se o MCP da UTMizey estiver disponível, fazer a configuração por ele em vez do navegador. O MCP exige avisar o que vai ser feito e esperar o "sim" do usuário antes de criar, ligar, cadastrar, pausar ou ativar; agrupar essas confirmações numa única mensagem.

1. `listar_dashboards` → se não existir dashboard do produto, `criar_dashboard` (nome do produto, BRL, America/Sao_Paulo). Anotar nome + ID em `estado.json` → `utmizey_dashboard` e **passar sempre `dashboard_id`** em todas as chamadas seguintes (sem ele o MCP usa o primeiro dashboard da conta — é o mesmo risco do incidente de 04/11).
2. `status_da_configuracao(dashboard_id)` → mostra os 6 passos (Meta, contas, plataforma, script, UTMs, pixel) e o que falta.
3. `listar_contas_de_anuncio` → se não houver Facebook conectado, mandar ao usuário o link devolvido (só ele conecta, no navegador). Depois `ligar_contas_de_anuncio` só com a(s) conta(s) do pré-voo.
4. `cadastrar_pixel(dashboard_id, nome, pixel_id, token_api_conversoes)` → o token CAPI vai só nesse parâmetro, nunca em arquivo/chat/log. Sem token, a compra não volta ao Meta pelo servidor.
5. `obter_codigos(dashboard_id, checkout="outra")` → script da página, script do pixel e código de UTM. Colar os scripts no `<head>` do site e salvar o código de UTM em `tracking/parametros-url.txt`.
6. Webhook da Wiapy fica para a fase 08: `criar_webhook(dashboard_id, plataforma="Wiapy")` devolve a URL (se já existir no dashboard, devolve a mesma — não sobrescreve). Na Wiapy continua valendo a REGRA CRÍTICA: integração NOVA só com o produto do lançamento.
7. Ao fim, rodar `status_da_configuracao` de novo e registrar o resultado em `tracking/verificacao.md`.
8. Na operação (fase 12 e escala), usar `desempenho_meta`, `quebra_de_vendas` e `resumo_financeiro` do dashboard do produto antes de pausar/escalar; `pausar_ou_ativar` só com confirmação.

Se o MCP não estiver conectado ou falhar 2 vezes, seguir o Passo B pelo navegador.

## Passo B — Tracking (sessão já autenticada)

1. Selecionar dashboard apropriado: procurar **Avançado → Criar novo Dashboard** ou menu equivalente mostrado na interface. Criar dashboard com nome do produto, **se a assinatura permitir**; planos básicos podem limitar dashboards.
2. Abrir **Integrações** e conectar **a conta Meta Ads exata**; completar OAuth sem tentar contornar autenticação.
3. Abrir **Pixel**, adicionar Pixel de otimização ou vínculo com fonte Meta conforme o produto exigir. Preencher ID e token apenas quando campos legítimos aparecerem. Algumas versões usam OAuth sem token manual; não forçar campo inexistente.
4. Copiar o script de Pixel **somente se a plataforma recomendar instalá-lo no site**; instalar no local indicado pela documentação, evitando dois scripts conflitantes que enviem o mesmo evento.
5. Abrir **Integrações → UTMs** (ou equivalente). Obter (a) **script UTMs** da página e (b) **template de parâmetros de URL para anúncios Meta** — **são itens diferentes**. Copiar/baixar os códigos reais exibidos, não fabricá-los.
6. Inserir o script UTMs no `<head>`/posição recomendada do código do site. Ele deve preservar `utm_*` e identificadores ao chegar ao checkout; não remover `sck` quando o rastreador o utiliza. O deploy com o script pode sair junto com a atualização da fase 09.
7. Salvar o template de parâmetros de URL em `tracking/parametros-url.txt` (não é segredo); ele será colado em cada anúncio na fase 11.
8. Registrar somente o nome/versão da ferramenta, IDs não secretos e status de integração.

## Verificação desta fase

- Pixel/dataset criado ou reaproveitado, com ID registrado (mascarado no estado).
- Integração Meta conectada à conta de anúncios correta na ferramenta de tracking.
- Script UTM presente **uma única vez** no código do site; build local sem erro.
- Template de parâmetros salvo em `tracking/parametros-url.txt`.

Iniciar `tracking/verificacao.md` com esses itens. Webhook, PageView, InitiateCheckout, Purchase e duplicidade ficam marcados como `PENDENTE — fases 08/09`, nunca como OK.

### Referências públicas para orientar navegação

- UTMizey + Wiapy: `https://utmizey.com.br/blog/rastrear-vendas-wiapy-meta-ads`
- UTMizey pedido/API: `https://utmizey.com.br/docs/envio-de-vendas`
- Wiapy ajuda: `https://help.wiapy.com/pt-br/`
- Meta Gerenciador de Eventos: `https://business.facebook.com/events_manager2`

### REGRA CRÍTICA — integrações em contas que já têm outros produtos (UTMizey, Wiapy, pixel)
Incidente real (lançamento anterior): o agente gerou/copiou o webhook Wiapy do UTMizey com OUTRO dashboard ativo e substituiu o webhook Wiapy que já existia nesse dashboard de outro produto do usuário. Para nunca repetir:
1. Antes de qualquer ação em Integrações/Webhooks/Pixel do UTMizey, ler o seletor de dashboard no topo e confirmar que é EXATAMENTE o dashboard do lançamento atual (nome e ID anotados em estado.json). Se não for, trocar de dashboard primeiro. Depois de trocar, **recarregar a página** e conferir de novo o cabeçalho "Dashboard · <nome>": a lista de webhooks/pixels não atualiza sozinha e continua mostrando o dashboard anterior. Se não der para ter certeza, parar e perguntar.
2. Nunca clicar em "Adicionar webhook", "Gerar novo", "Regenerar", "Excluir" ou "Substituir" em um dashboard que já tenha webhook da mesma plataforma; isso pode sobrescrever a integração de outro produto. Se o dashboard do lançamento já tiver um, reutilizar a URL dele.
3. Na Wiapy, criar sempre uma integração NOVA, marcando somente o produto do lançamento ("Todos os produtos" desmarcado). Nunca editar, desativar ou excluir integrações existentes.
4. Antes de salvar, registrar em estado.json: dashboard UTMizey (nome+ID), URL do webhook (só o ID final abreviado), produto Wiapy marcado. Depois de salvar, conferir nos dois painéis que as integrações antigas continuam ativas e intactas.
5. Mesma lógica para pixels/conjuntos de dados e contas de anúncio: nunca reaproveitar, renomear ou alterar ativos de outros produtos.
