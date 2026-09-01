# User Stories and Acceptance Criteria — AgroMoreira

Gherkin-style acceptance criteria for the Must-have RF that carry a dedicated user story, per the modeling guide's rule (only Must-have RF get an HU + CA pair). English versions of the 17 stories from the original draft, plus 3 new ones (HU-18, HU-21, HU-25) added to cover the Technician/compliance scope built out in this delivery.

---

**HU-01** (RF-01) — *As an Administrator, Technician or Farmworker, I want to register and manage plots/lots so that the farm's spatial inventory stays accurate.*
- CA-01.1: Given the 7 required fields are filled in, When I save a new plot, Then it appears in the general listing in under 2 seconds.

**HU-03** (RF-03) — *As a Farmworker or Technician, I want to register agricultural activities so that every plot keeps a full operational history.*
- CA-03.1: Given date, plot and worker are provided, When I save an activity, Then it is linked to the plot's history immediately.

**HU-04** (RF-04) — *As a Farmworker, I want to register harvest using the crop's own unit so that production data stays consistent.*
- CA-04.1: Given a crop with a defined unit, When I register a harvest in a different unit, Then the system rejects the record.

**HU-05** (RF-05) — *As an Administrator, Technician or Farmworker, I want to see yield per plot and period so that I can compare performance over time.*
- CA-05.1: Given fewer than 2 harvest records exist for a plot, When I open its yield report, Then the system shows "insufficient data" instead of an average.

**HU-06** (RF-06) — *As a Technician or Farmworker, I want net profit calculated automatically so that I don't have to do manual bookkeeping.*
- CA-06.1: Given income and expense records exist for a period, When I open the financial module, Then net profit equals income minus expenses exactly.

**HU-07** (RF-07) — *As an Administrator, Technician or Farmworker, I want to manage input inventory so that stock levels are always accurate.*
- CA-07.1: Given an input's stock is updated after use, When I check the inventory module, Then the available quantity reflects the deduction immediately.

**HU-08** (RF-08) — *As an Administrator, Technician or Farmworker, I want to be alerted when input stock is low so that I can reorder in time.*
- CA-08.1: Given stock drops below the configured threshold, When the check runs, Then the responsible user is notified within 5 minutes.

**HU-09** (RF-09) — *As an Administrator, Technician or Farmworker, I want AI-generated pest alerts with human verification so that I never act on an unverified suggestion.*
- CA-09.1: Given the AI generates a pest suggestion, When it is shown to me, Then it must display a justification (max. 60 words) and a data source, and must not be applied automatically.

**HU-11** (RF-11) — *As an Administrator, Technician or Farmworker, I want to assign and track tasks by status so that field work is coordinated.*
- CA-11.1: Given a task exists in one of the 4 states, When I filter by that state, Then only tasks in that exact state are shown, for the selected plot/worker.

**HU-19** (RF-19) — *As an Administrator or Technician, I want to generate reports with charts so that I can review farm performance visually.*
- CA-19.1: Given data exists in the selected date range, When I generate a report, Then the totals shown match exactly the sum of the underlying records.

**HU-20** (RF-20) — *As any user, I want role-based access control so that I only see the functions relevant to my role.*
- CA-20.1: Given a user with the "farmworker" role, When they try to open the financial module, Then access is denied.

**HU-21** (RF-21) — *As a Technician, I want to register periodic technical visits so that plot compliance status stays evidenced over time.*
- CA-21.1: Given a technical visit is registered with findings, When non-compliance is marked, Then the system prompts to link a training record or PPE registration.

**HU-22** (RF-22) — *As any user, I want to give explicit consent for personal-data processing so that my data is handled per LOPDP Art. 8.*
- CA-22.1: Given it is my first login, When the system shows the data-processing notice, Then I cannot access any module until I explicitly accept or reject it.

**HU-23** (RF-23) — *As a Farmworker, I want to exercise my ARCO+ rights (access, rectification, cancellation, opposition) so that I retain control over my personal data (LOPDP Art. 13-19).*
- CA-23.1: Given I submit an ARCO+ request, When it is received, Then the system logs it with a tracking status and processes it within the legal term.

**HU-18** (RF-18) — *As a Technician, I want to register occupational risk and suggested PPE per plot so that workers are warned before starting risky tasks.*
- CA-18.1: Given a plot has a registered occupational risk, When a task on that plot is assigned, Then the worker sees the PPE warning before the assignment can be confirmed.

**HU-25** (RF-25) — *As an Administrator, I want to request/renew BPA certification before AGROCALIDAD so that the farm's compliance status stays valid (Res. AGROCALIDAD 183, Art. 39-43).*
- CA-25.1: Given required training records are missing, When I request certification renewal, Then the system blocks the request until the missing training is registered.

**HU-17** (RF-17) — *As a Farmworker, I want a quick chat/voice report channel so that I can flag a field situation without filling in structured fields.*
- CA-17.1: Given I submit a quick report (text or voice), When it is saved, Then it is flagged for Technician review/triage without requiring any other field to be completed first.

**HU-26** (RF-26) — *As a Technician or Farmworker, I want to register manual income/expenses so that occasional transactions outside automatic tracking are captured.*
- CA-26.1: Given I register a manual income or expense with concept, amount, date and type, When I save it, Then it is reflected in the next net-profit calculation.

**HU-34** (RF-34) — *As a Technician, I want configurable attributes per crop variety so that data-entry forms match the crop being registered.*
- CA-34.1: Given a variety has a defined attribute set, When I create a plot with that variety, Then only that variety's fields are shown on the form.

**HU-37** (RF-37) — *As a Farmworker, Technician or Administrator, I want to raise a notice for suspected quarantine-pest symptoms so that AGROCALIDAD's mandatory reporting duty is met (Res. AGROCALIDAD 0072, Art. 3.6.1.a).*
- CA-37.1: Given a Technician confirms the suspected symptom, When the notice is finalized, Then it becomes available for formal submission to AGROCALIDAD and is never auto-sent without that confirmation.

**HU-24-38** (RF-24 + RF-38) — *As an Administrator, I want worker health certificates and a biosecurity entry/exit log so that the farm meets Res. AGROCALIDAD 183 Art. 33-34 and Res. 0072 Art. 3.6.1.d.*
- CA-24-38.1: Given a technical visit or quarantine-pest notice is registered, When the event is logged, Then a corresponding biosecurity entry/exit record is created automatically.

---

*RF without a dedicated HU (RF-02, RF-10, RF-12 to RF-16, RF-27 to RF-33, RF-35, RF-36, RF-39, and all RNF) are Should-have/Could-have items or transversal RNF, and per the modeling guide's rule are documented directly in the traceability matrix without an individual user story.*
