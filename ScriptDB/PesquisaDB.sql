create table pesquisa ( 
pesquisa_id SERIAL PRIMARY key, 
pesquisa_nome varchar(128) not null, 
data_inicio timestamp not null, 
data_fim timestamp not null, 
data_cadastro timestamp not null default current_timestamp, 
ativo boolean not null default true 
); 

COMMENT ON TABLE pesquisa IS 'Tabela que armazena as pesquisas'; 
comment on column pesquisa.pesquisa_id is 'Chave primária da tabela'; 
comment on column pesquisa.pesquisa_nome is 'Nome da pesquisa'; 
comment on column pesquisa.data_inicio is 'Data de início da pesquisa'; 
comment on column pesquisa.data_fim is 'Data de encerramento da pesquisa'; 
comment on column pesquisa.data_cadastro is 'Data de cadastro do registro'; 
comment on column pesquisa.ativo is 'Se a pesquisa está ativa ou não (Éxclusão lógica)'; 

create table pesquisa_pergunta_tipo( 
pesquisa_pergunta_tipo_id SERIAL PRIMARY key,  
pesquisa_pergunta_tipo varchar(32) not null, 
data_cadastro timestamp not null default current_timestamp, 
ativo boolean not null default true	 
);

COMMENT ON TABLE pesquisa_pergunta_tipo IS 'Tabela que armazena os tipos de pergunta associados às pesquisas'; 
comment on column pesquisa_pergunta_tipo.pesquisa_pergunta_tipo_id is 'Chave primária da tabela'; 
comment on column pesquisa_pergunta_tipo.pesquisa_pergunta_tipo is 'Descrição do tipo de pergunta'; 
comment on column pesquisa_pergunta_tipo.data_cadastro is 'Data de cadastro do registro'; 
comment on column pesquisa_pergunta_tipo.ativo is 'Se o tipo de pergunta está ativo ou não (Exclusão lógica)';

create table pesquisa_pergunta( 
pesquisa_pergunta_id SERIAL PRIMARY key, 
pesquisa_id int not null, 
pesquisa_pergunta_tipo_id int not null, 
data_cadastro timestamp not null default current_timestamp, 
ativo boolean not null default true, 
constraint fk_pesquisa_x_pergunta_pesquisa foreign key (pesquisa_id) references pesquisa(pesquisa_id), 
constraint fk_pesquisa_pergunta_x_pesquisa_pergunta_tipo foreign key (pesquisa_pergunta_tipo_id) references pesquisa_pergunta_tipo(pesquisa_pergunta_tipo_id)	 
);

COMMENT ON TABLE pesquisa_pergunta IS 'Tabela que armazena as perguntas de cada pesquisa'; 
comment on column pesquisa_pergunta.pesquisa_pergunta_id is 'Chave primária da tabela'; 
comment on column pesquisa_pergunta.pesquisa_id is 'Chave estrangeira para a tabela pesquisa'; 
comment on column pesquisa_pergunta.pesquisa_pergunta_tipo_id is 'Chave estrangeira para a tabela pesquisa_pergunta_tipo'; 
comment on column pesquisa_pergunta.data_cadastro is 'Data de cadastro da pergunta'; 
comment on column pesquisa_pergunta.ativo is 'Se a pergunta está ativa ou não (Exclusão lógica)';

create table genero( 
genero_id SERIAL PRIMARY key, 
genero varchar(128) 
);

COMMENT ON TABLE genero IS 'Tabela que armazena as opções de gênero'; 
comment on column genero.genero_id is 'Chave primária da tabela'; 
comment on column genero.genero is 'Descrição do gênero';

create table entrevistado( 
entrevistado_id SERIAL PRIMARY key, 
entrevistado_nome varchar(256) not null, 
entrevistado_email varchar(128), 
entrevistado_nome_social varchar(32), 
entrevistado_data_nascimento date not null, 
sexo char(1) not null,  
genero_id int not null, 
data_cadastro timestamp not null default current_timestamp, 
constraint fk_entrevistado_x_genero foreign key (genero_id) references genero(genero_id) 
);

COMMENT ON TABLE entrevistado IS 'Tabela que armazena os entrevistados de cada pesquisa'; 
comment on column entrevistado.entrevistado_id is 'Chave primária da tabela'; 
comment on column entrevistado.entrevistado_nome is 'Nome completo do entrevistado'; 
comment on column entrevistado.entrevistado_email is 'Email do entrevistado'; 
comment on column entrevistado.entrevistado_nome_social is 'Nome social do entrevistado (se aplicável)'; 
comment on column entrevistado.entrevistado_data_nascimento is 'Data de nascimento do entrevistado'; 
comment on column entrevistado.sexo is 'Sexo do entrevistado (M para masculino, F para feminino, O para outros)'; 
comment on column entrevistado.genero_id is 'Chave estrangeira para a tabela de gênero'; 
comment on column entrevistado.data_cadastro is 'Data de cadastro do registro';

create table telefone_tipo( 
telefone_tipo_id SERIAL PRIMARY key, 
telefone_tipo varchar(32), 
ativo boolean not null default true 
);

COMMENT ON TABLE telefone_tipo IS 'Tabela que armazena os tipos de telefone'; 
comment on column telefone_tipo.telefone_tipo_id is 'Chave primária da tabela'; 
comment on column telefone_tipo.telefone_tipo is 'Descrição do tipo de telefone'; 
comment on column telefone_tipo.ativo is 'Se o tipo de telefone está ativo ou não';

create table entrevistado_telefone( 
entrevistado_telefone_id SERIAL PRIMARY key, 
entrevistado_id int, 
ddi int not null default 55, 
ddd int not null, 
telefone int not null, 
telefone_tipo_id int not null, 
eh_telefone_principal boolean not null default true, 
data_cadastro timestamp not null default current_timestamp, 
ativo boolean not null default true,	 
constraint fk_entrevistado_telefone_x_entrevistado foreign key (entrevistado_id) references entrevistado(entrevistado_id), 
constraint fk_entrevistado_telefone_x_telefone_tipo foreign key (telefone_tipo_id) references telefone_tipo(telefone_tipo_id) 
);

COMMENT ON TABLE entrevistado_telefone IS 'Tabela que armazena os telefones associados aos entrevistados'; 
comment on column entrevistado_telefone.entrevistado_telefone_id is 'Chave primária da tabela'; 
comment on column entrevistado_telefone.entrevistado_id is 'Chave estrangeira para a tabela de entrevistado'; 
comment on column entrevistado_telefone.ddi is 'Código do país (DDI), padrão 55 para o Brasil'; 
comment on column entrevistado_telefone.ddd is 'Código da área (DDD) do telefone'; 
comment on column entrevistado_telefone.telefone is 'Número de telefone'; 
comment on column entrevistado_telefone.telefone_tipo_id is 'Chave estrangeira para a tabela de tipo de telefone'; 
comment on column entrevistado_telefone.eh_telefone_principal is 'Indica se o número de telefone é o principal do entrevistado'; 
comment on column entrevistado_telefone.data_cadastro is 'Data de cadastro do telefone'; 
comment on column entrevistado_telefone.ativo is 'Se o telefone está ativo ou não (Exclusão lógica)';

create table pergunta_resposta ( 
pergunta_resposta_id SERIAL PRIMARY key, 
pesquisa_pergunta_id int not null, 
entrevistado_id int not null, 
resposta varchar(2048), 
data_cadastro timestamp not null default current_timestamp, 
constraint fk_pergunta_resposta_x_pesquisa_pergunta foreign key (pesquisa_pergunta_id) references pesquisa_pergunta(pesquisa_pergunta_id), 
constraint fk_pergunta_resposta_x_entrevistado foreign key (entrevistado_id) references entrevistado(entrevistado_id) 
);

COMMENT ON TABLE pergunta_resposta IS 'Tabela que armazena as respostas dadas pelos entrevistados às perguntas'; 
comment on column pergunta_resposta.pergunta_resposta_id is 'Chave primária da tabela'; 
comment on column pergunta_resposta.pesquisa_pergunta_id is 'Chave estrangeira para a tabela pesquisa_pergunta'; 
comment on column pergunta_resposta.entrevistado_id is 'Chave estrangeira para a tabela entrevistado'; 
comment on column pergunta_resposta.resposta is 'Resposta fornecida pelo entrevistado'; 
comment on column pergunta_resposta.data_cadastro is 'Data de cadastro da resposta';

create table pesquisa_pergunta_opcao ( 
pesquisa_pergunta_opcao_id SERIAL PRIMARY key, 
pesquisa_pergunta_id int, 
indice int not null default 1, 
opcao varchar(128), 
data_cadastro timestamp not null default current_timestamp, 
ativo boolean not null default true,		 
constraint fk_pesquisa_pergunta_opcao_x_pesquisa_pergunta foreign key (pesquisa_pergunta_id) references pesquisa_pergunta(pesquisa_pergunta_id) 
); 

COMMENT ON TABLE pesquisa_pergunta_opcao IS 'Tabela que armazena as opções no caso de perguntas do tipo não aberta'; 
comment on column pesquisa_pergunta_opcao.pesquisa_pergunta_opcao_id is 'Chave primária da tabela'; 
comment on column pesquisa_pergunta_opcao.pesquisa_pergunta_id is 'Chave estrangeira da Pergunta'; 
comment on column pesquisa_pergunta_opcao.indice is 'Campo que armazena o indice da opção, para dar liberdade de exibicao da ordem das opções'; 
comment on column pesquisa_pergunta_opcao.opcao is 'Label da opção'; 
comment on column pesquisa_pergunta_opcao.data_cadastro is 'Data de cadastro do Registro'; 
comment on column pesquisa_pergunta_opcao.ativo is 'Se opção está ativa ou não (Exclusão lógica)'; 

create table entrevistado_endereco(  
entrevistado_endereco_id SERIAL PRIMARY key, 
entrevistado_id int not null, 
logradouro varchar(256) not null, 
numero varchar(64) not null, 
complemento varchar(256), 
bairro varchar(256) not null, 
cidade varchar(256) not null, 
uf varchar(2) not null, 
cep varchar(8) not null, 
descricao varchar(32), 
constraint fk_entrevistado_endereco_x_entrevistado foreign key (entrevistado_id) references entrevistado(entrevistado_id) 
);

COMMENT ON TABLE entrevistado_endereco IS 'Tabela que armazena os endereços dos entrevistados'; 
comment on column entrevistado_endereco.entrevistado_endereco_id is 'Chave primária da tabela'; 
comment on column entrevistado_endereco.entrevistado_id is 'Chave estrangeira para a tabela entrevistado'; 
comment on column entrevistado_endereco.logradouro is 'Logradouro do endereço (ex.: Rua, Avenida)'; 
comment on column entrevistado_endereco.numero is 'Número do endereço (ex.: número da casa ou apartamento)'; 
comment on column entrevistado_endereco.complemento is 'Complemento do endereço (ex.: bloco, andar)'; 
comment on column entrevistado_endereco.bairro is 'Bairro onde o entrevistado reside'; 
comment on column entrevistado_endereco.cidade is 'Cidade onde o entrevistado reside'; 
comment on column entrevistado_endereco.uf is 'Unidade federativa (estado) do endereço, representada por sigla'; 
comment on column entrevistado_endereco.cep is 'CEP (Código de Endereçamento Postal) do entrevistado'; 
comment on column entrevistado_endereco.descricao is 'Descrição opcional para detalhamento do endereço';

/*----------------------------------------------------------------*/ 
/*Inserção de dados iniciais*/ 
/*Inserção de dados de gênero*/ 
INSERT INTO public.genero (genero) VALUES('Cisgênero (Quando se identifica com seu sexo biológico)'); 
INSERT INTO public.genero (genero) VALUES('Transgênero (Quando se identifica com o sexo biológico oposto)'); 
INSERT INTO public.genero (genero) VALUES('Outra identificação'); 

/*Cadastro os tipos de telefone*/  
INSERT INTO public.telefone_tipo (telefone_tipo) VALUES('Celular');  
INSERT INTO public.telefone_tipo (telefone_tipo) VALUES('Comercial');  
INSERT INTO public.telefone_tipo (telefone_tipo) VALUES('Residencial');  
INSERT INTO public.telefone_tipo (telefone_tipo) VALUES('Recado');  

/*Cadastro dos tipos de pergunta*/  
INSERT INTO public.pesquisa_pergunta_tipo (pesquisa_pergunta_tipo) VALUES('Escolha única');  
INSERT INTO public.pesquisa_pergunta_tipo (pesquisa_pergunta_tipo) VALUES('Múltipla escolha');  
INSERT INTO public.pesquisa_pergunta_tipo (pesquisa_pergunta_tipo) VALUES('Sim/Não');  
INSERT INTO public.pesquisa_pergunta_tipo (pesquisa_pergunta_tipo) VALUES('Sim/Não/NI');  
INSERT INTO public.pesquisa_pergunta_tipo (pesquisa_pergunta_tipo) VALUES('Verdadeiro/Falso');  
INSERT INTO public.pesquisa_pergunta_tipo (pesquisa_pergunta_tipo) VALUES('Texto Livre');  

/*Cadastrar uma pesquisa*/  
INSERT INTO public.pesquisa (pesquisa_nome, data_inicio, data_fim) VALUES('Mobilidade e desafios de comunidades insulares', '2024-09-09', '2024-11-09');  
select * from pesquisa_pergunta_tipo 
select * from pesquisa_pergunta 

/*Cadastrar uma pergunta de resposta única*/ 
INSERT INTO public.pesquisa_pergunta 
(pesquisa_id, pesquisa_pergunta_tipo_id, pergunta_texto) 
VALUES(1, 1, 'Qual é o principal meio de transporte que você utiliza para se deslocar dentro da ilha?'); 

INSERT INTO public.pesquisa_pergunta_opcao (pesquisa_pergunta_id, indice, opcao) VALUES(1, 1, 'Bicicleta'); 
INSERT INTO public.pesquisa_pergunta_opcao (pesquisa_pergunta_id, indice, opcao) VALUES(1, 2, 'Motocicleta'); 
INSERT INTO public.pesquisa_pergunta_opcao (pesquisa_pergunta_id, indice, opcao) VALUES(1, 3, 'Charrete'); 
INSERT INTO public.pesquisa_pergunta_opcao (pesquisa_pergunta_id, indice, opcao) VALUES(1, 4, 'A pé, não utiliza'); 

/*Cadastrar uma pergunta de resposta múltipla*/ 
INSERT INTO public.pesquisa_pergunta 
(pesquisa_id, pesquisa_pergunta_tipo_id, pergunta_texto) 
VALUES(1, 2, 'Quais das seguintes opções você considera necessárias para melhorar a mobilidade na ilha? (Selecione todas que se aplicam)'); 

INSERT INTO public.pesquisa_pergunta_opcao (pesquisa_pergunta_id, indice, opcao) VALUES(2, 1, 'Liberar carros dentro da ilha'); 
INSERT INTO public.pesquisa_pergunta_opcao (pesquisa_pergunta_id, indice, opcao) VALUES(2, 2, 'Construir ciclovias'); 
INSERT INTO public.pesquisa_pergunta_opcao (pesquisa_pergunta_id, indice, opcao) VALUES(2, 3, 'Mais locais para barcos'); 
INSERT INTO public.pesquisa_pergunta_opcao (pesquisa_pergunta_id, indice, opcao) VALUES(2, 4, 'Disponibilizar patinetes/ biciletas elétricas'); 

/*Select da pesquisa*/ 
select *  
from pesquisa p  
join pesquisa_pergunta pp on pp.pesquisa_id = p.pesquisa_id  
join pesquisa_pergunta_opcao ppo on ppo.pesquisa_pergunta_id = pp.pesquisa_pergunta_id  

/*Cadastro o entrevistado*/ 
INSERT INTO public.entrevistado 
(entrevistado_nome, entrevistado_email, entrevistado_nome_social, entrevistado_data_nascimento, sexo, genero_id) 
VALUES('Alvaro', 'alvaro.barros@professores.ibmec.edu.br', 'Alvaro', '1979-08-09', 'M', 1); 
select * from public.entrevistado 

/*Cadastrando respostas para a pesquisa*/ 
INSERT INTO public.pergunta_resposta 
(pesquisa_pergunta_id, entrevistado_id, resposta) 
VALUES(1, 1, 'Motocicleta'); 
INSERT INTO public.pergunta_resposta 
(pesquisa_pergunta_id, entrevistado_id, resposta) 
VALUES(2, 1, 'Liberar carros dentro da ilha|Construir ciclovias|Mais locais para barcos'); 
select * from pergunta_resposta pr