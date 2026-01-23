# Sprint 8: Automação de Testes de Aplicativos Web – Urban Routes

Este projeto contém **testes automatizados** para o aplicativo **Urban Routes**, simulando todo o processo de solicitação de um táxi usando **Python**, **Selenium** e **Page Object Model (POM)**.  

Os testes cobrem desde o preenchimento do endereço até a solicitação do táxi, incluindo extras e comentários, garantindo que o fluxo do usuário funcione corretamente.

---

## 🚀 Objetivo do Projeto
Automatizar os seguintes fluxos no aplicativo:

- Definir o endereço de destino
- Selecionar a tarifa **Comfort** (com condição para evitar falhas)
- Preencher o número de telefone (com código SMS recuperado via `helpers.py`)
- Adicionar um cartão de crédito (com foco simulado)
- Escrever comentário para o motorista
- Pedir **cobertor**, **lenços** e **2 sorvetes**
- Solicitar o táxi e verificar a janela modal de busca de carros

---

## 🛠 Tecnologias utilizadas

- **Python 3.x**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- **PyCharm** (IDE)
- Arquivo `helpers.py` para funções auxiliares (ex.: retrieve_phone_code)

---

## 📂 Estrutura do Projeto


---

## ⚙️ Como instalar e executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
pip install -r requirements.txt
pytest main.py -v
