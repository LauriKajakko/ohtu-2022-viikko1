import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

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
    
    def test_neg_tilavuus_niin_nolla(self):
        v = Varasto(-1)
        self.assertAlmostEqual(v.tilavuus, 0)

    def test_ei_nolla_saldo_nollaa(self):
        v = Varasto(10, -1)
        self.assertAlmostEqual(v.saldo, 0)

    def test_ota_neg_maara(self):
        res = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(res, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_yli_saldo(self):
        self.varasto.lisaa_varastoon(8)
        res = self.varasto.ota_varastosta(9)
        self.assertAlmostEqual(res, 8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_neg_varastoon(self):
        res = self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(res, None)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_yli_tilavuus(self):
        res = self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_lisaa_ok_maara(self):
        res = self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_toString(self):
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")