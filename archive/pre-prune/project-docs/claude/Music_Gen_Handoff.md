# Music Generation Handoff (open-source AI music on Gen's gaming PC)

Written 3 Nov 2026.

## Start here
Install an open-source music model on Gen's gaming PC (NVIDIA GPU), generate a few calm background tracks with commercial rights, and put them where the video pipeline can use them.

## Where things live
- Video pipeline: `claude/Video_Pipeline.md` (section "Background music (planned 1 Nov 2026)") and code `claude/cg_video_build.py`. Music is not built into the code yet: spec keys `music` and `music_db` are planned only.
- Brand video rules: `brand/10_VIDEO.md` v1.2, section 8 (music line marked PLANNED).
- Video work on the Mac: `Desktop/ClaudeConcat/`. The Mac render workspace is `$HOME/cgr` in the Mac shell (build.py, specs R1 to R4, Full).
- Planned track folder: `Documents/5 Laws of Lasting Change/Brand/Music/` (does not exist yet; create it).

## Done
- Research summary (1 Nov 2026, from memory, not verified this session): ACE-Step (said to be Apache 2.0, full instrumental tracks, NVIDIA GPU with about 8 GB or more of video memory) is the first pick. Stable Audio Open (commercial use under a revenue limit, clips up to about 47 s, gated download on Hugging Face) is the second. MusicGen weights are non-commercial only: do not use.
  - Update 3 Nov 2026: superseded by the verified licence check below. The current version is ACE-Step 1.5 (MIT), and Stable Audio 3.0 replaces Stable Audio Open as the second pick.
- Gen decided against paid stock libraries for now and wants to try his own GPU first.
- Paid Suno is the fallback (commercial use only for songs made on a paid plan).
- Step 1 done (3 Nov 2026): the PC is linked to Claude as device "genisonspc", Windows 64-bit. GPU: NVIDIA RTX 3060 (Gen confirmed). VRAM not yet confirmed: most desktop 3060s have 12 GB, a rarer version has 8 GB. Either works for ACE-Step 1.5. Exact Windows version (10 or 11) not checked yet.
- Step 2 done (3 Nov 2026): licence check, see "Licence check" below.

## Licence check (3 Nov 2026, verified from official sources)

### ACE-Step 1.5 (first pick, cleared)
- Repo: https://github.com/ace-step/ACE-Step-1.5 . Repo licence: MIT (LICENSE file and README "License & Disclaimer" section). Co-led by ACE Studio and StepFun.
- Model card: https://huggingface.co/ACE-Step/Ace-Step1.5 . Model licence: MIT. The model card states generated music may be used for commercial purposes and that training data is licensed, royalty-free or synthetic.
- Caveat: an open GitHub discussion (#1256, https://github.com/ace-step/ACE-Step-1.5/discussions/1256) asks the team for a separate written statement on output terms. Unanswered as of 3 Nov 2026. The README asks users to check originality and disclose AI involvement. Neither changes the MIT grant.
- Note: the older ACE-Step v1 (https://github.com/ace-step/ACE-Step) was Apache 2.0. Use 1.5, not v1.
- Fit for the RTX 3060: README table puts 8 to 16 GB cards on the 2B turbo or sft model with the 0.6B planner model (8 to 12 GB) or 1.7B (12 to 16 GB). The UI picks the setting for the card automatically. XL models need 12 GB with offload, so they are a stretch on a 12 GB 3060 and out on an 8 GB one.
- Length: 10 s to 10 min per track. Instrumental is supported. Speed: under 10 s per full song on an RTX 3090, so a 3060 should take well under a minute.
- Windows install options: (a) portable package with everything pre-installed, linked from the README (files.acemusic.ai, ACE-Step-1.5.7z), started with `start_gradio_ui.bat`. (b) uv: `git clone`, `uv sync`, `uv run acestep`. Models download on first run. UI opens at http://localhost:7860. Needs Python 3.11 to 3.12 for option (b).

### Stable Audio 3.0 (second pick, cleared for Gen's size)
- Released 20 May 2026. Open weights for Small (459M, tracks up to 2 min), Small SFX (sound effects) and Medium (1.4B, tracks up to 6:20). Large is API only. Source: https://the-decoder.com/stability-ai-launches-stable-audio-3-0-with-up-to-six-minute-tracks-and-open-weights/
- Licence: Stability AI Community License. Users own generated audio and may use it commercially. Organisations above USD 1 million annual revenue need an Enterprise licence. Trained on licensed data. Instrumental and sound effects only (no vocals), which matches our rule.
- Stability's own licensing explainer: https://stability.ai/explainers/stable-audio-vs-competitors-licensing-export-rights-and-self-hosting-compared
- The old Stable Audio Open 1.0 (47 s clips, https://huggingface.co/stabilityai/stable-audio-open-1.0) is superseded. Skip it.
- Hugging Face download is likely gated (login and accept terms). Gen does that himself. Not installed, not needed unless ACE-Step disappoints.

### Still ruled out
- MusicGen: non-commercial weights.

## In progress
Nothing installed yet. The gaming PC is not linked to any Claude session. This chat's session is linked to the Mac only.
- Update 3 Nov 2026: the PC is now linked (device "genisonspc"). Steps 1 and 2 done. Next is step 3. Note: Claude's shell on the PC runs in a Linux sandbox and cannot see the GPU or install Windows software, so step 3 is done either by Gen running the portable package or by Claude driving the PC with computer use.

## Next, in order
1. Check what the PC is: ask Gen for the GPU model and its video memory (VRAM), and the Windows version, or read it if the PC is linked. To link: open the Claude desktop app on the PC and start or link the chat to that computer. (Done 3 Nov 2026: RTX 3060.)
2. Verify licences before installing: open the current ACE-Step repository and model card and confirm the licence allows commercial use. Do the same for Stable Audio Open if used. Write what you found into this doc with links. (Done 3 Nov 2026, see "Licence check".)
3. Install ACE-Step following its own README (Python, PyTorch with CUDA for his card, the model download). Keep it in its own folder, for example `C:\AI\ACE-Step`. (Use ACE-Step 1.5. Portable package is the simplest route on Windows.)
4. Generate test tracks, instrumental only, 60 to 90 s, 3 or 4 takes per prompt:
   - "Cinematic ambient piano, slow, hopeful, soft strings swell, no drums, no vocals, 70 bpm"
   - "Minimal inspirational underscore, warm pads, gentle piano motif, slow build, no percussion, instrumental"
   - "Calm documentary background, felt piano, airy synth pad, reflective, steady, instrumental"
5. Gen picks 2 or 3 favourites by ear. Save them as wav or high-bitrate mp3 into `Documents/5 Laws of Lasting Change/Brand/Music/` with simple names (for example `calm_piano_01.wav`) plus a `LICENCE.txt` noting the model, its licence, date and prompt.
6. Hand back to the video work: add the `music` and `music_db` spec keys to build.py (sidechain ducking under the voice, start about -22 dB under the voice, 1 s fade in, 2 s fade out, loop if short), then a blind level test on The Marathon Reel (2 or 3 levels, loudness matched, random labels, key file), checked on a phone speaker.

## Rules for this work
- Commercial rights only. No model or track with a non-commercial licence.
- Instrumental only. No vocals.
- Very low in the mix: Gen wants "just enough to rouse a hey there's sounds instinct".
- Blind tests for anything Gen picks by ear: one difference only, loudness matched, random labels, key in a file, never reveal before he picks.
- Never type passwords or tokens for him. If Hugging Face needs a login or token (Stable Audio Open), he enters it himself.
- No em dashes in his documents.

## Suggested skills
- `anthropic-skills:autopilot-video-edit` when adding music to the pipeline (step 6).
- `anthropic-skills:computer-use` if the work is done by driving apps on the PC.
- `anthropic-skills:pick-model` if he asks which model or effort to use. Install and setup: Sonnet, medium. Picking music: his ears.
