from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches


def FormatDocument(NewInfo):
    try:
        doc = DocxTemplate('./docs/Plantilla.docx')
        context = {
            'motivo' : NewInfo.Motivo,
            'date' : NewInfo.Date,
            'hora' : NewInfo.Hora,
            'Integrantes' : NewInfo.Integrantes,
            'project' : NewInfo.Project,
            'orden_dia' : NewInfo.Orden_dia,
            'desarrollo_reunion' : NewInfo.Desarrollo_reunion,
            'Compromisos' : NewInfo.Compromisos,
            'Firmas' : NewInfo.Firmas
        }
        doc.render(context)
        path ='./docs/%i/PT-AR-01-ActaReunion_%i.docx' % (NewInfo.Project,NewInfo.date)
        doc.save(path)
        return {'Succes' : True, 'path' : path}

    except Exception:
        return False


# Integrantes = [
#         {
#             'Nombre' : 'Integrante1',
#             'Cargo' : 'Cargo1'
#         },
#         {
#             'Nombre' : 'Integrante2',
#             'Cargo' : 'Cargo2'
#         }
#     ]

# Compromisos = [
#         {
#             'Actividad' : 'Una actividad',
#             'Responsable' : 'Persona 1',
#             'FechaEntrega' : '01/02/2023',
#             'Estado' : 'Pendiente'
#         },
#         {
#             'Actividad' : 'Una actividad 2',
#             'Responsable' : 'Persona 2 3',
#             'FechaEntrega' : '01/12/2023',
#             'Estado' : 'Entregado'
#         },
#         {
#             'Actividad' : 'Una actividad 3',
#             'Responsable' : 'Persona 3',
#             'FechaEntrega' : '21/04/2023',
#             'Estado' : 'Pendiente'
#         }
#     ]

# Firmas = [
#     {
#         'Nombre' : 'Moisés Pineda',
#         'Img' : InlineImage(doc,'./docs/Firmas/MiLogoYo.png', width=Inches(2), height=Inches(2))
#     }
# ]

