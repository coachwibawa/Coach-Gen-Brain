---
name: bookkeeping-automation
description: Notion + Kwitansi (Indonesian receipt) generation automation for Coach Gen's coaching payment settlement workflow
sources: [cowork]
aliases: [kwitansi automation, coaching payments ledger]
---
- [stated] Business entity: PT Gapai Bangkit Wibawa (f.s.o. Coach Gen); address Jalan Pulau Putri III no 15; email genison@coachwibawa.com; phone ID +62 815 8662 4566, SG +65 8250 9098; bank BCA, account holder Genison Bertholino Wibawa
- [stated] 3 coaching programs: 5 Laws Core, Public Speaking, Introvert; 2 tiers: 30-Day (4 sessions, Rp 3,800,000 individual / Rp 5,000,000 org-sponsored), 90-Day "Lifetime Change" (13 sessions, Rp 9,500,000 individual / Rp 12,000,000 org-sponsored); rate types Individual / Org-Sponsored
- [stated] Guarantee: full refund, 7 days after program completion, no conditions
- [stated] Notion "Coaching Payments Ledger" DB tracks invoice-to-payment lifecycle; has a Kwitansi File property (files type, newly added, empty on all rows)
- [stated] Goal workflow: point to an invoice number, mark it paid, auto-generate a filled Kwitansi matching Invoice Template branding, attach it to the Notion record
- [stated] Finalized design (Aug 31, 2026): invoice PDFs already saved in his Documents folder are the source of truth at settlement (they contain full extractable text: client, program, tier, rate type, total due). Nothing gets written to Notion until an invoice is settled; there's no Pending pre-log step
- [stated] Kwitansi numbering: reuses the invoice number directly (no separate KW- prefix)
- [stated] Materai (duty stamp) handling: generator just flags/notes it as a reminder for now, doesn't calculate or apply a threshold
- [stated] Invoice/Kwitansi numbering convention (finalized): traditional Indonesian style, NNN/INV-CGN/roman-month/year (e.g. 128/INV-CGN/VIII/2026); sequence is continuous and never resets yearly
- [stated] His existing invoices Coach_Gen_Invoice_P0127 and P0128 are retroactively folded into the new sequence as numbers 127 and 128 (not renumbered from scratch); next new invoice starts at 129. No need to rename those existing files since "127"/"128" already appear in their filenames for lookup
- [stated] He'd previously been manually renaming paid invoice files with a "_CLOSED" suffix as a stopgap before this automation existed; going forward Notion Status is the source of truth for paid/unpaid, no file renaming needed
- [stated] Doesn't want the materai/e-Meterai reminder printed on the Kwitansi document itself (called it "yapping"); it should just be tracked as an internal note instead
- [stated] Wants invoice/Kwitansi files kept organized in folders rather than left loose in the Documents root
- [stated] Client on invoice 128 (Kin Ng) doesn't read Indonesian, so that Kwitansi should be generated in English rather than the Indonesian default
- [stated] Provided a signature image (kept in Documents/Coaching Payments/Assets/Gen Signature.png) and wants it auto-stamped onto every generated Kwitansi, since any Kwitansi this pipeline generates is by definition for an already-settled invoice
- [stated] New agreements implicitly extend old ones (e.g. an upgrade from 30-Day to 90-Day): don't go back and edit the old agreement's Notion row; the newest row carries the current dates
