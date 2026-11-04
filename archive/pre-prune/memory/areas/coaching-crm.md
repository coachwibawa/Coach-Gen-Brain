---
name: coaching-crm
description: Notion CRM and integration stack for coaching client management
sources: [backfill]
aliases: [project-rebirth, "80/20 client relations"]
---
- [stated] Uses a Notion CRM ("Project Rebirth: 80/20 client relations")
- [stated] Notion CRM DB ID: 34ff1e0ae9c38008b7fef283bdeab4b3
- [stated] Notion CRM data source: 34ff1e0a-e9c3-80a7-b687-000bb126e7a0
- [stated] Pipeline stages: Intake → Triage → Submarine → Coaching
- [stated] WA JID linking method: search unique sent message → extract @lid JID → write to "WA JID" field in Notion
- [stated] Voice & Memory Notion page: https://www.notion.so/35af1e0ae9c3817aa69af3dcfc7b4815 — fetch as Step 0 in all cron/API calls
- [stated] Drafting voice: warm but direct, casual Indonesian register (uses "nih", "tadi"), not afraid to reach out, "I'm valuable, it's their loss" Sandler posture
- [stated] Draft flow: sent / skip / edit → update Notion Last Contact Date
- [stated] Uses WhatsApp MCP bridge (natigravity), runs locally on Mac
- [stated] Uses Make.com for scheduled automation
- [stated] Uses a Supabase + Resend email stack
- [stated] Codes in Antigravity IDE
- [stated] natigravity known issue: sync_contacts returns empty; link_contact_by_message Notion side returns 404 — use Claude's native Notion connector instead
- [stated] Overall lead funnel is roughly: website → assessment → Supabase → email → CRM → newsletter (his words: "not my fullstack but close")
- [stated] CRM (Project Rebirth) is currently stale (no client contact logged in 3.5+ months) because he's been focused on building out the new "5 Laws of Lasting Change" framework instead
