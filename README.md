# 📊 Dashboard KPI & SLA

Sistema de monitoramento de chamados no terminal com controle de SLA, alertas automáticos e dashboard de indicadores — desenvolvido em Python.

## 📸 Preview

```
╔══════════════════════════════════════════╗
║      📊  DASHBOARD KPI & SLA  📊          ║
║        github.com/rosariodutra            ║
╚══════════════════════════════════════════╝

  ──────────────────────────────────────────
  KPI                                  VALOR
  ──────────────────────────────────────────
  Total de chamados                        8
  Abertos                                  3
  Em andamento                             2
  Encerrados                               3
  ──────────────────────────────────────────
  SLA vencidos 🔴                          1
  SLA a vencer (≤4h) 🟡                    1
  Taxa de encerramento                 37.5%
  ──────────────────────────────────────────

  ⚠️  ATENÇÃO: 1 chamado(s) com SLA VENCIDO!
```

## ✨ Funcionalidades

- **Dashboard** com KPIs em tempo real (total, abertos, encerrados, taxa)
- **Controle de SLA** automático por prioridade (Crítica: 2h, Alta: 8h, Média: 24h, Baixa: 72h)
- **Alertas automáticos** para chamados vencidos ou a vencer em até 4h
- **Cadastro e gestão** de chamados com título, descrição e prioridade
- **Atualização de status** (Aberto → Em andamento → Encerrado)
- **Exportação de relatório** em `.txt`
- **Persistência em JSON** — dados salvos entre sessões

## 🚀 Como executar

```bash
# Clone o repositório
git clone https://github.com/rosariodutra/dashboard-kpi-sla.git

# Entre na pasta
cd dashboard-kpi-sla

# Execute
python dashboard_kpi.py
```

> Requer Python 3.6+. Sem dependências externas.

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-7c3aed?style=flat-square&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-6d28d9?style=flat-square&logo=json&logoColor=white)

## 👩‍💻 Autora

Feito com 💜 por [Rosário Dutra](https://github.com/rosariodutra)
