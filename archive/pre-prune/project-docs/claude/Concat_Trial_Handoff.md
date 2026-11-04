# Concat Trial Handoff

## Start here

Install Concat (a free, open-source CapCut alternative with a built-in MCP server) on Coach Gen's Mac, connect it to the Claude desktop app, and run one small trial edit to see whether Claude can build first-cut Reel drafts for him. He gave the go-ahead for the trial on 2026-10-21.

## Where things live

- Repo and README: https://github.com/jub0t/Concat (version 0.2.8, beta, AGPL-3.0, about 10k stars).
- MCP setup doc: https://github.com/jub0t/Concat/blob/main/docs/MCP.md
- Download site: concatenate.pages.dev (or GitHub Releases on the repo).
- Developer docs (JSON-RPC and gRPC API): https://concatenate.pages.dev/docs
- Mac app binary once installed: `/Applications/Concat.app/Contents/MacOS/concat`
- Claude desktop config: Settings > Developer > Edit Config (`claude_desktop_config.json`).
- His connected Mac folder: `/Users/coachwibawa/Documents/5 Laws of Lasting Change` (has `Social Images/`).
- Instagram and Coachinator rules: `claude/Coach_Gen_Social_Posting_Rules.md` (Instagram section). Append-only.

## Done

- Read the README and MCP doc. Gave him pros and cons against CapCut.
- He decided to trial it in a fresh chat, since adding an MCP server needs a Claude app restart, which starts a new session anyway.

Key facts from the docs (verify, the app is beta):
- MCP runs over stdio. Modes: `--mcp auto` (default), `--mcp window` (connects to the open app via Settings > Automation > Scripts and apps), `--mcp headless` (runs the engine with nothing open).
- Tools include: `project_create/open/save`, `media_import`, `clip_add`, `clips_add_sequence`, `clip_trim`, `clips_split`, `title_add`, `captions_add`, `keyframe_set`, `effect_layer_add`, `template_list`, `template_instantiate`, `export_start/wait`, `preview_frame`.
- Edits stay in memory until `project_save`. The agent can't edit the project open on his screen (live mode planned, issue #337).
- Files are written only under his home folder unless `CONCAT_MCP_ROOTS` is set.
- Times in seconds; keyframe positions and sizes are fractions (0 to 1).
- Headless export is listed but not explicitly confirmed. Test it.
- No CapCut project import, no stock music or trending sounds library.

## In progress

Nothing installed yet. Waiting on the new chat to start.

## Next, in order

1. Confirm the plan with him in one short message before touching anything (he wants understanding confirmed before Claude acts).
2. Check whether his Mac is Apple silicon or Intel, then find the matching Mac build on the official release page.
3. Download: tell him the file name, source, and size first, and wait for his yes (download permission is per file). Use computer use on his Mac, not the Chrome extension, unless he says otherwise.
4. He drags Concat into Applications if the installer needs it.
5. Gatekeeper: the Mac build is unsigned, so macOS will block it. Unblocking (System Settings > Privacy & Security > Open Anyway, or the README's `xattr -dr com.apple.quarantine` command) is a security setting change: he does it himself. Claude only tells him the steps.
6. Claude config: show him the exact JSON to add, and he pastes and saves it himself:
   ```json
   "mcpServers": {
     "concat": {
       "command": "/Applications/Concat.app/Contents/MacOS/concat",
       "args": ["--mcp"]
     }
   }
   ```
   If the file already has an `mcpServers` block, the `concat` entry goes inside it.
7. He restarts the Claude app and starts a new chat linked to his Mac. Concat tools should appear as `mcp__remote-devices__concat__*` (local MCP servers are proxied through the device bridge). Not yet tested: if they don't show, report it plainly.
8. Trial edit, small: a vertical 1080x1920 project, import 2 or 3 images from `Social Images/` (or slides he exports from The Coachinator), sequence them, add one title and auto-captions on a short voice clip he provides, export, and check a `preview_frame`. Record time and tokens.
9. Report: what worked, what broke, time and tokens, and whether it's worth keeping next to CapCut. He opens the saved project himself to judge it.

## Rules for this work

- Never type passwords or sign in for him.
- Ask before every download, with file name, source, and size.
- He does any security change himself (Gatekeeper, quarantine removal, privacy permissions).
- He edits and saves the Claude config himself. Claude only supplies the exact text.
- Don't use the Chrome extension unless he asks. Confirm understanding first, then act.
- Don't edit a Concat project he has open. Save before telling him to open it.
- His writing rules still apply to anything in his voice: no em dashes, simple words.
- Keep CapCut untouched. This is a trial alongside it, not a migration.

## Suggested skills

- `anthropic-skills:computer-use`: before the first step that controls his Mac (download, opening the app).
- `anthropic-skills:chrome-browser`: only if he asks to use Chrome instead.
- `anthropic-skills:handoff`: to update this note at the end of the trial (add a dated section, never condense).
