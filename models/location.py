from odoo import models, fields, api


class Location(models.Model):
    _name = 'real_estate_ci.location'
    _description = 'real_estate_ci.location'

    name = fields.Char('Ref')
    propriete_id = fields.Many2one('real_estate_ci.propriete', 'Propriété', help="Propriété concerner par la location")
    locataire_id = fields.Many2one('real_estate_ci.locataire', 'Locataire')
    debut = fields.Date('Date de Début')
    fin = fields.Date('Date de Début')
    note = fields.Text()
    proprietaire_id = fields.Many2one(related="propriete_id.proprietaire_id")
    statut = fields.Selection([('brouillon', 'Brouillon'), ('active', 'Active'), ('annule', 'Annulé'), ('termine', 'Terminé')], default="brouillon")
