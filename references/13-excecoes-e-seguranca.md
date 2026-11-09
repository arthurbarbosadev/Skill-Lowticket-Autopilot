# 13 — Tratamento de exceções, autonomia e segurança

## Política de recuperação

- **Botão/menu mudou:** procurar pelo nome semântico, abrir ajuda oficial e verificar onde está a função. Não clicar aleatoriamente em controles destrutivos.
- **MCP indisponível:** usar outro meio de interação **existente e autorizado**. Se impossível, preparar arquivos e registrar exatamente a ação faltante, sem fingir acesso.
- **Login/captcha/2FA:** informar qual autenticação humana é requerida; não contornar bloqueios nem pedir códigos secretos em chat. Para as contas listadas em `contas_com_2fa`, avisar antes do login.
- **Assinatura não inclui dashboard/pixel adicional:** reutilizar um existente somente se **vinculado ao mesmo projeto** e com integridade; não contratar upgrade sem autorização.
- **Gmail não autorizado:** não ler mensagens; usar e-mail de suporte informado ou ficar bloqueado nessa subparte.
- **Anúncio encontrado sem preço confirmado:** marcar preço como não confirmado, não atribuir falsamente R$ 10–29.
- **Faltam dez referências:** ampliar critérios de busca; registrar número real e seguir apenas com decisão sustentada por evidência.
- **SaveWeb2Zip falha/parece violar direitos:** reconstruir a página originalmente com base nas funções e estrutura observáveis.
- **Imagem ChatGPT falha:** reabrir sessão/gerar novamente com abordagem permitida; não usar imagens com artefatos ou texto falso.
- **Webhook não funciona:** verificar evento, assinatura, URL e correspondência de pedidos; não fabricar confirmação nem colar token em relatório.
- **Orçamento diário não definido:** construir campanha em rascunho e perguntar o valor diário, sem ativação.
- **Erro de QA da compra:** não conduzir tráfego pago para funil quebrado.

## Segurança, propriedade e privacidade

- Acesso administrativo não equivale a permissão ilimitada. Limitar alterações aos recursos criados neste lançamento.
- Nunca explorar, exportar ou compartilhar mensagens particulares, listas de clientes, credenciais, informações financeiras ou conteúdo protegido de terceiros fora da necessidade autorizada.
- O token CAPI só é gerado e manuseado pelo agente depois de o usuário confirmar ciência (`capi_token_ciente`). Jamais enviá-lo ao frontend ou Git; guardar em painel/secret manager autenticado. Se exposto, avisar, revogar e substituir.
- Não criar provas falsas de resultados, WhatsApp, PIX, métricas, avaliação, quantidade de compradores ou estoque digital fictício.
- Promessas e dados pessoais devem respeitar normas de privacidade, publicidade e direitos do consumidor. Políticas de garantia/reembolso devem refletir prática e lei aplicáveis.
- Não produzir produtos digitais usando cópias não autorizadas de gibis, livros, músicas, PDFs alheios ou personagens licenciados. Aceitar somente conteúdo original/licenciado.
- Não burlar mecanismos antifraude de Wiapy, Facebook, tracking ou sistemas de conta.

## Regra de automação sem microaprovação

Atividades de pesquisa e edição criativa internas são autônomas; ações financeiras e externas são limitadas ao escopo explicitamente autorizado. Se um passo exige permissão real da plataforma ou consentimento indispensável, pedir **uma única intervenção objetiva**. Prosseguir com os outros passos quando possível e preservar estado.
