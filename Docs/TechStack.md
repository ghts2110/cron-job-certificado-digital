## TechStack:
Next.js: 15.3.1
TypeScript: 5.8.3
Tremor: 3.18.7
Tailwind CSS: 4.1.5
@supabase/supabase-js: 2.49.4
Jest: 29.7.0

---

## Infraestrutura & DevOps
- CI/CD: Automatizar deploy e testes com GitHub Actions e Vercel.
- Ambientes separados: Criar ambientes `development`, `staging` e `production`.
- Linting e Code Style:
  - ESLint para padronização.
  - Prettier para formatação automática.
- Husky + lint-staged: Executar lint/testes automaticamente antes de `git commit` ou `git push`.

---

## Segurança
- Row-Level Security (RLS) no Supabase: Garantir que usuários vejam apenas seus dados.
- Rate limiting: Prevenir abusos com middlewares (ex: `rate-limit`).
- Criptografia de dados sensíveis: Se armazenar dados como documentos, senhas secundárias, etc.

---

## Performance e Monitoramento
- Monitoramento de Erros: Usar ferramentas como Sentry ou LogRocket.
- Analytics: Usar Vercel Analytics.
- Code Splitting & Lazy Loading: Melhorar performance em rotas e componentes pesados.
- Caching:
  - React Query para chamadas ao Supabase.
  - Revalidação automática (`revalidate` no Next.js).

---

## Testes e Qualidade
- Testes de Integração: React Testing Library.
- Testes End-to-End: Playwright.
- Cobertura de Código: Medir com `--coverage` do Jest.
- Testar Supabase: Usar mocking ou um ambiente separado para testes.

---

##  Experiência do Usuário
- Internacionalização (i18n): `next-i18next` para suporte multilíngue.
- Acessibilidade (a11y): Verificação com ferramentas como axe-core, lint de acessibilidade.
- Animações: Usar `framer-motion` para suavizar transições e UX.

---

## Documentação
- README.md completo: Setup, comandos, deploy e contribuição.
- Storybook: Documentar e visualizar componentes de UI isoladamente.
- Documentação de API: Usar OpenAPI/Swagger se houver backend próprio ou endpoints complexos.
- Changelog: Manter um `CHANGELOG.md` para controle de versões.

---

## Organização do Projeto
- Estrutura de pastas clara: Separar bem páginas, componentes, hooks, contextos, serviços, etc.
- Aliases de importação: Usar `@/components`, `@/lib`, etc. com `tsconfig.json`.

---

## Extra
- Feature flags: Controlar lançamentos com `unleash` ou feature toggles simples.
- Dark mode: Habilitar tema escuro com Tailwind (`darkMode: 'class'`).
- PWA: Se necessário, transformar o app em Progressive Web App.