from odoo import models, fields, api


class Locataire(models.Model):
    _name = 'real_estate_ci.locataire'
    _description = 'real_estate_ci.locataire'

    name = fields.Char('Nom')
    prenoms = fields.Char('Prénoms')
    contact = fields.Char('Contact')
    adresse = fields.Text('Adresse')
    ville = fields.Char("Ville")
    pays = fields.Char("Pays")
    location_ids = fields.One2many('real_estate_ci.location', 'locataire_id', string='Propriétés')