# Modeling Package — AgroMoreira (English, individual files)

This package replaces the earlier Spanish, multi-page draft. Every diagram is now an **individual `.drawio` file** (one `<diagram>` per file — no internal tabs), in **English**, in the **same visual style, color palette and shape conventions** as the 16 original reference diagrams the team had already produced (BCE-layered sequence diagrams with UML `alt` fragments and activation bars, swimlane activity diagrams, the `light-dark(...)` color palette). Every diagram also ships as a PNG image in `Images/`, generated directly from the `.drawio` source so the two never drift apart.

## What changed vs. the 16 original diagrams

The 16 original diagrams (AD01-03, CD01, COMP01, DEP01, SD01, SEQ01-09) were built for an earlier phase of the project: 2 actors only (Administrator, Farmworker), an older RF numbering (~RF-01 to RF-16), and a domain model with no legal/compliance entities. They are kept as the **format template** — their layout and style are unchanged — but every RF/UC reference inside them was corrected to the **current** catalog (39 RF + 15 RNF, CU-01 to CU-14), and the component/deployment diagrams were extended with a `ComplianceModule` and an AGROCALIDAD external system node.

16 new diagrams were added, in the same style, to cover what the originals didn't: the Technician and AGROCALIDAD actors, the AI System actor, and the LOPDP/AGROCALIDAD legal-compliance domain (consent, ARCO+ rights, technical visits, occupational risk, quarantine-pest notice, BPA compliance).

## Diagram index (`Diagrams/`, 32 files)

| File | Type | Covers |
|---|---|---|
| CTX01_Context_Diagram | Context | All actors ↔ system |
| CTX02_Power_Interest_Matrix | Stakeholder matrix | All stakeholders |
| ISTAR01_Strategic_Dependency_SD | i* SD | All actors |
| ISTAR02_Strategic_Rationale_SR | i* SR | Administrator |
| UC01_General_Use_Case_Diagram | Use case | CU-01 to CU-14, 5 actors |
| CD01_Refined_Class_Diagram | Class (updated) | Core operational domain |
| CD02_Legal_Compliance_Class_Diagram | Class (new) | LOPDP/AGROCALIDAD domain |
| AD01-03 | Activity (updated) | CU-02/03/05/06/07/08 |
| AD04-07 | Activity (new) | CU-09, CU-10/13, CU-11, CU-14 |
| SEQ01-09 | Sequence (updated) | CU-01, CU-02, CU-03, CU-05, CU-04, CU-07, CU-09 |
| SEQ10-14 | Sequence (new) | CU-09 (consent, ARCO+), CU-06 (confirm/discard/disagree), CU-10, CU-14 |
| SD01 | State (updated) | CU-07 (task lifecycle) |
| SD02 | State (new) | CU-06 (AI alert lifecycle) |
| COMP01 | Component (updated) | Full architecture incl. ComplianceModule |
| DEP01 | Deployment (updated) | Full deployment incl. AGROCALIDAD node |

## Mockups (`Mockups/`, 9 individual screens + 1 general prototype)

`MU-01` to `MU-09`, one HTML file per screen, each self-contained and each also exported to `Mockups/Images/*.png`. `MU-00_Prototype.html` is the general entry point: a clickable shell (sidebar + phone-frame stage) that links every individual screen together, so it can be opened and clicked through as *the* prototype without needing all 9 files pre-loaded in the reviewer's head.

## Supporting text

- `00_Use_Case_Specifications.md` — full textual spec for CU-01 to CU-14 (English).
- `00_User_Stories_Acceptance_Criteria.md` — Gherkin HU/CA for the Must-have RF that carry one (English).

## Traceability

See `../04_Trazabilidad/Matriz_Trazabilidad_v2.csv` and its README — 60 closed rows, all IDs in this package (CU, Component, Mockup) match the matrix exactly.

## Regenerating

Everything here is produced from Python scripts using `gen_lib.py` (diagram builder matching the reference style) and `render_drawio.py` / `render_mockups.py` (Playwright-based PNG export), so the whole package can be rebuilt deterministically if requirement text changes again.
