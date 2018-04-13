# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

class WorkTypeWebDirectory(models.Model):

    _name = "worktype"
    _description = "Budget Work Type"
    
    name = fields.Char(string="Name")
    interest_category_id = fields.Many2one('res.partner.category')
    description = fields.Text(string="Description")

		
class BudgetWebDirectory(models.Model):

    _name = "budget"
    _description = "Budgets"
    
    partner_id = fields.Many2one('res.partner', string="Partner Budgets")
    name = fields.Char(
        'Number', default=lambda self: self.env['ir.sequence'].next_by_code('budget.code.serial'),
        required=True, readonly=True, help="Unique Process/Serial Number")
    work_type = fields.Many2one('worktype', string="Budget work type")
    country_id = fields.Many2one('res.country', string='Country', required=True)
    state_id = fields.Many2one('res.country.state', string="State", domain="[('country_id', '=', country_id)]")
    city = fields.Char(string="City")
    description = fields.Text(string="Description")
    min_price = fields.Float(string="Minimum Price")
    max_price = fields.Float(string="Maximum Price")



class ProposalWebDirectory(models.Model):

    _name = "proposal"
    _description = "Budgets Proposals"

    budget_id = fields.Many2one('budget', string="Budgets Proposals")
    partner_id = fields.Many2one('res.partner', string="Partner Budgets")
    description = fields.Text(string="Description")
    status = fields.Selection((('draft','Draft'), ('rejected','Rejected'), ('accepted','Accepted'), ('confirmed','Confirmed')),'Status' )
    exp_start_date = fields.Date(string="Expected start date")
    

    
	