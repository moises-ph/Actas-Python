from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches

doc = DocxTemplate('./docs/Plantilla.docx')

Integrantes = [
        {
            'Nombre' : 'Integrante1',
            'Cargo' : 'Cargo1'
        },
        {
            'Nombre' : 'Integrante2',
            'Cargo' : 'Cargo2'
        }
    ]

Compromisos = [
        {
            'Actividad' : 'Una actividad',
            'Responsable' : 'Persona 1',
            'FechaEntrega' : '01/02/2023',
            'Estado' : 'Pendiente'
        },
        {
            'Actividad' : 'Una actividad 2',
            'Responsable' : 'Persona 2 3',
            'FechaEntrega' : '01/12/2023',
            'Estado' : 'Entregado'
        },
        {
            'Actividad' : 'Una actividad 3',
            'Responsable' : 'Persona 3',
            'FechaEntrega' : '21/04/2023',
            'Estado' : 'Pendiente'
        }
    ]

Firmas = [
    {
        'Nombre' : 'Moisés Pineda',
        'Img' : InlineImage(doc,'./docs/Firmas/MiLogoYo.png', width=Inches(2), height=Inches(2))
    }
]

context = {
    'motivo' : "El motivo",
    'date' : "01/01/2005",
    'hora' : "12:37",
    'Integrantes' : Integrantes,
    'project' : "Nodens",
    'orden_dia' : 'Terminar esto',
    'desarrollo_reunion' : 'Desarrollo',
    'Compromisos' : Compromisos,
    'Firmas' : Firmas
}

doc.render(context)
doc.save('output.docx')