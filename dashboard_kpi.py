# =============================================================
#  📊 DASHBOARD KPI & SLA — MONITORAMENTO DE CHAMADOS
#  Autor: Rosário Dutra
#  GitHub: github.com/rosariodutra
#  Descrição: Sistema de monitoramento de chamados com controle
#             de SLA, alertas automáticos e dashboard de KPIs.
# =============================================================

import os
import json
from datetime import datetime, timedelta

# ── Arquivo de dados ──────────────────────────────────────────
ARQUIVO = "chamados.json"

# ── Cores ─────────────────────────────────────────────────────
ROXO    = "\033[35m"
VERDE   = "\033[32m"
AMARELO = "\033[33m"
VERMELHO= "\033[31m"
RESET   = "\033[0m"
NEGRITO = "\033[1m"

# ── Persistência ──────────────────────────────────────────────

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar(chamados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(chamados, f, ensure_ascii=False, indent=2)

# ── Utilitários ───────────────────────────────────────────────

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cabecalho():
    print(f"{ROXO}")
    print("╔══════════════════════════════════════════╗")
    print("║      📊  DASHBOARD KPI & SLA  📊          ║")
    print("║        github.com/rosariodutra            ║")
    print("╚══════════════════════════════════════════╝")
    print(f"{RESET}")

def agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def parse_dt(s):
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

def status_sla(chamado):
    if chamado["status"] == "Encerrado":
        return f"{VERDE}✅ Encerrado{RESET}"
    prazo = parse_dt(chamado["criado_em"]) + timedelta(hours=chamado["sla_horas"])
    agora_dt = datetime.now()
    diff = prazo - agora_dt
    horas_restantes = diff.total_seconds() / 3600

    if horas_restantes < 0:
        return f"{VERMELHO}🔴 VENCIDO ({abs(int(horas_restantes))}h atraso){RESET}"
    elif horas_restantes <= 4:
        return f"{AMARELO}🟡 A vencer ({int(horas_restantes)}h restantes){RESET}"
    else:
        return f"{VERDE}🟢 No prazo ({int(horas_restantes)}h restantes){RESET}"

def proximo_id(chamados):
    if not chamados:
        return 1
    return max(c["id"] for c in chamados) + 1

# ── Dashboard principal ───────────────────────────────────────

def dashboard(chamados):
    limpar()
    cabecalho()

    total     = len(chamados)
    abertos   = sum(1 for c in chamados if c["status"] == "Aberto")
    andamento = sum(1 for c in chamados if c["status"] == "Em andamento")
    encerrados= sum(1 for c in chamados if c["status"] == "Encerrado")

    vencidos  = 0
    a_vencer  = 0
    for c in chamados:
        if c["status"] == "Encerrado":
            continue
        prazo = parse_dt(c["criado_em"]) + timedelta(hours=c["sla_horas"])
        diff  = (prazo - datetime.now()).total_seconds() / 3600
        if diff < 0:
            vencidos += 1
        elif diff <= 4:
            a_vencer += 1

    taxa_enc = f"{(encerrados/total*100):.1f}%" if total > 0 else "0%"

    print(f"  {'─'*42}")
    print(f"  {'KPI':30} {'VALOR':>10}")
    print(f"  {'─'*42}")
    print(f"  {'Total de chamados':<30} {ROXO}{total:>10}{RESET}")
    print(f"  {'Abertos':<30} {AMARELO}{abertos:>10}{RESET}")
    print(f"  {'Em andamento':<30} {ROXO}{andamento:>10}{RESET}")
    print(f"  {'Encerrados':<30} {VERDE}{encerrados:>10}{RESET}")
    print(f"  {'─'*42}")
    print(f"  {'SLA vencidos 🔴':<30} {VERMELHO}{vencidos:>10}{RESET}")
    print(f"  {'SLA a vencer (≤4h) 🟡':<30} {AMARELO}{a_vencer:>10}{RESET}")
    print(f"  {'Taxa de encerramento':<30} {VERDE}{taxa_enc:>10}{RESET}")
    print(f"  {'─'*42}\n")

    # Alertas
    if vencidos > 0:
        print(f"  {VERMELHO}{NEGRITO}⚠️  ATENÇÃO: {vencidos} chamado(s) com SLA VENCIDO!{RESET}")
    if a_vencer > 0:
        print(f"  {AMARELO}⏰  {a_vencer} chamado(s) a vencer nas próximas 4 horas!{RESET}")
    if vencidos == 0 and a_vencer == 0 and total > 0:
        print(f"  {VERDE}✅  Todos os chamados estão dentro do SLA!{RESET}")
    print()

# ── Listar chamados ───────────────────────────────────────────

def listar(chamados, filtro=None):
    limpar()
    cabecalho()

    lista = chamados
    if filtro:
        lista = [c for c in chamados if c["status"] == filtro]

    if not lista:
        print("  Nenhum chamado encontrado.\n")
        input("  [Enter para voltar]")
        return

    print(f"  {'ID':<5} {'Título':<25} {'Prioridade':<12} {'Status SLA'}")
    print(f"  {'─'*65}")
    for c in lista:
        sla = status_sla(c)
        print(f"  {c['id']:<5} {c['titulo'][:24]:<25} {c['prioridade']:<12} {sla}")
    print()
    input("  [Enter para voltar]")

# ── Cadastrar chamado ─────────────────────────────────────────

def cadastrar(chamados):
    limpar()
    cabecalho()
    print("  ── Novo Chamado ──\n")

    titulo    = input("  Título: ").strip()
    descricao = input("  Descrição: ").strip()

    print("\n  Prioridade:\n  1. Baixa\n  2. Média\n  3. Alta\n  4. Crítica\n")
    prioridades = {"1": "Baixa", "2": "Média", "3": "Alta", "4": "Crítica"}
    p = input("  Opção: ").strip()
    prioridade = prioridades.get(p, "Média")

    sla_map = {"Baixa": 72, "Média": 24, "Alta": 8, "Crítica": 2}
    sla_horas = sla_map[prioridade]
    print(f"\n  SLA definido automaticamente: {sla_horas}h para prioridade {prioridade}")

    chamado = {
        "id":         proximo_id(chamados),
        "titulo":     titulo,
        "descricao":  descricao,
        "prioridade": prioridade,
        "status":     "Aberto",
        "sla_horas":  sla_horas,
        "criado_em":  agora(),
        "encerrado_em": None,
    }
    chamados.append(chamado)
    salvar(chamados)
    print(f"\n  {VERDE}✅ Chamado #{chamado['id']} criado com sucesso!{RESET}\n")
    input("  [Enter para continuar]")

# ── Atualizar status ──────────────────────────────────────────

def atualizar(chamados):
    limpar()
    cabecalho()
    print("  ── Atualizar Status ──\n")

    id_str = input("  ID do chamado: ").strip()
    if not id_str.isdigit():
        print("  ⚠️  ID inválido!"); input("  [Enter]"); return

    chamado = next((c for c in chamados if c["id"] == int(id_str)), None)
    if not chamado:
        print("  ⚠️  Chamado não encontrado!"); input("  [Enter]"); return

    print(f"\n  Chamado: {chamado['titulo']}")
    print(f"  Status atual: {chamado['status']}\n")
    print("  1. Aberto\n  2. Em andamento\n  3. Encerrado\n")

    op = input("  Novo status: ").strip()
    status_map = {"1": "Aberto", "2": "Em andamento", "3": "Encerrado"}

    if op not in status_map:
        print("  ⚠️  Opção inválida!"); input("  [Enter]"); return

    chamado["status"] = status_map[op]
    if chamado["status"] == "Encerrado":
        chamado["encerrado_em"] = agora()

    salvar(chamados)
    print(f"\n  {VERDE}✅ Status atualizado para: {chamado['status']}{RESET}\n")
    input("  [Enter para continuar]")

# ── Detalhar chamado ──────────────────────────────────────────

def detalhar(chamados):
    limpar()
    cabecalho()
    id_str = input("  ID do chamado: ").strip()
    if not id_str.isdigit():
        print("  ⚠️  ID inválido!"); input("  [Enter]"); return

    c = next((c for c in chamados if c["id"] == int(id_str)), None)
    if not c:
        print("  ⚠️  Não encontrado!"); input("  [Enter]"); return

    print(f"\n  {'─'*42}")
    print(f"  ID          : #{c['id']}")
    print(f"  Título      : {c['titulo']}")
    print(f"  Descrição   : {c['descricao']}")
    print(f"  Prioridade  : {c['prioridade']}")
    print(f"  Status      : {c['status']}")
    print(f"  SLA         : {c['sla_horas']}h")
    print(f"  Criado em   : {c['criado_em']}")
    print(f"  Encerrado em: {c['encerrado_em'] or '—'}")
    print(f"  SLA Status  : {status_sla(c)}")
    print(f"  {'─'*42}\n")
    input("  [Enter para voltar]")

# ── Exportar relatório ────────────────────────────────────────

def exportar(chamados):
    nome = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nome, "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE CHAMADOS — Dashboard KPI & SLA\n")
        f.write(f"Gerado em: {agora()}\n")
        f.write("=" * 50 + "\n\n")
        for c in chamados:
            f.write(f"#{c['id']} | {c['titulo']} | {c['prioridade']} | {c['status']} | SLA: {c['sla_horas']}h\n")
            f.write(f"   Criado: {c['criado_em']} | Encerrado: {c['encerrado_em'] or '—'}\n\n")
    print(f"\n  {VERDE}✅ Relatório exportado: {nome}{RESET}\n")
    input("  [Enter para continuar]")

# ── Menu principal ────────────────────────────────────────────

def main():
    chamados = carregar()

    while True:
        limpar()
        cabecalho()
        dashboard(chamados)

        print("  1. Listar todos os chamados")
        print("  2. Listar por status")
        print("  3. Novo chamado")
        print("  4. Atualizar status")
        print("  5. Detalhar chamado")
        print("  6. Exportar relatório (.txt)")
        print("  0. Sair\n")

        op = input("  Opção: ").strip()

        if op == "1":
            listar(chamados)
        elif op == "2":
            limpar(); cabecalho()
            print("  1. Aberto\n  2. Em andamento\n  3. Encerrado\n")
            f = input("  Filtro: ").strip()
            fm = {"1": "Aberto", "2": "Em andamento", "3": "Encerrado"}
            listar(chamados, fm.get(f))
        elif op == "3":
            cadastrar(chamados)
        elif op == "4":
            atualizar(chamados)
        elif op == "5":
            detalhar(chamados)
        elif op == "6":
            exportar(chamados)
        elif op == "0":
            limpar(); cabecalho()
            print(f"  Até logo! 💜\n"); break
        else:
            print("  ⚠️  Opção inválida!"); input("  [Enter]")

if __name__ == "__main__":
    main()
