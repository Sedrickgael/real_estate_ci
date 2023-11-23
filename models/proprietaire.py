from odoo import models, fields, api


class Proprietaire(models.Model):
    _name = 'real_estate_ci.proprietaire'
    _description = 'real_estate_ci.proprietaire'

    name = fields.Char('Nom')
    prenoms = fields.Char('Prénoms')
    contact = fields.Char('Contact')
    adresse = fields.Text('Adresse')
    ville = fields.Char("Ville")
    pays = fields.Char("Pays")
    propriete_ids = fields.One2many('real_estate_ci.propriete', 'proprietaire_id', string='Propriétés')