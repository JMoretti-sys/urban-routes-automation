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

## 📋 Pré-requisitos

- Python 3.x instalado
- Google Chrome (versão mais recente)
- ChromeDriver compatível
- Git instalado

---

## 📂 Estrutura do Projeto

```
projeto-urban-routes/
├── main.py          # Arquivo principal com os testes
├── pages.py         # Classes POM para interação com elementos
├── helpers.py       # Funções auxiliares (código SMS)
├── requirements.txt # Dependências do projeto
└── README.md       # Documentação do projeto
✅ Funcionalidades Testadas
[x] Definir endereços de origem e destino
[x] Selecionar tarifa Comfort
[x] Preencher número de telefone com código SMS
[x] Adicionar método de pagamento (cartão)
[x] Escrever comentário para o motorista
[x] Solicitar extras (cobertor, lenços, sorvetes)
[x] Confirmar solicitação do táxi
[x] Verificar modal de busca do motorista
⚙️ Como instalar e executar
Clone o repositório:
git clone https://github.com/JMoretti-sys/urban-routes-automation.git
cd urban-routes-automation
Instale as dependências:
pip install -r requirements.txt
Execute os testes:
pytest main.py -v
📝 Observações
Os testes foram desenvolvidos seguindo o padrão Page Object Model (POM)
Utiliza funções auxiliares para recuperação de códigos SMS
Inclui tratamento de condições para evitar falhas nos testes

```
