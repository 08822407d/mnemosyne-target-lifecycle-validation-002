def beta_feature(value: str) -> str:
    return f"beta:{value}"


def sort_invoices(invoices):
    return sorted(invoices, key=lambda item: (item["due_date"], item["invoice_id"]))
