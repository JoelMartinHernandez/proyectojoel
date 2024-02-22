# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RegistroCreacionEmpresa(models.Model):
    _name = 'proyectojoel.registro_creacion_empresa'
    _description = 'Registro de Creación de Empresas'

    user = fields.Char(string='Usuario')
    empresaName = fields.Char(string='Empresa')
    fecha = fields.Datetime(string='Fecha/Hora', default=fields.Datetime.now)
    tipo_accion = fields.Char(string='Accion')



class proyectojoel_empresas_contratadoras(models.Model):
     _name = 'proyectojoel.empresas_contratadoras'
     _description = 'proyectojoel.empresas_contratadoras'

     name = fields.Char(string="Empresa contratada")
     email = fields.Char(string="Correo electronico")
     phone = fields.Integer(string="Número de Teléfono")
     project = fields.One2many("project.project","empresas",string="Proyectos")
     numero_empleados = fields.Integer(string="Número de empleados")
     tam_empresa = fields.Char(string="Tamaño de la empresa",compute="_tamempresa",store=True)
     show_task = fields.Boolean(string= "Mostrar tareas", default=lambda self: self._get_show_task())
     dropdown_field = fields.Char(string= "Dropdown Field", default=lambda self: self._get_dropdown_field())

     def _get_show_task(self):
          param = self.env['ir.config_parameter'].sudo().get_param('proyectojoel.show_task')
          return param.lower() == 'true' if param else False
     
     def _get_dropdown_field(self):
          param = self.env['ir.config_parameter'].sudo().get_param('proyectojoel.dropdown_field')
          return param
          

     @api.depends('numero_empleados')
     def _tamempresa(self):
          for r in self:
               if r.numero_empleados > 0:
                    r.tam_empresa = 'Pequeña'
               if r.numero_empleados > 50:
                    r.tam_empresa = 'Mediana'
               if r.numero_empleados > 100:
                    r.tam_empresa = 'Grande'

     @api.model
     def create(self, values):
        res = super(proyectojoel_empresas_contratadoras, self).create(values)

        # Crear registro de creación de empresa
        nuevo1 = self.env['proyectojoel.registro_creacion_empresa'].create({
            'user': self.env.user.name,
            'empresaName': res.name,
            'tipo_accion': 'creacion',
        })
        return res 

     def write(self, values):
        res = super(proyectojoel_empresas_contratadoras, self).write(values)

        # Crear registro de creación de empresa
        nuevo2 = self.env['proyectojoel.registro_creacion_empresa'].create({
            'user': self.env.user.name,
            'empresaName': self.name,
            'tipo_accion': 'modificacion',
        })
        return res 

     
class proyectojoel_proyectos(models.Model):
     _name = 'project.project'
     _inherit = "project.project"

     empresas = fields.Many2one("proyectojoel.empresas_contratadoras",string="Nombre de la empresa",required=True,ondelete="cascade")

class proyectojoel_tareas(models.Model):
     _name = 'project.task'
     _inherit = "project.task"

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_task = fields.Boolean(string='ver tareas', config_parameter="proyectojoel.show_task")
    dropdown_field = fields.Selection([
        ('America', 'America'),
        ('España', 'España'),
        ('España 2', 'España 2'),
    ], string='Dropdown Field', config_parameter="proyectojoel.dropdown_field")

