# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields
import repositories.custom_models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'banner_id')),
                ('ativo', models.NullBooleanField(db_column=b'banner_ativo')),
                ('nome', models.TextField(db_column=b'banner_nome')),
                ('poweredby', models.TextField(db_column=b'banner_poweredby')),
                ('chamada', models.TextField(db_column=b'banner_chamada')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, db_column=b'banner_valor')),
                ('url_thumbnail', models.TextField(db_column=b'banner_url_thumbnail')),
                ('url_screenshots', models.TextField(db_column=b'banner_url_screenshots')),
                ('url_download', models.TextField(db_column=b'banner_url_download')),
                ('url_lojamodelo', models.TextField(db_column=b'banner_url_lojamodelo')),
                ('data_criacao', models.DateTimeField(default=0, db_column=b'banner_data_criacao')),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column=b'banner_data_modificacao')),
            ],
            options={
                'db_table': 'faturamento"."tb_banner',
            },
        ),
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'colecao_id')),
                ('nome', models.TextField(db_column=b'colecao_nome')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_column=b'colecao_data_criacao')),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column=b'colecao_data_modificacao')),
            ],
            options={
                'db_table': 'faturamento"."tb_colecao',
            },
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'consumo_id')),
                ('data', models.DateField(default=None, db_column=b'consumo_data')),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column=b'consumo_data_modificacao')),
                ('trafego', models.BigIntegerField(default=0, db_column=b'consumo_trafego')),
                ('visitas', models.BigIntegerField(default=0, db_column=b'consumo_visitas')),
            ],
            options={
                'db_table': 'faturamento"."tb_consumo',
            },
        ),
        migrations.CreateModel(
            name='DadosCobranca',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'dados_cobranca_id')),
                ('forma_pagamento', models.TextField(db_column=b'dados_cobranca_forma_pagamento', choices=[(b'BOLETO', 'Boleto'), (b'CARTAO DE CREDITO', 'Cart\xe3o de cr\xe9dito'), (b'WHITELABEL', 'Whitelabel')])),
                ('tipo_pessoa', models.TextField(db_column=b'dados_cobranca_tipo_pessoa', choices=[(b'PF', 'Pessoa F\xedsica'), (b'PJ', 'Pessoa Jur\xeddica')])),
                ('email_nfe', models.TextField(db_column=b'dados_cobranca_email_nfe')),
                ('nome_responsavel', models.TextField(db_column=b'dados_cobranca_nome_responsavel')),
                ('cpf', models.TextField(null=True, db_column=b'dados_cobranca_cpf')),
                ('razao_social', models.TextField(null=True, db_column=b'dados_cobranca_razao_social')),
                ('cnpj', models.TextField(null=True, db_column=b'dados_cobranca_cnpj')),
                ('telefone_principal', models.TextField(null=True, db_column=b'dados_cobranca_telefone_principal')),
                ('telefone_alternativo', models.TextField(db_column=b'dados_cobranca_telefone_alternativo')),
                ('endereco_logradouro', models.TextField(db_column=b'dados_cobranca_endereco_logradouro')),
                ('endereco_numero', models.TextField(db_column=b'dados_cobranca_endereco_numero')),
                ('endereco_complemento', models.TextField(db_column=b'dados_cobranca_endereco_complemento')),
                ('endereco_bairro', models.TextField(db_column=b'dados_cobranca_endereco_bairro')),
                ('endereco_cidade_ibge', models.TextField(db_column=b'dados_cobranca_endereco_cidade_ibge')),
                ('endereco_estado', models.TextField(db_column=b'dados_cobranca_endereco_estado')),
                ('endereco_cep', models.TextField(db_column=b'dados_cobranca_endereco_cep')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_column=b'dados_cobranca_data_criacao')),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column=b'dados_cobranca_data_modificacao')),
            ],
            options={
                'db_table': 'faturamento"."tb_dados_cobranca',
            },
        ),
        migrations.CreateModel(
            name='DadosCobrancaCartao',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'dados_cobranca_cartao_id')),
                ('nome_portador', models.TextField(db_column=b'dados_cobranca_cartao_nome_portador')),
                ('numero', models.TextField(max_length=64, db_column=b'dados_cobranca_cartao_numero')),
                ('cvv', models.TextField(max_length=64, db_column=b'dados_cobranca_cartao_cvv')),
                ('expiracao_mes', models.TextField(max_length=255, db_column=b'dados_cobranca_cartao_expiracao_mes')),
                ('expiracao_ano', models.TextField(max_length=255, db_column=b'dados_cobranca_cartao_expiracao_ano')),
                ('ultimos_numeros', models.TextField(max_length=255, db_column=b'dados_cobranca_cartao_ultimos_numeros')),
                ('salt', models.TextField(max_length=23, db_column=b'dados_cobranca_cartao_salt')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_column=b'dados_cobranca_cartao_data_criacao')),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column=b'dados_cobranca_cartao_data_modificacao')),
            ],
            options={
                'db_table': 'faturamento"."tb_dados_cobranca_cartao',
            },
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'fatura_id')),
                ('situacao', models.TextField(db_column=b'fatura_situacao', choices=[(b'PAGA', 'Paga'), (b'AGUARDANDO PAGAMENTO', 'Aguardando pagamento'), (b'CANCELADA', 'Cancelada'), (b'ESTORNADA', 'Estornada'), (b'CHARGEBACK', 'Chargeback'), (b'ISENTA', 'Isenta'), (b'WHITELABEL', 'Whitelabel')])),
                ('valor_cheio', models.DecimalField(decimal_places=2, max_digits=12, db_column=b'fatura_valor_cheio')),
                ('valor_impostos', models.DecimalField(decimal_places=2, max_digits=12, db_column=b'fatura_valor_impostos')),
                ('valor_impostos_json', jsonfield.fields.JSONField(default=None, null=True, db_column=b'fatura_valor_impostos_json')),
                ('valor_cobrado', models.DecimalField(decimal_places=2, max_digits=12, db_column=b'fatura_valor_cobrado')),
                ('valor_pago', models.DecimalField(default=0, decimal_places=2, max_digits=12, db_column=b'fatura_valor_pago')),
                ('dados_forma_pagamento', models.TextField(db_column=b'fatura_dados_forma_pagamento', choices=[(b'BOLETO', 'Boleto'), (b'CARTAO DE CREDITO', 'Cart\xe3o de cr\xe9dito'), (b'WHITELABEL', 'Whitelabel')])),
                ('dados_tipo_pessoa', models.TextField(db_column=b'fatura_dados_tipo_pessoa', choices=[(b'PF', 'Pessoa F\xedsica'), (b'PJ', 'Pessoa Jur\xeddica')])),
                ('dados_email_nfe', models.TextField(db_column=b'fatura_dados_email_nfe')),
                ('dados_nome_responsavel', models.TextField(db_column=b'fatura_dados_nome_responsavel')),
                ('dados_cpf', models.TextField(default=None, db_column=b'fatura_dados_cpf')),
                ('dados_razao_social', models.TextField(default=None, db_column=b'fatura_dados_razao_social')),
                ('dados_cnpj', models.TextField(default=None, db_column=b'fatura_dados_cnpj')),
                ('dados_telefone_principal', models.TextField(default=None, db_column=b'fatura_dados_telefone_principal')),
                ('dados_telefone_alternativo', models.TextField(default=None, db_column=b'fatura_dados_telefone_alternativo')),
                ('dados_endereco_logradouro', models.TextField(db_column=b'fatura_dados_endereco_logradouro')),
                ('dados_endereco_numero', models.TextField(db_column=b'fatura_dados_endereco_numero')),
                ('dados_endereco_complemento', models.TextField(default=None, db_column=b'fatura_dados_endereco_complemento')),
                ('dados_endereco_bairro', models.TextField(db_column=b'fatura_dados_endereco_bairro')),
                ('dados_endereco_cidade_ibge', models.TextField(db_column=b'fatura_dados_endereco_cidade_ibge')),
                ('dados_endereco_estado', models.TextField(db_column=b'fatura_dados_endereco_estado')),
                ('dados_endereco_cep', models.TextField(db_column=b'fatura_dados_endereco_cep')),
                ('data_vencimento', models.DateField(db_column=b'fatura_data_vencimento')),
                ('data_tolerancia', models.DateField(db_column=b'fatura_data_tolerancia')),
                ('data_pagamento', models.DateField(default=None, db_column=b'fatura_data_pagamento', db_index=True)),
                ('boleto_codigo_de_barras', models.TextField(default=None, db_column=b'fatura_boleto_codigo_de_barras')),
                ('boleto_url', models.TextField(default=None, db_column=b'fatura_boleto_url')),
                ('cartao_de_credito_cv', models.TextField(default=None, db_column=b'fatura_cartao_de_credito_cv')),
                ('cartao_de_credito_numero', models.TextField(default=None, db_column=b'fatura_cartao_de_credito_numero')),
                ('cartao_de_credito_msgret', models.TextField(default=None, db_column=b'fatura_cartao_de_credito_msgret')),
                ('cartao_de_credito_codret', models.TextField(default=None, db_column=b'fatura_cartao_de_credito_codret')),
                ('cartao_de_credito_data_autorizacao', models.DateField(default=None, db_column=b'fatura_cartao_de_credito_data_autorizacao')),
                ('controle_lancamento_numero', models.TextField(default=None, db_column=b'fatura_controle_lancamento_numero', db_index=True)),
                ('controle_lancamento_quitado', models.BooleanField(default=False, db_column=b'fatura_controle_lancamento_quitado')),
                ('controle_nota_fiscal', models.IntegerField(default=None, db_column=b'fatura_controle_nota_fiscal')),
                ('json', jsonfield.fields.JSONField(default=None, null=True, db_column=b'fatura_json')),
                ('observacao', models.TextField(db_column=b'fatura_observacao')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_column=b'fatura_data_criacao')),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column=b'fatura_data_modificacao')),
            ],
            options={
                'db_table': 'faturamento"."tb_fatura',
            },
        ),
        migrations.CreateModel(
            name='FaturaItem',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'fatura_item_id')),
                ('valor_cheio', models.DecimalField(decimal_places=2, max_digits=12, db_column=b'fatura_item_valor_cheio')),
                ('valor_cobrado', models.DecimalField(decimal_places=2, max_digits=12, db_column=b'fatura_item_valor_cobrado')),
                ('referencia_tabela', models.TextField(default=None, null=True, db_column=b'fatura_item_referencia_tabela')),
                ('referencia_campo', models.TextField(default=None, null=True, db_column=b'fatura_item_referencia_campo')),
                ('referencia_id', models.IntegerField(default=None, null=True, db_column=b'fatura_item_referencia_id')),
                ('referencia_situacao_principal', models.TextField(default=None, null=True, db_column=b'fatura_item_referencia_situacao_principal')),
                ('referencia_situacao_complementar', models.TextField(default=None, null=True, db_column=b'fatura_item_referencia_situacao_complementar')),
                ('json', jsonfield.fields.JSONField(default=None, null=True, db_column=b'fatura_item_json')),
            ],
            options={
                'db_table': 'faturamento"."tb_fatura_item',
            },
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'plano_id')),
                ('nome', models.TextField(db_column=b'plano_nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, db_column=b'plano_valor')),
                ('indice', models.IntegerField(default=0, db_column=b'plano_indice')),
                ('controle_trafego', models.BigIntegerField(default=0, db_column=b'plano_controle_trafego')),
                ('controle_visitas', models.BigIntegerField(default=0, db_column=b'plano_controle_visitas')),
                ('controle_produtos', models.IntegerField(default=0, db_column=b'plano_controle_produtos')),
                ('comissao', models.DecimalField(default=0, decimal_places=2, max_digits=12, db_column=b'plano_comissao')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_column=b'plano_data_criacao')),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column=b'plano_data_modificacao')),
            ],
            options={
                'db_table': 'faturamento"."tb_plano',
            },
        ),
        migrations.CreateModel(
            name='PlanoAssinatura',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'plano_assinatura_id')),
                ('acao', models.TextField(default=b'MANTEVE', db_column=b'plano_assinatura_acao', choices=[(b'MANTEVE', 'Manteve'), (b'UPGRADE', 'Upgrade'), (b'DOWNGRADE', 'Downgrade'), (b'PRIMEIRO', 'rimeiro')])),
                ('ciclo_inicio', models.DateField(db_column=b'plano_assinatura_ciclo_inicio')),
                ('ciclo_fim', models.DateField(db_column=b'plano_assinatura_ciclo_fim')),
                ('controle_trafego', models.BigIntegerField(default=0, db_column=b'plano_assinatura_controle_trafego')),
                ('controle_visitas', models.BigIntegerField(default=0, db_column=b'plano_assinatura_controle_visitas')),
                ('controle_produtos', models.IntegerField(default=0, db_column=b'plano_assinatura_controle_produtos')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_column=b'plano_assinatura_data_criacao')),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column=b'plano_assinatura_data_modificacao')),
            ],
            options={
                'db_table': 'faturamento"."tb_plano_assinatura',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', repositories.custom_models.BigAutoField(serialize=False, primary_key=True, db_column=b'tema_id')),
                ('ativo', models.NullBooleanField(db_column=b'tema_ativo')),
                ('nome', models.TextField(db_column=b'tema_nome')),
                ('poweredby', models.TextField(db_column=b'tema_poweredby')),
                ('chamada', models.TextField(db_column=b'tema_chamada')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, db_column=b'tema_valor')),
                ('headtags', models.TextField(db_column=b'tema_headtags')),
                ('footags', models.TextField(db_column=b'tema_footags')),
                ('layout_parametros', jsonfield.fields.JSONField(default=None, null=True, db_column=b'tema_layout_parametros')),
                ('url_thumbnail', models.TextField(db_column=b'tema_url_thumbnail')),
                ('url_screenshots', models.TextField(db_column=b'tema_url_screenshots')),
                ('url_download', models.TextField(db_column=b'tema_url_download')),
                ('url_lojamodelo', models.TextField(db_column=b'tema_url_lojamodelo')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_column=b'tema_data_criacao')),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column=b'tema_data_modificacao')),
                ('colecao', models.ForeignKey(to='faturamento.Colecao', db_column=b'colecao_id')),
            ],
            options={
                'db_table': 'faturamento"."tb_tema',
            },
        ),
    ]
