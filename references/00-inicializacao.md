# 00 — Inicialização e pré-voo

## Meta
Iniciar o projeto com autonomia, perguntar o mínimo, registrar limites, checar ferramentas e definir como continuar mesmo se alguma conexão não estiver disponível.

## Perguntas obrigatórias (uma mensagem, somente o que ainda não foi informado)

- **E-mail de suporte** da operação (aparece no campo de suporte do checkout).
- **Conta Google da operação:** "Qual conta Google eu uso para o **Drive** (pasta pública do entregável) e para o **Gmail** (ler e-mails de ativação/confirmação das plataformas)? É a mesma conta?". Perguntar também: **"Você autoriza ler os e-mails necessários no Gmail dessa conta?"**. Antes de criar pasta no Drive ou ler e-mail, conferir no canto superior direito (avatar/conta ativa) que é EXATAMENTE essa conta; se o Chrome estiver em outra, trocar de conta ou parar e perguntar. Registrar em `estado.json` → `conta_google_drive`, `conta_gmail`, `gmail_autorizado`. Sem permissão de Gmail, o restante continua.
- **Nome exato da conta de anúncios dentro da BM** a usar. Quando várias contas tiverem o mesmo nome, consultar seletor e buscar identificação adicional antes de ações com gasto.
- **Página do Facebook** que vai veicular os anúncios. Perguntar também se há **Instagram** para vincular; é opcional, dá para anunciar só com a Página.
- **Tracking: UTMizey.** Se o MCP da UTMizey estiver conectado, perguntar só: **ID do pixel da Meta** (ou autorização para criar um) e **quais contas de anúncio ligar** no dashboard. O resto (dashboard, webhook, códigos) o agente faz pelo MCP — ver `07-tracking.md`.
- **Tipo de entregável na Wiapy:** perguntar "Como você quer entregar o produto: **link do Google Drive** (pasta pública, enviado por e-mail — recomendado quando há mais de um arquivo) ou **arquivo anexado** na Wiapy (E-book, um arquivo só)?". Registrar em `estado.json` → `tipo_entregavel`.
- **Order bumps e upsell:** "Quer que eu já crie os order bumps (3) e o upsell? Eu pesquiso as melhores opções, crio os produtos e entregáveis, cadastro os bumps na Wiapy e monto a página do upsell." Registrar em `estado.json` → `extras.fazer`.
- **Cronômetro (opcional):** só perguntar se o usuário falar em urgência; por padrão não há cronômetro.
- **Orçamento diário em reais:** "Quanto você vai gastar por dia?". Esse é o valor do conjunto de anúncios. Não perguntar orçamento total nem duração.
- **Permissão de veicular anúncios com gasto real** na conta especificada se não estiver explícita no pedido.
- **Token CAPI:** avisar que, se a integração de tracking exigir, o agente vai gerar o token da API de Conversões da Meta e colá-lo no campo seguro da plataforma de tracking, sem registrá-lo em arquivo, repositório, log ou chat. Perguntar: **"Você está ciente e de acordo que eu gere e use o token CAPI para configurar o tracking?"** Registrar só a resposta em `capi_token_ciente`, nunca o token.
- **2FA:** "Alguma das contas usadas tem verificação em duas etapas (Meta/BM, Wiapy, GitHub, Vercel, ChatGPT, tracking, Gmail)?". Registrar em `contas_com_2fa` e, antes de cada login numa dessas contas, avisar o usuário que ele vai precisar concluir a verificação.

Caso Wiapy, GitHub, Vercel, ChatGPT, Meta ou tracking exijam login/2FA e não tenham sessão conectada, solicite apenas a ação do usuário para autenticar/autorizar; nunca peça senha ou código 2FA por chat.

## Auditoria de capacidades

Verificar recursos disponíveis para:
- Pesquisar Web e Biblioteca de Anúncios; navegador/controle de computador conforme permitido.
- Criar, visualizar, editar e zipar PDFs, planilhas, imagens e arquivos digitais.
- ChatGPT: ferramenta conectada apropriada **ou** uso da interface web já autenticada via navegador autorizado; não pressupor MCP oficial para ChatGPT, nem inventar ferramenta.
- GitHub e Vercel via MCP quando conectados; como alternativa, terminal/Git e interfaces autenticadas quando autorizados.
- Meta Business / Events Manager / Ads Manager, Wiapy e a plataforma de tracking autenticadas.
- **MCP da UTMizey** (ferramentas `status_da_configuracao`, `criar_dashboard`, `ligar_contas_de_anuncio`, `cadastrar_pixel`, `criar_webhook`, `obter_codigos`, `desempenho_meta` etc.): se estiver conectado, é o caminho padrão para a UTMizey; o navegador fica só como alternativa.
- Conta Google ativa no Chrome (Drive/Gmail) bate com a informada no pré-voo.

## Estrutura de trabalho

O agente tem permissão para criar as pastas e arquivos do projeto sem pedir confirmação. Criá-las FORA da pasta da skill:

```text
lancamentos/AAAA-MM-DD-slug/
  estado.json
  pesquisa/10-ofertas.md
  pesquisa/oferta-vencedora.md
  produto/briefing.md
  produto/entregaveis/
  produto/preview/
  produto/entrega-final.zip
  branding/
  criativos/imagens/
  criativos/copies.md
  site/
  tracking/verificacao.md
  tracking/parametros-url.txt
  checkout/configuracao.md
  ads/plano.md
  ads/resultado-da-publicacao.md
  relatorio-final.md
```

Nomes de paths são referências, não obrigações quando o executor usa workspace virtual.

## Registro

Copiar `assets/modelo-estado.json` para `estado.json` e preencher com as respostas do pré-voo. Atualizar após cada etapa. Antes de criar um recurso, pesquisar se já existe neste projeto; reaproveitar em caso de retomada.

## Sem permissões

A pesquisa, o briefing, a produção dos entregáveis e o site local podem avançar sem login nas plataformas. Registre bloqueio de deploy, integração ou anúncios e continue o restante que for seguro; jamais afirme que configurou uma conta não acessada.
