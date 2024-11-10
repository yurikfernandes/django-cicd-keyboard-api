# models.py
from django.db import models

STARS = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
]

class Keyboard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('stagepiano', 'Stage Piano'),
        ('workstation', 'Workstation'),
        ('synth', 'Synthesizer'),
        ('digital_piano', 'Digital Piano'),
        ('arranger', 'Arranjador'),
        ('controller', 'Controlador MIDI')

    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.category}"
    

class KeyboardFeature(models.Model):
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    has_it = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.keyboard.name} {self.name}"


class KeyboardEvaluation(models.Model):
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    avaliation = models.TextField(null=True, blank=True)

    sound_versatility = models.IntegerField(null=True, blank=True, choices=STARS, verbose_name="Versatilidade sonora", help_text="Avalia a variedade e qualidade dos sons disponíveis, além do piano.")
    editing_features = models.IntegerField(null=True, blank=True, choices=STARS, verbose_name="Funcionalidades de edição", help_text="Refere-se às opções para editar, mixar e ajustar sons diretamente no teclado.")
    ease_of_use = models.IntegerField(null=True, blank=True, choices=STARS, verbose_name="Facilidade de uso", help_text="Mede o quão intuitivo e fácil é operar o teclado e navegar pelos menus.")
    connectivity = models.IntegerField(null=True, blank=True, choices=STARS, verbose_name="Conectividade", help_text="Avalia as opções de conexão MIDI, USB, Bluetooth, entradas e saídas de áudio.")
    build_quality = models.IntegerField(null=True, blank=True, choices=STARS, verbose_name="Qualidade da construção", help_text="Avalia a qualidade da construção do teclado, incluindo a qualidade de materiais e a estrutura.")
    weight_and_size = models.IntegerField(null=True, blank=True, choices=STARS, verbose_name="Peso e tamanho", help_text="Avalia o peso e o tamanho do teclado, incluindo a altura e a largura.")
    key_feeling = models.IntegerField(null=True, blank=True, choices=STARS, verbose_name="Sensibilidade das teclas", help_text="Avalia a sensibilidade das teclas e o conforto ao tocar.")
    auto_accompaniment_features = models.IntegerField(null=True, choices=STARS, blank=True, verbose_name="Funcionalidades de acompanhamento automático", help_text="Avalia as opções de acompanhamento automático, como melodia e ritmo.")
    expandability = models.IntegerField(null=True, blank=True, choices=STARS, verbose_name="Expandibilidade", help_text="Mede se o teclado permite adicionar mais sons, atualizações ou expansão de memória.")
    price_and_value_for_money = models.IntegerField(null=True, blank=True, choices=STARS, verbose_name="Preço e valor para dinheiro", help_text="Avalia o preço e o valor do teclado em relação ao seu custo.")
    
    overall_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.keyboard.name} Evaluation - Ratintg: {self.overall_rating}"
