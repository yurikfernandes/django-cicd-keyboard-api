from django.db import models
import random

STARS = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
]

KEYBOARDS_CATEGORIES = [
    ('stagepiano', 'Stage Piano'),
    ('workstation', 'Workstation'),
    ('synth', 'Sintetizador'),
    ('digital_piano', 'Digital Piano'),
    ('arranger', 'Arranjador'),
    ('controller', 'Controlador MIDI')
]

class KeyboardCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, choices=KEYBOARDS_CATEGORIES)

    def __str__(self):
        return self.name
    
    @property
    def get_category_display(self):
        for category in KEYBOARDS_CATEGORIES:
            if category[0] == self.name:
                return category[1]
        return self.name

    @staticmethod
    def generate_default_category():
        for category in KEYBOARDS_CATEGORIES:
            KeyboardCategory.objects.get_or_create(name=category[0])


class Keyboard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(KeyboardCategory)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    overall_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_top_keyboards():
        top_queryset = Keyboard.objects.none()

        for category in KEYBOARDS_CATEGORIES:
            top_queryset |= Keyboard.objects.filter(
                category=category[0]
            ).order_by('-overall_rating').first()

        return top_queryset

    def get_keyboard_dict(self):
        data = {
            'name': self.name,
            'description': self.description,
            'categories': self.get_categories_string(),
            'overall_rating': self.overall_rating
        }
        return data
    
    def get_categories_string(self):
        return ', '.join(category.get_category_display for category in self.categories.all())
    
    def calculate_overall_rating(self):
        evaluations = self.evaluations.all()
        overall_rating = (sum(evaluation.rating_0_to_100 for evaluation in evaluations) / len(evaluations)) / 100
        self.overall_rating = overall_rating
        self.save()

    @staticmethod
    def get_random_keyboard(num=10):
        for i in range(num):
            keyboard = Keyboard(
                name=f"Teclado {i+1}",
                description=f"Descrição do piano {i+1}",
                # marca=["Yamaha", "Roland", "Korg"][random.randint(1, 3)],
                # numero_de_teclas=[88, 76, 61][random.randint(1, 3)]
            )
            keyboard.save()
            for _ in range(random.randint(1, 3)):
                keyboard.categories.add(KeyboardCategory.objects.get(name=random.choice(KEYBOARDS_CATEGORIES)[0]))

class KeyboardFeature(models.Model):
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    has_it = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.keyboard.name} {self.name}"


class KeyboardEvaluation(models.Model):
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE, related_name='evaluations')
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
    
    def __str__(self):
        return f"{self.keyboard.name} Evaluation"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.keyboard.calculate_overall_rating()

    @property
    def rating_0_to_100(self):
        list_of_features = [
            'sound_versatility',
            'editing_features',
            'ease_of_use',
            'connectivity',
            'build_quality',
            'weight_and_size',
            'key_feeling',
            'auto_accompaniment_features',
            'expandability',
            'price_and_value_for_money'
        ]

        list_of_values = [getattr(self, feature) for feature in list_of_features]
        rating = sum(list_of_values) / len(list_of_values) * 100

        return rating

    @staticmethod
    def generate_random_avaliations():
        keyboards = Keyboard.objects.all()
        for keyboard in keyboards:
            avaliacao = KeyboardEvaluation(
                keyboard=keyboard,

                sound_versatility=random.randint(1, 5),
                editing_features=random.randint(1, 5),
                ease_of_use=random.randint(1, 5),
                connectivity=random.randint(1, 5),
                build_quality=random.randint(1, 5),
                weight_and_size=random.randint(1, 5),
                key_feeling=random.randint(1, 5),
                auto_accompaniment_features=random.randint(1, 5),
                expandability=random.randint(1, 5),
                price_and_value_for_money=random.randint(1, 5),

                avaliation="Avaliação genérica para o teclado {}".format(keyboard.name)
            )
            avaliacao.save()
