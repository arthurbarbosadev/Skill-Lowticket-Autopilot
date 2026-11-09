# 15 — Otimização e escala (fase 13)

Objetivo: nos dias seguintes ao lançamento, ler os números certos, tomar **uma** decisão por dia com base neles e escalar só o que dá lucro. Rodar quando o usuário pedir ("olha as campanhas", "como foi ontem", "quero escalar").

## 1. Fonte da verdade

- **Vendas, faturamento, lucro e ROAS vêm do tracking (UTMizey ou equivalente), nunca do Gerenciador de Anúncios.** O pixel da Meta atribui vendas a anúncios de forma diferente e costuma errar por anúncio.
- Do Gerenciador, usar só o que é da Meta: gasto, CTR, CPC, CPM, frequência, status e se o conjunto bateu o orçamento.
- Se a conta de anúncios tiver mais de um produto, o lucro de cada produto é o das **campanhas dele** (filtrar por nome de campanha). O total da conta mistura produtos.
- Cada produto tem seu dashboard no tracking: trocar de dashboard, **recarregar** e conferir o nome antes de ler (ver REGRA CRÍTICA no SKILL.md).
- Ler sempre **ontem** (dia fechado) e **máximo** (acumulado). O dia de hoje ainda está incompleto.
- Registrar a leitura em `estado.json` → `diario` (data, gasto, vendas, faturamento, ROAS por campanha, decisão tomada).

## 2. Janela de aprendizado

- Nos **3 primeiros dias** de uma campanha nova, não mexer em orçamento, público nem anúncios, salvo erro grave (link quebrado, anúncio reprovado, gasto muito acima do autorizado).
- Mudança grande (mais de 20% de orçamento, trocar público, editar anúncio ativo) reinicia o aprendizado. Por isso uma mudança por vez e uma por dia.
- Nunca editar texto ou imagem de anúncio que já está rodando: duplicar e trocar na cópia.

## 3. Regras de decisão (padrão; o usuário pode definir outras no pré-voo)

| Situação (dia fechado, por campanha) | Ação |
|---|---|
| ROAS acima de 1,5 por 2 dias seguidos | Subir o orçamento do conjunto em 20% |
| ROAS entre 1,0 e 1,5 | Manter; olhar criativos |
| ROAS abaixo de 1,0 depois de gastar 3 vezes o preço do produto | Pausar o conjunto ou a campanha |
| Anúncio com gasto de 2 vezes o preço e nenhuma venda (no tracking) | Pausar o anúncio e ligar um reserva |
| Um anúncio concentra quase todas as vendas | Criar 3 a 5 variações dele (mesmo ângulo, outra headline e outra imagem) numa campanha de teste nova |

- "ROAS" aqui é faturamento líquido ÷ gasto, com os números do tracking.
- Antes de subir orçamento, conferir se os **order bumps e o upsell estão ligados**: cada real a mais no ticket médio baixa o CPA de empate e deixa a escala mais segura.
- Subir orçamento ou criar campanha nova é gasto novo: **pedir confirmação do usuário** com o valor exato antes de aplicar. Pausar algo que está dando prejuízo pode ser feito direto quando o usuário já autorizou otimizar; avisar em seguida.

## 4. Campanha de escala

Quando 2 ou mais anúncios estiverem com ROAS acima de 1,5 por 3 dias:
1. Duplicar a campanha com recomendações desmarcadas.
2. Deixar só os anúncios vencedores (os mesmos IDs de post, para manter o engajamento, quando possível).
3. Orçamento inicial igual ao da campanha de teste; confirmar com o usuário.
4. Manter a campanha de teste rodando com os criativos novos.

## 5. Criativos novos

- Base: o anúncio que mais vende no tracking. Manter o ângulo, variar headline, imagem e formato.
- Testar vídeo curto (até 15 s, legenda grande, gancho nos 2 primeiros segundos) quando as imagens começarem a cansar (CTR caindo e frequência subindo).
- Gerar as imagens no ChatGPT (`references/10-criativos.md`) e subir numa campanha de teste nova, sem mexer nos anúncios ativos.

## 6. Pix pendente e recuperação

- Vendas pendentes no tracking são Pix gerados e não pagos. Conferir se a recuperação de carrinho/Pix do checkout está ligada no produto.

## 7. Produto de data comemorativa

- Ler a data limite registrada em `estado.json`. Uma semana antes, avisar o usuário; nos últimos dias, não subir orçamento.
- Depois da data, sugerir pausar as campanhas e virar o produto (ex.: Natal → Ano Novo) ou encerrar.

## 8. Mensagem diária para o usuário

Curta e em linguagem simples: tabela por campanha (gasto, vendas, faturamento, ROAS) do dia anterior e do acumulado, o que mudou, a decisão proposta e o que precisa de confirmação. Não prometer resultado.
