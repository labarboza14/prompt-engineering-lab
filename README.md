# ⚡ Prompt Engineering Lab: Guia Prático com Gemini & Streamlit

> **Um laboratório prático e interativo construído para demonstrar visualmente como técnicas de Engenharia de Prompts impactam a precisão e a estrutura das respostas de Modelos de Linguagem (LLMs).**

---

##  Sobre o Projeto

Este repositório foi desenvolvido como parte de uma iniciativa do **Google Student Ambassadors (Embaixadores Estudantis do Google)**. 

O objetivo principal deste projeto é traduzir os conceitos teóricos do guia oficial [What is Prompt Engineering? — Google Cloud](https://cloud.google.com/discover/what-is-prompt-engineering?hl=pt-BR) em uma **experiência prática, interativa e altamente aplicável**.

Em vez de apenas ler sobre técnicas de engenharia de prompts, este laboratório permite que estudantes, desenvolvedores e entusiastas de IA **testem e comparem no mundo real** como diferentes estruturas de instruções afetam a qualidade das respostas geradas pelo **Google Gemini**.

---

##  O Caso Prático: Análise de Incidentes de TI

Para tornar o aprendizado concreto, o laboratório simula um cenário real do dia a dia do mercado corporativo: **Análise e Classificação Automática de Logs de Erro de TI**.

O usuário pode alternar entre três níveis de maturidade de prompts sobre o mesmo log de erro:

| Técnica | Abordagem | Resultado Esperado |
| :--- | :--- | :--- |
| **1. Zero-Shot** | Instrução direta e simples sem exemplos prévios. | Resposta genérica em texto corrido, variando em formato e profundidade. |
| **2. Few-Shot** | Instrução combinada com exemplos práticos (entrada/saída). | Resposta padronizada segundo os exemplos fornecidos, reduzindo ambiguidades. |
| **3. Chain-of-Thought (CoT)** | Raciocínio guiado passo a passo com restrição de formato JSON. | Resposta altamente estruturada, com análise lógica das etapas e pronta para integração via API. |

---

##  Funcionalidades da Aplicação

1. ** Comparador de Técnicas:** Compare em tempo real como o Gemini reage a estratégias de Zero-Shot, Few-Shot e Chain-of-Thought.
2. ** Cheat Sheet (Google Cloud):** Resumo visual dos 5 pilares fundamentais da Engenharia de Prompts segundo a documentação do Google Cloud.
3. ** Gerador de Prompts Estruturados:** Ferramenta interativa que ajuda o usuário a montar um prompt completo (Persona + Tarefa + Contexto + Formato de Saída).

---

##  Tecnologias Utilizadas

* **[Streamlit](https://streamlit.io/):** Framework em Python para construção rápida da interface web interativa.
* **[Google Gemini API (`google-generativeai`)](https://ai.google.dev/):** Modelo de linguagem avançado do Google utilizado para o processamento e execução dos prompts.
* **Python 3.10+**

---

##  Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Uma chave de API gratuita obtida no **[Google AI Studio](https://aistudio.google.com)**.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação Streamlit:**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador:**
   Abra `http://localhost:8501`, insira sua Gemini API Key na barra lateral e comece a testar!

---

##  Estrutura do Repositório

```text
├── app.py              # Código principal da aplicação Streamlit
├── requirements.txt    # Dependências do projeto (streamlit, google-generativeai)
└── README.md           # Documentação do projeto
```

---

##  Aprendizados & Conclusões

Através deste laboratório, fica evidente que **a Engenharia de Prompts não é apenas sobre "saber fazer perguntas", mas sim sobre arquitetar o contexto, delimitar formatos e direcionar o raciocínio da IA**. 

Dominar essas técnicas permite transformar respostas genéricas em saídas determinísticas e estruturadas, prontas para alimentar pipelines automatizados em ambientes de produção.

---

 *Desenvolvido como parte do programa de Embaixadores Estudantis do Google com base na documentação oficial do Google Cloud: https://cloud.google.com/discover/what-is-prompt-engineering?hl=pt-BR .*
