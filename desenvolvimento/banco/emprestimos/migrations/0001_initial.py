# Generated by Django 5.0.4 on 2024-04-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SimulacaoEmprestimo",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                (
                    "valor_emprestimo",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("taxa_juros", models.DecimalField(decimal_places=2, max_digits=5)),
                ("prazo_meses", models.IntegerField()),
            ],
        ),
    ]
