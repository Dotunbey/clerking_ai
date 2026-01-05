from drafting.templates import PEDIATRIC_TEMPLATE

def generate_draft(entities: dict, domain="pediatrics") -> str:
    complaints = "\n".join(
        f"- {c}" for c in entities.get("complaints", [])
    )

    return PEDIATRIC_TEMPLATE.format(
        age=entities.get("age", ""),
        sex=entities.get("sex", ""),
        complaints=complaints
    )
