
# API I.A Granto Seguros

15 Atributos de entrada
1 saída
## Documentação da API

#### Retorna todos os itens

```http
  POST /testar
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Genero` | `int` | 0 - Mulher, 1 - Homem |
| `Idade` | `float` | Idade mínima: 18 |
| `Debito` | `float` | Quantia em reais da dívida |
| `Casado` | `int` | 0 - Solteiro(a)/Divorciado(a)/Viúvo(a), 1 - Casado(a) |
| `Possui_Conta_Banco` | `int` | 0 - Não, 1 - Sim |
| `Tipo_Industria` | `float` | 0 - 0 - Industrial, 1 - Material, 2 - Servico de Comunicacao, 3 - Transporte, 4 - Tecnologia da Informacao, 5 - Financas, 6 - Energia, 7 - Imobiliaria, 8 - Servico de Utilidade Publica, 9 - Consumidor Discrionario, 10 - Educacao, 11 - Bens de Consumo, 12 - Assistencia Medica, 13 - Pesquisas
| `Etnia` | `float` | 0 - Branco, 1 - Preto/Negro, 2 - Asiatico, 3 - Latino,  - Outro |
| `Anos_Empregado` | `float` | Tempo em anos que se trabalhou |
| `Inadimplente` | `int` | 0 - Não, 1 - Sim  |
| `Empregado` | `int` | 0 - Não, 1 - Sim |
| `Pontuacao_Credito` | `float` | Pontuação de Crédito da pessoa |
| `Habilitado` | `int` | 0 - Não, 1 - Sim |
| `Cidadania` | `float` | 0 - Cidadão de nascimento, 1 - Cidadão por outros meios, 2 - Cidadão temporário |
| `Codigo_Postal` | `float` | de 0 a 2000 |
| `Renda` | `float` | Renda pessoal em reais |

#### Retorna uma 

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Aprovado` | `int` | 0 - Não, 1 - Sim |
