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
