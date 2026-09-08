# `src/cobalt/settings/__init__.py`

## What it does
Re-exports `TraderSettings`, `TraderSettingsStore` and the key lists. The
package holds the trader's OWN settings — the sheet dollars, the enabled
grades, the reduced rung, the `.htk` template, the step-down table.

## Why it is its own module
Those settings are read by `cobalt.aset` AND `cobalt.daymode` and belong
to neither. Hanging the table off either would make the other import it
sideways for data it half-owns. They are the TRADER'S settings, so they
get the module that says so.

## The law it carries
Nothing in the runtime reads a YAML for these values.
`load_sheet_modes_config()` and `load_daymode_config()` keep their names
and their call sites; both resolve through the database.
