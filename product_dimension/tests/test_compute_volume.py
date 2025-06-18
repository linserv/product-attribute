# Copyright 2015 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.tests.common import TransactionCase


class TestComputeVolumeOnProduct(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = cls.env["product.product"].new()
        cls.uom_m = cls.env["uom.uom"].search([("name", "=", "m")])

    def test_it_computes_volume_in_meters(self):
        self.product.product_length = 6.0
        self.product.product_height = 2.0
        self.product.product_width = 10.0
        self.product.dimensional_uom_id = self.uom_m
        self.assertAlmostEqual(120, self.product.volume)


class TestComputeVolumeOnTemplate(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.template = cls.env["product.template"].new()
        cls.uom_m = cls.env["uom.uom"].search([("name", "=", "m")])

    def test_it_computes_volume_in_meters(self):
        self.template.product_length = 6.0
        self.template.product_height = 2.0
        self.template.product_width = 10.0
        self.template.dimensional_uom_id = self.uom_m
        self.assertAlmostEqual(120, self.template.volume)
