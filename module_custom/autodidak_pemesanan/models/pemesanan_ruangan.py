from datetime import date
from odoo import models, fields, api, exceptions


class pemesanan_ruangan(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    booking_number = fields.Char(string='Nomor Pemesanan', required=True, readonly=True, copy=False,
                                 default=lambda self: self._generate_booking_number())
    room_id = fields.Many2one('my_module.master_ruangan', string='Ruangan', required=True)
    booking_name = fields.Char(string='Nama Pemesanan', required=True, unique=True)
    booking_date = fields.Date(string='Tanggal Pemesanan', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('on_going', 'On Going'),
        ('done', 'Done')
    ], string='Status Pemesanan', default='draft')
    notes = fields.Text(string='Catatan Pemesanan')

    _sql_constraints = [
        ('unique_booking_name', 'UNIQUE(booking_name)', 'Nama Pemesanan tidak boleh sama.')
    ]

    @api.model
    def _generate_booking_number(self):
        room_type = self.room_id.room_type if self.room_id else 'unknown'
        today_str = date.today().strftime('%Y%m%d')
        sequence = self.env['ir.sequence'].next_by_code('pemesanan.ruangan.sequence') or '0001'
        booking_number = f"{room_type}/{today_str}/{sequence}"
        return booking_number

    @api.constrains('room_id', 'booking_date')
    def _check_booking_conflict(self):
        for record in self:
            conflicts = self.search([
                ('room_id', '=', record.room_id.id),
                ('booking_date', '=', record.booking_date),
                ('id', '!=', record.id)
            ])
            if conflicts:
                raise exceptions.ValidationError("Tidak boleh memesan ruangan dan tanggal pemesanan yang sama.")

    def action_proses_pemesanan(self):
        for record in self:
            if record.status == 'draft':
                record.status = 'on_going'
            elif record.status == 'on_going':
                record.status = 'done'
