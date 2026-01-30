# Sprint 7 – Introduction to Automation Testing – Urban Routes

This project contains the **preparation for automated tests** for the Urban Routes application using Python.  
In Sprint 7, **no real browser execution is performed**. Only base functions and project structure are created so that Sprint 8 can implement Selenium and end-to-end automated tests.

## 🚀 Objective
- Create the base for automated tests using Python.
- Separate test data into **data.py**.
- Create helper functions in **helpers.py**.
- Define empty test functions in **main.py**, prepared for Pytest.
- Check the availability of the Urban Routes server before running tests.

## 🛠 Technologies Used
- Python 3.x
- Pytest
- PyCharm (IDE)
- **helpers.py** for auxiliary functions (e.g., `retrieve_phone_code` and `is_url_reachable`)

## 📂 Project Structure
sprint-07/
├── main.py # Main file with empty test functions
├── data.py # Test constants (addresses, phone, card, etc.)
├── helpers.py # Provided helper functions (do not modify)
└── README.md # Sprint 7 documentation


## ✅ Prepared Functionalities
- [x] Test functions defined in `main.py`:
  - test_set_route
  - test_select_plan
  - test_fill_phone_number
  - test_fill_card
  - test_comment_for_driver
  - test_order_blanket_and_handkerchiefs
  - test_order_2_ice_creams
  - test_car_search_model_appears
- [x] Check if Urban Routes server is active (`setup_class` with `is_url_reachable`)
- [x] Helper for retrieving SMS code (`retrieve_phone_code`)
- [x] Ice cream order preparation (loop with comment `#Add in S8`)

## ⚙️ How to Run
1. Clone the repository:
```bash
git clone https://github.com/JMoretti-sys/urban-routes-automation.git
cd urban-routes-automation
Create and activate a virtual environment:

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Run tests (they will not perform real browser actions yet):

pytest main.py -v

---

💡 **O que mudou:**
- Ajustei o texto para **inglês**, consistente com outros READMEs.
- Corrigi os blocos de código (`bash`) para `git`, `python`, `pip` e `pytest`.
- Corrigi pequenos erros de formatação no passo a passo.
- Padronizei comentários dentro do código para inglês.  

Se você quiser, posso **fazer também a versão final do README da Sprint 8** no mesmo estilo, pronto para colocar no GitHub, mantendo tudo consistente.  

Quer que eu faça isso agora?
Você disse:
Em português, por favor.
O ChatGPT disse:
Perfeito, João! 😄 Então aqui está o README da Sprint 7 todo em português, com formatação correta e pronto para colocar no GitHub:

# Sprint 7 – Introdução à Automação de Testes – Urban Routes

Este projeto contém a **preparação para os testes automatizados** do aplicativo Urban Routes utilizando Python.  
Na Sprint 7, **não há execução real no navegador**. Apenas são criadas funções base e a estrutura do projeto, para que a Sprint 8 possa implementar Selenium e testes automatizados de ponta a ponta.

## 🚀 Objetivo
- Criar a base para testes automatizados usando Python.
- Separar dados de teste em **data.py**.
- Criar funções auxiliares em **helpers.py**.
- Definir funções de teste vazias em **main.py**, preparadas para Pytest.
- Verificar a disponibilidade do servidor Urban Routes antes de executar os testes.

## 🛠 Tecnologias utilizadas
- Python 3.x
- Pytest
- PyCharm (IDE)
- **helpers.py** para funções auxiliares (ex.: `retrieve_phone_code` e `is_url_reachable`)

## 📂 Estrutura do Projeto
sprint-07/
├── main.py # Arquivo principal com funções de teste vazias
├── data.py # Constantes de teste (endereços, telefone, cartão, etc.)
├── helpers.py # Funções auxiliares fornecidas (não modificar)
└── README.md # Documentação da Sprint 7


## ✅ Funcionalidades Preparadas
- [x] Funções de teste definidas em `main.py`:
  - test_set_route
  - test_select_plan
  - test_fill_phone_number
  - test_fill_card
  - test_comment_for_driver
  - test_order_blanket_and_handkerchiefs
  - test_order_2_ice_creams
  - test_car_search_model_appears
- [x] Verificação se o servidor Urban Routes está ativo (`setup_class` com `is_url_reachable`)
- [x] Helpers para recuperar código SMS (`retrieve_phone_code`)
- [x] Preparação de pedido de sorvete (loop com comentário `#Adicionar em S8`)

## ⚙️ Como executar
1. Clone o repositório:
```bash
git clone https://github.com/JMoretti-sys/urban-routes-automation.git
cd urban-routes-automation
Crie e ative um ambiente virtual:

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Instale as dependências:

pip install -r requirements.txt
Execute os testes (eles não farão ações reais no navegador nesta Sprint):

pytest main.py -v
