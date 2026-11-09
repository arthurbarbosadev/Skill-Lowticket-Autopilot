# 04 — Controlar ChatGPT para gerar mockups e imagens de página

## Meios de execução

Preferir uma ferramenta/API de geração de imagens autorizada que produza arquivos reais. Se a intenção for **usar o ChatGPT**, abrir a sessão do ChatGPT autenticada pelo usuário por navegação/computador **quando essa capacidade e permissão existirem**; não assumir que um MCP específico exista. Carregar as prévias reais e descrição dos entregáveis conforme permitam as ferramentas. Guardar arquivos resultantes no workspace.

Se não puder controlar ChatGPT, avisar bloqueio específico e, se existir outro gerador de imagem conectado e autorizado, usá-lo como alternativa sem afirmar que usou o ChatGPT.

## Regra principal

**Todas** as imagens do site e do checkout (mockup hero, mockups secundários, capa, banners e thumb do checkout) são geradas no ChatGPT. Prints crus de planilha/PDF não entram na página. Anexe as prévias reais ao ChatGPT como referência para o mockup refletir o conteúdo verdadeiro (mesmas seções, cores e tipo de material), sem inventar itens que não existem.

## Inventário a pedir/gerar (quando relevante)

1. Mockup principal hero: caixa/ebook/celular e amostras visíveis **fiéis ao conteúdo real**.
2. Capa frontal limpa do produto (quadrada) para Wiapy, preferencialmente otimizada para **até 1 MB** quando exigido.
3. Dois ou mais mockups secundários: páginas internas, tablet, notebook, folhas impressas, etc., conforme formato real.
4. Imagem horizontal de benefício/demonstração.
5. Dois banners horizontais discretos para o checkout (um principal e uma variação).
6. Elementos gráficos necessários (ícones sem marcas, divisórias, pequenos selos factuais).
7. Possíveis imagens adicionais para order bumps, se realmente criados.

Atenção: os **10 criativos de anúncios** são feitos depois, na fase 10, não misturar assets do site com anúncios finais.

## Briefing de geração visual

Usar `assets/prompts-chatgpt.md` como base, adaptando nome, cores, formato, quantidade e prévias reais. Solicitar imagens originais, tipografia legível e nada de logos/personagens de terceiros. Não pedir imagens que aparentem ser prints reais de pagamentos, mensagens ou avaliações inexistentes. Preferir mostrar amostras verdadeiras do PDF/planilha, montadas no site usando código quando o gerador distorcer texto.

## Ciclo de qualidade

- Inspecionar visualmente dimensões, resolução, fidelidade, contraste, composição e deformações de texto.
- Se falhar, refazer o asset, não mudar silenciosamente o produto real.
- Para textos exatos, preferir sobreposição tipográfica no site/canvas de edição, evitando erros da geração.
- Exportar formatos apropriados (WebP/PNG/JPEG), comprimir mantendo qualidade; garantir que a miniatura atende ao limite do checkout.
- Guardar manifestos: `branding/identidade.md`, `branding/assets.md` com arquivo, destino, proporção e fonte.

**Gate:** toda imagem publicada deve ter direito de uso, legibilidade e compatibilidade com o produto de verdade.
