# 05 — Criar página de vendas original inspirada na estrutura da referência

## Estudo da concorrência

Abrir a landing page da oferta escolhida. Anotar **estrutura comercial**, sequência das seções, hierarquia, posição de CTA, benefícios, perguntas e elementos de conversão; registrar URL/observações. A meta é produzir uma página nova com experiência tão clara quanto a referência, **não publicar clone literal**.

### SaveWeb2Zip (opcional)

Se houver direito de usar/baixar o site de referência para **análise interna**, é possível fazer uma captura por ferramenta equivalente a SaveWeb2Zip apenas para mapear blocos e interações, observando termos e direitos de terceiros. Não reutilizar para publicação HTML/CSS, imagens, textos, marcas, scripts de tracking, pixels ou arquivos alheios. Se a captura não for permitida, observar a página no navegador e reconstruir do zero.

## Implementação

- Criar site próprio com stack simples e apropriada (HTML/CSS/JS estático, Vite ou Next.js), considerando rapidez de carregamento e facilidade de manutenção.
- Textos originais baseados em `produto/briefing.md` e fatos do material produzido.
- Identidade visual original, imagens geradas e prévias reais do produto.
- Prioridade **mobile first**: mobile 360–430px, tablet, desktop; checar sem overflow horizontal.
- Seções recomendadas, adaptáveis: hero com promessa honesta, mockup, o que recebe, prévias, para quem serve, diferenciais, exemplos de uso, bônus reais, preço, FAQ, suporte/garantia conforme política existente, CTAs repetidos com moderação.
- Preço exato entre R$ 10 e R$ 29 visível, sem âncoras de desconto falsas.
- Incluir acesso, formato, limitações, prazo de entrega, informação de produto digital e meios de suporte; política de privacidade adequada ao uso de analytics/cookies e tratamento de dados.
- Remover links quebrados, imagens de placeholder e frases "Lorem ipsum".

## CTA em duas fases

**Antes do checkout:** criar CTA em componente/configuração única, com placeholder interno identificável (`CHECKOUT_URL_PENDING`) que não seja tratado como funcional em QA. A publicação inicial na Vercel é técnica para obter a URL exigida na Wiapy; não enviar tráfego de anúncios ainda.

**Depois do checkout:** substituir todas as ocorrências pela URL **real da Oferta Principal** da Wiapy; tratar preservação/propagação de parâmetros UTM conforme script oficial do tracking. Não codificar manualmente macros de rastreamento se o script oficial gerencia links.

## Estrutura obrigatória acima da dobra

1. **Faixa de header** (texto curto em destaque): "Oferta especial de lançamento" ou uma data de fim real. Nada de "somente hoje" com data que se atualiza sozinha.
2. **Headline** de 2 a 3 linhas no celular (cerca de 6 a 12 palavras), sem fonte exagerada.
3. **Mockup** gerado no ChatGPT.
4. **Sub-headline** de 1 a 2 frases.
5. **CTA**.

Regras de layout: textos alinhados (centralizados no mobile), seções curtas, muito respiro, **sem botão sticky**. Seções seguintes: o que vem (cards com imagens GPT), para quem é, como funciona, bônus, preço, garantia, FAQ, CTA final. Avaliações só reais; antes delas, usar "o que você vai conseguir fazer".

Antes de construir, estudar os sites de referência do usuário (ex.: pasta de referências indicada pelo usuário) e seguir o mesmo padrão de construção.

## Performance e acessibilidade

- Imagens comprimidas, `width`/`height` adequados, lazy load fora do hero, bons contrastes, alts significativos, títulos sem salto semântico e botões acessíveis.
- Captura de desempenho e layout; página precisa funcionar em navegação com teclado e dispositivos móveis.
- Cronômetro só se o usuário pedir. Se houver prazo real, o relógio reflete esse prazo (inclusive ao recarregar e no fuso certo); se for um cronômetro de sessão, o texto ao lado diz o que ele mede.

## Entrega técnica

`site/` deve incluir código-fonte, configurações de build, assets e documentação mínima de instalação e deploy; sem segredos versionados. Registrar `site/arquitetura.md`, `site/checklist.md`.

**Gate:** build/local preview ok, navegação funcional e site visualmente validado. Avançar para GitHub/Vercel inicial.
