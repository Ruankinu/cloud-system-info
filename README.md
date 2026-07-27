# ☁️ Cloud System Info

Projeto de infraestrutura cloud desenvolvido para demonstrar conhecimentos práticos em **AWS, Linux, segurança de rede e deploy de aplicações em ambiente controlado**, com foco em bases que são muito valorizadas em vagas de **Engenharia de Dados**.

A proposta do projeto foi simular uma arquitetura real de produção com:

* um **Bastion Host** para acesso administrativo
* uma **instância privada EC2** sem IP público
* **Nginx** como camada de serviço
* uma aplicação **Flask** executada em ambiente Linux
* regras de segurança baseadas em **Security Groups**

Este repositório mostra domínio de fundamentos importantes para Engenharia de Dados, especialmente em contextos que envolvem **cloud, isolamento de rede, servidores Linux e infraestrutura para serviços de dados**.

---

## 📋 Índice

* [Sobre o Projeto](#sobre-o-projeto)
* [Objetivo](#objetivo)
* [Arquitetura](#arquitetura)
* [O que este projeto demonstra](#o-que-este-projeto-demonstra)
* [Stack Tecnológica](#stack-tecnológica)
* [Segurança da Arquitetura](#segurança-da-arquitetura)
* [Como Foi Construído](#como-foi-construído)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Deploy](#deploy)
* [Possíveis Melhorias](#possíveis-melhorias)
* [Aprendizados](#aprendizados)
* [Relação com Engenharia de Dados](#relação-com-engenharia-de-dados)
* [Contato](#contato)

---

## Sobre o Projeto

Este projeto foi criado como exercício prático de infraestrutura cloud na AWS, com uma arquitetura pensada para representar cenários comuns em ambientes profissionais.

A aplicação principal é uma interface simples em Flask, mas o foco real do repositório está na **estrutura de rede, no isolamento da instância privada e na forma como o acesso ao sistema foi organizado**.

Em vez de expor a aplicação diretamente à internet, a solução utiliza uma arquitetura mais próxima da realidade de produção, com pontos de acesso controlados e camadas de segurança.

---

## Objetivo

O principal objetivo do projeto foi praticar e demonstrar:

* criação e gerenciamento de instâncias EC2
* administração de servidores Ubuntu
* acesso remoto via SSH
* arquitetura com **Bastion Host**
* segmentação entre ambiente público e privado
* controle de tráfego com **Security Groups**
* deploy de aplicação em ambiente cloud
* uso de **Nginx** como camada intermediária

Esse tipo de conhecimento é muito útil em vagas de Engenharia de Dados porque pipelines e serviços de dados normalmente rodam em ambientes que exigem **segurança, automação, rede bem configurada e servidores bem administrados**.

---

## Arquitetura

Fluxo da infraestrutura:

```text
Usuário
   |
   v
Internet
   |
   v
ngrok
   |
   v
Bastion Host
(Ubuntu EC2 - IP Público)
   |
   | SSH
   v
Private EC2
(Ubuntu - Sem IP Público)
   |
   v
Nginx
   |
   v
Flask Application
```

A ideia dessa arquitetura é manter a instância principal protegida, sem exposição direta à internet, e centralizar o acesso administrativo em um ponto controlado.

---

## O que este projeto demonstra

Este projeto foi pensado para mostrar competências que ajudam bastante em vagas de Engenharia de Dados, Cloud e Infraestrutura.

### Cloud e AWS

* criação de servidores EC2
* entendimento de arquitetura pública e privada
* noções de VPC e segmentação de rede
* uso de Security Groups como firewall virtual

### Linux

* administração de Ubuntu Server
* instalação e configuração de serviços
* uso do terminal para gestão da aplicação
* organização de ambiente em servidor

### Segurança

* princípio do menor privilégio
* acesso controlado via Bastion Host
* redução da superfície de ataque
* bloqueio de acesso direto ao servidor privado

### Deploy e operação

* instalação de aplicação Python em ambiente Linux
* uso de Nginx como serviço
* validação de aplicação em cloud
* exposição temporária com ngrok para testes

---

## Stack Tecnológica

### Cloud

* AWS EC2
* Security Groups
* VPC
* Bastion Host

### Sistema Operacional

* Ubuntu Linux

### Aplicação

* Python
* Flask

### Serviços

* Nginx
* SSH
* ngrok

---

## Segurança da Arquitetura

A infraestrutura foi desenhada para evitar exposição desnecessária.

### Private EC2

A instância privada foi configurada para:

* não possuir IP público
* não aceitar acesso externo direto
* permitir acesso somente através do Bastion Host

### Bastion Host

O Bastion Host funciona como ponto de entrada administrativo e foi usado para:

* acesso SSH
* gerenciamento remoto da instância privada
* centralização das conexões

### Security Groups

As regras de segurança foram configuradas para:

* limitar portas abertas
* permitir comunicação apenas entre recursos autorizados
* restringir o acesso à instância privada
* manter a infraestrutura mais protegida

---

## Como Foi Construído

### 1. Criação da infraestrutura na AWS

Foram criadas duas instâncias EC2:

* uma instância pública atuando como Bastion Host
* uma instância privada responsável pela aplicação

### 2. Configuração do ambiente Linux

A máquina privada foi preparada com Ubuntu para receber a aplicação e os serviços necessários.

### 3. Instalação da aplicação Flask

Uma aplicação simples foi criada para validar o funcionamento do ambiente cloud.

### 4. Configuração do Nginx

O Nginx foi utilizado como camada de serviço e reverse proxy, servindo de entrada para a aplicação.

### 5. Controle de acesso

As regras de rede foram ajustadas para garantir que a instância privada não ficasse exposta diretamente à internet.

### 6. Validação externa

O ngrok foi usado apenas como recurso temporário para teste e demonstração da aplicação.

---

## Estrutura do Projeto

```text
cloud-system-info/
├── app.py
├── templates/
│   ├── home.html
│   └── status.html
├── README.md
└── .gitignore
```

---

## Deploy

O processo de implantação seguiu os passos abaixo:

1. criação das instâncias EC2 na AWS
2. configuração do Bastion Host com IP público
3. instalação da aplicação Flask na instância privada
4. configuração do Nginx como camada de serviço
5. definição das regras de Security Groups
6. teste do acesso entre as máquinas via SSH
7. validação da aplicação por meio de túnel temporário

---

## Possíveis Melhorias

Para deixar este projeto ainda mais forte para Engenharia de Dados, algumas evoluções possíveis são:

* adicionar **Terraform** para provisionamento da infraestrutura
* criar uma **VPC completa** com subnets públicas e privadas
* adicionar **PostgreSQL privado**
* incluir **Amazon S3** como camada de armazenamento
* integrar **Apache Airflow** para orquestração
* criar um pipeline simples de ingestão de dados
* adicionar monitoramento com **CloudWatch**
* configurar logs centralizados
* implementar CI/CD

---

## Aprendizados

Durante esse projeto, pratiquei:

* arquitetura cloud na AWS
* administração de Linux
* SSH e acesso remoto
* segmentação de rede
* segurança básica em ambientes de produção
* deploy de aplicação em servidor
* organização de infraestrutura com foco em controle e isolamento

---

## Relação com Engenharia de Dados

Embora este repositório não seja um pipeline de dados em si, ele representa uma base muito importante para Engenharia de Dados.

Em ambientes reais, soluções de dados costumam depender de:

* servidores Linux
* instâncias cloud
* acesso controlado a serviços internos
* bancos de dados privados
* orquestração de pipelines
* monitoramento e segurança

Ter domínio de AWS, redes e servidores ajuda a entender melhor **onde os dados rodam, como os serviços se comunicam e como estruturar ambientes mais confiáveis para processamento de dados**.

Esse projeto mostra justamente essa base de infraestrutura, que complementa muito bem projetos de ETL, orquestração e banco de dados.

---

## Contato

**Ruan Pablo Matos do Sacramento**

LinkedIn: https://www.linkedin.com/in/ruan-pablo-matos/

E-mail: [ruankinu@gmail.com](mailto:ruankinu@gmail.com)
