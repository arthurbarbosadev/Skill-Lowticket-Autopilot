# 06 — GitHub privado + Vercel (publicação em duas fases)

## Ordem proposital

A Wiapy exige o campo URL da página de vendas. Por isso, **publicar primeiro um preview técnico** em `.vercel.app`, depois configurar o checkout, depois atualizar a URL de compra e publicar a versão final. Não lançar anúncios apontando para preview com CTA pendente.

## GitHub

1. Verificar MCP do GitHub. Se indisponível, usar Git/CLI ou navegador autenticado e autorizado.
2. Criar repositório **privado** com slug original, por exemplo `lt-nome-produto`.
3. Configurar `.gitignore` para `.env`, `node_modules`, builds locais, downloads com tokens, arquivos confidenciais e credenciais.
4. Fazer commit somente do site e documentação pública apropriada; não subir base de clientes, tokens do pixel/CAPI, credenciais do tracking, arquivos particulares ou materiais de produto pagos que não precisem ser públicos.
5. Registrar URL do repositório e hash de commit. Se já existir repo correspondente ao projeto, reutilizar para evitar duplicação.

## Vercel

1. Verificar MCP Vercel. Se indisponível, usar Vercel CLI ou interface autenticada.
2. Identificar o plano da conta/time (**Hobby** ou **Pro**) e registrar em `vercel_plano`. Não bloquear: criar o projeto normalmente em qualquer plano. Se for Hobby, o aviso de que uso comercial exige Pro vai no relatório e na mensagem final (fase 12).
3. Importar o repo privado, configurar framework, comandos de build e diretório de saída observados.
4. Definir variáveis de ambiente pela interface segura quando necessárias; nunca registrar valores secretos em logs ou texto.
4b. Adicionar um domínio `.vercel.app` **curto e sem hífen** ao projeto (ex.: `meuproduto.vercel.app`) e usar esse endereço na Wiapy e nos anúncios.
5. Publicar, aguardar status pronto e obter URL exata `https://slug.vercel.app` (o slug **não pode ser inventado**).
6. Acessar URL pública em desktop e celular, checar HTTP, assets, SEO básico, nenhum vazamento de diretórios/código-fonte secreto.
7. Guardar URL para formulário Wiapy e integração tracking.

## Atualização após checkout

Reabrir site, inserir link de checkout real, verificar scripts oficiais, atualizar consentimento/privacidade, buildar, commitar e confirmar deploy atualizado na Vercel. Confirmar mudança no domínio público (não apenas no ambiente local).

## Problemas comuns

- Conta sem acesso MCP: usar navegador se permitido ou interromper apenas deploy.
- Repo já existente: verificar proprietário e reutilizar; não sobrescrever projetos alheios.
- Build quebrado: resolver dependências, paths e erros antes de avançar.
- Domínio Vercel já ocupado: escolher variação original, guardar a URL real.
- Secret acidental no Git: remover do histórico quando necessário e revogar/rotacionar imediatamente.

**Gate inicial:** URL real da página acessível, ainda que o CTA esteja pendente. **Gate final:** checkout e scripts presentes e testados.
