![Edmar Siqueira - Portfólio](app/static/img/readme-banner.webp)

# 🚀 Portfólio Profissional – Arquitetura Modular, SRP e SEO Dinâmico

[![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)]()
[![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask)]()
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-38BDF8?style=for-the-badge&logo=tailwindcss)]()
[![Jinja2](https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge&logo=jinja)]()
[![Status](https://img.shields.io/badge/Status-Ativo-success?style=for-the-badge)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)]()

Este repositório contém o **sistema completo** que gerencia o portfólio de projetos de **Edmar Siqueira**.  
Diferente de um site estático, este portfólio foi projetado como um **produto modular**, seguindo princípios de arquitetura limpa, SRP, componentização e carregamento dinâmico de conteúdo.

O resultado é um sistema:

- escalável  
- organizado  
- fácil de manter  
- com SEO avançado  
- com páginas dinâmicas  
- com templates inteligentes  
- com design premium  

---

# 🧠 Pilares Técnicos do Projeto

## ✔ 1. Arquitetura Modular (Blueprints + SRP)
Cada módulo do sistema tem **uma única responsabilidade**, seguindo o princípio **SRP (Single Responsibility Principle)**:

- `routes/` → rotas separadas por contexto  
- `templates/` → componentes reutilizáveis  
- `data/` → fonte de dados dos projetos  
- `services/` → camada preparada para integrações futuras  
- `static/` → assets organizados  

Benefícios:

- manutenção simples  
- escalabilidade  
- clareza arquitetural  
- facilidade para adicionar novos projetos  

---

## ✔ 2. Páginas de Projetos Dinâmicas (JSON + Templates)

Cada projeto é carregado a partir de: 
```text
data/projects.json
```
E renderizado dinamicamente por:
```text
project_detail.html
```
O conteúdo técnico de cada projeto fica em:
```text
templates/projects/<slug>.html
```

Vantagens:

- adicionar novos projetos sem alterar rotas  
- conteúdo técnico separado  
- layout global reaproveitado  
- atualização simples e rápida  

---

## ✔ 3. SEO Avançado e Dinâmico

O sistema implementa:

- `<title>` dinâmico  
- `<meta description>` dinâmica  
- OpenGraph (WhatsApp, LinkedIn, Facebook)  
- Twitter Cards  
- Imagem de preview  
- SEO por projeto  

Tudo configurado via Jinja2 + blocks.

---

## ✔ 4. Design Premium com TailwindCSS

O layout utiliza:

- animações suaves (fade-in, stagger)  
- cards responsivos  
- componentes reutilizáveis  
- dark theme nativo  
- tipografia refinada  
- espaçamentos consistentes  

---

## ✔ 5. Rota Inteligente para GitHub

Cada projeto possui:

- botão GitHub inteligente  
- comportamento diferente para projetos públicos/privados  
- ícone elegante **↗** para links externos  

---

# 🧩 Estrutura Completa do Projeto

```text
app/
 ├── routes/                     # Blueprints e rotas
 │    ├── home.py                # Página inicial
 │    ├── projects.py            # Lista de projetos
 │    ├── project_detail.py      # /projects/<slug> + /github
 │    ├── contact.py             # Página de contato
 │    └── seo.py                 # SEO dinâmico
 │
 ├── templates/
 │    ├── components/            # Cards, grids, navbar, footer
 │    ├── projects/              # Conteúdo técnico dos projetos
 │    │     ├── alpha_bot.html
 │    │     ├── notebook_manager.html
 │    │     └── portfolio_manager.html
 │    ├── project_detail.html    # Página dinâmica de projeto
 │    ├── projects.html          # Lista de projetos
 │    ├── home.html
 │    ├── contact.html
 │    └── base.html              # Layout global + SEO
 │
 ├── static/
 │    ├── img/                   # Imagens do site
 │    ├── css/
 │    └── js/
 │
 ├── data/
 │    └── projects.json          # Banco de dados dos projetos
 │
 └── __init__.py                 # Factory Pattern

```
# 🖥️ Projetos em Destaque

## 🔹 Portfolio Manager – Edmar (Público)
Sistema que gerencia todo o portfólio, com:
- **Arquitetura modular**
- **SRP aplicado** (Single Responsibility Principle)
- **Templates dinâmicos**
- **Animações suaves**
- **SEO avançado**
- **Design premium**

🔗 **GitHub:** [https://github.com/jesiqueira/edmar-portfolio](https://github.com/jesiqueira/edmar-portfolio)

---

## 🔹 Alpha Bot Trading – US500 (Privado)
Robô profissional de alta performance com:
- **Arquitetura SRP**
- **Estratégias em camadas**
- **IA com XGBoost**
- **PostgreSQL + auditoria completa**
- **API com FastAPI**

---

## 🔹 Notebook Manager – Konecta (Privado)
Sistema corporativo focado em:
- **Gestão de notebooks**
- **Auditoria detalhada**
- **Governança de TI**
- **Conformidade**
- **API com FastAPI + PostgreSQL**

---

## 📦 Como rodar o projeto
1. **Clone o repositório:**
```bash
git clone https://github.com/jesiqueira/edmar-portfolio.git
cd edmar-portfolio
```

2. **Crie o ambiente virtual**
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
4. **Execute o servidor Flask**
```bash
flask run
```
5. **🧪 Modo Debug**
```bash
flask run --debug
```
Ativa:
- reload automático
- debugger interativo
- logs detalhados

## 🌐 Deploy (planejado)
- **Render**
- **Railway**
- **Fly.io**
- **Dockerfile + docker-compose**
- **GitHub Actions (CI/CD)**

## 🔍 SEO Implementado
- **Títulos dinâmicos**
- **Descrições dinâmicas**
- **OpenGraph**
- **Twitter Cards**
- **Preview image**
- **SEO por projeto**

## 🗺️ Roadmap Técnico
- [ ] Dark/Light Mode com persistência
- [ ] Página de Serviços
- [ ] Formulário de contato funcional
- [ ] Versão em inglês
- [ ] Deploy em produção
- [ ] Testes automatizados
- [ ] Painel admin para gerenciar projetos
- [ ] API interna para CRUD de projetos

## 📄 Licença
MIT — livre para uso e estudo.

## ✨ Autor
**Edmar Siqueira** Desenvolvedor Python & Automação  
📧 [edmar.ade@gmail.com](mailto:edmar.ade@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/edmarsiqueira/)