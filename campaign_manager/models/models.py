# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class campaign_manager(models.Model):
#     _name = 'campaign_manager.campaign_manager'
#     _description = 'campaign_manager.campaign_manager'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, api, fields

class personaje(models.Model):
    _name = 'campaign_manager.personaje'
    _descripcion = 'Detalles de un personaje, raza, clase, etc...'

    name = fields.Char(string = 'Nombre del Personaje', required = True)
    ancestry = fields.Char(string = 'Ascendencia', required = True)
    lvl = fields.Integer(int = 'Nivel del personaje', required = True)
    clase = fields.Char(string = 'clase del personaje', required = False)
    subclass = fields.Char(string = 'Subclase del personaje', required = False)

    jugador_id = fields.Many2one('campaign_manager.jugador', 'personaje_ids', String = 'Propietario')

class jugador(models.Model):
    _name = 'campaign_manager.jugador'
    _description = 'Detalles del jugador'

    name = fields.Char(string = 'Nombre del jugador', required = True)
    mail = fields.Char(string = 'correo de contacto del jugadror', required = True)

    #coleccion de personajesç
    personaje_ids = fields.One2many('campaign_manager.personaje', 'jugador_id', String = 'Lista de Personajes')
    campana_ids = fields.Many2many('campaign_manager.campana', String = 'Campañas en las que se participa')

class campana(models.Model):
    _name = 'campaign_manager.campana'
    _descripcion = 'Detalles de la campaña'

    name = fields.Char(string = 'Titulo de la campaña', required = True)
    fechaInicio = fields.Date(string = 'Fecha de inicio de la campaña', required = False)
    numSesionesAprox = fields.Integer('Numero de sesiones de duracion', required = True, default = 1)
    numSesionesJugadas = fields.Integer('Numero de sesiones jugadas', default = 0)
    numSesionesRestantes = fields.Integer('Numero de sesiones restantes', compute = '_get_restantes')
    terminada = fields.Boolean('Ha terminado la campaña?', default = False, compute = '_get_finished')

    #coleccion de jugadores
    jugador_ids = fields.Many2many('campaign_manager.jugador', String = 'Participantes')

    @api.depends('numSesionesJugadas', 'numSesionesAprox')
    def _get_restantes (self):
        for campana in self:
            campana.numSesionesRestantes = campana.numSesionesAprox - campana.numSesionesJugadas

    @api.depends('numSesionesJugadas', 'numSesionesAprox')
    def _get_finished(self):
        for campana in self:
            campana.terminada = campana.numSesionesRestantes == 0