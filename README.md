# toys_shop_5

from toy_department.models import Buyer, Toy

Buyer.objects.create(name='Лиза', balance=500, age=25)
Buyer.objects.create(name='Коля', balance=700, age=24)
Buyer.objects.create(name='Миша', balance=250, age=5)

Toy.objects.create(title='Кукла Игнат', cost=2000, weight=350, description='Забавная кукла', age_limited=False, in_stock=5, picture_min='Ignatiy.png', picture_max='Ignatiy.gif')
Toy.objects.create(title='Медвежонок Тэдди', cost=950, weight=500, description='Очень мимимишка!', age_limited=False, in_stock=3, picture_min='teddy_bear.png', picture_max='teddy_bear.gif')
Toy.objects.create(title='Наглый кот', cost=1050, weight=250, description='Мышей не ловит. Только ест, спит и со стола ворует.', age_limited=False, in_stock=5, picture_min='Cat.png', picture_max='Cat.gif')
Toy.objects.create(title='Заяц Пафнутий', cost=2100, weight=475, description='Ну, заяц... Уши есть. Хвост тоже. Но...', age_limited=True, in_stock=2, picture_min='Pafnutiy.png', picture_max='Pafnutiy.gif')

Buyer.objects.get(id=1).toys.set(([x for x in [1, 2, 3, 4] if (Buyer.objects.get(id=1).age > 18 or Toy.objects.get(id=x).age_limited != True)]))
Buyer.objects.get(id=2).toys.set(([x for x in [1, 4] if (Buyer.objects.get(id=2).age > 18 or Toy.objects.get(id=x).age_limited != True)]))
Buyer.objects.get(id=3).toys.set(([x for x in [1, 2, 3, 4] if (Buyer.objects.get(id=3).age > 18 or Toy.objects.get(id=x).age_limited != True)]))
