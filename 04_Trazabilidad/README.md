# Traceability — AgroMoreira

`Matriz_Trazabilidad_v2.xlsx` contains 60 closed rows: 54 base rows (one per RF/RNF/RD in the current catalog: 39 RF + 15 RNF, transcribed from the legal-first requirements draft) plus 6 secondary rows.

## Why 60 and not 54

A requirement matrix row is not required to be 1:1 with a use case. Six requirements genuinely support a second use case beyond their primary one, and the second relationship is documented as its own row rather than silently dropped:

| RF | Primary CU | Secondary CU | Why |
|---|---|---|---|
| RF-03 | CU-02 | CU-06 | Activity/treatment history is the direct input the AI pest-alert engine analyzes. |
| RF-01 | CU-01 | CU-08 | Reports are generated per plot/lot, so plot identification data feeds reporting. |
| RF-04 | CU-03 | CU-08 | Production reports are built from registered harvest records. |
| RF-07 | CU-05 | CU-04 | The cost of inputs used is an expense that feeds the net-profit calculation. |
| RF-11 | CU-07 | CU-05 | Spraying/application tasks consume inventory inputs. |
| RF-29 | CU-01 | CU-08 | Full plot history is itself a report-type view. |

## Column rules

- **ID-CU**: from the RF→CU table in Section 3 of the modeling guide.
- **ID-HU / ID-CA**: filled only for RF marked Must-have that carry a dedicated user story (see `03_Modelado/00_User_Stories_Acceptance_Criteria.md`); all other rows show `N/A`.
- **ID-Component**: from `03_Modelado/Diagrams/COMP01_Component_Diagram.drawio`.
- **ID-Mockup**: from the 9 mockups in `03_Modelado/Mockups/` (MU-01 to MU-09) plus the general prototype `MU-00_Prototype.html`.

## Coverage note

Every CU in the current scope (CU-01 to CU-14) now has at least one component and one mockup reference — CU-10 (Technical Visits), CU-11 (Occupational Risk & PPE), CU-12 (Quick Report Channel), CU-13 (BPA Compliance) and CU-14 (Quarantine Pest Notice) are covered by the Technician-facing `MU-09_Compliance_Technical_Visits` screen and by `ComplianceModule` in the component diagram, closing the gap that existed in the earlier draft (where these CUs showed "pending, no dedicated mockup"). CU-15 (sensor integration, RF-32) stays `N/A` — it is a documented Won't-have.

This matrix is built as "model first, MVP afterward": the prototype in `03_Modelado/Mockups/` and the MVP to be implemented next must stay consistent with these 60 rows, not the other way around.
