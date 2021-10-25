# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsitePayment(http.Controller):
    @http.route(['/covid_form'], type='http', auth="public", website=True)
    def covid_form(self, **post):
        # Pre logic if needed
        return request.render("covid19_assessment.covid_form")

    @http.route('/covid_form_submit/', type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def covid_form_submit(self, **kw):
        # Send email and return thank you page
        email = kw.get('email')
        mail_template = request.env.ref('covid19_assessment.covid_email_template')

        email_values = {
            'email_to': email
        }
        mail_template.sudo().send_mail(request.env.user.id, force_send=True, email_values=email_values)

        return request.render("covid19_assessment.covid_thank_you")
