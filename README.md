# ⚡ Prompt Engineering Lab: Guia Prático com Gemini & Streamlit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://prompt-engineering-lab-mzfgjsfjj84rg8deo6khze.streamlit.app/)

> **Um laboratório prático, visual e interativo para entender como diferentes técnicas de Engenharia de Prompts moldam as respostas de Modelos de Linguagem (LLMs) usando o Google Gemini.**

 **Acesse a aplicação online:** [Prompt Engineering Lab na Nuvem](https://prompt-engineering-lab-mzfgjsfjj84rg8deo6khze.streamlit.app/)

---

##  Sobre o Projeto

Este repositório foi criado no âmbito do programa **Google Student Ambassadors (Embaixadores Estudantis do Google)**.

A proposta principal é **desmistificar a Engenharia de Prompts** para iniciantes e estudantes de tecnologia. Em vez de focar apenas em teoria, este projeto traduz o guia oficial do Google Cloud ([What is Prompt Engineering?](https://cloud.google.com/discover/what-is-prompt-engineering?hl=pt-BR)) em um ambiente prático de experimentação visual.

###  O que é Engenharia de Prompts (de forma simples)?
Se a Inteligência Artificial Generativa é como um profissional altamente qualificado, a **Engenharia de Prompts** é a arte de dar as **instruções corretas, no formato certo e com o contexto adequado** para que essa IA entregue exatamente o que você precisa, sem "adivinhar" ou gerar respostas vagas.

---

##  O Caso Prático: Análise de Incidentes de TI

Para demonstrar a evolução das respostas da IA, a aplicação utiliza um cenário do mundo real: **Triagem Automática de Logs de Erro de Sistema**.

O usuário pode alternar entre três níveis de maturidade de instrução para o mesmo erro:

| Técnica | O que ela faz? | Analogia do Dia a Dia | Resultado no Gemini |
| :--- | :--- | :--- | :--- |
| **1. Zero-Shot** | Pede uma solução direta sem exemplos ou formato obrigatório. | Pedir a um cozinheiro: *"Faça um almoço"*. | Resposta genérica em texto corrido, detalhada porém não padronizada. |
| **2. Few-Shot** | Fornece 1 ou mais exemplos de entrada e resposta esperada. | Mostrar ao cozinheiro a foto de 2 pratos montados antes de pedir o seu. | Resposta padronizada e previsível, seguindo o padrão dos exemplos. |
| **3. Chain-of-Thought (CoT)** | Força a IA a raciocinar em etapas lógicas e responder em JSON. | Pedir ao cozinheiro que anote a receita passo a passo e entregue a ficha técnica. | Análise profunda do incidente com saída estruturada pronta para automação/APIs. |

---

##  O que você encontra na Aplicação

1. ** Comparador de Técnicas (Aba 1):** Veja lado a lado o prompt enviado, a explicação teórica da técnica e a resposta gerada pelo modelo `gemini-2.5-flash`.
2. ** Cheat Sheet - Google Cloud (Aba 2):** Os 5 pilares essenciais de um bom prompt (Persona, Contexto, Instrução Imperativa, Formato de Saída e Exemplos).
3. ** Gerador Estruturado de Prompts (Aba 3):** Um formulário interativo para você montar seu próprio prompt profissional preenchendo apenas 4 campos simples.

---

##  Como Usar a Aplicação

Você pode usar o app de **duas formas**:

### Opção A: Acessar Diretamente pelo Navegador (Sem Instalar Nada)
1. Acesse o link oficial: [prompt-engineering-lab.streamlit.app](https://prompt-engineering-lab-mzfgjsfjj84rg8deo6khze.streamlit.app/)
2. Obtenha uma chave de API gratuita no [Google AI Studio](https://aistudio.google.com).
3. Na barra lateral (Sidebar) à esquerda do app, cole sua chave no campo **"Insira sua Gemini API Key"**.
4. Escolha uma das abas no topo da tela e comece a interagir!

---

### Opção B: Executar Localmente na sua Máquina

#### Pré-requisitos
* **Python 3.10+** instalado no seu computador.
* Chave de API do [Google AI Studio](https://aistudio.google.com).

#### Passo a Passo
```bash
# 1. Clone este repositório
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio

# 2. Crie e ative um ambiente virtual
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie a aplicação
streamlit run app.py
