# Rules (the Rules Refactor Plan, Phase 2)

- `inventory/`: step 6. Every rule from every source, with its tier, outputs, check type and fate. Read `inventory/INVENTORY.md`. Edit the three `.psv` files and run `python3 rules/inventory/build_inventory.py`, which checks every row and rewrites `INVENTORY.md` and `inventory.json`.
- Step 7 (the clashes) and step 8 (the merged rulebook and the five cards) build on it.

The old text of every source is in `archive/pre-prune/`. The `loc` column points at line numbers there.
