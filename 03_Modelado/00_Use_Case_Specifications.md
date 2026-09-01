# Use Case Specifications — AgroMoreira

Textual specification for the 14 use cases in scope (CU-01 to CU-14). CU-15 "Sensor integration path" is a documented Won't-have (RF-32) and is not developed further. Pre/post-conditions are taken directly from the RF/RNF catalog and from the traceability matrix (`04_Trazabilidad/Matriz_Trazabilidad_v2.csv`).

---

## CU-01. Manage Plots / Lots

- **Primary actor(s):** Administrator, Technician, Farmworker.
- **Related RF:** RF-01, RF-02, RF-16, RF-29, RF-34, RF-35.
- **Precondition:** user authenticated with edit permission (RF-01); crop catalog already configured (RF-02).
- **Postcondition:** plot visible in the general listing (RF-01); no crop record is left with an unspecified "other" value (RF-02).
- **Basic flow:**
  1. The user selects "New plot".
  2. Enters name, sector, location, area, crop, variety and plant count.
  3. The system displays the field set that corresponds to the selected variety (RF-34).
  4. The user saves the plot.
  5. The system shows the plot in the general listing in under 2 seconds.
- **Alternative flows / exceptions:**
  - If any of the 7 required fields is missing, the system rejects the save and flags the empty fields (RF-01).
  - If the user tries to enter a crop outside the closed catalog, the system rejects it (RF-02).
  - The user may record weather/soil condition at any later time (RF-16).
  - The user may register a soil analysis prior to planting (RF-35).
- **Business rules:**
  - CU-01 does not allow an "other" value for crop (RF-02).
  - The crop/variety catalog is editable only by the Administrator.
  - A plot marked as "for export" enables the ExportBatch fields (RF-14, see CU-03).

---

## CU-02. Register Agricultural Activities

- **Primary actor(s):** Farmworker, Technician.
- **Related RF:** RF-03.
- **Precondition:** plot already exists (RF-01 already executed).
- **Postcondition:** activity is linked to the plot's history.
- **Basic flow:**
  1. The user selects the plot.
  2. Enters date, activity type (spraying, fertilizing, pruning, irrigation, cleaning), input/product used and responsible worker.
  3. The system saves the record and links it to the plot's history.
- **Alternative flows / exceptions:**
  - If date, plot or worker is missing, the system rejects the save (RF-03).
- **Business rules:**
  - Any activity that uses a catalog input automatically decrements inventory (see CU-05).
  - The activity history is the source of "treatment history" consumed by CU-06 (AI Pest Alerts).

---

## CU-03. Register Harvest

- **Primary actor(s):** Farmworker.
- **Related RF:** RF-04, RF-13, RF-14, RF-15.
- **Precondition:** plot and crop exist (RF-04); a harvest already registered that day (for RF-13).
- **Postcondition:** harvest added to the plot/period total; full history from bagging to packing is queryable if the plot is for export (RF-14).
- **Basic flow:**
  1. The user selects plot and crop.
  2. The system determines the expected unit for the crop (drum/quintal for cacao, bunch/box for plantain).
  3. The user enters quantity and unit.
  4. The system validates the unit, saves the harvest and updates the plot/period total.
  5. If applicable, the user checks the current market price and the system estimates projected income (RF-15).
- **Alternative flows / exceptions:**
  - Invalid harvest unit for the crop → the system rejects the record (RF-04).
  - The user registers a rejected quantity and reason (disease, pest, mechanical damage); the system automatically excludes the rejected amount from the usable total (RF-13).
  - If the plot is for export, the user registers ribbon color, bagging week and box quality (RF-14).
- **Business rules:**
  - The harvest unit depends exclusively on the crop, never free text.
  - The usable total always excludes the registered rejection.

---

## CU-04. Calculate Yield and Finance

- **Primary actor(s):** Administrator, Technician, Farmworker.
- **Related RF:** RF-05, RF-06, RF-26.
- **Precondition:** 2 or more harvest records exist for the plot (RF-05); income and expense records exist for the period (RF-06).
- **Postcondition:** value shown in the plot report (RF-05); value visible in the financial module (RF-06); movement reflected in the net-profit calculation (RF-26).
- **Basic flow:**
  1. The system queries the plot's harvest history and calculates average production per period, allowing period comparison.
  2. The system queries income and expense records (automatic from inputs + manual from RF-26) for the period.
  3. The system calculates net profit (income − expenses) and displays it in the financial module.
- **Alternative flows / exceptions:**
  - If fewer than 2 harvest records exist, the system shows "insufficient data" instead of an average.
  - The user can manually register an additional income or expense (concept, amount, date, type) independent of the automatic calculation (RF-26).
- **Business rules:**
  - Net profit = sum of income − sum of expenses for the period, without exception.
  - Yield average is calculated as sum divided by N records.

---

## CU-05. Manage Input Inventory

- **Primary actor(s):** Administrator, Technician, Farmworker.
- **Related RF:** RF-07, RF-08, RF-30.
- **Precondition:** none to register a new input; a threshold defined for the input (RF-08).
- **Postcondition:** stock reduced after each registered use (RF-07); notification sent and logged if the threshold is crossed (RF-08).
- **Basic flow:**
  1. The user registers the use of a quantity of an input.
  2. The system updates available stock.
  3. The system checks whether the new stock is below the configured minimum threshold (RF-30).
  4. If so, the system notifies the responsible party in under 5 minutes.
- **Alternative flows / exceptions:**
  - The Technician can configure/edit the minimum stock threshold for each input at any time (RF-30).
- **Business rules:**
  - CU-05 triggers an alert when the minimum stock is crossed (RF-08, RF-30).
  - Stock may never go negative; the system must warn before allowing it.

---

## CU-06. AI-Assisted Pest Alerts

- **Primary actor(s):** Administrator, Technician, Farmworker.
- **Secondary actor(s):** AI System.
- **Related RF:** RF-09, RF-10, RF-31, RF-33.
- **Precondition:** a trained AI model available (RF-09); internet connection (RF-10, if image diagnosis is used).
- **Postcondition:** the alert is logged with the result of human verification (RF-09).
- **Basic flow:**
  1. The AI System analyzes the plot's data (treatment history, and optionally a photo uploaded by the user) and generates a suggestion with justification and data source.
  2. The system notifies the responsible user, explicitly marked as a suggestion to be confirmed in the field.
  3. The user reviews the justification and confirms or discards the suggestion.
  4. The system logs the decision.
- **Alternative flows / exceptions:**
  - User discards the AI suggestion (RF-09).
  - The user may formally register disagreement with a recommendation, distinct from a simple confirm/discard, which stays available for the technical team's review (RF-33).
  - The system compares a newly entered value against the plot's historical average and warns if it is an outlier before saving (RF-31).
- **Business rules:**
  - No alert is ever auto-applied to a plot without confirmation from the responsible user (central rule of RF-09, tied to RNF-05/RNF-06).
  - Every alert must show its justification (max. 60 words) and at least one data source before the confirmation button.

---

## CU-07. Assign and Track Tasks

- **Primary actor(s):** Administrator, Technician, Farmworker.
- **Related RF:** RF-11, RF-12, RF-27, RF-28.
- **Precondition:** worker registered (RF-11); worker with a registered device (RF-12).
- **Postcondition:** task filterable by its 4 states (RF-11); notification delivered (RF-12).
- **Basic flow:**
  1. The user assigns a task to a worker, indicating plot, date and type.
  2. The system creates the task with status "pending" and makes it visible with its status.
  3. The system notifies the worker (push/SMS) including plot, date and task type.
  4. The worker updates the task status (pending → in progress → blocked → completed) and may attach a free-text observation (RF-28).
  5. The worker can consult the view of their own pending tasks at any time (RF-27).
- **Alternative flows / exceptions:**
  - If the plot is flagged with an occupational risk (CU-11), the system shows the PPE warning before confirming the assignment.
- **Business rules:**
  - The status filter must show exclusively the tasks in that status, without mixing plots or workers.
  - The observation on a completed task remains visible when viewing the task detail (RF-28).

---

## CU-08. Generate Reports

- **Primary actor(s):** Administrator, Technician.
- **Related RF:** RF-19.
- **Precondition:** data exists in the selected date range.
- **Postcondition:** report generated and downloadable.
- **Basic flow:**
  1. The user selects a date range and one or more plots.
  2. The system consolidates production, costs and pest-related losses, and yield per plot/period.
  3. The system generates color-coded bar and pie charts.
  4. The user exports the report.
- **Alternative flows / exceptions:**
  - If no data exists in the selected range, the system reports "no data available" instead of an empty report.
- **Business rules:**
  - The generated report must reflect exactly the sum of the records in the selected date range (no undeclared rounding).

---

## CU-09. Authentication and Access Control

- **Primary actor(s):** All (Administrator, Technician, Farmworker).
- **Related RF:** RF-20, RF-22, RF-23.
- **Precondition:** user previously registered (RF-20).
- **Postcondition:** access granted only to the functions of the user's role (RF-20); consent logged before any processing of personal data (RF-22).
- **Basic flow:**
  1. The user enters username and password.
  2. The system validates credentials and determines the role.
  3. If it is the first login, the system displays the personal-data-processing notice (LOPDP Art. 8) and requests the user's explicit acceptance before continuing.
  4. The system registers consent (free, specific, informed and unambiguous) and grants access according to role.
- **Alternative flows / exceptions:**
  - Invalid credentials → the system denies access.
  - A user with the "farmworker" role attempting to access the financial module → the system denies access (RF-20).
  - The worker may request access, rectification or deletion of their own personal data at any time (ARCO+ rights, RF-23).
- **Business rules:**
  - CU-09 is a regulatory Must-have: no module of the system is accessible without authentication and without logged LOPDP consent.
  - Role exhaustively determines the set of visible functions (least-privilege principle).

---

## CU-10. Technical Visits

- **Primary actor(s):** Technician.
- **Related RF:** RF-21.
- **Precondition:** plot exists.
- **Postcondition:** visit registered with findings and, if applicable, a follow-up flag.
- **Basic flow:**
  1. The Technician selects the plot to visit.
  2. Registers date, findings and whether follow-up is required.
  3. The system saves the visit and links it to the plot's compliance history.
- **Alternative flows / exceptions:**
  - If non-compliance is found, the system prompts for related training or PPE registration (see CU-11, CU-13).
- **Business rules:**
  - Periodic technical visits are the primary evidence source for BPA certification renewal (CU-13).

---

## CU-11. Occupational Risk and PPE

- **Primary actor(s):** Farmworker, Technician.
- **Related RF:** RF-18, RF-24.
- **Precondition:** plot exists; task about to be assigned or in progress.
- **Postcondition:** risk registered with suggested PPE (RF-18); health certificate attached when applicable (RF-24).
- **Basic flow:**
  1. On assigning or receiving a task, the system checks whether the plot has a registered occupational risk.
  2. If not registered, the Technician registers risk type, severity and suggested PPE.
  3. The system shows the PPE warning to the worker before confirming the assignment.
- **Alternative flows / exceptions:**
  - The Administrator attaches the worker's health certificate to the record (RF-24, Res. AGROCALIDAD 183 Art. 33-34).
- **Business rules:**
  - No task on a plot with a registered risk may be confirmed without the PPE warning being shown first.

---

## CU-12. Quick Report Channel

- **Primary actor(s):** Farmworker.
- **Related RF:** RF-17.
- **Precondition:** user authenticated.
- **Postcondition:** quick report (chat/voice) logged and routed to the relevant module (activity, disease, risk).
- **Basic flow:**
  1. The worker opens the quick-report channel.
  2. Records a short message (text or voice) describing a field situation.
  3. The system stores the report and flags it for review/triage by the Technician.
- **Alternative flows / exceptions:**
  - If the report describes a suspected quarantine pest, the system suggests escalating it as a formal phytosanitary notice (CU-14).
- **Business rules:**
  - The quick-report channel favors low digital literacy (RNF-03) and does not require structured fields to start.

---

## CU-13. BPA Compliance

- **Primary actor(s):** Administrator.
- **Related RF:** RF-25, RF-36, RF-38, RF-39.
- **Precondition:** technical visits and training records available as supporting evidence.
- **Postcondition:** BPA certification request/renewal filed before AGROCALIDAD (RF-25); training and biosecurity records available for audit (RF-36, RF-38, RF-39).
- **Basic flow:**
  1. The Administrator reviews the compliance dashboard (certificate validity, pending training, biosecurity log completeness).
  2. If the certificate is expiring or missing supporting evidence, the Administrator requests renewal before AGROCALIDAD.
  3. The system attaches training records (pesticide handling, first aid) and the biosecurity entry/exit log as supporting evidence.
- **Alternative flows / exceptions:**
  - If required training is missing, the system blocks the renewal request until it is registered (RF-36, RF-39).
- **Business rules:**
  - This CU is a regulatory Must-have (Res. AGROCALIDAD 183): its absence was a legal gap identified by the team's legal-first method.

---

## CU-14. Quarantine Pest Notice (e.g. Moko)

- **Primary actor(s):** Farmworker, Technician, Administrator.
- **Secondary actor(s):** AGROCALIDAD.
- **Related RF:** RF-37, RF-38.
- **Precondition:** suspected quarantine-pest symptoms detected on a plot (Res. AGROCALIDAD 0072, Art. 3.6.1.a).
- **Postcondition:** notice logged and available for formal submission to AGROCALIDAD.
- **Basic flow:**
  1. A field user detects suspected symptoms (e.g. Moko) on a plot.
  2. Registers the symptom and affected plot in the system.
  3. The system generates a phytosanitary notice.
  4. A Technician confirms the symptom.
  5. The system leaves the notice available for formal submission to AGROCALIDAD and logs the biosecurity entry/exit event for the visit (RF-38).
- **Alternative flows / exceptions:**
  - The Technician discards the symptom after inspection → the notice is not sent, but stays logged as discarded, for traceability.
- **Business rules:**
  - This CU is a regulatory Must-have (Res. AGROCALIDAD 0072, Art. 3.6.1.a): its absence was a legal gap identified by the team's legal-first method.
  - No notice is sent to AGROCALIDAD without a Technician's confirmation.

---

*Note: CU-15 (sensor integration path, RF-32) is documented as a Won't-have for this delivery and has no dedicated diagrams or mockup.*
