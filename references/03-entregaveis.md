# 03 — CRIAR TODOS OS ENTREGÁVEIS DO PRODUTO (OBRIGATÓRIO)

**Nunca pule esta fase.** Antes de mockups, checkout, tráfego e promessa pública, construa os arquivos reais que o cliente receberá.

## 1. Inventário de conteúdo

Ler `produto/briefing.md`; converter promessas em checklist mensurável:

- Item 01, nome, formato, objetivo, tamanho estimado e critério de conclusão.
- Itens bônus, quando prometidos.
- Arquivos editáveis exigidos, instruções de edição e licença de uso.
- Quais modelos são originais e se há fontes/figuras com licença.

Se o pacote inicial parecer grande demais para produzir sem perda de qualidade, **ajustar a oferta e a copy antes de anunciar**. Nunca prometer centenas/milhares de arquivos inexistentes.

## 2. Produção por formato

**PDF / ebook / apostila:** redigir conteúdo completo, original e correto, capa, índice, seções com exemplos práticos, margens adequadas, paginação, fontes legíveis, links testados e página de suporte. Renderizar e revisar visualmente páginas variadas. Evitar textos repetitivos e conteúdo genérico de enchimento.

**Planilha / templates:** criar arquivo realmente editável, testar fórmulas em cenários normais e limites, documentar campos e proteger apenas células necessárias. Incluir exemplo preenchido sem dados pessoais reais.

**Atividades e imprimíveis:** criar páginas A4 em alta resolução, verificar sangria/margens, qualidade de impressão, ortografia, organização por assunto e páginas duplicadas. Incluir instruções de uso.

**Pacotes de modelos Canva:** criar modelos originais, disponibilizar links de template válidos quando a conta permitir, testar abertura em janela de usuário diferente; incluir alternativa de arquivo quando cabível. Não declarar "editável no Canva" sem testar.

**Áudio / playback / vídeo:** produzir ou licenciar arquivos adequadamente, verificar audição, metadados, integridade e uso comercial; jamais inserir músicas protegidas sem direitos.

**Coleção de imagens:** usar geração original autorizada, exportar PNG/JPEG/PDF conforme oferta, revisar visualmente e reduzir imagens com defeitos. Não incluir marcas/personagens sem autorização.

## 2b. Aparência caprichada (obrigatório)

O material precisa parecer um produto premium e "fofinho/arrumadinho": paleta definida, capas ilustradas (geradas no ChatGPT), ícones, cabeçalhos estilizados, espaçamentos generosos, tipografia consistente. Planilhas com cabeçalho colorido, abas coloridas, instruções visuais e nada com cara de Excel padrão. Revise visualmente cada página antes do QA.

## 3. Conteúdo útil, não decorativo

Cada elemento prometido precisa existir e ajudar o comprador a realizar algo. Produzir guias, exemplos, modelos e checklist de uso. Não fabricar certificações, provas de lucro, depoimentos, artigos de lei desatualizados, cálculos financeiros errados ou dicas perigosas.

## 4. Controle de qualidade obrigatório

- Abrir **todos** os arquivos e fazer amostragem reforçada de páginas, fórmulas, links, imagens e mídias.
- Checar PDFs: capa, sumário, legibilidade em celular, ortografia e tamanho; verificar que imprimíveis A4 estão em A4.
- Checar arquivos zip: extrair para pasta temporária e conferir ausência de erro.
- Verificar nomes consistentes; nenhuma pasta vazia, placeholder, amostra indevida ou arquivo temporário.
- Aplicar antivírus quando disponível e não embutir executáveis desnecessários.
- Verificar quantitativos: anunciado vs. entregue vs. conteúdo da página e checkout.
- Fazer checklist para direito autoral/licenças, especialmente músicas, gibis, marcas e personagens.

## 5. Organização e compactação

```text
produto/
  briefing.md
  entregaveis/
    00-LEIA-PRIMEIRO.pdf
    01-produto-principal.pdf
    02-bonus-01.pdf
    ...
  preview/
    pagina-amostra-01.png
    pagina-amostra-02.png
  entrega-final.zip
  manifesto-entrega.md
```

Os nomes acima são ilustrativos: use extensões realmente adequadas. Criar `manifesto-entrega.md` com quantidade de arquivos, extensões, tamanhos, data, versões, licença e instruções de acesso. `entrega-final.zip` deve ser validado por extração. Se upload individual for melhor no checkout, manter arquivos individuais e zip de backup.

## 6. Prévias para vender sem falsidade

Criar 3–8 prévias reais do material (capturas de páginas e arquivos), que depois serão usadas em mockups e na landing page. Nunca mockup de arquivo que não exista.

## 7. Mini-produtos opcionais (order bumps)

Se criados, cada bump deve ter pasta e zip separados, sem repetir o conteúdo do produto principal; seguir `references/14-orderbumps.md`.

## Gate de conclusão

**Bloquear o lançamento** enquanto houver entregável ausente, corrompido, não revisado, sem licença quando necessário ou inconsistente com a promessa. Salvar `produto/manifesto-entrega.md` com status PASS/FAIL e evidências. Prosseguir automaticamente para assets quando PASS.
