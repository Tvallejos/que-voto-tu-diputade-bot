from typing import Dict
import logging


def bold(msg: str):
    return f'<b>{msg}</b>'


def string_of_vote(v: Dict, info: bool):
    extra = ""
    if info:
        extra += "\ninformación extra:\n"
        extra += f"articulo: {v['articulo']}\n"
        extra += f"tramite: {v['tramite']}\n"
        extra += f"tipo de votacion: {v['tipo de votacion']}\n"
        extra += f"quorum: {v['quorum']}\n"
    vg = v['voto_general']
    sv = f"{v['diputade']} votó { bold(v['voto']) }\n"
    sv += f"en {v['name']} {v['sesion']}\n"
    sv += f"Resultado: {bold(v['resultado']) }\n"
    sv += f"Materia: {v['materia']}\n"
    sv += f"Votacion general: a favor: {vg['a favor']} "
    sv += f"| en contra: {vg['en contra']} | abstencion: "
    sv += f"{vg['abstencion']} | dispensados: {vg['dispensados']}"""
    if info:
        sv += extra

    logging.debug(f'vote string: {sv}')
    return sv
