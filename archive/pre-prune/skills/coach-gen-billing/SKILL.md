---
name: "coach-gen-billing"
description: "Issue a Coach Gen invoice and/or settle one (Kwitansi receipt + Paid row in the Coaching Payments Ledger). Use when Coach Gen asks for an invoice, a kwitansi/receipt, or says an invoice is settled/paid."
---

# Coach Gen billing: issue + settle

Arguments (any order, any wording): client, program, tier, rate type, amount, description, language, issue date, payment date, email, attn/PIC, address, invoice number to settle, note.

## Fields

ASK if missing (use AskUserQuestion, all missing ones in one call):
- Client name (issue)
- Program (5 Laws Core / Public Speaking / Introvert, or a bundle like "5 Laws Core + Public Speaking"), tier (30-Day / 90-Day), rate type (Individual / Org-Sponsored) (issue)
- Receipt language: Indonesian (id) or English (en) (settle). Check memory first: a client known not to read Indonesian gets en.

DEFAULT silently if missing:
- Amount: standard price. 30-Day: Individual 3,800,000 / Org 5,000,000. 90-Day: Individual 9,500,000 / Org 12,000,000. Upgrades or discounts: the user gives the amount; if they don't, ask.
- Issue date and payment date: today. Due date: issue + 7 days.
- Email, address, attn/PIC: blank / N/A / "Client".
- Payment method: Bank Transfer (BCA).
- Program completion: payment date + 30 or 90 days. Refund window closes: completion + 7 days.

## Upgrades and extensions
A new agreement implicitly extends the old one (e.g. 30-Day to 90-Day). For the new agreement, count program completion from the client's ORIGINAL start date: pass --start with the earlier agreement's payment date, found in the Notion ledger. Don't ask about this. Never edit the old agreement's Notion row; the newest row carries the current dates. In the new row's Notes, name the earlier invoice number and the combined total.

## Files and locations (user's Mac, Documents/Coaching Payments)
- Scripts/ : cg.py and helpers, Scripts/assets/ (logo, signature)
- Invoices/ : Coach_Gen_Invoice_<seq>.pdf (older ones: Coach_Gen_Invoice_P0127.pdf etc.)
- Kwitansi/ : Kwitansi_<seq>-INV-CGN-<ROMAN>-<YYYY>[_EN].pdf

## Numbering
NNN/INV-CGN/<roman month>/<year>, e.g. 129/INV-CGN/IX/2026. Continuous sequence, never resets. Next seq = highest number found in Invoices/ + 1. The Kwitansi reuses the invoice number.

## Steps
1. Stage the whole Scripts/ folder (and, for settle, the invoice PDF) into the cloud container. `pip install reportlab num2words pymupdf --break-system-packages` if missing. pdftotext must exist.
2. Issue: `python3 cg.py issue --seq N --client ... --program ... --tier 30|90 --rate Individual|Org-Sponsored [--amount] [--desc] [--date YYYY-MM-DD] [--email] [--attn] [--address] [--status Open|Paid] --out OUT`. Use --status Paid when settling in the same request.
3. Settle: `python3 cg.py settle --invoice PATH --lang id|en [--date] [--start YYYY-MM-DD for upgrades] [--tier-text "custom wording"] [--note "..."] --out OUT`. It prints notion_properties JSON.
4. Render each PDF to PNG and look at it before delivering.
5. SendUserFile the PDFs, then device_commit_files into Invoices/ and Kwitansi/.
6. Notion: notion-create-pages under data source 84090b70-855c-42e3-a5fd-1b875bf77e85 (Coaching Payments Ledger) with the printed properties. Only settled invoices go into Notion; there are no Pending rows.
7. Attach the Kwitansi to the Kwitansi File property. Call notion-create-file-upload with filename = the Kwitansi filename. From the cloud container, run `curl -X POST <upload_url> -H "authorization: <header value>" -F "file=@<pdf>;type=application/pdf"` and expect 200. Then call notion-update-page, command update_properties, with {"Kwitansi File": [{"type":"file_upload","file_upload":{"id":"<file_upload_id>"}}]}. api.notion.com is on the org's network allowlist. If the POST fails anyway, say so in one line and tell him to check Settings > Capabilities > Additional allowed domains. Don't fall back to the browser.

## Rules
- The signature is always stamped on the Kwitansi: anything generated here is for a closed invoice.
- Never print the materai note on the document; it lives only in the Notion Notes field.
- No em dashes anywhere.
- Total Due on the invoice is the authoritative amount, not the sum of line items.
- A bundle ("A + B") goes to Notion as Program = A, with the full bundle written in Notes.
- End with a short summary: the files made, the Notion row link(s), and any decision he needs to make.