from flask import Blueprint, redirect, render_template,request, flash
from databases.models.links import Link
from peewee import DoesNotExist
import requests
encurtador =  Blueprint('encurtador', __name__)

class StatusCodeError(Exception):
    """Custom exception for handling non-200 status codes."""
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(f"Status code was {status_code}")

@encurtador.route('/', methods=['GET','POST'])
def inicial():
    return render_template('encurtador.html')


@encurtador.route('/link', methods=['POST'])
def link():
    data = request.form
    idlink = None
    linkk = data['Linkenc']
    if not linkk.startswith("https://"):
        linkk = "https://" + linkk
    else:
        pass
    try:
        linkk = linkk.strip().lower()
        link_record = Link.get(Link.link == linkk)
        idlink = link_record.id
    except:
        pass
    if idlink:
        flash(idlink, 'id')
    else:
         try:
            acessar = requests.get(url=linkk)
            if acessar.status_code != 200:
                raise StatusCodeError(acessar.status_code)
            else:
                Link.create(link=linkk)
                flash('Salvo com sucesso', 'success')
    # Link.create(link=linkk)
         except requests.exceptions.MissingSchema as e:
                flash(f"{e}", 'error')
         except StatusCodeError as e:
                flash(f"{e}", 'error')
         except requests.exceptions.RequestException as e:
                # Handle other requests exceptions if needed
                flash(f"{e}", 'error')
    return redirect('/enc/')

@encurtador.route('/<int:id>')
def linkencurtado(id):
    link1 = Link.get_by_id(id)
    return redirect(link1.link)