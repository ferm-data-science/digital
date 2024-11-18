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

                Почати


.. grid:: 3

    .. grid-item-card::  Data Warehouse
        :link: https://agrohuborgua.sharepoint.com/:f:/s/msteams_be7208-DataScience/Ep37mPTOh6VJuJ_yu07lV3gB5dFo6bxPA5VeuaH0CvDXxA?e=i0MgKS
        :padding: 1

        Розрахунок вартості володіння сховищем даних

    .. grid-item-card::  Власники техніки
        :link: https://agrohuborgua.sharepoint.com/:f:/s/msteams_be7208-DataScience/Et1pzy8q0-dKvtzuC_zMYdcBRFj62w_9FUt72zKRZYO9_w?e=BMIGmD
        :padding: 1

        Джерела інформації та співставлення даних з YouControl

    .. grid-item-card::  Дані для фінансової аналітики
        :link: https://example.com
        :padding: 1

        Дані АЗС, перелік ОЕЗ, коди митниць

    .. grid-item-card::  Цінові парсери
        :link: https://example.com
        :padding: 1

        * Активні

    .. grid-item-card::  Сайти та контакти
        :link: https://agrohuborgua.sharepoint.com/:f:/s/msteams_be7208-DataScience/Ek5RJBNYM6VFmPX5Khoii3sBW-FmTNRYfDtiJJ1SUDYG7A?e=adVAMD
        :padding: 1
        
        Перелік разових замовлень та отримання контактів

    .. grid-item-card::  Маркетингова аналітика
        :link: https://agrohuborgua.sharepoint.com/:f:/s/msteams_be7208-DataScience/Ena45JfsKaVHoPbCvrtKetEBRxEPu0Gdm0h1E9oyEenvHA?e=TRHmlh
        :padding: 1

        Дані Ahrefs, Google Analitics
    
    .. grid-item-card::  Тендерні майданчики
        :link: https://agrohuborgua.sharepoint.com/:f:/s/msteams_be7208-DataScience/Et51vFbhr5ZEr0M5Hf3GLO4BioaFy3CrWK79KBMBJaGLjw?e=z72ekm
        :padding: 1

        Дані публічних та комерційних тендерів

    .. grid-item-card::  Трейдери
        :link: https://example.com
        :padding: 1

        * Кросс-Докинг

    .. grid-item-card::  Talent
        :link: https://agrohuborgua.sharepoint.com/:f:/s/msteams_be7208-DataScience/Ek-gMwbyjNtOuy6Ifyqy_rcBrurTxtLOTR-qVZ-E3YhvQA?e=VVcIEl
        :padding: 1

        Дані про вакансії та резюме, зведена аналітика


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

- Доступ до сайтів відбувається через протоколи HTTP, HTTPS. 
- За допомогою Python створюються срипти та обсяг парсингу. Тобто, як потрібно аналізувати певний ресурс — повністю чи вибірково. 
- Весь процес будується за допомогою введених параметрів для збору потрібної інформації та вилучення контенту. 
- Налаштування пошуку в парсерах вводяться під конкретну задачу та мету визначення даних.
- Зазвичай експорт даних відбувається у два формати: CSV та Excel
- Інформація передаєтся замовнику з отриманням зворотнього зв'язку. 

=========================
Діяльність у межах закону
=========================

`Cтаття 34 «Конституції України»`_ : «Кожен має право вільно збирати, зберігати, використовувати і поширювати інформацію усно, письмово або в інший спосіб — на свій вибір.».  
Але, в `статті 4 закону «Про доступ до публічної інформації»`_ вказано про «Вільне отримання, поширення та будь-яке інше використання інформації, що була надана або оприлюднена відповідно Закону, крім обмежень, які ним встановлено». Ознайомитись з видами обмежень можна в статті 6 Закону України.  
Аналізування контенту у вільному доступі в інтернеті не заборонена законом. Винятком є особисті дані особи, які можуть її ідентифікувати. Парсити дозволено або деперсоніфіковані дані, або ж потрібно отримати згоду розпорядника інформації — власника сайту, на якому користувач зареєстрований. 
Щодо інформації, яка не є персональною — вона може вважатись конфіденційною тільки якщо про це зазначено. Так, на деяких ресурсах є розділ «Політика конфіденційності».  
Також, згідно з  `Законом України «Про авторське право і суміжні права»`_ варто враховувати можливе порушення авторських прав. Лише той, хто створив матеріал, визначає як його можна використовувати.

.. _Cтаття 34 «Конституції України»: https://www.president.gov.ua/ua/documents/constitution/konstituciya-ukrayini-rozdil-ii
.. _статті 4 закону «Про доступ до публічної інформації»: https://zakon.rada.gov.ua/laws/show/2939-17#Text
.. _Законом України «Про авторське право і суміжні права»: https://zakon.rada.gov.ua/laws/show/3792-12#Text

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