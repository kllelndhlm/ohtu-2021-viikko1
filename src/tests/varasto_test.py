import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, -1)
        self.varasto = Varasto(10, 0)

#    def test_konstruktori_luo_tyhjan_varaston(self):
 #       # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
  #      self.asserAlmostEqual(self.varasto.saldo, 0)

    def test_tulostus_oikein(self):
        tulostus = str(self.varasto)

        self.assertEqual(tulostus, "saldo = 0, vielä tilaa 10")

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastosta_otetaan_liian_vahan(self):
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastosta_otetaan_liikaa(self):
        self.varasto.ota_varastosta(11)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_varastoon_liian_vahan(self):
        self.varasto.lisaa_varastoon(-1)
        saldo_lisayksen_jalkeen = self.varasto.saldo
        self.assertAlmostEqual(saldo_lisayksen_jalkeen, 0)

    def test_lisaa_varastoon_liikaa(self):
        self.varasto.lisaa_varastoon(1000000)
        saldo_lisayksen_jalkeen = self.varasto.saldo
        self.assertAlmostEqual(saldo_lisayksen_jalkeen, 10)

    def test_miinusvarastolla_oikea_tilavuus(self):
        self.varasto = Varasto(-1)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

#    def test_konstruktori_luo_miinussaldon(self):
 #       self.varasto = Varasto(10, -1)
  #      self.asserAlmostEqual(self.varasto.saldo, 0)

