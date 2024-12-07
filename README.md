## Problem Statement

Gestores municipais Brasileiros têm até dezembro de 2025 para elaborar seus **Planos Locais de Ação Climática (PLACs)**, conforme a Lei 14.904/24. Este é um desafio complexo, envolvendo análises detalhadas, consultas a dados confiáveis e a participação de diversos stakeholders. ResiliêncIA foi criada para ser uma ferramenta de apoio nesse processo, simplificando etapas e fornecendo informações relevantes de forma simples para gestores.

# ResiliêncIA

ResiliêncIA é a nossa abordagem para apoiar gestores municipais na elaboração de seus PLACs. A ferramenta utiliza inteligência artificial para fornecer respostas contextualizadas e baseadas em dados, integrando informações de riscos climáticos mapeados pelo **INPE**, outras fontes de dados do IBGE e benchmarks de PLACs de excelência. 

O objetivo é criar um assistente virtual que não só responda perguntas, mas que também facilite o processo iterativo e colaborativo necessário para a construção de um PLAC robusto.

ResiliêncIA é uma ferramenta baseada em inteligência artificial que utiliza **RAG** (Retrieve-Augmented Generation) para melhorar a qualidade das respostas fornecidas pelo modelo, integrando informações relevantes de um banco de dados. Este projeto combina o poder da API da OpenAI, o indexador FAISS e um prompt elaborado com melhores práticas de engenharia de prompt para criar uma experiência conversacional robusta.

---

## Sobre o Projeto

ResiliêncIA é um **MVP** criado por professores de escolas públicas que estão expandindo suas carreiras para a área de tecnologia. Este projeto começou a ser desenvolvido dentro do **Playlab.ia**, um espaço foca em IA Generativa para educação básica, foi testado e refinado com o **Create GPT**, e também criado a primeira versão em código aberto disponibilizado no **resliencia_v2.py**.

Como parte desse Read.me, além de disponibilizar as funcionalidades, requisitos e instalação do **resliencia_v2.py**, ensinamos a configurar e utilizar a ferramenta tanto no Playlab.ia quanto no Create GPT, promovendo o aprendizado prático e incentivando o uso de tecnologia por outros  profissionais.

---

## Metodologia + Prompt

A verdadeira inovação por trás do ResiliêncIA está na **inteligência por trás da construção da ferramenta**, desenvolvida para guiar os gestores municipais no processo de elaboração de um PLAC conforme as necessidades de sua população e território. Entendemos que isso não é algo que acontece em minutos, mas sim em diversas interações com o bot, a equipe de planejamento e os stakeholders locais. 

### O que a metodologia integra:
- **Bases de Dados do IBGE**: Para contextualizar a realidade demográfica e socioeconômica de cada município.
- **Informações de Riscos Climáticos**: Dados do **INPE** e da plataforma **AdaptaBrasil** para subsidiar análises dos riscos prioritários.
- **Referências de PLACs de Excelência**: Exemplos de boas práticas nacionais e internacionais.

### Diferenciais da Engenharia do Prompt

O diferencial do ResiliêncIA está no **prompt** desenvolvido com técnicas avançadas de engenharia prompt, que incluem:

1. **Contextualização**: Adapta as interações às especificidades de cada município e ao estágio do processo de elaboração do PLAC.

2. **Acionamento da Cadeia de Pensamento (Chain of Thought)**: Orienta o modelo a resolver problemas passo a passo, organizando o raciocínio de maneira clara e estruturada.

3. **Uso de Elementos de Memória**: Permite à ferramenta lembrar informações relevantes sobre o usuário e interações anteriores, criando uma experiência personalizada e eficiente.

4. **Guardrails**: Garantem que o bot se mantenha focado no tema e evite divagações, mesmo em interações complexas.

---

### Iteração e Evolução do Prompt

A primeira versão do prompt tinha apenas 600 palavras, sem referências claras ou estrutura definida. Após um extenso processo de iteração e refinamento, chegamos a um **prompt de 3000 palavras**, dividido em **quatro etapas interconectados que se retroalimentam**. Cada etapa captura informações do usuário, transforma e detalha os dados, até culminar na versão final do PLAC, alinhada às necessidades locais.

---

## Funcionalidades **resliencia_v2.py**

- **Integração com OpenAI API**: Utiliza o modelo `text-embedding-ada-002` para geração de embeddings e `gpt-4o` para conversas.
- **Processamento de Base de Dados**: Analisa e transforma um arquivo CSV (`Base de Riscos do Adapta Brasil.csv`) em embeddings para busca.
- **Indexação com FAISS**: Cria um índice de similaridade para busca rápida.
- **RAG (Retrieve-Augmented Generation)**: Melhoria das respostas com documentos relevantes do banco de dados.
- **Interface Conversacional**: Chatbot interativo.

---

## Requisitos

- Python 3.8 ou superior
- Uma API_KEY válida da OpenAI.
- Dependências Python:
  - `openai`
  - `numpy`
  - `pandas`
  - `faiss`
  - `python-dotenv`

---

## Instalação do **resliencia_v2.py**

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/resiliencIA.git
   cd resiliencIA

2. Isntale as dependências:
  ```bash
    pip install -r requirements.txt
