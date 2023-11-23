from odoo import models, fields, api


class TypeDePropriete(models.Model):
    _name = 'real_estate_ci.type.propriete'
    _description = 'real_estate_ci.type.propriete'

    name = fields.Char('Nom')
    description = fields.Text('Description')
    propriete_ids = fields.One2many('real_estate_ci.propriete', 'type_id', string='Propriétés')