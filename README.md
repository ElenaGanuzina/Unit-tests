# Unit-tests

## HW_1. Задание 1. 
В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент скидки 
и возвращает сумму с учетом скидки.
Ваша задача - проверить этот метод с использованием библиотеки AssertJ. 
Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException. 
Не забудьте написать тесты для проверки этого поведения.

## HW_2. Задание 1.
Проект Vehicle. Написать следующие тесты с использованием JUnit5:

- Проверить, что экземпляр объекта Car также является экземпляром транспортного средства 
(используя оператор instanceof).

- Проверить, что объект Car создается с 4-мя колесами.

- Проверить, что объект Motorcycle создается с 2-мя колесами.

- Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).

- Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).

- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) 
машина останавливается (speed = 0).

- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) 
мотоцикл останавливается (speed = 0).

В этом проекте, вы будете работать с проектом ""Vehicle"", который представляет собой иерархию классов, 
включающую абстрактный базовый класс ""Vehicle"" и два его подкласса ""Car"" и ""Motorcycle"".

Базовый класс ""Vehicle"" содержит абстрактные методы ""testDrive()"" и ""park()"", а также поля ""company"", ""model"",
""yearRelease"", ""numWheels"" и ""speed"".

Класс ""Car"" расширяет ""Vehicle"" и реализует его абстрактные методы. При создании объекта ""Car"", 
число колес устанавливается в 4, а скорость в 0. В методе ""testDrive()"" скорость устанавливается на 60, 
а в методе ""park()"" - обратно в 0.

Класс ""Motorcycle"" также расширяет ""Vehicle"" и реализует его абстрактные методы. 
При создании объекта ""Motorcycle"", число колес устанавливается в 2, а скорость в 0. 
В методе ""testDrive()"" скорость устанавливается на 75, а в методе ""park()"" - обратно в 0.


## HW_3.
## Задание 1.

Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли переданное число 
четным или нечетным. (код приложен в презентации)

## Задание 2.

Разработайте и протестируйте метод numberInInterval, который проверяет, 
попадает ли переданное число в интервал (25;100). (код приложен в презентации)

## Задание 3.  (необязательное)

Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей, кроме администраторов. 
Для этого, вам потребуется расширить класс User новым свойством, указывающим, 
обладает ли пользователь админскими правами. Протестируйте данную функцию.

## HW_4 
## Задание 2.

У вас есть класс BookService, который использует интерфейс BookRepository для получения информации 
о книгах из базы данных.
Ваша задача написать unit-тесты для BookService, использу Mockito для создания мок-объекта BookRepository.

## HW_6
## Задание 1. 
Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:
a. Рассчитывает среднее значение каждого списка.
b. Сравнивает эти средние значения и выводит соответствующее сообщение:
- ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
- ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
- ""Средние значения равны"", если средние значения списков равны.

Важно:
Приложение должно быть написано в соответствии с принципами объектно-ориентированного программирования.
Используйте Pytest (для Python) или JUnit (для Java) для написания тестов, 
которые проверяют правильность работы программы. 
Тесты должны учитывать различные сценарии использования вашего приложения.
Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.
Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.

*Формат и требования к сдаче: *
Отчет о выполнении этого задания должен включать в себя следующие элементы:
- Код программы
- Код тестов
- Отчет pylint/Checkstyle
- Отчет о покрытии тестами
- Объяснение того, какие сценарии покрыты тестами и почему вы выбрали именно эти сценарии.