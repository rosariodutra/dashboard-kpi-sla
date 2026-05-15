# 📊 Dashboard KPI & SLA — Monitoramento de Chamados

> Sistema de monitoramento de chamados técnicos com controle de SLA, alertas automáticos e dashboard de indicadores em tempo real — desenvolvido em Python puro.

---

## 🧩 Contexto de Negócio

Em ambientes de suporte técnico e operações, o não cumprimento do SLA (Service Level Agreement) gera penalidades contratuais, insatisfação de clientes e retrabalho. A falta de visibilidade em tempo real sobre chamados vencidos ou a vencer impede que as equipes priorizem corretamente suas demandas.

Este projeto simula o sistema de monitoramento que desenvolvi na prática durante minha atuação como Analista de Processos, adaptado para demonstrar o raciocínio de controle operacional com dados.

**Problema resolvido:** centralizar o status de chamados, automatizar alertas de vencimento e gerar KPIs que apoiem a tomada de decisão do gestor sem depender de planilhas manuais.

---

## 🎯 Funcionalidades

- Dashboard com KPIs em tempo real (total, abertos, encerrados, taxa de resolução)
- Controle de SLA automático por prioridade
- Alertas para chamados vencidos ou a vencer em até 4h
- Cadastro, atualização e detalhamento de chamados
- Exportação de relatório em `.txt`
- Persistência em JSON entre sessões

---

## 📋 Regras de Negócio — SLA por Prioridade

| Prioridade | SLA       | Uso recomendado                        |
|-----------|-----------|----------------------------------------|
| Crítica   | 2 horas   | Sistemas fora do ar, impacto total     |
| Alta      | 8 horas   | Degradação de serviço, impacto parcial |
| Média     | 24 horas  | Solicitações operacionais urgentes     |
| Baixa     | 72 horas  | Melhorias, dúvidas, solicitações gerais|

---

## 🗂️ Estrutura de Dados — Dicionário

Cada chamado é armazenado em `chamados.json` com a seguinte estrutura:

| Campo          | Tipo    | Descrição                                      |
|----------------|---------|------------------------------------------------|
| `id`           | int     | Identificador único do chamado                 |
| `titulo`       | string  | Título resumido do chamado                     |
| `descricao`    | string  | Descrição detalhada do problema                |
| `prioridade`   | string  | Nível: Crítica, Alta, Média ou Baixa           |
| `status`       | string  | Estado: Aberto, Em andamento ou Encerrado      |
| `sla_horas`    | int     | Prazo em horas definido pela prioridade        |
| `criado_em`    | datetime| Data e hora de abertura do chamado             |
| `encerrado_em` | datetime| Data e hora de encerramento (null se aberto)   |

---

## 💡 Insights do Projeto

- Chamados **Críticos** abertos há mais de 2h acionam alerta vermelho automaticamente, independente da fila
- O cálculo de SLA é feito em tempo real a cada abertura do dashboard — sem necessidade de atualização manual
- A taxa de encerramento é um KPI direto de produtividade da equipe
- A exportação em `.txt` permite integração simples com sistemas legados ou envio por e-mail

---

## 📸 Preview

```
╔══════════════════════════════════════════╗
║      📊  DASHBOARD KPI & SLA  📊          ║
╚══════════════════════════════════════════╝

  ──────────────────────────────────────────
  KPI                                  VALOR
  ──────────────────────────────────────────
  Total de chamados                        8
  Abertos                                  3
  Em andamento                             2
  Encerrados                               3
  SLA vencidos 🔴                          1
  SLA a vencer (≤4h) 🟡                    1
  Taxa de encerramento                 37.5%
  ──────────────────────────────────────────

  ⚠️  ATENÇÃO: 1 chamado(s) com SLA VENCIDO!
```

---

## 🚀 Como executar

```bash
# Clone o repositório
git clone https://github.com/rosariodutra/dashboard-kpi-sla.git
cd dashboard-kpi-sla

# Sem dependências externas — Python 3.6+ puro
python dashboard_kpi.py
```

> Os dados são salvos automaticamente em `chamados.json` na mesma pasta.

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-7c3aed?style=flat-square&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-6d28d9?style=flat-square&logo=json&logoColor=white)

---

## 👩‍💻 Autora

Feito com 💜 por [Rosário Dutra](https://github.com/rosariodutra) · Analista de Dados & BI
