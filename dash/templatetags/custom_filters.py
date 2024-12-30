from django import template

register = template.Library()

@register.filter
def format_money(value):
    """Formata um número para exibição como moeda com ponto como separador de milhar e duas casas decimais."""
    if value is None:
        return ""
    try:
        return f"R${value:,.3f}".replace(",", ".")
    except (ValueError, TypeError):
        return value
