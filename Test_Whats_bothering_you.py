import unittest
from main import Whats_bothering_you
from main import Soul, Hand, Throat


class Test_Chto_Bolit(unittest.TestCase):
    def setUp(self):
        self.chto = Whats_bothering_you()

    def test_chto_bolit1(self):
        self.assertEqual(self.chto.whats_bothering_you(1), "Душа")

    def test_chto_bolit2(self):
        self.assertEqual(self.chto.whats_bothering_you(2), "Рука")

    def test_chto_bolit3(self):
        self.assertEqual(self.chto.whats_bothering_you(3), "Горло")


class Test_Hand(unittest.TestCase):
    def setUp(self):
        self.gru = Hand()

    def test_hand1(self):
        self.assertEqual(self.gru.bolit_hand("да", "", ""),
                         "Обратитесь к терапевту или педиатру")

    def test_hand2(self):
        self.assertEqual(self.gru.bolit_hand("нет", "да", ""),
                         "Обратитесь к терапевту или педиатру")

    def test_hand3(self):
        self.assertEqual(self.gru.bolit_hand("нет", "нет", "да"),
                         "Обратитесь к терапевту или педиатру")

    def test_hand4(self):
        self.assertEqual(self.gru.bolit_hand("нет", "нет", "нет"),
                         "Дайте вашей руке покой и отдых,"
                         "если у вас были планы провести тренировки для "
                         "данной руки, то лучше перенести их на другой день.")


class Test_Gorlo(unittest.TestCase):
    def setUp(self):
        self.gor = Throat()

    def test_gorlo1(self):
        self.assertEqual(self.gor.bolit_throat("да", "да", "сухой", "", "", ),
                         "Тонзиллит")

    def test_gorlo2(self):
        self.assertEqual(self.gor.bolit_throat("да", "нет", "", "", "", ),
                         "Ангина")

    def test_gorlo3(self):
        self.assertEqual(
            self.gor.bolit_throat("да", "да", "влажный", "", "", ),
            "Бронхит")

    def test_gorlo4(self):
        self.assertEqual(self.gor.bolit_throat("да", "да", "сухой", "", "", ),
                         "Тонзиллит")

    def test_gorlo5(self):
        self.assertEqual(self.gor.bolit_throat("нет", "", "", "да", ""),
                         "Не напрягайте их в ближайшее время")

    def test_gorlo6(self):
        self.assertEqual(self.gor.bolit_throat("нет", "", "", "нет", "да"),
                         "Обратись к ЛОР-врачу")

    def test_gorlo7(self):
        self.assertEqual(self.gor.bolit_throat("нет", "", "", "нет", "нет"),
                         "Симулянт")


class Test_Soul(unittest.TestCase):
    def setUp(self):
        self.gol = Soul()

    def test_soul1(self):
        self.assertEqual(self.gol.bolit_soul("да", "нет", "", ""),
                         "Обратитесь за помощью к специалистам")

    def test_soul2(self):
        self.assertEqual(self.gol.bolit_soul("нет", "да", "", ""),
                         "Сходите к психологу")

    def test_soul3(self):
        self.assertEqual(self.gol.bolit_soul("нет", "нет", "да", ""),
                         "Займитесь переосмыслением вашей жизни, уделите "
                         "как можно больше времени вашим желаниям и нуждам!")

    def test_soul4(self):
        self.assertEqual(self.gol.bolit_soul("нет", "нет", "нет", "да"),
                         "В данный момент все мы переживаем трудности " \
                         "душевного характера, осознание прогнившего " \
                         "мира гложет всех нас, но главное есть инфа " \
                         "от знающего человека, что у нас в стране " \
                         "скоро ожидаются реальные изменения. От нас " \
                         "требуется сидеть тихо. После того, как все сделают, все будет у нас хорошо." \
                         " Главное сейчас сидеть тихо и не суетиться. Никаких митингов, никаких навальных." \
                         " Просто переждать и всё будет хорошо, там все схвачено"
                         )

    def test_soul5(self):
        self.assertEqual(self.gol.bolit_soul("нет", "нет", "нет", "нет"),
                         "КТО Я ?")


if __name__ == '__main__':
    unittest.main()
