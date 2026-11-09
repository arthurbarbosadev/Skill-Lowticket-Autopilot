# 09 — Publicação final, integração e QA de funil

## Consolidar site + checkout

1. Substituir cada CTA pendente pela URL **real da Oferta Principal da Wiapy**. Procurar em toda a árvore de código `CHECKOUT_URL_PENDING`; no build de produção não pode sobrar nenhuma ocorrência.
2. Garantir que o script oficial da ferramenta de tracking (instalado na fase 07) esteja presente **uma vez** e não conflite com outro serviço.
3. Conferir localmente que os botões do hero, meio e rodapé apontam para a Oferta Principal.
4. Aplicar política de privacidade/aviso de cookies conforme eventos e dados realmente coletados, com dados corretos da operação.
5. Validar texto de entrega, suporte, preço, titular do produto e garantia declarada; não anunciar políticas inexistentes.
6. Fazer commit no GitHub privado, acompanhar redeploy da Vercel e visitar URL **publicada** depois do deploy.

## Testes de tracking ponta a ponta (na URL publicada)

Só agora o funil inteiro existe: Pixel e script (fase 07), checkout e webhook (fase 08) e CTA real (passo 1 acima).

1. Página Vercel recebe visita com UTMs e carrega scripts permitidos sem erro de console.
2. Botões preservam UTMs ao ir para Wiapy; comparar parâmetros em origem e destino.
3. Eventos PageView e InitiateCheckout aparecem nas ferramentas de teste quando aplicáveis.
4. Teste de webhook Wiapy chega ao dashboard de tracking (evento de teste separado de venda real).
5. **Purchase** só pode ser marcado como validado após evento **real de pagamento confirmado ou simulação oficial que a integração claramente suporte**; não fazer compra real sem consentimento específico.
6. Verificar duplicidades e ausência de vazamento de dados pessoais.

Completar `tracking/verificacao.md` (iniciado na fase 07) com OK / PARCIAL / FALHA, dados não secretos e capturas redigidas. **Nunca declarar a compra real validada a partir de PageView ou teste incompleto.**

## Checklist técnico obrigatório

- [ ] `.vercel.app` acessível com HTTPS; sem erros graves de console.
- [ ] Hero, cores, textos, preço, mocks e prévias corretos no celular e desktop.
- [ ] Imagens carregam, sem textos cortados.
- [ ] CTA do topo abre checkout correto.
- [ ] CTA intermediário abre checkout correto.
- [ ] CTA final abre checkout correto.
- [ ] Não resta placeholder de link, foto ou texto.
- [ ] UTMs e parâmetros necessários se propagam adequadamente.
- [ ] Pixel/PageView reconhecido no teste; conversões marcadas com status de validação honesto.
- [ ] Checkout com mesmo nome, preço e conteúdo da página.
- [ ] Entregáveis disponíveis no cadastro do produto.
- [ ] E-mail de suporte e dados de contato adequados.
- [ ] Performance e mobile satisfatórios.
- [ ] Política real de privacidade e termos da oferta visíveis.
- [ ] Sem cookies/integrações duplicadas involuntárias.

## Gate antes de anúncios

**Falhas bloqueantes:** CTA quebrado, checkout errado/inacessível, produto não entregue, tracking completamente ausente quando a campanha depende de otimização por conversão, promessa falsa, orçamento não autorizado, vínculo de conta incorreto.

**Falhas parciais relatáveis:** Purchase ainda não validado por compra real, pequena limitação de preview ou métrica não disponível; informe limite e, se estiver seguro para operar, deixe claro o escopo do teste.

Registrar `site/checklist.md` com resultados e evidências; não declarar tudo aprovado se não estiver.
