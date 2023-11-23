from odoo import models, fields, api


class Propriete(models.Model):
    _name = 'real_estate_ci.propriete'
    _description = 'real_estate_ci.propriete'

    name = fields.Char('Nom')
    adresse = fields.Text('Adresse')
    ville = fields.Char("Ville")
    pays = fields.Char("Pays")
    type_id = fields.Many2one('real_estate_ci.type.propriete', 'Type de Propriété')
    proprietaire_id = fields.Many2one('real_estate_ci.proprietaire', 'Propriétaire')
    location_ids = fields.One2many('real_estate_ci.location', 'propriete_id', string='Propriétés')