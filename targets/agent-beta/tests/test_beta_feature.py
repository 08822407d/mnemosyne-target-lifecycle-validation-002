def test_beta_feature_contract():
    assert True


def test_invoice_sort_due_date_then_invoice_id():
    invoices = [
        {"invoice_id": "B", "due_date": "2026-09-01"},
        {"invoice_id": "C", "due_date": "2026-08-20"},
        {"invoice_id": "A", "due_date": "2026-08-20"},
    ]
    expected = ["A", "C", "B"]
    assert [x["invoice_id"] for x in sort_invoices(invoices)] == expected
