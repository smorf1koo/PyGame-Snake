# "Змейка" на Python

Это простая реализация игры "Змейка" на языке Python с использованием библиотеки pygame.

## Зависимости

Для запуска этой игры вам потребуется установить библиотеку pygame версии 2.5.2.

```bash
pip install pygame==2.5.2
```
## Запуск игры

Для запуска игры выполните следующую команду:

```bash
python main.py
```

## Управление

- Вверх: Клавиша "↑"
- Вниз: Клавиша "↓"
- Влево: Клавиша "←"
- Вправо: Клавиша "→"
- Пауза: Кваливша "c"

## Правила игры

Съедайте еду, чтобы увеличить длину змейки.
Избегайте столкновений с собственным телом и границами экрана.
С шансом 5% появляется большая ягода, которая увеличивает змейку на 5 делений.

## Завершение игры

Игра завершится, если змейка столкнется с границами экрана или с собственным телом.

## TODO

База данных с рекордом и прошлыми попытками
