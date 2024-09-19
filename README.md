# Projeto de Pesquisa e Entrevistas - Banco de Dados

Este projeto está em desenvolvimento para gerenciar pesquisas e entrevistas, incluindo o cadastro de entrevistados, suas informações pessoais, perguntas e respostas das pesquisas, além de controle de dados relacionados a telefones e endereços. O banco de dados foi modelado para ser escalável, seguro e de fácil manutenção.

## Estrutura do Projeto

O banco de dados é composto por várias tabelas interrelacionadas que permitem armazenar informações detalhadas sobre pesquisas, entrevistados e suas respectivas respostas. Abaixo estão as tabelas principais e suas descrições:

### 1. **Tabela `pesquisa`**
Armazena os detalhes de cada pesquisa cadastrada, como nome, datas de início e término, e se está ativa.

- `pesquisa_id`: Chave primária.
- `pesquisa_nome`: Nome da pesquisa.
- `data_inicio`: Data de início da pesquisa.
- `data_fim`: Data de término da pesquisa.
- `data_cadastro`: Data de cadastro do registro.
- `ativo`: Indica se a pesquisa está ativa (exclusão lógica).

### 2. **Tabela `pesquisa_pergunta_tipo`**
Define os tipos de perguntas que podem ser associados às pesquisas, como "Múltipla Escolha", "Resposta Aberta", etc.

- `pesquisa_pergunta_tipo_id`: Chave primária.
- `pesquisa_pergunta_tipo`: Descrição do tipo de pergunta.
- `data_cadastro`: Data de cadastro do tipo.
- `ativo`: Indica se o tipo de pergunta está ativo (exclusão lógica).

### 3. **Tabela `pesquisa_pergunta`**
Armazena as perguntas associadas a uma pesquisa específica.

- `pesquisa_pergunta_id`: Chave primária.
- `pesquisa_id`: Chave estrangeira que se refere à tabela `pesquisa`.
- `pesquisa_pergunta_tipo_id`: Chave estrangeira que se refere à tabela `pesquisa_pergunta_tipo`.
- `data_cadastro`: Data de cadastro da pergunta.
- `ativo`: Indica se a pergunta está ativa (exclusão lógica).

### 4. **Tabela `genero`**
Armazena as diferentes opções de gênero disponíveis para os entrevistados.

- `genero_id`: Chave primária.
- `genero`: Descrição do gênero.

### 5. **Tabela `entrevistado`**
Armazena as informações pessoais dos entrevistados, como nome, email, data de nascimento, gênero, entre outros.

- `entrevistado_id`: Chave primária.
- `entrevistado_nome`: Nome completo do entrevistado.
- `entrevistado_email`: Email do entrevistado.
- `entrevistado_nome_social`: Nome social (se aplicável).
- `entrevistado_data_nascimento`: Data de nascimento do entrevistado.
- `sexo`: Sexo do entrevistado (M, F ou O).
- `genero_id`: Chave estrangeira que se refere à tabela `genero`.
- `data_cadastro`: Data de cadastro do entrevistado.

### 6. **Tabela `telefone_tipo`**
Armazena os diferentes tipos de telefones (ex.: Celular, Fixo).

- `telefone_tipo_id`: Chave primária.
- `telefone_tipo`: Descrição do tipo de telefone.
- `ativo`: Indica se o tipo está ativo (exclusão lógica).

### 7. **Tabela `entrevistado_telefone`**
Armazena os números de telefone associados aos entrevistados, permitindo múltiplos números por entrevistado.

- `entrevistado_telefone_id`: Chave primária.
- `entrevistado_id`: Chave estrangeira que se refere à tabela `entrevistado`.
- `ddi`: Código de discagem internacional (padrão 55 para o Brasil).
- `ddd`: Código de discagem da área (ex.: 11 para São Paulo).
- `telefone`: Número de telefone.
- `telefone_tipo_id`: Chave estrangeira que se refere à tabela `telefone_tipo`.
- `eh_telefone_principal`: Indica se o telefone é o principal.
- `data_cadastro`: Data de cadastro do telefone.
- `ativo`: Indica se o telefone está ativo (exclusão lógica).

### 8. **Tabela `pergunta_resposta`**
Armazena as respostas dadas pelos entrevistados às perguntas da pesquisa.

- `pergunta_resposta_id`: Chave primária.
- `pesquisa_pergunta_id`: Chave estrangeira que se refere à tabela `pesquisa_pergunta`.
- `entrevistado_id`: Chave estrangeira que se refere à tabela `entrevistado`.
- `resposta`: Resposta fornecida pelo entrevistado.
- `data_cadastro`: Data de cadastro da resposta.

### 9. **Tabela `pesquisa_pergunta_opcao`**
Armazena as opções de respostas para perguntas do tipo "Múltipla Escolha".

- `pesquisa_pergunta_opcao_id`: Chave primária.
- `pesquisa_pergunta_id`: Chave estrangeira que se refere à tabela `pesquisa_pergunta`.
- `indice`: Ordem da opção de resposta.
- `opcao`: Texto da opção.
- `data_cadastro`: Data de cadastro da opção.
- `ativo`: Indica se a opção está ativa (exclusão lógica).

### 10. **Tabela `entrevistado_endereco`**
Armazena os endereços dos entrevistados.

- `entrevistado_endereco_id`: Chave primária.
- `entrevistado_id`: Chave estrangeira que se refere à tabela `entrevistado`.
- `logradouro`: Logradouro do endereço (ex.: Rua, Avenida).
- `numero`: Número do endereço.
- `complemento`: Complemento (ex.: bloco, apartamento).
- `bairro`: Bairro.
- `cidade`: Cidade.
- `uf`: Unidade Federativa (Estado) representada por sigla.
- `cep`: Código de Endereçamento Postal (CEP).
- `descricao`: Descrição adicional do endereço (ex.: Casa, Trabalho).

## Tecnologias Utilizadas

- **PostgreSQL**: Sistema de banco de dados relacional usado para modelar e gerenciar as tabelas e relacionamentos.
- **SQL**: Linguagem utilizada para criação de tabelas, relacionamento de entidades, restrições e exclusão lógica.
- **Python**: Linguagem de programação utilizada para desenvolvimento de scripts e integração com o banco de dados.

## Considerações Finais

Este projeto está em desenvolvimento com o objetivo de fornecer uma análise para a Ilha Primeira com o fácil crescimento e manutenção de novas pesquisas e entrevistados ao longo do tempo. O banco de dados está preparado para armazenar grandes volumes de dados de forma organizada, garantindo a integridade e segurança das informações.
