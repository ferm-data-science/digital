.. tets documentation master file, created by
   sphinx-quickstart on Fri Jul 28 19:38:14 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


:sd_hide_title:

Welcome to tets's documentation!
================================

.. div:: :style: padding: 0.1rem 0.5rem 0.6rem 0; 
        background-image: linear-gradient(315deg, #9efed0 0%, #1572f4 74%);
        clip-path: polygon(0px 0px, 100% 0%, 100% 100%, 0% calc(100% - 1.5rem)); 
        -webkit-clip-path: polygon(0px 0px, 100% 0%, 100% 100%, 0% calc(100% - 1.5rem))
    
    .. grid:: 
        :gutter: 2 3 3 3 
        :reverse:
        :margin: 4 4 1 2

        .. grid-item::
            :columns: 12 4 4 4
            :class: sd-width-25 sd-m-auto sd-animate-grow50-rot20

            .. image:: ./../images/cube.svg
                :class: sd-m-auto sd-animate-grow50-rot20

        .. grid-item::
            :columns: 12 8 8 8
            :child-align: justify
            :class: sd-text-white sd-fs-3

            | FERM digital
            | автоматизований збір та структурування даних з інтернету

            .. button-ref:: refname2
                :color: primary
                :ref-type: ref
                :class: underline

                Button text


.. grid:: 3

    .. grid-item-card::  Data Warehouse
        :link: https://example.com
        :padding: 1

        * Общие положения
        * Топология склада

    .. grid-item-card::  Власники техніки
        :link: https://example.com
        :padding: 1

        * Джерела інформації
        * Співставлення з YouControl

    .. grid-item-card::  Дані для фінансової аналітики
        :link: https://example.com
        :padding: 1

        * Дані по АЗС
        * Перелік ОЕЗ
        * Tripoli

    .. grid-item-card::  Цінові парсери
        :link: https://example.com
        :padding: 1

        * Активні

    .. grid-item-card::  Сайти
        :link: https://example.com
        :padding: 1

        * Консолидация
        * Транзит
        * Хранение

    .. grid-item-card::  Дані по АЗС
        :link: https://example.com
        :padding: 1

        * Кросс-Докинг

    .. grid-item-card::  Маркетингова аналітика
        :link: https://example.com
        :padding: 1

        * Ahrefs
        * Google Analitics
    
    .. grid-item-card::  Тенедерні майданчики
        :link: https://example.com
        :padding: 1

        * Smarttender
        * APS

    .. grid-item-card::  Трейдери
        :link: https://example.com
        :padding: 1

        * Кросс-Докинг

    .. grid-item-card::  Talent
        :link: https://example.com
        :padding: 1

        * Настройки

    .. grid-item-card::  Учасники будівельних тендерів
        :link: https://example.com
        :padding: 1

        * Настройки

    .. grid-item-card::  Пошук контактів
        :link: https://example.com
        :padding: 1

        * Учасники будівельних тендерів
        * Flagma, OLX, Prom, RST, ...



=====================================
Мета створення інформаційного ресурсу
=====================================

Відображення актуальних та архівних даних, які були створені на підставі первісних вимог замовників щодо автоматизованого збору інформації - парсингу.

.. _refname1:

==========================
Мета використання парсингу
==========================

- Збір інформації з сайтів, асортимент, особливості, сильні та слабкі сторони;
- Дослідження ринку та динаміки змін (аналіз цін, попиту, пропозицій на певні товари чи послуги);
- Збір відгуків та коментарів;
- Копіювання каталогів сайтів та адаптація під свої потреби;
- Створення бази потенційних лідів, маркетингова аналітика.

==============================================
Яка інформація доступна за допомогою парсингу?
==============================================

- Ціни;
- Товарні картки з характеристиками;
- Канали telegram, viber;
- Контакти;
- Аналітика Google Search API;

=============
Як це працює?
=============

Доступ до сайтів відбувається через протоколи HTTP, HTTPS. 
За допомогою Python створюються срипти та обсяг парсингу. Тобто, як потрібно аналізувати певний ресурс — повністю чи вибірково. 
Весь процес будується за допомогою введених параметрів для збору потрібної інформації та вилучення контенту. 
Налаштування пошуку в парсерах вводяться під конкретну задачу та мету визначення даних.
Зазвичай експорт даних відбувається у два формати: CSV та Excel
Інформація передаєтся замовнику з отриманням зворотнього зв'язку. 


=========================
Що забороняється законом?
=========================

- Навмисна шкода сайтам (DDOS);
- Пошук особистих даних користувачів, які не є у вільному доступі;
- Розміщення чужого контенту;
- Збір, розповсюдження інформації, яка є комерційною або державною таємницею.


.. _refname2:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   tips
   github