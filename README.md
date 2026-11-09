# Low Ticket Autopilot

Skill para o **Claude** lançar produtos digitais low ticket (R$ 10 a R$ 29) do zero e com o mínimo de intervenção: pesquisa de oferta na Biblioteca de Anúncios, criação do produto e dos arquivos, imagens no ChatGPT, página de vendas, checkout, tracking, anúncios na Meta, order bumps, upsell e acompanhamento diário das campanhas.

> Feita e testada em lançamentos reais. Não é promessa de resultado: venda depende de oferta, criativo, orçamento e mercado.

## O que ela faz

| Fase | O que acontece |
|---|---|
| 00 | Pergunta só o necessário (orçamento, conta de anúncios, página, e-mail de suporte etc.) numa mensagem |
| 01–02 | Minera anúncios ativos, pontua 10 oportunidades e escolhe uma para modelar (sem copiar) |
| 03 | Produz os entregáveis de verdade: planilhas com fórmulas, PDFs com design, PDFs preenchíveis |
| 04 | Gera mockups, capas e imagens no ChatGPT |
| 05–06 | Cria a página de vendas e publica na Vercel (repositório privado no GitHub) |
| 07 | Configura o tracking (UTMizey, de preferência pelo MCP) e o pixel da Meta |
| 08 | Cria produto, checkout, banner e webhook na Wiapy |
| 08b | Cria order bumps e upsell (produtos, arquivos, página do upsell e integração) |
| 09 | Testa a jornada inteira antes de gastar |
| 10–11 | Gera 10 criativos e monta a campanha ABO 1-1-5 na Meta |
| 12 | Relatório final com status real de cada etapa |
| 13 | Nos dias seguintes: lê os números no tracking e decide subir, manter ou pausar |

## Pré-requisitos

- **Claude** com acesso a navegador (extensão Claude in Chrome) e, de preferência, ao computador pelo app desktop.
- Contas logadas no Chrome: **Meta Business** (conta de anúncios + página), **Wiapy**, **UTMizey**, **GitHub**, **Vercel**, **ChatGPT** (plano pago, para gerar imagens) e uma conta **Google** (Drive/Gmail, opcional).
- **Vercel Pro** para uso comercial (o plano Hobby não permite).
- Orçamento de anúncios definido por você.

Usa outro checkout ou outro tracking? A lógica das fases continua igual; veja "Ferramentas e adaptação" no `SKILL.md`.

## Instalação

1. Baixe este repositório (Code → Download ZIP) ou clone.
2. No Claude, adicione a pasta como skill (Configurações → Capacidades/Skills → enviar a pasta ou o ZIP), mantendo o nome `low-ticket-autopilot`.
3. Opcional: conecte o MCP da UTMizey para o tracking ser configurado sem navegador.

## Como usar

Exemplo de pedido:

> Rode a low-ticket-autopilot. Orçamento de R$ 30 por dia, conta de anúncios [NOME], página [PÁGINA], sem Instagram, e-mail de suporte [EMAIL]. Estou ciente do uso do token CAPI. Quero order bumps e upsell. Pode decidir produto, copy e criativos sem me consultar.

Depois do lançamento:

> Olha as campanhas de ontem no UTMizey e me diz o que fazer.

## Segurança e limites

- Nunca salva senhas, códigos de verificação ou tokens em arquivo, repositório ou chat. Login e 2FA são sempre seus.
- Não publica nem aumenta gasto sem a sua autorização; o orçamento diário que você informar é o teto do conjunto.
- Arquivos pagos nunca ficam em link público.
- Em contas com outros produtos, não mexe em integrações, pixels ou webhooks existentes (regra crítica no `SKILL.md`).
- Não inventa depoimentos, descontos ou contadores; cronômetro só se você pedir.

## Responsabilidade

Você é responsável pelos anúncios veiculados, pelo gasto, pelo cumprimento das políticas da Meta e da plataforma de pagamento, da LGPD e do Código de Defesa do Consumidor, e por ter direitos sobre o que vende. A skill modela estrutura de ofertas que funcionam, mas não deve copiar material protegido de concorrentes.

## Estrutura

```
SKILL.md                 orquestrador (leia primeiro)
references/00–15         passo a passo de cada fase
assets/                  modelos (estado, relatório, candidatos, upsell, prompts do ChatGPT)
scripts/validar_skill.py confere a estrutura do pacote
```
