# 11 — Meta Ads: campanha ABO 1-1-5

## Interpretação exata

**ABO 1-1-5 = 1 campanha + 1 conjunto de anúncios com orçamento no conjunto + 5 anúncios ativos.** Os outros cinco dos 10 criativos produzidos ficam como **reserva**, sem gasto inicial. Não confundir com 1 campanha, 5 conjuntos nem ligar 10 criativos de uma vez.

## Pré-condições

- Conta de anúncio na BM identificada sem ambiguidade; Página do Facebook informada no pré-voo; Instagram só se o usuário indicou um (é opcional).
- Autorização explícita ou já inequívoca para gastar verba na conta informada.
- **Orçamento diário** informado pelo usuário no pré-voo (`orcamento_diario_brl`).
- Página publicada e checkout acessível, entregáveis reais, política adequada e tracking ao menos testado.
- Não criar ou editar campanhas de outro cliente/conta.

## Campanha

1. Abrir Ads Manager em conta correta.
2. Criar **1 campanha** com objetivo `Vendas` (quando disponível e coerente com Pixel/checkout). Escolher objetivo equivalente na interface atual, sem inventar opção.
3. Nomear `LT | [NOME PRODUTO] | ABO | TESTE 01 | [DATA]`.
4. Desabilitar orçamento de campanha (CBO/Advantage Campaign Budget) se necessário para **ABO**; configurar orçamento no conjunto.
5. Configurar evento de conversão apropriado, preferencialmente `Purchase` **apenas se configurado e disponível**. Se compra não rastreável, não prometer otimização por compra; registrar bloqueio ou escolher alternativa justificável.

## Conjunto (1)

1. Nomear `CJ01 | Broad ou Público-Definido | BR`.
2. Definir território Brasil, idioma conforme disponibilidade, faixa etária legalmente apropriada, público compatível com produto e regras de segmentação da Meta.
3. Seguir boa prática para produto digital de baixo valor: começar simples; não forçar interesses ultra-restritos sem evidência.
4. Posicionamentos Advantage+ automáticos se disponíveis e compatíveis com formato, ou manuais justificados.
5. Definir o orçamento diário do conjunto **exatamente** com o valor informado no pré-voo. Não aumentar, não duplicar conjunto nem criar campanha extra para gastar mais.
6. O orçamento diário da Meta é uma média: o gasto real pode variar um pouco de um dia para o outro. Não afirmar teto rígido por dia no relatório.

## Anúncios (5)

Selecionar os melhores **cinco** criativos, com diversidade de ângulos; para cada:
- Nome `AD01 | [ÂNGULO]`, ..., `AD05 | [ÂNGULO]`.
- Imagem estática correspondente e copy/título de `criativos/copies.md`.
- Página informada (e Instagram, se houver), URL do site Vercel testada, CTA como `Saiba mais`/`Comprar agora` conforme política e interface.
- Colar em **Parâmetros de URL** o template salvo em `tracking/parametros-url.txt` na fase 07 (não o script JS do site). Testar pré-visualização e clique; não quebrar a URL com dois sinais `?` nem codificar as macros indevidamente.
- Revisar preview de Feed e Stories/Reels se forem placements usados.

## Publicar e controlar gasto

- Publicar os cinco anúncios depois de revisar todas as seleções e autorização de gasto.
- Confirmar status real: enviado para análise, em análise, aprovado, ativo, rejeitado. **Publicado não significa aprovado ou entregando**.
- Registrar IDs não secretos de campanha, conjunto e anúncios, data, orçamento e URL.
- Evitar novas campanhas duplicadas se retomar execução.
- Se o orçamento diário não tiver sido informado, **deixar em rascunho/pausado** e perguntar o valor, sem ativar.
- A campanha segue ativa até o usuário pausar; deixar isso claro no relatório.

## Primeira análise (sem supor resultados)

Criar relatório-modelo para CTR, CPC, CPM, custo por checkout iniciado, compras confirmadas, CPA, ROAS, reembolso e receita líquida estimada após taxas **conhecidas**. Não pausar criativos após poucos reais apenas por regra fixa sem significância; considerar orçamento, eventos, criativo e aprendizado. Cinco criativos de reserva são candidatos ao próximo ciclo, e não devem entrar automaticamente nem aumentar o orçamento diário autorizado.

**Gate:** estrutura 1-1-5 real, URLs/UTMs revisados, estados reportados e orçamento diário do conjunto igual ao autorizado (ou campanha não ativada).

## Rodada de criativos novos na mesma oferta (lição de 08/11/2026)
- Caminho mais rápido: **duplicar a campanha vencedora** (desmarcar "Selecionar todas as recomendações"; fica "Em rascunho") e trocar nome, mídia e texto de cada anúncio copiado.
- Subir as 5 imagens de uma vez na biblioteca (Adicionar mídia → Adicionar imagem → passo Mídia → Carregar). Na tela seguinte, a Meta oferece **publicar o upload nos anúncios ativos**: deixar tudo desmarcado e voltar.
- Para trocar a imagem: **Remover mídia** (lixeira) → Adicionar mídia → Adicionar imagem → passo Mídia → marcar só a imagem nova. Usar "Alterar seleções" sem remover antes deixa a imagem antiga como principal e a nova vira só "taxa de proporção".
- A Meta agrupa imagens parecidas como variações; conferir no clique da bandeja que a "Mídia original" é a certa e "Imagem de IA: 0".
- O bloco "Geração de texto Advantage+" **volta a marcar "Aplicar tudo (5 de 5)" e "Personalizar por personas" toda vez que o texto principal muda** (demora uns 5 s para aparecer). Depois de colar o texto, esperar, desmarcar e conferir "0 de 5" no texto e no título. Se abrir a pesquisa de feedback, clicar "Manter desmarcadas".
- Tecla Esc fecha o assistente inteiro; para fechar só o popup da mídia, clicar fora dele.
