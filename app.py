import streamlit as st
import google.generativeai as genai
import json

# Configuração da página no Streamlit
st.set_page_config(
    page_title="Prompt Engineering Lab | Google Cloud Guide",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Prompt Engineering Lab")
st.caption("Demonstração prática baseada no Guia Oficial de Engenharia de Prompts do Google Cloud")

# Barra Lateral - Configuração
st.sidebar.header(" Configuração")
api_key = st.sidebar.text_input("Insira sua Gemini API Key:", type="password")
st.sidebar.markdown("[Obtenha uma chave gratuita no Google AI Studio](https://aistudio.google.com)")

# Log de exemplo para os testes de TI
LOG_EXEMPLO = """[2026-08-16 10:14:02] ERROR [auth-service] ConnectionTimeout: Failed to connect to AWS Cognito auth endpoint.
User ID: 94821 | IP: 192.168.1.45 | Retries: 3/3
Stacktrace: com.auth.cognito.TimeoutException: Endpoint unreachable at auth.us-east-1.amazonaws.com
Impact: User unable to log in to SaaS Dashboard."""

# Navegação por Abas
aba1, aba2, aba3 = st.tabs([" Comparador de Técnicas", " Cheat Sheet (Google Cloud)", " Gerador de Prompts"])

# ==========================================
# ABA 1: COMPARADOR DE TÉCNICAS
# ==========================================
with aba1:
    st.header("Análise de Incidentes de TI: Compare as Técnicas")
    st.write("Veja como a precisão e a estrutura da resposta do Gemini evoluem conforme aplicamos técnicas avançadas.")

    opcao = st.selectbox(
        "Escolha a técnica de Prompting a ser testada:",
        [
            "1. Zero-Shot (Comando Direto / Simples)",
            "2. Few-Shot (Com Exemplos Práticos)",
            "3. Chain-of-Thought (Raciocínio Passo a Passo + JSON)"
        ]
    )

    if "Zero-Shot" in opcao:
        prompt_final = f"""Analise este log de erro de TI e me diga o que fazer:

{LOG_EXEMPLO}"""
        explicacao = "<b>Zero-Shot:</b> Envia apenas a instrução direta, sem contexto prévio ou exemplos de saída esperada."

    elif "Few-Shot" in opcao:
        prompt_final = f"""Atue como um Analista de Suporte de TI. Classifique o log em: Causa Raiz, Severidade e Ação Recomendada.

Exemplo 1:
Log: [2026-08-16 09:00:00] ERROR [db-cluster] OutOfMemoryError: Java heap space.
Classificação: Causa Raiz: Memória insuficiente no DB | Severidade: Alta | Ação: Reiniciar serviço e aumentar Heap.

Exemplo 2:
Log: [2026-08-16 09:15:00] WARN [web-server] Disk space usage above 85%.
Classificação: Causa Raiz: Disco quase cheio | Severidade: Média | Ação: Limpar arquivos temporários.

Agora classifique este novo log:
Log: {LOG_EXEMPLO}
Classificação:"""
        explicacao = "<b>Few-Shot:</b> Fornece exemplos de entrada e saída para guiar o formato e o padrão da resposta."

    else:  # Chain-of-Thought
        prompt_final = f"""Atue como um Analista de Suporte de TI de Nível Senior.
Analise o log fornecido seguindo este raciocínio passo a passo:

Etapa 1: Identifique o serviço afetado e a causa raiz técnica.
Etapa 2: Avalie o impacto no usuário final e determine o nível de severidade (Baixa, Média, Alta, Crítica).
Etapa 3: Defina o SLA ideal de atendimento (ex: 1h, 4h, 24h).
Etapa 4: Recomende a ação corretiva imediata.

Após o raciocínio, retorne a resposta OBRIGATORIAMENTE no seguinte formato JSON:
{{
  "servico": "nome do serviço",
  "causa_raiz": "descrição curta",
  "severidade": "Nível",
  "sla_recomendado": "tempo",
  "acao_recomendada": "passos para resolução"
}}

Log para análise:
{LOG_EXEMPLO}"""
        explicacao = "<b>Chain-of-Thought (CoT):</b> Força o modelo a quebrar o problema em etapas lógicas e exige um formato estruturado (JSON)."

    st.markdown(explicacao, unsafe_allow_html=True)
    st.text_area("Prompt Enviado ao Gemini:", prompt_final, height=180)

    if st.button("Executar Prompt com Gemini", type="primary"):
        if not api_key:
            st.error("Por favor, insira sua Gemini API Key na barra lateral para executar.")
        else:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(prompt_final)
                
                st.subheader("Resposta Gerada pelo Gemini:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Erro ao conectar com a API: {e}")

# ==========================================
# ABA 2: CHEAT SHEET (GOOGLE CLOUD)
# ==========================================
with aba2:
    st.header("Guia Rápido de Engenharia de Prompts (Google Cloud)")
    st.write("Principais pilares para construir prompts eficazes para modelos LLM:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **1. Persona e Papel (Role Prompting)**
        * *Conceito:* Defina quem o modelo deve simular.
        * *Exemplo:* "Atue como um Arquiteto de Cloud Sênior..."

        **2. Contexto Claro**
        * *Conceito:* Forneça dados de fundo, restrições e o cenário de negócio.
        * *Exemplo:* "A aplicação roda em ambiente AWS e o erro afetou o login corporativo."

        **3. Instrução Direta e Verbos no Imperativo**
        * *Conceito:* Seja específico sobre a tarefa final.
        * *Exemplo:* "Classifique, extraia os dados e sugira uma solução."
        """)

    with col2:
        st.markdown("""
        **4. Formato de Saída (Output Formatting)**
        * *Conceito:* Especifique o formato exato da resposta (JSON, Tabela, Bullets).
        * *Exemplo:* "Retorne os resultados em uma tabela Markdown de 3 colunas."

        **5. Exemplos de Validação (Few-Shot)**
        * *Conceito:* Dê ao modelo 1 a 3 exemplos de entrada e saída esperadas para reduzir alucinações.
        """)

# ==========================================
# ABA 3: GERADOR DE PROMPTS
# ==========================================
with aba3:
    st.header("Gerador Estruturado de Prompts")
    st.write("Monte prompts otimizados preenchendo os campos abaixo:")

    papel = st.text_input("1. Qual o papel da IA?", "Analista de Suporte de TI Nível 2")
    tarefa = st.text_area("2. Qual é a tarefa principal?", "Analisar relatório de erro e sugerir comandos de terminal para solução.")
    formato = st.selectbox("3. Formato da Resposta:", ["Lista de Passos (Bullets)", "Tabela Markdown", "JSON Estruturado", "Texto Explicativo"])
    contexto_add = st.text_area("4. Contexto Adicional (Opcional):", "Ambiente Linux Ubuntu 22.04 LTS.")

    prompt_gerado = f"""Atue como: {papel}

Sua tarefa principal é:
{tarefa}

Contexto relevante:
{contexto_add}

Formato de saída exigido:
Por favor, responda no formato: {formato}.
"""

    st.subheader("Seu Prompt Estruturado:")
    st.code(prompt_gerado, language="text")
